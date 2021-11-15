# используется для сортировки
from operator import itemgetter
 
class Book:
    """Книга"""
    def __init__(self, id, name, cost, lib_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.lib_id = lib_id
 
class Library:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class BookLibrary:
    """
    'Книги библиотеки' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lib_id, book_id):
        self.lib_id = lib_id
        self.book_id = book_id
 
# Библиотеки
libs = [
    Library(1, 'Центральная библиотека'),
    Library(2, 'Пушкинская'),
    Library(3, 'Московская'),
 
    Library(11, 'Абрамовская'),
    Library(22, 'Аппель'),
    Library(33, 'Универсальная'),
]
 
# Книги
books = [
    Book(1, 'Белый бим черное ухо', 2500, 1),
    Book(2, 'Искра жизни', 1000, 2),
    Book(3, 'Общество потребления', 500, 3),
    Book(4, 'Искусство любить', 1100, 3),
    Book(5, 'О дивный новый мир', 900, 3),
]
 
libs_books = [
    BookLibrary(1,1),
    BookLibrary(2,2),
    BookLibrary(3,3),
    BookLibrary(3,4),
    BookLibrary(3,5),
 
    BookLibrary(11,1),
    BookLibrary(22,2),
    BookLibrary(33,1),
    BookLibrary(33,2),
    BookLibrary(33,5),
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(b.name, b.cost, l.name) 
        for l in libs
        for b in books 
        if b.lib_id==l.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, lb.lib_id, lb.book_id) 
        for l in libs 
        for lb in libs_books
        if l.id==lb.lib_id]
    
    many_to_many = [(b.name, b.cost, lib_name) 
        for lib_name, lib_id, book_id in many_to_many_temp
        for b in books if b.id==book_id]
 
    print('Задание Д1')
    res_11 = [(b.name, b.cost, l.name) 
        for l in libs 
        for b in books
        if b.lib_id==l.id and b.cost>1000]
    print(res_11)
    
    print('\nЗадание Д2')
    res_12_unsorted = []
    # Перебираем все библиотеки
    for l in libs:
        # Список книг библиотеки
        b_lib = list(filter(lambda i: i[2]==l.name, one_to_many))
        # Если библиотека не пустая   
        if len(b_lib) > 0:
            # Цены книг
            b_costs = [cost for _,cost,_ in b_lib]
            # Средняя цена книг
            b_costs_mean = sum(b_costs) / len(b_costs)
            res_12_unsorted.append((l.name, b_costs_mean))
 
    # Сортировка по средней зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
    
    print('\nЗадание Д3')
    res_13 = {}
    # Перебираем все библиотеки
    for l in libs:
        if l.name.lower().startswith('а'):
            # Список книг библиотеки
            books_of_l = list(filter(lambda i: i[2]==l.name, many_to_many))
            # Только названия книг
            books_names = [x for x,_,_ in books_of_l]
            # Добавляем результат в словарь
            # ключ - библиотека, значение - список названий
            res_13[l.name] = books_names
 
    print(res_13)
 
if __name__ == '__main__':
    main()
