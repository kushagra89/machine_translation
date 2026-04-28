import gradio as gr
from src.translator import translate_text

demo = gr.Interface(
    fn=translate_text, 
    inputs=gr.Textbox(lines=5, placeholder="Enter English text here...", label="English Input"),
    outputs=gr.Textbox(label="French Translation"),
    title="My AI Translator",
    description="Translation powered by Helsinki-NLP (v5 Compatible)"
)

if __name__ == "__main__":
    # share=True lets you access it from your phone/other devices
    demo.launch()