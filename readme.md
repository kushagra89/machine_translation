# Machine Translation Demo

A simple Gradio-powered English-to-French translator using the Helsinki-NLP `opus-mt-en-fr` model from Hugging Face Transformers.

## Features

- Transliteration from English to French
- Gradio web UI for quick testing
- Uses `transformers` and `torch`

## Files

- `app.py` - launches the Gradio app
- `src/translator.py` - loads the model and handles translation
- `requirements.txt` - Python dependencies

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install packages:

```powershell
pip install gradio transformers torch
```

3. Run the app:

```powershell
python app.py
```

## Usage

- Open the local Gradio URL shown in the terminal
- Enter English text in the input box
- View the French translation in the output box

## Notes

- The first run may take a little longer while the Hugging Face model downloads.
- If the model fails to load, check the terminal output for errors.

## Deploying to GitHub

1. Create a new repository on GitHub.
2. Add the remote:

```powershell
git remote add origin https://github.com/<your-username>/<repo-name>.git
```

3. Push the branch:

```powershell
git push -u origin main
```
