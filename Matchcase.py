menu=int(input("enter the menu number: " ))
match menu:
    case 1: print("idly")
    case 2: print("dosa")   
    case 3: print("pongal")
    case _: print("invalid menu number")