while True:
    try:
        number_1 = int(input("Enter a number 1 : "))
        number_2 = int(input("Enter a number 2 : "))

    except ValueError:
        print("Something Wrong Bro Please Enter a number")

    else:
        print(number_1 + number_2)
