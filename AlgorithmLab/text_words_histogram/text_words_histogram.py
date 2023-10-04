from collections import defaultdict


def calc_words(text):
    counter = defaultdict(int)
    words = text.split()
    for wrd in words:
        v = wrd.strip(".,!:").lower()
        if v:
            counter[v] += 1
    return counter
