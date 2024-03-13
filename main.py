import torch
import sounddevice as sou_voi
import time


language = 'ru'
id_mode = 'ru_v4'
sample_rate = 48000
speaker = 'daya'
put_accent = True
put_yoo = True
device = torch.device('cpu')
text = "Привет"


def bib_model():
    _ = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_tts', language=language, speaker=id_mode)


def ttss_audio():
    bib_model().apply_tts(text=text, speaker=speaker, sample_rate=sample_rate, put_accent=put_accent,
                          put_yoo=put_yoo)


if __name__ == '__main__':
    print(text)
    bib_model()
    sou_voi.play(ttss_audio(), sample_rate)
    time.sleep(len(ttss_audio()) / sample_rate)
    sou_voi.stop()