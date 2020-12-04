## Description

A stt plugin for mycroft using the google chrome browser api

The "plugins" are pip install-able modules that provide new STT engines for mycroft, more info in the [docs](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/plugins)

This STT API [has been deprecated](http://www.chromium.org/developers/how-tos/api-keys) for developers and no new keys are issued, however it still works, most likely due to it being used in browsers

[a key is bundled](https://github.com/Uberi/speech_recognition/blob/master/speech_recognition/__init__.py#L870) with this plugin that has been functional for a long time


List of supported languages can be found [in this stackoverflow comment](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134)

By using this plugin you will lose some privacy (mycroft backend proxy) but will have less latency and more configuration options, while keeping the same accuracy, this is the same STT engine used by [Mycroft Selene](https://github.com/MycroftAI/selene-backend/blob/6f2de64f3bce70da2d82bdf5534338f5e7d3f9c3/api/public/public_api/endpoints/google_stt.py#L92)

## Install

`mycroft-pip install jarbas-stt-plugin-chromium`


## Configuration

By default the global language used by mycroft-core will be used

```json
  "stt": {
    "module": "chromium_stt_plug"
  }
 
```

### Advanced configuration


```json
  "stt": {
    "module": "chromium_stt_plug",
    "chromium_stt_plug": {
        "lang": "en-US",
        "pfilter": 0
    }
  }
 
```

`pfilter` -  The profanity filter level can be adjusted with ``pfilter``: 0 - No filter, 1 - Only shows the first character and replaces the rest with asterisks. The default is level 0.

`lang` - override core language and use this one instead