# Actividad — Fase 2: Manos a la obra con ElevenLabs

Es hora de poner manos a la acción con ElevenLabs. En esta fase puedes usar ElevenLabs directamente desde la plataforma, o integrado con Cursor.

## Cómo empezar

Elige una de estas dos opciones:

1. **Clonar el repositorio.** Ya viene con todo preparado.
2. **Usar el prompt de Cursor.** Copia el siguiente prompt y pégalo en la ventana de chat de Cursor, en una carpeta vacía, para que el agente cree el proyecto e instale automáticamente las dependencias:

```
Crea un proyecto Python mínimo en esta carpeta para conectarme con la API de ElevenLabs y probar Text-to-Speech. Necesito:

- .gitignore (excluyendo .env, venv/, __pycache__/, *.pyc, *.mp3)
- requirements.txt con elevenlabs y python-dotenv
- .env.example con la variable ELEVENLABS_API_KEY vacía
- test_connection.py que cargue la API key desde .env con python-dotenv, cree un cliente ElevenLabs, genere un audio corto de prueba con client.text_to_speech.convert() usando el modelo eleven_multilingual_v2, lo guarde como test_output.mp3, y maneje errores comunes (key faltante, key inválida/401) con mensajes claros
- README.md con instrucciones de setup (crear entorno virtual, instalar dependencias, configurar .env, ejecutar el script)

Después crea el entorno virtual, instala las dependencias, y avísame cuando necesites que yo pegue mi API key real en el archivo .env para poder ejecutar la prueba.
```

Después, en cualquiera de las dos opciones:

1. Genera tu **API key** desde la página de ElevenLabs.
2. Ponla en tu archivo `.env`.
3. Corre el script de Python para generar un audio de prueba.
4. Listo — ya puedes empezar a experimentar con las skills de ElevenLabs.

## Objetivo de la actividad

Convertir la narración elaborada previamente en la fase 1, en contenido para redes sociales.

## Tu contenido debe incluir

- El problema principal que expone el recurso analizado.
- Una narración accesible en español, de 3 a 5 minutos, para personas sin contexto del tema.
- Ideas clave explicadas sin jerga.
- Por qué el tema es importante.
- Un cierre: formas en que personas de distintos backgrounds pueden contribuir o aprender más sobre AI Safety.

## Dónde entregar

Coloca tu output en la carpeta [`Literature Review Output`](./Literature%20Review%20Output).

## Recomendaciones

- **No exagerar los hallazgos.** Valoramos un aporte de perspectiva, pero siempre basado en evidencia.
- **Enfoque.** Concéntrate en 1 a 3 ideas clave que quieras compartir con los demás participantes. No intentes abarcarlo todo — comparte lo que te pareció más sorprendente o interesante.
- **Formato técnico.** Todos los outputs deben estar en la carpeta compartida, ya que se proyectarán desde la misma computadora y no se cambiará de equipo durante el evento.

---

Nos vemos a las 6:30 para ver los trabajos, ¡con pizza!
