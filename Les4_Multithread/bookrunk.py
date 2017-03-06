from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen
from concurrent.futures import ThreadPoolExecutor

REGEX = compile("#([\d,]+) in Books ")
AMZN = 'https://www.amazon.com/books-used-books-textbooks/b/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}


def getRanking(isbn):
    page = uopen('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print("- %r ranked %s" % (ISBNs[isbn], getRanking(isbn)))


def main():
    print("At ", ctime(), " on Amazon...")
    with ThreadPoolExecutor(3) as executor:
        for isbn in ISBNs:
            # _showRanking(isbn)
            # Thread(target=_showRanking, args=(isbn,)).start()
            executor.submit(_showRanking, isbn)

@register
def _atexit():
    print("All done at: ", ctime())

main()
