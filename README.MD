# 🩺 Multimodal-Med-AI –> Your AI Doctor Assistant

MediBot 2.0 is an AI-powered health care assistant that leverages speech recognition, text-to-speech, and multimodal large language models to analyze patient images and voice inputs. The system provides a simulated doctor's response both as text and synthesized speech.
![Screenshot](C:\Users\prern_dcreuet\OneDrive\Desktop\Documents\python programs\Pictures\Screenshots\Screenshot 2026-04-07 232641.png)

## 🚀 Key Features

- **🎙️ Speech-to-Text**: Converts patient voice input to text using Whisper via Groq API.
- **🖼️ Image Analysis**: Analyzes uploaded patient images for medical concerns using a multimodal LLM (Llama-3 Vision via Groq API).
- **🔊 Text-to-Speech**: Converts AI-generated responses into speech with Google Text-to-Speech (gTTS).
- **🌐 Gradio Web Interface**: User-friendly web interface for uploading images and recording voice.

## 📁 Project Structure

```
.env
brain_of_the_doctor.py
voice_of_the_doctor.py
voice_of_the_patient.py
gradio_app.py
Pipfile
Pipfile.lock
acnes.jpg
final.mp3
final.wav
gtts_test_autoplay.mp3
gtts_test.mp3
gtts_test.wav
patient_voice_test_for_patient.mp3
explanation.pdf
```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd MediBot2.0
```

### 2. Install Dependencies

This project uses [Pipenv](https://pipenv.pypa.io/en/latest/):

```sh
pip install pipenv
pipenv install
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with your API keys:

```
GROQ_API_KEY="your_groq_api_key"
ELEVENLABS_API_KEY="your_elevenlabs_api_key"
```

> **Note:** The `.env` file is already present in the repo. Update it with your own API keys.

### 4. Install System Dependencies

- **ffmpeg** and **portaudio** are required for audio processing.
- **Windows**: Download [ffmpeg](https://ffmpeg.org/download.html) and add it to your PATH.
- **Linux/macOS**: Install via package manager, e.g., `sudo apt install ffmpeg portaudio19-dev`.

### 5. Run the Gradio App

```sh
pipenv run python gradio_app.py
```

The app will launch at [http://127.0.0.1:7860](http://127.0.0.1:7860).

## Run With Docker
### 🛠️ 1. Build the Docker Image
```sh
docker build -t medibot .
```
### 🔐 2. Log In to Docker Hub (if pushing to remote registry)
```sh
docker build -t ai-medi-app .
```
### 🚀 3. Tag & Push the Image to Docker Hub
Replace prerna2424 with your Docker Hub username:
```sh
docker tag ai-medi-app prerna2424/ai-medi-app:latest
docker push prerna2424/ai-medi-app:latest
```
### 📥 4. Pull the Image (if deploying elsewhere)
To pull your image on another machine or cloud server:
```sh
To pull your image on another machine or cloud server:
```
### ▶️ 5. Run the Container
Make sure to pass required environment variables like your Groq API key:
```sh
docker run -d ^
  -p 1234:7860 ^
  -e GROQ_API_KEY="your_groq_api_key_here" ^
  --name ai-medi-app-container ^
  prerna2424/ai-medi-app
```
✅ This will expose the app at http://localhost:1234

### 🛑 6. Stop or Remove the Container

```sh
docker stop ai-medi-app-container
```

To remove:

```sh
docker rm ai-medi-app-container
```
**Note:**
1. Make sure you replace "your_groq_api_key_here" with your actual key.

2. If you also require ELEVENLABS_API_KEY, add -e ELEVENLABS_API_KEY="your_key" in the docker run command.

3. Ensure Docker Desktop or Engine is running before any of these steps.

## 🧪 How to Use


1. **Open the Gradio Web Interface**.
2. **Record your voice** using the microphone input.
3. **Upload a patient image** (e.g., a face photo).
4. **Submit** to receive:
   - The transcribed text of your speech.
   - The doctor's response based on your speech and the image.
   - The doctor's response as an audio file.

### 🔍 Example Interaction

#### Input

- **Voice**: "I have some redness on my cheek. Can you tell me what it is?"
- **Image**: Upload a clear photo of your face.

#### Output

- **Speech to Text**: "I have some redness on my cheek. Can you tell me what it is?"
- **Doctor's Response**: "With what I see, I think you have mild skin irritation possibly due to an allergic reaction, and keeping the area clean with gentle skincare should help."
- **Doctor's Voice**: (Audio playback of the above response)

## 📝 File Descriptions

- [`gradio_app.py`](gradio_app.py): Main entry point; defines the Gradio interface and orchestrates the workflow.
- [`brain_of_the_doctor.py`](brain_of_the_doctor.py): Handles image encoding and analysis using Groq's multimodal LLM.
- [`voice_of_the_patient.py`](voice_of_the_patient.py): Handles audio recording and speech-to-text transcription.
- [`voice_of_the_doctor.py`](voice_of_the_doctor.py): Handles text-to-speech conversion and audio playback.
- [`Pipfile`](Pipfile): Lists Python dependencies.
- `.env`: Stores API keys (do not share this file publicly).

## 🎛️ Customization

- **Change the system prompt** in [`gradio_app.py`](gradio_app.py) to adjust the doctor's persona or response style.
- **Switch models** by editing the model names in [`brain_of_the_doctor.py`](brain_of_the_doctor.py) and [`voice_of_the_patient.py`](voice_of_the_patient.py).

## ❗Troubleshooting

- Ensure your API keys are valid and have sufficient quota.
- Make sure `ffmpeg` and `portaudio` are installed and accessible.
- If you encounter microphone or audio device errors, check your system permissions.

## ⚠️ Disclaimer

This project is intended for educational use only. It does not provide real medical advice or diagnosis. Please consult a licensed healthcare provider for actual medical concerns.

---



