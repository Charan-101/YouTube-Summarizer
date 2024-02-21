# YouTube Summarizer

This project is a web application that allows users to summarize the content of a YouTube video. It utilizes Python for backend processing and Flask for serving the web application.

## Project Structure

The project consists of the following components:

1. **app.py**: This is the main Flask application file. It handles the web server and routes requests. It serves the HTML template and handles the POST request to summarize the YouTube video.

2. **ytsummariser.py**: This file contains the Python code for summarizing the YouTube video. It includes logic for downloading the video audio, performing automatic speech recognition (ASR), and summarization.

3. **templates/index.html**: This HTML template resides in the `templates` directory. It contains the frontend code for the web application, including a form for users to input the YouTube video link and display the summarized text.



## Usage

To run the project:

1. Install the required Python packages:

2. Run the Flask application:


3. Access the web application in your browser at `http://localhost:5000`. Enter a valid YouTube video link and click the "Summarize" button to see the summarized text.

## Dependencies

- Flask: Micro web framework for Python.
- Pytube: Library for downloading YouTube videos.
- Librosa: Python package for music and audio analysis.
- Soundfile: Library for reading and writing audio files.
- Transformers: Library for natural language understanding (NLU) using state-of-the-art pre-trained models.
- Huggingsound: Python package for accessing Hugging Face's speech processing models.
- OpenAI: Library for accessing OpenAI's GPT-3 language model.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.



