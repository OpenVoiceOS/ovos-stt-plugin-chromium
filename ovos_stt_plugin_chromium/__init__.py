from ovos_utils.log import LOG
from ovos_plugin_manager.templates.stt import STT
import json
import requests
import logging


class ChromiumSTT(STT):
    def __init__(self):
        super().__init__()
        self.pfilter = self.config.get("pfilter", False)
        self.lang = self.config.get("lang") or self.lang

        # no keys issued since at least march 9 2016
        # http://web.archive.org/web/20160309230031/http://www.chromium.org/developers/how-tos/api-keys
        # key scrapped from commit linked bellow, dated Jun 8, 2014
        # https://github.com/Uberi/speech_recognition/commit/633c2cf54466a748d1db6ad0715c8cbdb27dbb09
        # let's hope it just keeps on working!
        default_key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"

        self.key = self.config.get("key") or default_key
        self.debug = self.config.get("debug", False)
        if not self.debug:
            log = logging.getLogger("urllib3.connectionpool")
            log.setLevel("INFO")

    def execute(self, audio, language=None):
        flac_data = audio.get_flac_data(
            convert_rate=None if audio.sample_rate >= 8000 else 8000,
            # audio samples must be at least 8 kHz
            convert_width=2  # audio samples must be 16-bit
        )

        params = {
            "client": "chromium",
            "lang": language or self.lang,
            "key": self.key,
            "pFilter": int(self.pfilter)
        }
        sample_rate = str(audio.sample_rate)
        headers = {"Content-Type": "audio/x-flac; rate=" + sample_rate}
        url = "http://www.google.com/speech-api/v2/recognize"
        r = requests.post(url, headers=headers, data=flac_data, params=params)

        # weirdly this returns something like
        """
        {"result":[]}
        {"result":[{"alternative":[{"transcript":"Hello world","confidence":0.83848035},{"transcript":"hello hello"},{"transcript":"Hello"},{"transcript":"Hello old"},{"transcript":"Hello howdy"}],"final":true}],"result_index":0}
        """

        result = r.text.split("\n")[1]
        data = json.loads(result)["result"]
        if len(data) == 0:
            return ""
        data = data[0]["alternative"]
        if self.debug:
            LOG.debug("transcriptions:" + str(data))
        if len(data) == 0:
            return ""

        # we arbitrarily choose the first hypothesis by default.
        # results seem to be ordered by confidence
        best_hypothesis = data[0]["transcript"]

        # if confidence is provided return highest conf
        candidates = [alt for alt in data if alt.get("confidence")]
        if self.debug:
            LOG.debug("confidences: " + str(candidates))

        if len(candidates):
            best = max(candidates, key=lambda alt: alt["confidence"])
            best_hypothesis = best["transcript"]
            if self.debug:
                LOG.debug("best confidence: " + best_hypothesis)
        return best_hypothesis
