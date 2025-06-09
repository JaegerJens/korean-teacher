# Korean teacher

## Install

setup Python venv

```bash
python -m venv venv
./venv/scripts/activate
python -m pip install --upgrade pip
```

### Korean TTS model

using [Massively Multilingual Speech (MMS): Korean Text-to-Speech](https://huggingface.co/facebook/mms-tts-kor)

```bash
pip install --upgrade transformers accelerate
```

playing on speakers

```bash
pip install sounddevice
```

uroman pre-processing

```bash
pip install uroman
```
