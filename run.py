import json
from os import getenv
from pathlib import Path
import os
import shutil
from image_processing import images_to_video, natural_sort_key
from pdf_processing import pdf_to_images
from moviepy.audio.io.AudioFileClip import AudioFileClip
from flask import Flask, render_template, request
from transformers import pipeline

from gtts import gTTS
from PyPDF2 import PdfReader
from moviepy.editor import VideoFileClip, concatenate_videoclips

app = Flask(__name__)

# Define the summarization pipeline using the facebook/bart-large-cnn model
summarizer = pipeline("summarization", model="pszemraj/long-t5-tglobal-base-16384-book-summary")

@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    if "pdf_file" not in request.files:
        return jsonify({"error": "No file part"})

    pdf_file = request.files["pdf_file"]
    if pdf_file.filename == "":
        return jsonify({"error": "No selected file"})

    # Save the uploaded PDF file
    pdf_path = os.path.join("uploads", pdf_file.filename)
    pdf_file.save(pdf_path)

    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)

    # Summarize the extracted text
    summary = summarize_text(text)

    # Generate audio from the summary
    audio_path = generate_audio(summary, pdf_file.filename)
    
    # Generate video from the audio and images from the research paper
    video_path = generate_video(audio_path, pdf_path)

    # Return the video URL
    video_url = f"http://localhost:5000/{video_path}"
    return jsonify({"video_url": video_url})


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def summarize_text(text):
    # Split the text into chunks of 200 words
    chunks = [text[i:i + 1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        summary += summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
    return summary

def generate_audio(text, filename):
    audio_path = os.path.join("uploads", filename.replace(".pdf", "_summary.mp3"))
    tts = gTTS(text=text, lang="en")
    tts.save(audio_path)
    return audio_path
def generate_video(audio_path, pdf_path):
    output_folder = "uploads"
    pdf_to_images(pdf_path, output_folder)
    images_folder = Path(output_folder)
    
    image_paths = sorted([str(image_path) for image_path in images_folder.glob('*.png')], key=natural_sort_key)

    # Setting the path for the output video file
    output_video_file = Path("uploads", "output_video.mp4")

    # Calculate the duration based on the length of the audio file
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    # Calculate the duration per page
    num_pages = len(image_paths)
    duration_per_page = audio_duration / num_pages
    print(duration_per_page)
    print (image_paths)

    # Creating the video from images
    # images_to_video(image_paths,   str(output_video_file), int(duration_per_page) )
    
    images_to_video(image_paths, str(output_video_file), fps=30, duration=int(duration_per_page))
    



    # Combine audio and video
    output_video_file_str = str(output_video_file)
    video_clip = VideoFileClip(output_video_file_str)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_video_file_str + ".mp4")

    return output_video_file_str




if __name__ == "__main__":
    app.run(debug=True)
