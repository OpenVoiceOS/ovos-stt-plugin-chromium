## Description

This is an STT plugin for OpenVoiceOS. It uses the speech recognition API of the Google Chrome browser.

The plugin ships with a bundled API key. Google stopped issuing new keys for this API ([announcement](http://www.chromium.org/developers/how-tos/api-keys)), but the bundled key still works, most likely because it is [also used inside Chromium itself](https://stackoverflow.com/questions/26485531/google-speech-api-v2).

A list of supported languages is in [this Stack Overflow comment](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134).

This is the same speech recognition service as the "google" module in mycroft-core. That module is supported in mycroft-core but cannot be used there, because mycroft-core cannot obtain new API keys. A [pull request to fix this](https://github.com/MycroftAI/mycroft-core/pull/1493) was proposed and blocked.

Using this plugin removes the need for a backend proxy, so latency is lower and you get more configuration options. Accuracy stays the same, since this is the same speech recognition service used by [Mycroft Selene](https://github.com/MycroftAI/selene-backend/blob/6f2de64f3bce70da2d82bdf5534338f5e7d3f9c3/api/public/public_api/endpoints/google_stt.py#L92).

## Install

```bash
pip install ovos-stt-plugin-chromium
```

## Configuration

By default, the plugin uses the global language set in your OVOS configuration.

```json
  "stt": {
    "module": "ovos-stt-plugin-chromium"
  }
```

### Advanced configuration

```json
  "stt": {
    "module": "ovos-stt-plugin-chromium",
    "ovos-stt-plugin-chromium": {
        "lang": "en-US",
        "pfilter": false,
        "debug": false
    }
  }
```

- `lang` — overrides the global language. Use a code from the supported languages list.
- `pfilter` — profanity filter. When `true`, the plugin censors profanity, showing only the first character and replacing the rest with asterisks, for example `f***`.
- `debug` — when `true`, logs the confidence score and alternative transcriptions.

## Docker

You can run this plugin behind [ovos-stt-http-server](https://github.com/OpenVoiceOS/ovos-stt-http-server) to expose it as an HTTP STT server, without needing device pairing.

```bash
docker run -p 8080:8080 ghcr.io/openvoiceos/google-stt-proxy:master
```

Public instances of [ovos-stt-http-server](https://github.com/OpenVoiceOS/ovos-stt-http-server) that run this plugin:

- [https://stt.smartgic.io/chromium](https://stt.smartgic.io/chromium/status), hosted by [@goldyfruit](https://github.com/goldyfruit)
