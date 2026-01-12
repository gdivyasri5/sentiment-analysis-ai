from textblob import TextBlob

def analyze_sentiment(text):
    # TextBlob calculates 'polarity'
    # Polarity ranges from -1 (Very Negative) to +1 (Very Positive)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    print("--- ✨ SENTIMENT ANALYSIS AI ✨ ---")
    print("Type a sentence to check its emotion (or 'exit' to quit).")
    
    while True:
        user_input = input("\nEnter text: ")
        if user_input.lower() == 'exit':
            break
        
        result = analyze_sentiment(user_input)
        print(f"👉 Sentiment: {result}")