import re

book_re = re.compile('\A(?P<code>[A-Z]{3,})\s(?P<quantity>[0-9]+)\Z')

class Book:
    def __init__(self, code, quantity):
        self.code = code
        self.category = code[0]
        self.quantity = int(quantity)


    @classmethod
    def from_string(cls, str):
        matched_book = book_re.match(str)

        return cls(matched_book.group('code'), matched_book.group('quantity'))

class Stock:
    def __init__(self, books):
        self.books = books


    def filter_stock(self, categories):
        return Stock(list(filter(lambda book: book.category in categories, self.books)))


    def _count(self):
        count = {}
        for book in self.books:
            if book.category in count:
                count[book.category] += book.quantity
            else:
                count[book.category] = book.quantity

        return count


    def to_string(self, list_of_cat):
        count = self._count()
        formatted = [f'({category} : {count[category] if category in count else 0})' for category in list_of_cat]
        return ' - '.join(formatted)


def stock_list(list_of_art, list_of_cat):
    print(list_of_art, list_of_cat)
    if not list_of_art or not list_of_cat:
        return ''

    stock = Stock([Book.from_string(str) for str in list_of_art])
    return stock.filter_stock(list_of_cat).to_string(list_of_cat)
