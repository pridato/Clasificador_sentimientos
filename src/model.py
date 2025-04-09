from transformers import pipeline

# Crear un pipeline para análisis de sentimientos
modelo = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")


def analyze_sentiment(text):
    """
    Función para analizar el sentimiento de un texto dado.
    :param text: Texto a analizar preprocesado
    :return: Resultado del análisis de sentimiento
    ¿Qué significan las etiquetas?
    '1 star': Muy negativo

    '2 stars': Negativo

    '3 stars': Neutro

    '4 stars': Positivo

    '5 stars': Muy positivo

    Score es la confianza del modelo en la predicción.
    """
    return modelo(text)
