import yt_dlp
import os
from pydub import AudioSegment

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
        }],

        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        # Original filename
        original_filename = ydl.prepare_filename(info)

        # Change extension to wav
        filename = os.path.splitext(original_filename)[0] + ".wav"

        return filename



def convert_to_wav(input_path:str)->str:
    """Convert audio file to wav format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)  # Convert to mono and set frame rate
    audio.export(output_path, format="wav")
    return output_path


def chunk_audio(wav_path:str,chunk_minutes:int=10)->list:
    """Chunk the audio file into smaller segments."""
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes * 60 * 1000  # Convert minutes to milliseconds
    chunks = []
    
    for i,start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start:start + chunk_ms]
        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)
    
    return chunks

def process_input(source:str)->list:
    if source.startswith("http://") or source.startswith("https://"):
        print("Downloading Youtube URl and converting to wav...")
        wav_path = download_youtube_audio(source)
    else:
        print("Converting local audio file to wav...")
        wav_path = convert_to_wav(source)

    print("Chunking audio file...")
    chunks = chunk_audio(wav_path)
    print(f"Audio ready - {len(chunks)} chunks created.")
    return chunks
