# Website/App Crash Reporter

![Report Summary](images/report_summary.png)

## Description

The Website/App Crash Reporter is a collection of Python scripts designed to streamline the process of extracting, classifying, and summarizing tweets related to website and app crashes. By leveraging OpenAI's natural language processing capabilities and integrating with Microsoft Teams, this toolkit provides a comprehensive solution for monitoring and analyzing user-reported issues on social media platforms, resulting in saving 100 hours of manual work every month.

## Problems

- Manually filtering out tweets, which is very labor-intensive work.
- Slow and time-consuming (100 hours every month).
- Manually setting keywords to search for relevant complaints.
- Missing out on other tweets indicating website/app issues.

## Solutions

- Leveraging OpenAI's natural language processing capabilities and integrating with Microsoft Teams to streamline the process of extracting, classifying, and summarizing tweets related to website and app crashes.

## Outcome

**Quantity:**
- Able to cover as many texts as you want; little need to set predefined keywords.

**Speed:**
- Takes less than a minute from extracting, predicting, to summarizing, resulting in saving 100 of hours every month.

**Accuracy:**
- Accuracy: 0.9090909090909091
- Precision: 0.8888888888888888
- Recall: 0.9846153846153847
- F1-score: 0.9343065693430657

**Scalability:**
- Able to support many other languages.
- Able to cover sources outside tweets.

## Built With

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![OpenAI](https://img.shields.io/badge/OpenAI-FF6600?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
- [![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
- [![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
- ![Webhook](https://img.shields.io/badge/Webhook-FFB6C1?style=for-the-badge&logo=webhook&logoColor=white)
- [![Microsoft Teams](https://img.shields.io/badge/Microsoft%20Teams-6264A7?style=for-the-badge&logo=microsoft-teams&logoColor=white)](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)

## Contents
- `scripts/`: Folder containing Python scripts for different functionalities.
- `data/`: Folder containing input JSON files.
- `results/`: Folder containing output CSV files.
- `images/`: Folder containing images used in the README.

## Features
- **Tweet Scraping**:
  - Extract tweets from JSON files and save them into a CSV file.
- **Classification**:
  - Predict whether a tweet indicates a website/app crash.
- **Summary Generation**:
  - Generates a summary of tweets indicating crashes by category.
- **Integration with Microsoft Teams**:
  - Sends tweet summaries to Microsoft Teams for collaborative communication.
- **Performance Evaluation**:
  - Evaluates the model performance of the tweet classification process.

## Example Data
To help users understand how the scripts work, we provide example input data in the form of JSON files containing tweets. Additionally, we include the expected output, which is a CSV file containing the extracted tweets from the input JSON files.

- **Input Data**:
  - `data/tweets1.json` to `data/tweets5.json`: Sample JSON files containing tweets.

- **Expected Output**:
  - `results/extracted_tweets.csv`: CSV file containing the extracted tweets from the input JSON files.

- **Example tweets (maybe/maybe not) reporting issues**:
  - "Maybe it's time to hire new web developers. The Morocco-Portugal website won't let you log in. Always the same error 'mandatory field cannot be left blank' although I fill that field."
  - "@SBICard_Connect The fix from your team only lasted for 1 day and now again I am facing the same issue and cannot login to my account. Tried the app as well as the website but getting the same error."
  - "A man who sued #Powerball and the #DCLottery for their website #error that showed he had the #winning numbers, making him believe he would receive $340 million last year, will

## Challenges and Learnings
- Collection of dataset due to lack of access to Twitter API at the moment (due to financial reasons), so scraped tweets from JSON files acquired from the web.

## Future Plans
- [ ] Cover other languages, which has been proven to be working.
- [ ] Expand to "predicting" website crashes based on tweets about big events/releases.
- [ ] Fine-tune classification models.
- [ ] Integrate with Twitter API for real-time tweet extraction.