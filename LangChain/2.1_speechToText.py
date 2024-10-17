import streamlit as st
from audio_recorder_streamlit import audio_recorder
import openai
import base64


# Initialize openai client
def setup_api(api_key):
    return openai.OpenAI(api_key=api_key)


# Fun to transcribe audio to text
def transcribe_audio(client, audio_path):
    with open(audio_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model = "whisper-1",
            file = audio_file
        )
        return transcript.text

# Taking response from OpenAI
def fetch(client, input_text):
    messages = [
        {"role":"user", "content":input_text}
    ]
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    return response.choices[0].message.content

# Text card function
def create_text(text, title="Response"):
    card_html = f"""
     <style>
            .card {{
                box-shadow:0 4px 8px 0 rgba(0,0,0,0.2);
                transition: 0.3s;
                border-radius: 5px;
                padding: 15px;
            }}
            . card:hover{{
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
            }}
            .container {{
                padding: 2px 16px;
            }}
     </style>
     <div class-"card">
            <div class="container">
                <h4><b>{title}</b></h4>
                <p>{text}</p>
            </div>
     </div>

     """
    st.markdown(card_html, unsafe_allow_html=True)


# On click button
def click_button():
    st.write("Button")



def main():

    st.sidebar.title("API KEY CONFRIGURATION")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type='password')

    st.title("Chatbot")

    # Check API key is there
    if api_key:
        client = setup_api(api_key)
        input = st.text_input("Hi How can I assist you today?")
        button = st.button("Submit", on_click=click_button)

        if input and button:
            response = fetch(client,input)
            create_text(response, "AI Response")

        recorded_audio = audio_recorder()
        # check if recording is done & Available
        if recorded_audio:
            audio_file = "audio.mp3"
            with open(audio_file, 'wb') as f:
                f.write(recorded_audio)

            transcribed_text = transcribe_audio(client,audio_file)
            create_text(transcribed_text, "Transcribed Text")


            ai_response = fetch(client,transcribed_text)
            create_text(ai_response, "AI Response")

        


if __name__=="__main__":
    main()