import gradio as gr
from transformers import pipeline

# Load your model (adjust with the correct model ID)
model = pipeline("text-generation", model="arshadshk/Mistral-Hinglish-7B-Instruct-v0.2", use_auth_token='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')

def predict(input_text):
    response = model(input_text)
    return response[0]['generated_text']

# Create the Gradio interface
interface = gr.Interface(fn=predict, inputs="text", outputs="text")
interface.launch()
