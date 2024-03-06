import nltk

FREQUENCY_OF_SQUID = 15

def is_vowel(ch: str) -> str:
    return ch.lower() in "aeiou"

def is_consonant(ch: str) -> str:
    return ch.isalpha() and not is_vowel(ch)

class LanguageError(Exception):

    def __init__(self) -> None:
        super().__init__("Only English (eng) and Russian (rus) are currently supported.")

class Replacer:

    def __init__(self, language: str = "eng") -> None:
        if language not in ("eng", "rus"):
            raise LanguageError()
        self.language = language

    def replace_squid(self, text: str) -> str:
        word_tokens = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(word_tokens, tagset="universal", lang=self.language)
        sentence = ""
        for (word, pos) in pos_tags:

            # this should never happen
            if word == "":
                continue

            # non-verbs + adjectives should just be added
            if pos != "VERB" and pos != "ADJ":
                if pos == "." or word == "'s":
                    sentence += word
                    continue
                else:
                    # most of the time, but non randomly, these words will not be squidified
                    if hash(word) % FREQUENCY_OF_SQUID != 0:
                        sentence += " " + word
                        continue

            # verbs and adjectives should be squidified
            first_vowel_index = 0
            is_capital = False
            for i, ch in enumerate(word):
                if is_vowel(ch):
                    first_vowel_index = i
                    is_capital = word[0].isupper()
                    break

            segment = " Sq" if is_capital else " sq"
            sentence += segment + word[first_vowel_index:]

        return sentence.lstrip()
