print("1 Arabic\n2 English\n3 French")
choice=int(input("What's your choice ? "))
match choice :
    case 1:
        print("Arabic")
    case 2:
        print("English")
    case 3:
        print("French")
    case _ :
        print("i dont understand other languages !")