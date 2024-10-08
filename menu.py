from HELLOWORLD.webscrapping.book_scrapping.books1 import books

USER_CHOICE = '''Enter one of the following 
-'b' to look at 5-star books
-'c' to look at the cheapest books
-'n' to get the next available book on the catalogue
-'q' to exit

Enter your choice:  
'''

def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)



def print_cheapest_books():
    best_books = sorted(books, key=lambda x: x.price)[:5]
    for book in best_books:
        print(book)

books_generator = (x for x in books)

def get_next_book():
    print(next(books_generator))


def menu():
    user_input = input(USER_CHOICE)

    user_choices = {
        'b': print_best_books,
        'c': print_cheapest_books,
        'n': get_next_book
    }
    while user_input != 'q':
        if user_input in user_choices:
            user_choices[user_input]()
        else:
            print('Please enter a valid command')
        user_input = input(USER_CHOICE)

menu()






# print('--BEST BOOKS--')
# print_best_books()
# print('--CHEAPEST BOOKS--')
# print_cheapest_books()