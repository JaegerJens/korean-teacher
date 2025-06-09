# Korean teacher

Use an LLM to learn to understand korean language.

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

### Ollama Korean teacher

Using [Ollama tool support](https://ollama.com/blog/tool-support) for a Korean teacher:

Korean teacher should speak a Korean word or sentence via tool and I should answer with the English translation.

```bash
pip install ollama
```

Example code: [tools.py](https://github.com/ollama/ollama-python/blob/main/examples/tools.py)
