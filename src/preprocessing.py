import spacy

# Cargar el modelo de SpaCy para procesamiento de texto
nlp = spacy.load("es_core_news_sm")

def preprocess_text(text):
    """
    Usar SpaCy para tokenizar, eliminar stopwords y hacer lematización. Es decir limpiamos el texto para procesarlo
    :param text: Texto a procesar
    :return: Texto procesado
    """
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

