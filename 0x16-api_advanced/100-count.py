#!/usr/bin/python3
"""Contains the count_words function"""
import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {
        "User-Agent": "YourAppName/1.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            for word in word_list:
                word = word.lower()
                count = title.lower().count(word)
                if count > 0:
                    if word in word_count:
                        word_count[word] += count
                    else:
                        word_count[word] = count

        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no matching posts.")

# Example usage
subreddit = "news"
word_list = ["javascript", "python", "java"]
count_words(subreddit, word_list)
