from openai import OpenAI
import csv

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def predict_website_crash(text):
    # Call OpenAI's chat completion endpoint
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you're helpful assistant. return 1 if a given text indicates website/app crash, otherwise return 0"},
            {"role": "user", "content": text}
        ]
    )
    # Extract the completion text
    result = response.choices[0].message.content
    return result

def read_tweets_from_csv(csv_file):
    tweets_urls = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tweets_urls.append((row['Tweet'], row['URL']))
    return tweets_urls

def main():
    # Read tweets and URLs from CSV
    tweets_urls = read_tweets_from_csv('extracted_tweets.csv')

    # Write predicted results to a new CSV file
    with open('predicted_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Tweet', 'URL', 'Predicted Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tweet, url in tweets_urls:
            predicted_value = predict_website_crash(tweet)
            writer.writerow({'Tweet': tweet, 'URL': url, 'Predicted Value': predicted_value})

if __name__ == "__main__":
    main()
