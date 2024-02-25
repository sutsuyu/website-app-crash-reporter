import json
import csv

def extract_tweets_to_csv(input_files, output_file):
    tweets = []
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        try:
            entries = data['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][0]['entries']
            for entry in entries:
                try:
                    tweet_data = entry['content']['itemContent']['tweet_results']['result']
                    tweet_text = tweet_data['legacy']['full_text']
                    if 'urls' in tweet_data['legacy']['entities'] and len(tweet_data['legacy']['entities']['urls']) > 0:
                        tweet_url = tweet_data['legacy']['entities']['urls'][0]['expanded_url']
                    else:
                        tweet_url = f"https://twitter.com/{tweet_data['core']['user_results']['result']['legacy']['screen_name']}/status/{tweet_data['rest_id']}"
                    tweets.append([tweet_text, tweet_url])
                except KeyError:
                    pass  # Skip entries without tweet data
        except KeyError:
            print(f"Error: Invalid JSON structure in {input_file}. Please check the JSON file format.")

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Text', 'URL'])
        writer.writerows(tweets)

# List of input JSON files
input_files = ['tweets1.json', 'tweets2.json', 'tweets3.json', 'tweets4.json', 'tweets5.json']

# Output CSV file
output_file = 'extracted_tweets.csv'

# Extract tweets from input files and save to CSV
extract_tweets_to_csv(input_files, output_file)
