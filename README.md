# Voicemaker

Voicemaker.in is an online text-to-speech service with a dead-simple API. This package is just a wrapper around their API.

This is an unofficial package, and is in no way associated to Voicemaker.

The official API documentation is here: https://developer.voicemaker.in/apidocs

## Latest API supported version

The lastest API supported version is the `v2.2`.

## Prerequisites

The only thing you will need is your API token, which you can obtain in the official API documentation page once you log in.

## Usage

### List all available voices for a language

```python
from voicemaker import Voicemaker

vm = Voicemaker()
vm.list_voices(language="en-US")
```

Which returns an array of `dict` elements with the following structure:

```json
[
  {
    "Engine": "neural",
    "VoiceId": "ai1-Joanna",
    "VoiceGender": "Female",
    "VoiceWebname": "Joanna",
    "Country": "US",
    "Language": "en-US"
  },
  ...
]
```

### Generate URL for text

```python
from voicemaker import Voicemaker

vm = Voicemaker()
vm.set_token('<TOKEN>')
vm.generate_audio_url('I met a traveller from an antique land Who said: Two vast and trunkless legs of stone Stand in the desert.')
```

Returns the URL of the generated voice in MP3 format.

Also accepts the following optional arguments:

```
text (str): Text to generate an audio from.
engine (str, optional): Choose between 'standard' and 'neutral'. Defaults to 'neural'.
voice_id (str, optional): Uses the selected voice id from the available one for the selected language. Defaults to 'ai3-Jony'.
language_code (str, optional): Language of the target voice. Defaults to 'en-US'.
output_format (str, optional): Choose from 'mp3' and 'wav'. Defaults to 'mp3'.
sample_rate (int, optional): Choose from 48000, 44100, 24000, 22050, 16000, 8000. Defaults to 48000.
effect (str, optional): Effect to give to the voice. Defaults to 'default'.
master_speed (int, optional): Speed from -100 to 100. Defaults to 0.
master_volume (int, optional): Volume of the voice from -100 to 100. Defaults to 0.
master_pitch (int, optional): Pitch of the voice, from -100 to 100. Defaults to 0.
```

### Save generated audio to disk
This is a convenience method. It just calles `generate_audio_url`, gets the URL, downloads the file and saves it to disk.

```python
from voicemaker import Voicemaker

vm = Voicemaker()
vm.set_token('<TOKEN>')
vm.generate_audio_to_file('test.mp3', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone Stand in the desert.')
```
