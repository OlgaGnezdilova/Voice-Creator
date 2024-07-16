import torch
import sounddevice as sou_voi
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000 # 48000
speaker = 'baya' # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu') # cpu или gpu
text = "Хауди Хо, друзья!!!"


def bib_model():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_tts', language=language, speaker=id_mode)
    return model


def ttss_audio():
    print(bib_model())
    audio = bib_model().apply_tts(
        text=text,
        speaker=speaker,
        sample_rate=sample_rate,
        put_accent=put_accent,
        put_yo=put_yo
    )
    return audio


if __name__ == '__main__':
    print(text)
    bib_model()
    sou_voi.play(ttss_audio(), sample_rate)
    time.sleep(len(ttss_audio()) / sample_rate + 0.2)
    sou_voi.stop()
