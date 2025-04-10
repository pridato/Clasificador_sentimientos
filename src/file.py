import csv

def save_to_csv(text, sentiment_result, filename="sentiment_analysis_results.csv"):
    """
    Guarda el texto y su análisis de sentimiento en un archivo CSV.
    :param text: Texto original
    :param sentiment_result: Resultado del análisis de sentimiento
    :param filename: Nombre del archivo CSV
    """
    # Verificamos si el archivo ya existe
    try:
        with open(filename, mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            # Si el archivo está vacío, escribimos las cabeceras
            if file.tell() == 0:
                writer.writerow(["Texto", "Sentimiento", "Confianza"])  # Cabeceras del CSV
            # Escribimos una fila con el texto, sentimiento y confianza
            writer.writerow([text, sentiment_result[0]['label'], sentiment_result[0]['score']])
    except Exception as e:
        print(f"Error al guardar los resultados en el archivo CSV: {e}")