from transformers import VitsModel, AutoTokenizer
import torch
import uroman as ur
import sounddevice as sd

model = VitsModel.from_pretrained("facebook/mms-tts-kor")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-kor")

koreanText = "안녕하세요"
uroman = ur.Uroman()
romanizedText = uroman.romanize_string(koreanText)
inputs = tokenizer(romanizedText, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs).waveform

sampling_rate = model.config.sampling_rate
sd.play(output.squeeze().numpy(), samplerate=sampling_rate)
sd.wait()
