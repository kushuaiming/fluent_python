import re
import reprlib

RE_WORD = re.compile('\w+')


class Setence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SetenceIterator(self.words)

class SetenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self

if __name__ == '__main__':
    s = Setence('"The time has come," the Walrus said,')
    for word in s:
        print(word)