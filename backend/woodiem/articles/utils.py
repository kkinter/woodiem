import re


def count_words(text):
    words = re.findall(r"\w+", text)
    num_words = len(words)
    return num_words


def calculate_read_time(article):
    words_per_minute = 200

    title = count_words(article.title)
    body = count_words(article.body)
    description = count_words(article.description)

    total = title + body + description

    read_time_minutes = total / words_per_minute

    return round(read_time_minutes)
