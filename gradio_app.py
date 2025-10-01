import os
import gradio as gr 
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio , transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

system_prompt = """You have to act as a professional doctor, and even though you are not, this is for learning purposes. 

Look at the image carefully. If anything looks medically wrong or concerning, mention it.

If you can make a differential diagnosis, suggest likely causes and simple remedies.

Do not include any numbers or special characters. Your response should be in one long paragraph with a maximum of two sentences.

Always speak like you're talking to a real patient, not as an AI model. Start your answer directly without saying things like 'In the image I see'. 

Instead say things like 'With what I see, I think you have...'. Make sure to still give an answer even if the user did not say anything."""



def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = ""
    
    if audio_filepath:
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
    
    if image_filepath:
        combined_query = system_prompt + " " + speech_to_text_output
        doctor_response = analyze_image_with_query(
            query=combined_query,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor_path = text_to_speech_with_gtts(
        input_text=doctor_response, out_filepath_mp3="final.mp3", out_filepath_wav="final.wav"
    )

    return speech_to_text_output, doctor_response, voice_of_doctor_path


iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
