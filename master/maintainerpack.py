def readmaster():
    import pickle
    B1 = {"BookNo":1107, "Book_name": "Dan Brown: ORIGIN"}
    B2 = {"BookNo":2207, "Book_name": "Dan Brown: DIGITAL FORTRESS"}
    B3 = {"BookNo":3307, "Book_name": "Dan Brown: DECEPTION POINT"}
    B4 = {"BookNo":4407, "Book_name": "Dan Brown: INFERNO"}
    B5 = {"BookNo":5507, "Book_name": "Dan Brown: THE DA VINCI CODE"}
    with open("BOOK.dat", "w+b") as filemaster:
        pickle.dump((B1, B2, B3, B4, B5), filemaster)
    print("File - op completed....")    
    xono = int(input("Enter the book No."))
    fx = open("BOOK.dat","rb")
    with open("BOOK.dat", "rb") as filemaster:
        dump = pickle.load(filemaster) 
        for i in dump:
            x = i["BookNo"]
            if x == xono:
                print(i)
            else:
                print("Book not found in current repository......")

readmaster()
