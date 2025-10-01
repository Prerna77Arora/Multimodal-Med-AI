# 1a) setup text to speech model with gtts 
import os
from gtts import gTTS 
def text_to_speech_with_gtts_old(input_text, out_filepath):
      language="en"
      audioobj=gTTS(
            text=input_text,
            lang=language,
            slow=False

      )

      audioobj.save(out_filepath)


input_text="Hey I am your vitual doctor doctor. How can I help you today?"     
#text_to_speech_with_gtts_old(input_text=input_text , out_filepath="gtts_test.mp3")

# use model for text output to voice
import os
import platform
import subprocess
from gtts import gTTS
from pydub import AudioSegment

def text_to_speech_with_gtts(input_text, out_filepath_mp3, out_filepath_wav):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(out_filepath_mp3)

    # Convert MP3 to WAV for Windows SoundPlayer
    sound = AudioSegment.from_mp3(out_filepath_mp3)
    sound.export(out_filepath_wav, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', out_filepath_wav])
        elif os_name == "Windows":
            subprocess.run([
                'powershell',
                '-c',
                f'(New-Object Media.SoundPlayer "{out_filepath_wav}").PlaySync();'
            ])
        elif os_name == "Linux":
            subprocess.run(['aplay', out_filepath_wav])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text ="Hi! I am your virtual doctor. How can I help you today?"
text_to_speech_with_gtts(
    input_text=input_text,
    out_filepath_mp3="gtts_test.mp3",
    out_filepath_wav="gtts_test.wav"
)
