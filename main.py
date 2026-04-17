import streamlit as st
# Whisper and transcription (placeholder)
def transcribe_audio(file_bytes: bytes) -> str:
    # In a real app: use whisper or another ASR model
    return "Transcribed text from audio (demo)."

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following lecture content into concise notes:\n{text}"
    return prompt  # In MVP, you would pass to LLM here

def main():
    st.title("AI Attendance & Notes Generator")
    audio_file = st.file_uploader("Record or upload lecture audio (WAV/MP3)", type=["wav","mp3"])
    if audio_file is not None:
        transcribed = transcribe_audio(audio_file.read())
        notes = summarize_text(transcribed)
        st.subheader("Transcription")
        st.write(transcribed)
        st.subheader("Lecture Notes")
        st.write(notes)

if __name__ == "__main__":
    main()
