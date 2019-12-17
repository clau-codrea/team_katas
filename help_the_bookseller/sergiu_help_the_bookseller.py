def get_categories_dict(categories):
    return {category: 0 for category in categories}


def get_stock_infos(book):
    infos = book.split()
    return infos[0], int(infos[1])


def build_string(categories):
    string_as_list = []
    total_stock = 0
    for category, stock in categories.items():
        string_as_list.append(f"({category} : {stock})")
        if total_stock == 0:
            total_stock += stock
    return " - ".join(string_as_list) if total_stock > 0 else ''


def stock_list(listOfArt, listOfCat):
    if len(listOfArt) == 0 or len(listOfCat) == 0:
        return ''
    categories = get_categories_dict(listOfCat)
    for book in listOfArt:
        code, stock = get_stock_infos(book)
        if categories.get(code[0]) is not None:
            categories[code[0]] += stock
    return build_string(categories)
