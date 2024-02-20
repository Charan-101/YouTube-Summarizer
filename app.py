from flask import Flask, render_template, request, jsonify
from pytube import YouTube
import librosa
import soundfile as sf
from transformers import pipeline
from huggingsound import SpeechRecognitionModel
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI model
client = OpenAI(api_key="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")

# Initialize Hugging Face model
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device="cpu")

# Initialize Hugging Face summarization pipeline
summarization = pipeline('summarization')

# Function to download YouTube audio and convert to WAV format
def download_and_convert_audio(video_url):
    # Download YouTube audio
    yt = YouTube(video_url)
    yt.streams.filter(only_audio=True, file_extension='mp4').first().download(filename='ytaudio.mp4')

    # Convert audio to WAV format
    !ffmpeg -i ytaudio.mp4 -acodec pcm_s16le -ar 16000 ytaudio.wav

    return 'ytaudio.wav'

# Function to transcribe audio chunks and summarize text
def transcribe_and_summarize_audio(audio_file):
    ytaudio, sr = librosa.load(audio_file, sr=16000)

    # Stream over 30 seconds chunks
    stream = librosa.stream(ytaudio, block_length=30, frame_length=16000, hop_length=16000)

    # Write audio chunks to files
    for i, speech in enumerate(stream):
        sf.write(f'{i}.wav', speech, sr)

    # Transcribe audio chunks
    audio_paths = [f'{i}.wav' for i in range(i + 1)]
    transcriptions = model.transcribe(audio_paths)

    # Combine transcriptions
    full_transcript = ''
    for item in transcriptions:
        full_transcript += ''.join(item['transcription'])

    # Summarize text
    summarized_text = summarization(full_transcript)

    return summarized_text

# Define a route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle form submission
@app.route('/summarize', methods=['POST'])
def summarize():
    # Get YouTube video URL from form
    video_url = request.form.get('video_url')

    # Download and convert audio
    audio_file = download_and_convert_audio(video_url)

    # Transcribe audio chunks and summarize text
    summarized_text = transcribe_and_summarize_audio(audio_file)

    return jsonify({'summarized_text': summarized_text})

if __name__ == '__main__':
    app.run(debug=True)
