import pyaudio
import wave
import logging
import whisper

# Configuración del logger
logging.basicConfig(level=logging.INFO)

whisper_model = whisper.load_model("base")

def listen_audio(file_name="output.wav", duration=5):
    """
    Graba audio desde el micrófono y lo guarda en un archivo WAV.
    :param file_name: Nombre del archivo a guardar
    :param duration: Duración de la grabación en segundos
    :return: Nombre del archivo guardado
    """
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    logging.info("Grabando audio...")

    frames = []

    for _ in range(0, int(44100 / 1024 * duration)):  # Graba durante la duración que se especifica
        data = stream.read(1024)
        frames.append(data)

    logging.info("Grabación terminada.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    _save_file(file_name, frames, p)
    text =  transcribe_audio(file_name)
    _delete_file(file_name)
    return text

def transcribe_audio(file_name):
    results = whisper_model.transcribe(file_name)
    logging.info("Transcripción terminada.")
    return results["text"]

def _save_file(file_name, frames, p):
    """
    Guarda el archivo de audio en formato WAV.
    :param file_name: Nombre del archivo a guardar
    :param frames: Datos de audio grabados
    :param p: Instancia de PyAudio
    :return: None
    """
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))

def _delete_file(file_name):
    """
    Elimina el archivo de audio.
    :param file_name: Nombre del archivo a eliminar
    :return: None
    """
    import os
    if os.path.exists(file_name):
        os.remove(file_name)
        logging.info(f"Archivo {file_name} eliminado.")
    else:
        logging.warning(f"El archivo {file_name} no existe.")