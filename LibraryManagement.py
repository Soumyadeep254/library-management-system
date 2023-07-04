import os

#Important Component of Library Management
if os.path.isfile("booklist.txt"):
      pass
else:
      file = open("booklist.txt","a+")

if os.path.isfile("lendlist.txt"):
      pass
else:
      file = open("lendlist.txt","a+")

#Library Management made by Akash khandelwal
class Library():



    def addbooks(self,bookname):
       print("********************ADD BOOK SECTION*****************************************")
       with open("booklist.txt") as op:
           if bookname in op.read():
                 print("Sorry this book is already in Library")
           else:
               with open("booklist.txt","a") as op:
                     op.write(bookname+"\n")
                     print("Book Added Successfully!!!!!!!!")

    def displaybooks(self):

         print("************************Book List***********************************")
         if os.stat("booklist.txt").st_size == 0:
              print("Here is No Data")
         else:
             list = []
             with open("booklist.txt") as op:
                for book in op:
                     list.append(book)

             for index,book in enumerate(list):
                   print(index,": "+book)



    def lendbooks(self,Personname,bookname):
         d={}
         with open("booklist.txt") as op:
              if bookname in op.read():
                   print("")
                   with open("lendlist.txt") as f:
                       if bookname in f.read():
                           print(" ")
                           with open("lendlist.txt") as op:
                                for line in op:
                                    (key,value) = line.split()
                                    d[(key)] = value

                                print("Sorry this book is lend by",d[bookname])

                       else:
                           with open("lendlist.txt","a") as op:
                               op.write(bookname+" "+Personname+"\n")
                               print("Book lend Successfully!!!")
              else:
                  print("Sorry this book is not available in Library")



    def deletebooks(self,bookname):
        if os.stat("booklist.txt").st_size == 0:
            print("Library has no Books to delete")

        else:
            with open("booklist.txt") as op:
                if bookname in op.read():
                    print("")
                    with open("lendlist.txt") as f:
                        if bookname in f.read():
                            print("this book is issued by someone it can not be deleted until return"+f.readline())

                        else:
                            print("Book Deleted Successfully")
                            with open("booklist.txt") as op:
                                data = op.readlines()

                            with open("booklist.txt","w") as f:
                                for line in data:
                                    if line.strip("\n") != bookname:
                                        f.write(line)



                else:
                     print("This book is not present in this library")

    def lendlist(self):
        if os.stat("lendlist.txt").st_size == 0:
            print("No Book lend by any Person")
        else:
            print("*********************Lend List****************************")
            with open("lendlist.txt") as op:
                 for Person in op:
                     print(Person)



    def deleteAllbooks(self):
        print("Are You Sure You Will lose all data regarding lendlist?(y/n)")
        ch = input()
        if ch.upper() == "Y":
            if os.stat("booklist.txt").st_size != 0:
                   print("All DATA has been Successfully Deleted")
                   with open("booklist.txt","w") as op:
                     op.seek(0)
                     op.truncate()


                   with open("lendlist.txt","w") as f:
                      f.seek(0)
                      f.truncate()

            else:
                 print("File has been Already Empty")

        else:
             pass

    def  returnbooks(self,Personname,bookname):
           with open("booklist.txt") as op:
               if bookname in op.read():
                   print("")
                   with open("lendlist.txt") as op:
                         if bookname and Personname in op.read():
                             print("")
                             with open("lendlist.txt") as f:
                               data = f.readlines()
                             print("Your Book has Successfully Return")
                             with open("lendlist.txt","w") as op:
                                for line in data:
                                 if line.strip("\n") != (bookname+" "+Personname):
                                     op.write(line)

                         else:
                             print("This "+bookname+" book is not lend to "+Personname)

               else:
                   print("You have Written Wrong book name")
def main():
    print("Welcome to Library Management")
    harry = Library()
    while True:
        print("*****************************************************************************************************")
        print("1.Add Books")
        print("2.Display Books")
        print("3.Lend Books")
        print("4.Book lend list")
        print("5.Return books")
        print("6.Delete All books")
        print("7.Delete Books")
        print("8.Exit")
        print("*****************************************************************************************************")
        print("Enter Your Choice?")
        try:
           _input =int(input())

        except Exception as e:
                print("You must be only enter numerical value!!")

        if _input == 1:
              print("Enter book name:")
              _input2 = input()
              harry.addbooks(_input2.upper())

        elif _input == 2:
              harry.displaybooks()


        elif _input == 3:
               print("Enter Your name:")
               _input3 = input()
               print("Enter book name:")
               _input4 = input()
               harry.lendbooks(_input3.upper(),_input4.upper())

        elif _input == 4:
              harry.lendlist()


        elif _input == 5:
              print("Enter Your name:")
              _input5 = input()
              print("Enter book name:")
              _input6 = input()
              harry.returnbooks(_input5.upper(),_input6.upper())


        elif _input == 6:
               harry.deleteAllbooks()

        elif _input ==  7:
                print("Enter Book name")
                _input7 = input()
                harry.deletebooks(_input7.upper())

        elif _input == 8:
            exit()


        else:
            print("Invalid Input")

if __name__ == '__main__':
            main()