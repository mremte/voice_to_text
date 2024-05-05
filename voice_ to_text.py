import streamlit as st
import speech_recognition as sr


def recognize_indonesian_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        indonesian_text = recognizer.recognize_google(audio_data, language='id-ID')
        return indonesian_text
    except sr.UnknownValueError:
        return "Sorry, could not recognize the speech."
    except sr.RequestError as e:
        return f"Error with the API request: {e}"


def main():
    st.title("Indonesian Speech Recognition")

    uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

    if uploaded_file is not None:
        st.write("File uploaded successfully.")

        if st.button("Recognize Indonesian Speech"):
            indonesian_text = recognize_indonesian_speech(uploaded_file)
            st.write("Recognized Indonesian Text:")
            st.write(indonesian_text)


if __name__ == "__main__":
    main()
