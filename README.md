# NewsTracker

This project is a Python tool that compares the coverage of a specific issue on Twitter and CNN and conducts sentiment analysis to classify the reactions of readers to the news.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries using pip: `pip install -r requirements.txt`
3. Run the `main.py` file to start the program.

## Usage

The program will ask for a keyword to search on Twitter and CNN. It will then scrape the latest 30 tweets and news articles containing the keyword and store them in separate lists. The program will then perform sentiment analysis on the texts to classify the reactions of readers to the news.

The results of the sentiment analysis will be displayed on a bar chart using the `matplotlib` library.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `tweepy` library
- `textblob` library
- `matplotlib` library
