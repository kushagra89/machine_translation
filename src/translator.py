from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_id = "Helsinki-NLP/opus-mt-en-fr"

try:
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    print("✅ Success! Model loaded without using deprecated pipelines.")
except Exception as e:
    print(f"❌ ERROR: {e}")
    model = None

def translate_text(text):
    if not text or not text.strip():
        return "Please enter some text."
    
    if model is None:
        return "Model not loaded. Check terminal errors."

    try:
        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        
        # Generate translation tokens
        translated_tokens = model.generate(**inputs)
        
        # Decode tokens back into string
        result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        return result
    except Exception as e:
        return f"Translation error: {str(e)}"