from model import analyze_sentiment
from preprocessing import preprocess_text
from audio import listen_audio

def main():
    text = listen_audio()
    processed_text = preprocess_text(text)
    sentiment_result = analyze_sentiment(processed_text)
    print(f"Texto: {text}")
    print(f"Resultado del análisis de sentimiento: {sentiment_result}")


if __name__ == "__main__":
    main()
