import nltk

from squidify.replacer import Replacer

if __name__ == "__main__":
    nltk.download("punkt", quiet=True)
    nltk.download("averaged_perceptron_tagger", quiet=True)
    nltk.download("universal_tagset", quiet=True)

    replacer = Replacer()

    print("Input:")
    text = input()
    print("Output:")
    print(replacer.replace_squid(text))
