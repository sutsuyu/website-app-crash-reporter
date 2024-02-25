from openai import OpenAI
import pandas as pd

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def generate_tweet_summary(tweets, links):
    """Generate a summary of tweets indicating website/app crashes by category."""
    messages = [
        {"role": "system", "content": "Filter out all tweets indicating website/app crash, and summarize them by category using company, brand name or website name, and others, and provide them with a summary of issues and corresponding all tweet links. Do not skip any possible skips or possible categories."},
    ]
    for tweet, link in zip(tweets, links):
        messages.append({"role": "user", "content": f"Tweet: {tweet}\nLink: {link}\n\n"})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,  # Adjust as needed
        n=1,  # Number of completions to generate
        stop=None,  # Specify early stopping criteria if needed
        temperature=1  # Controls the randomness of the generated completions
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    # Load the predicted tweets CSV file
    predicted_tweets = pd.read_csv('predicted_results.csv')

    # Extract tweets and links from the DataFrame
    tweets = predicted_tweets['Tweet'].tolist()
    links = predicted_tweets['URL'].tolist()

    # Generate a summary of tweets indicating website/app crashes by category
    tweet_summary = generate_tweet_summary(tweets, links)
    
    print(tweet_summary)  # Output the generated summary
