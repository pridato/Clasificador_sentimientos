# Análisis de Sentimientos en Textos

Este proyecto tiene como objetivo analizar sentimientos en textos mediante el uso de un modelo de análisis de sentimientos, procesando audio grabado, convirtiéndolo a texto y analizando los sentimientos de los mensajes. Los resultados se almacenan en un archivo CSV y se realizan análisis adicionales a través de visualizaciones con Python.

## Descripción del Proyecto
Este proyecto se compone de varias etapas que incluyen:

1. Captura de audio: El proyecto graba el audio desde el micrófono y lo guarda como un archivo WAV.

2. Conversión de audio a texto: Utiliza el modelo de Whisper de OpenAI para convertir el audio grabado a texto.

3. Análisis de sentimientos: El texto generado es procesado para determinar su sentimiento (por ejemplo, positivo, negativo o neutral) y la confianza del análisis.

4. Almacenamiento de datos: Los resultados del análisis de sentimientos, junto con la confianza asociada, se almacenan en un archivo CSV.

5. Análisis de datos: A través de un Jupyter Notebook, se realiza un análisis y visualización de los datos del CSV, incluyendo distribuciones de sentimientos y la creación de nubes de palabras.

Requisitos
Para ejecutar este proyecto, necesitarás tener instalados los siguientes requisitos:

Python 3.x

Jupyter Notebook

Librerías necesarias:
```
pip install pandas numpy matplotlib seaborn wordcloud openai pydub
```

- PyAudio: Necesario para grabar audio desde el micrófono.

- Whisper: Modelo de OpenAI para transcripción de audio a texto.

- Pandas: Para manipular y analizar los datos en formato CSV.

- Matplotlib: Para crear visualizaciones gráficas.

- WordCloud: Para generar nubes de palabras a partir de los textos.


Uso
#### 1. Grabación de Audio y Análisis de Sentimiento

El proceso comienza grabando audio desde el micrófono utilizando pyaudio, convirtiéndolo a texto utilizando el modelo Whisper, y luego analizando el sentimiento del texto utilizando un modelo preentrenado.

El flujo básico del proceso es el siguiente:

   1. El script audio.py graba un mensaje de audio y lo guarda en un archivo .wav.

   2. El archivo de audio grabado es transcrito a texto con el modelo Whisper.

   3. El texto es procesado y analizado utilizando un análisis de sentimiento (con un modelo de análisis de sentimientos simple).

Este análisis se guarda en un archivo CSV, con la estructura siguiente:

```csv
Texto,Sentimiento,Confianza
"Texto de ejemplo",5 stars,0.9
"Otro ejemplo",1 star,0.8
```

#### 2. Análisis de Datos en Jupyter Notebook

Una vez que tienes el archivo CSV con los datos de sentimiento, puedes abrir el archivo analisis_sentimientos.ipynb en Jupyter Notebook para realizar un análisis más detallado.

El notebook realiza lo siguiente:

- Carga de los datos desde el archivo CSV.
- Visualización de la distribución de sentimientos.
- Histograma de la confianza asociada con cada sentimiento.
- Generación de una nube de palabras a partir de los textos.
- Análisis de la confianza promedio por tipo de sentimiento.

## Ejecución

Para ejecutar el notebook, abre una terminal o consola y navega hasta el directorio donde se encuentra el archivo analisis_sentimientos.ipynb. Luego, ejecuta:
```bash
jupyter notebook analisis_sentimientos.ipynb
```
Esto abrirá Jupyter en tu navegador. Desde ahí, abre el archivo analisis_sentimientos.ipynb y ejecuta todas las celdas para analizar los datos.
