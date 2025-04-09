from model import analyze_sentiment
from preprocessing import preprocess_text

def main():
    # Texto de ejemplo
    text = """
    A mí me gusta salir a la calle
La buena gente de luz encendida
Los corazones que no caben dentro

Ay, cómo me gusta la vida

La primavera de brazos abiertos
Y las canciones que no son mentira
Ese milagro que vive en los besos
Ay, cómo me gusta la vida

Ir donde nos lleve el viento
Donde los sueños nos gritan
Donde me dicen de siempre amor

A mí lo que me gusta es eso
Ponerme a sonreír sin medida
Mojarme hasta calarme los huesos
Ay, a mí me gusta la vida

Culpable de sentir, lo confieso
Saber que siempre sana la herida
Si no hay por donde ir me lo invento
Ay, a mí me gusta la vida

Me gus-, me gus-, me gus-, me gus
Me gusta, me gusta la vida
Me gus-, me gus-, me gus-, me gus
Me gusta, me gusta la vida

A mí me gusta vivir el momento
Robarle tiempo a cualquier despedida
Salir detrás si alguien sale corriendo
Ay, cómo me gusta la vida

Saber que sientes lo mismo que siento
Saber jugar y empatar la partida
Saber también escuchar al silencio
Ay, cómo me gusta la vida

Ir donde nos lleve el viento
Donde los sueños nos gritan
Donde me dicen de siempre amor
A mí me gusta la vida

A mí lo que me gusta es eso
Ponerme a sonreír sin medida
Mojarme hasta calarme los huesos
Ay, a mí me gusta la vida

Culpable de sentir, lo confieso
Saber que siempre sana la herida
Si no hay por donde ir me lo invento
Ay, a mí me gusta la vida

Te gusta, te gusta, te gusta, te gusta
Te gusta, te gusta, te gusta
Me gusta, me gusta, me gusta, me gusta, ay

A mí lo que me gusta es eso
Ponerme a sonreír sin medida
Mojarme hasta calarme los huesos (funambulista)
Ay, a mí me gusta la vida

Culpable de sentir, lo confieso
Saber que siempre sana la herida
Si no hay por dónde ir, me lo invento
Ay, a mí me gusta la vida

Culpable de sentir, lo confieso
Saber que siempre sana la herida
Ay-ay-ay-ay, a mí me gusta la vida
A mí lo que me gusta es eso
Sin medida

A mí me gusta la vida
Me gus-, me gus-, me gus-, me gus-, me gus-
Me gusta la vida

    """

    # Preprocesar el texto
    processed_text = preprocess_text(text)

    print("Texto preprocesado:")
    print(processed_text)
    # Analizar el sentimiento del texto preprocesado
    sentiment_result = analyze_sentiment(processed_text)

    # Imprimir el resultado del análisis de sentimiento
    print(sentiment_result)

if __name__ == "__main__":
    main()
