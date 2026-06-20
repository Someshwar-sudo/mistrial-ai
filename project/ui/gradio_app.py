import json
import gradio as gr
import requests

URL = "http://127.0.0.1:8000/extract"

def predict(text):
    response = requests.post(URL, json={"text": text})

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    try:
        return response.json()   # ✅ BEST FIX
    except:
        return {"error": response.text}


demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=10),
    outputs=gr.JSON(),
    title="Movie Intelligence LLM"
)

demo.launch()