import fitz
import sys
import itertools


class TextCutter:
    def __init__(self, args):
        self.__args = args

    def read(self):
        pass

    def write(self):
        docs = map(lambda arg: fitz.open(arg), self.__args)
        pages = map(lambda doc: map(lambda page: doc[page].get_text(), range(len(doc))), docs)
        for text in itertools.chain(*pages):
            sys.stdout.buffer.write(text.encode('utf-8'))


if __name__ == '__main__':
    cutter = TextCutter(sys.argv[1:])
    cutter.read()
    cutter.write()

