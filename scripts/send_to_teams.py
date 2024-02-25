import requests

# Microsoft Teams webhook URL
teams_webhook_url = "YOUR_TEAMS_WEBHOOK_URL_HERE"

def send_to_teams(summary):
    """Send the tweet summary to Microsoft Teams."""
    # Prepare the payload to send to Microsoft Teams
    payload = {
        "text": summary
    }

    # Send the payload to Microsoft Teams using webhook
    response = requests.post(teams_webhook_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        print("Tweet summary sent to Microsoft Teams successfully.")
    else:
        print(f"Failed to send tweet summary to Microsoft Teams. Status code: {response.status_code}")

if __name__ == "__main__":
    # Import the generated tweet summary from tweet_summary.py
    from tweet_summary import tweet_summary
    
    # Send the tweet summary to Microsoft Teams
    send_to_teams(tweet_summary)
