#!/usr/bin/python3
"""
parses the title of all hot articles, and prints a
sorted count of given keywords.
"""
import requests, json


def count_words(subreddit, word_list):
  """
  Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
  Args:
    subreddit: The name of the subreddit to query.
    word_list: A list of keywords to search for.
  """
  # Get the hot articles from the subreddit.
  hot_articles = reddit.subreddit(subreddit).hot(limit=100)
  # Iterate over the hot articles and parse the title for each keyword.
  for article in hot_articles:
    for word in word_list:
      # Check if the keyword appears in the title.
      if word.lower() in article.title.lower():
        # Increment the count of the keyword.
        word_count[word.lower()] += 1
  # Sort the keywords by their count in descending order.
  word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
  # Print the sorted count of keywords.
  for word, count in word_count:
    print(f"{word}: {count}")
