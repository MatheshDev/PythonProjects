def main():
    print("Hello World")
    
    try:
        bookList = [] #empty List
        
        

        infile = open("bookList.txt","r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    
    except FileNotFoundError:
        print("The <bookList.txt> is not found")

    choice = 0
    while choice != 4:

        print("***Python Book Manager***")

        print("1) Add a Book")
        print("2) Search a Book")
        print("3) View all books")
        print("4) Exit")

        choice = int(input("Choose your Operation : "))

        if choice == 1:
            print("Adding a book..")
            nBook = input("Name of the Book : ")
            nAuthor = input("Name of the Author : ")
            nPages = input("Enter number of Pages : ")
            bookList.append([nBook,nAuthor,nPages])

        elif choice == 2:
            print("Searching..")
            key = input("Enter the name of the book : ")
            for book in bookList:
                if key in book:
                    for i in book:
                        print("\t",i)     
                else:
                    print("Book not found, Please check if you have any spelling errors.")   

        elif choice == 3:
            print("Collecting all book data")
            for i in bookList:
                print(i)

        elif choice == 4:
            print("Program Terminated")
        
        outfile = open("bookList.txt", "w")
        for book in bookList:
            outfile.write(",".join(book) + "\n")
        outfile.close()
if __name__ == "__main__":
    main()