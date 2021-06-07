#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
import string


def tokenize_sentence(sentence: str):
    snowball = SnowballStemmer(language="english")
    stop_words = stopwords.words("english")

    sanitized_sentence = sentence.replace("'", "").replace('"', "")
    tokens = word_tokenize(sanitized_sentence, language="english")
    tokens = [i for i in tokens if i not in string.punctuation]
    tokens = [i for i in tokens if i not in stop_words]
    tokens = [snowball.stem(i) for i in tokens]
    return tokens


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataAnalitics.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    tokenize_sentence()
