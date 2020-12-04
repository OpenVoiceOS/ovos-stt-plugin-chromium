from mycroft.stt import STT


class ChromiumSTT(STT):
    def __init__(self):
        super().__init__()
        self.pfilter = self.config.get("pfilter", 0)
        self.lang = self.config.get("lang") or self.lang

    def execute(self, audio, language=None):
        lang = language or self.lang
        return self.recognizer.recognize_google(audio,
                                                language=lang,
                                                pfilter=self.pfilter,
                                                show_all=False)


