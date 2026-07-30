"""
Script de prueba para verificar la conexión con la API de ElevenLabs.

Carga la API key desde un archivo .env, y genera un audio corto de
Text-to-Speech para confirmar que la autenticación y la conexión funcionan.

Uso:
    python test_connection.py
"""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Voz predeterminada de ElevenLabs ("George") usada solo para esta prueba.
DEFAULT_VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"
TEST_TEXT = "Hola, esta es una prueba de conexión con ElevenLabs."
OUTPUT_FILE = "test_output.mp3"


def main() -> None:
    if not API_KEY:
        print(
            "No se encontró ELEVENLABS_API_KEY.\n"
            "1. Copia .env.example a .env\n"
            "2. Pega tu API key real en el archivo .env\n"
            "3. Vuelve a ejecutar este script."
        )
        sys.exit(1)

    try:
        from elevenlabs.client import ElevenLabs
    except ImportError:
        print(
            "No se encontró el paquete 'elevenlabs'.\n"
            "Instala las dependencias con: pip install -r requirements.txt"
        )
        sys.exit(1)

    client = ElevenLabs(api_key=API_KEY)

    print("Conectando con ElevenLabs y generando audio de prueba...")

    try:
        audio = client.text_to_speech.convert(
            text=TEST_TEXT,
            voice_id=DEFAULT_VOICE_ID,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        with open(OUTPUT_FILE, "wb") as f:
            for chunk in audio:
                if isinstance(chunk, bytes):
                    f.write(chunk)

    except Exception as error:
        message = str(error)
        if "401" in message or "unauthorized" in message.lower():
            print(
                "Error de autenticación (401). Verifica que tu API key en "
                ".env sea correcta y que tenga permiso de Text to Speech."
            )
        else:
            print(f"Error al conectar con ElevenLabs: {message}")
        sys.exit(1)

    print(f"Conexión exitosa. Audio guardado en: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
