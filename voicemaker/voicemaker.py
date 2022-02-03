import requests

LANGUAGES_LIST = [
    'en-US', 'en-GB', 'en-AU', 'en-HK', 'en-NZ', 'en-SG', 'en-ZA', 'de-DE',
    'ar-XA', 'ar-SA', 'bn-IN', 'bg-BG', 'ca-ES', 'cmn-CN', 'zh-HK', 'cmn-TW',
    'cy-GB', 'cs-CZ', 'da-DK', 'de-CH', 'es-AR', 'es-CO', 'es-US', 'ga-IE',
    'gu-IN', 'hr-HR', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'nl-BE', 'en-CA',
    'en-IN', 'en-IE', 'et-EE', 'en-PH', 'fil-PH', 'fi-FI', 'fr-BE', 'fr-FR',
    'fr-CA', 'fr-CH', 'el-GR', 'he-IL', 'hi-IN', 'hu-HU', 'id-ID', 'it-IT',
    'ja-JP', 'lv-LV', 'lt-LT', 'ko-KR', 'nb-NO', 'pl-PL', 'pt-PT', 'pt-BR',
    'ro-RO', 'ru-RU', 'sk-SK', 'sw-KE', 'es-ES', 'es-MX', 'es-LA', 'es-US',
    'sl-SI', 'sv-SE', 'tr-TR', 'ta-IN', 'te-IN', 'th-TH', 'uk-UA', 'ur-PK',
    'vi-VN'
]


class Voicemaker():
  token: str = None
  base_url: str = None

  def __init__(self, token=None) -> None:
    self.base_url = "https://developer.voicemaker.in/voice"
    self.token = None

    if token is not None:
      self.set_token(token)

  def set_token(self, token: str) -> None:
    """Sets the API token. You can get yours from https://developer.voicemaker.in/apidocs

    Args:
        token (str): API Token.
    """
    self.token = token

  def __headers__(self) -> dict:
    headers = {'Content-Type': 'application/json'}

    if self.token is not None:
      headers['Authorization'] = 'Bearer ' + self.token

    return headers

  def __get__(self, api: str, params={}):
    result = requests.get(self.base_url + api, params=params,
                          headers=self.__headers__())
    result.raise_for_status()
    return result.json()

  def __post__(self, api: str, data={}):
    result = requests.post(self.base_url + api, json=data,
                           headers=self.__headers__())
    result.raise_for_status()
    return result.json()

  def generate_audio_url(self,
                         text: str,
                         engine='neural', voice_id='ai3-Jony', language_code='en-US',
                         output_format='mp3', sample_rate=48000, effect='default',
                         master_speed=0, master_volume=0,
                         master_pitch=0) -> str:
    """Generates an audio URL from the given text and using the selected options

    Args:
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

    Returns:
        str: URL of the MP3 to download, hosted on Voicemaker.in
    """
    return self.__post__('/api', {
        'Text': text,
        'Engine': engine,
        'VoiceId': voice_id,
        'LanguageCode': language_code,
        'OutputFormat': output_format,
        'SampleRate': str(sample_rate),
        'Effect': effect,
        'MasterSpeed': str(master_speed),
        'MasterVolume': str(master_volume),
        'MasterPitch': str(master_pitch),
    })['path']

  def generate_audio_to_file(self, out_path: str, text: str, **kwargs) -> None:
    """Generates audio from text and saves it to a file

    Args:
        out_path (str): Path where the generated audio should be written
        text (str): Text to generate an audio from
    """
    url = self.generate_audio_url(text, **kwargs)
    file = requests.get(url)
    with open(out_path, 'wb') as file_handle:
      file_handle.write(file.content)


  def list_voices(self, language='en-US') -> list:
    """Lists all available voices for the selected language

    Args:
        language (str, optional): Language of choice. Defaults to 'en-US'.

    Raises:
        ValueError: When the selected language is not supported

    Returns:
        list: List of languages of the form { "Engine": "xxx", "VoiceId": "xxx", "VoiceGender": "xxx", "VoiceWebname": "xxx", "Country": "XX", "Language": "xx-XX" }
    """
    if language not in LANGUAGES_LIST:
      raise ValueError('Selected language is not supported')
    return self.__get__('/list', {'language': language})['data']['voices_list']
