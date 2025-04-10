from model import analyze_sentiment
from preprocessing import preprocess_text
from audio import listen_audio
from file import save_to_csv

def main():
    text = listen_audio()
    processed_text = preprocess_text(text)
    sentiment_result = analyze_sentiment(processed_text)
    print(f"Texto: {text}")
    print(f"Resultado del análisis de sentimiento: {sentiment_result}")


    save_to_csv(text, sentiment_result)

if __name__ == "__main__":
    main()
