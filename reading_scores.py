import re
import math
from typing import List


# Constants
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


def compute_smog_score(filename: str) -> int:
    sentences = get_sentences_from_file(filename)
    sentence_count = len(sentences)
    polysyllabic_word_count = sum(list(map(count_polysyllabic_words_in_sentence, sentences)))
    # Using formula from wikipedia's SMOG score page
    return 1.0430 * (math.sqrt(polysyllabic_word_count * (30 / sentence_count))) + 3.1291
