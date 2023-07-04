import os


class Library:
    def __init__(self):
        self.booklist_path = "booklist.txt"
        self.lendlist_path = "lendlist.txt"

        if not os.path.isfile(self.booklist_path):
            open(self.booklist_path, "a").close()

        if not os.path.isfile(self.lendlist_path):
            open(self.lendlist_path, "a").close()

    def add_books(self, bookname):
        print("--------------- ADD BOOK SECTION ----------------------------")
        with open(self.booklist_path, "r") as file:
            if bookname.upper() in file.read():
                print("Sorry, this book is already in the library")
            else:
                with open(self.booklist_path, "a") as file:
                    file.write(f"{bookname}\n")
                    print("Book added successfully!")

    def display_books(self):
        print("----------- Book List -------------")
        if os.stat(self.booklist_path).st_size == 0:
            print("There are no books in the library")
        else:
            with open(self.booklist_path, "r") as file:
                for index, book in enumerate(file, 1):
                    print(f"{index}: {book.rstrip()}")

    def lend_books(self, personname, bookname):
        lendlist = self._load_lendlist()
        if bookname.upper() in lendlist:
            print(f"Sorry, the book '{bookname}' is already lent by {lendlist[bookname]}. "
                  "It cannot be deleted until returned.")
        else:
            with open(self.lendlist_path, "a") as file:
                file.write(f"{bookname} {personname}\n")
            print("Book lent successfully!")

    def delete_books(self, bookname):
        with open(self.booklist_path, "r") as file:
            if bookname.upper() in file.read():
                lendlist = self._load_lendlist()
                if bookname.upper() in lendlist:
                    print(f"The book '{bookname}' is currently lent by {lendlist[bookname]}. "
                          "It cannot be deleted until returned.")
                else:
                    with open(self.booklist_path, "r") as file:
                        books = file.readlines()

                    with open(self.booklist_path, "w") as file:
                        for line in books:
                            if line.rstrip("\n").upper() != bookname.upper():
                                file.write(line)
                    print("Book deleted successfully!")
            else:
                print("This book is not present in the library")

    def lend_list(self):
        print("--------------- Lend List -----------------")
        lendlist = self._load_lendlist()
        if len(lendlist) == 0:
            print("No books are currently lent by any person")
        else:
            for book, person in lendlist.items():
                print(f"{book} lent by {person}")

    def delete_all_books(self):
        print("Are you sure you want to delete all books and lending records? (y/n)")
        choice = input()
        if choice.lower() == "y":
            if os.stat(self.booklist_path).st_size != 0:
                open(self.booklist_path, "w").close()

            if os.stat(self.lendlist_path).st_size != 0:
                open(self.lendlist_path, "w").close()

            print("All data has been successfully deleted")
        else:
            print("Operation canceled")

    def return_books(self, personname, bookname):
        lendlist = self._load_lendlist()
        if bookname.upper() in lendlist and lendlist[bookname.upper()]:
            with open(self.lendlist_path, "r") as file:
                data = file.readlines()

            with open(self.lendlist_path, "w") as file:
                for line in data:
                    if not line.startswith(f"{bookname} {personname}"):
                        file.write(line)

            print("Your book has been successfully returned")
        else:
            print(f"The book '{bookname}' is not currently lent to {personname}")

    def _load_lendlist(self):
        lendlist = {}
        with open(self.lendlist_path, "r") as file:
            for line in file:
                book, person = line.strip().split(" ", 1)
                lendlist[book.upper()] = person
        return lendlist


def main():
    print("Welcome to Library Management")
    library = Library()
    while True:
       
        print("1. Add Books")
        print("2. Display Books")
        print("3. Lend Books")
        print("4. Book Lend List")
        print("5. Return Books")
        print("6. Delete All Books")
        print("7. Delete Books")
        print("8. Exit")
        print("------------------------")
        print("Enter Your Choice:")
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a numerical choice.")
            continue

        if choice == 1:
            print("Enter book name:")
            bookname = input().strip()
            library.add_books(bookname)

        elif choice == 2:
            library.display_books()

        elif choice == 3:
            print("Enter Your name:")
            personname = input().strip()
            print("Enter book name:")
            bookname = input().strip()
            library.lend_books(personname, bookname)

        elif choice == 4:
            library.lend_list()

        elif choice == 5:
            print("Enter Your name:")
            personname = input().strip()
            print("Enter book name:")
            bookname = input().strip()
            library.return_books(personname, bookname)

        elif choice == 6:
            library.delete_all_books()

        elif choice == 7:
            print("Enter Book name:")
            bookname = input().strip()
            library.delete_books(bookname)

        elif choice == 8:
            exit()

        else:
            print("Invalid choice. Please enter a valid choice.")


if __name__ == '__main__':
    main()
