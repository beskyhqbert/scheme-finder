# Scheme Finder

Many people miss out on government benefits simply because they don't know they qualify.
Describe your situation in plain words (any language your model supports) and Scheme Finder
suggests matching schemes, the documents you need, and the official link.

- 100% local and private, using an open model through [Ollama](https://ollama.com)
- Answers come only from `schemes.json`, so the model can't invent schemes
- Easy to extend: add a scheme by editing one JSON file

## Run it
```bash
ollama pull llama3.2
pip install -r requirements.txt
python app.py "I am a 45 year old farmer in Bihar with 2 acres of land"
```

## Contribute (Hacktoberfest)
Add schemes (central or state), fix outdated info, or translate. See [CONTRIBUTING.md](CONTRIBUTING.md).

> Always verify details on the official website. This tool is a guide, not legal advice.

MIT License
