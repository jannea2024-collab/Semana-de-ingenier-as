# Conexión con ElevenLabs

Proyecto mínimo para verificar la conexión con la API de [ElevenLabs](https://elevenlabs.io) usando Python.

## Requisitos previos

- Python 3.9 o superior.
- Una API key de ElevenLabs (Dashboard → Developers → API Keys → Create Key, con acceso a Text to Speech).

## Configuración

1. Crea y activa un entorno virtual:
  ```bash
   python3 -m venv venv
   source venv/bin/activate
  ```
2. Instala las dependencias:
  ```bash
   pip install -r requirements.txt
  ```
3. Copia el archivo de ejemplo de variables de entorno y agrega tu API key real:
  ```bash
   cp .env.example .env
  ```
   Luego edita `.env` y pega tu key:
   El archivo `.env` está incluido en `.gitignore`, así que nunca se subirá al control de versiones.



## Probar la conexión

Ejecuta el script de prueba:

```bash
python test_connection.py
```

Si todo está bien configurado, verás un mensaje de éxito y se generará un archivo `test_output.mp3` con un audio corto de prueba en español.

## Solución de problemas

- **"No se encontró ELEVENLABS_API_KEY"**: revisa que el archivo `.env` exista y tenga la variable definida.
- **Error 401 / Unauthorized**: la API key es inválida, expiró, o no tiene permiso de Text to Speech habilitado.
- `ModuleNotFoundError: elevenlabs`: asegúrate de haber activado el entorno virtual y ejecutado `pip install -r requirements.txt`.



## Próximos pasos

Con la conexión verificada, el siguiente paso es definir la integración específica que se quiera construir (por ejemplo, una API/backend con FastAPI, un agente conversacional, etc.).