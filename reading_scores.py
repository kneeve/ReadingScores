import re
from typing import List


SENTENCE_MATCH = re.compile(r" (.*?[!.?]\"?)")
VOWEL_GROUP_MATCH = re.compile(r"[aiou]+e*|[^aiou]e[^aiou]|[^aeiou]y$", re.I)


def get_sentences_from_file(filename: str) -> List[str]:
    with open(filename) as f:
        text = f.read()
    text = text.replace('\n', ' ')
    sentences = SENTENCE_MATCH.findall(text)
    return sentences


def remove_punctuation_from_sentence(sentence: str) -> str:
    return sentence.replace('.', '').replace(',', '').replace('"', '')


def get_words_from_sentence(sentence: str) -> List[str]:
    return sentence.split()


def count_syllables_in_word(word: str) -> int:
    return len(VOWEL_GROUP_MATCH.findall(word))


def count_polysyllabic_words_in_sentence(sentence: str) -> int:
    sentence = remove_punctuation_from_sentence(sentence)
    words = get_words_from_sentence(sentence)
    counts = map(count_syllables_in_word, words)
    return len(list(filter(lambda c: c >= 3, counts)))
