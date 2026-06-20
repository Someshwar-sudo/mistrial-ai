import gradio as gr
from main import MovieExtractor   

# create pipeline object once
extractor = MovieExtractor()

# function for UI
def predict_movie(text):
    return extractor.extract(text)


interface = gr.Interface(
    fn=predict_movie,
    inputs=gr.Textbox(lines=10, placeholder="Enter movie paragraph..."),
    outputs=gr.JSON(),
    title="🎬 Movie Intelligence LLM",
    description="Extract structured movie data from unstructured text"
)

if __name__ == "__main__":
    interface.launch()