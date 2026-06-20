import os
from dotenv import load_dotenv

import gradio as gr

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")


# ---------------- SET MOOD ----------------
def set_mode(choice):
    if choice == "Happy":
        mode = "You are a happy AI agent. Always respond cheerfully."
    elif choice == "Angry":
        mode = "You are an angry AI agent. Always respond in a rude tone."
    elif choice == "Sad":
        mode = "You are a sad AI agent. Always respond emotionally."
    else:
        mode = "You are a helpful AI assistant."

    messages = [SystemMessage(content=mode)]
    return messages, f"Mode set to: {choice}", []


# ---------------- CHAT FUNCTION ----------------
def chat(user_input, messages):
    if messages is None:
        messages = [SystemMessage(content="You are a helpful AI assistant.")]

    messages.append(HumanMessage(content=user_input))

    response = model.invoke(messages).content

    messages.append(AIMessage(content=response))

    return response, messages


# ---------------- RESPONSE ----------------
def respond(message, messages, history):
    if not message:
        return "", messages, history

    reply, messages = chat(message, messages)

    # OLD FORMAT (IMPORTANT for your Gradio version)
    history.append((message, reply))

    return "", messages, history


# ---------------- UI ----------------
with gr.Blocks() as demo:

    gr.Markdown("## 🤖 Mood Based AI Agent (LangChain + Mistral)")

    messages_state = gr.State(None)

    with gr.Row():
        mode_dropdown = gr.Dropdown(
            choices=["Happy", "Angry", "Sad"],
            label="Choose AI Mode"
        )
        status_box = gr.Textbox(label="Status")

    set_mode_btn = gr.Button("Set Mode")

    chatbot = gr.Chatbot()   # ❌ NO type="messages"

    user_input = gr.Textbox(label="Your Message")
    send_btn = gr.Button("Send")

    clear_btn = gr.Button("Clear Chat")


    # -------- SET MODE --------
    set_mode_btn.click(
        set_mode,
        inputs=mode_dropdown,
        outputs=[messages_state, status_box, chatbot]
    )

    # -------- SEND --------
    send_btn.click(
        respond,
        inputs=[user_input, messages_state, chatbot],
        outputs=[user_input, messages_state, chatbot]
    )

    # -------- CLEAR --------
    def clear():
        return [], None, []

    clear_btn.click(
        clear,
        outputs=[chatbot, messages_state, chatbot]
    )

demo.launch()