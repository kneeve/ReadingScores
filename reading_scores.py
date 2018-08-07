import re
from typing import List


SENTENCE_MATCH = re.compile(r" (.*?[!.?]\"?)")

def get_sentences_from_file(filename: str) -> List[str]:
    with open(filename) as f:
        text = f.read()
    text = text.replace('\n', ' ')
    sentences = SENTENCE_MATCH.findall(text)
    return sentences