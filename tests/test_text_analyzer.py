import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
from text_analyzer import count_words_and_sentences

@pytest.mark.parametrize("text, word_count, sentence_count", [
    ("Hello! How are you?", 4, 2),
    ("one. two. three...", 3, 3),
    ("the exsample of the text.", 5, 1),
])
def test_count_words_and_sentences(text, word_count, sentence_count):
    with open("temp.txt", "w", encoding="utf-8") as f:
        f.write(text)
    assert count_words_and_sentences("temp.txt") == (word_count, sentence_count)

