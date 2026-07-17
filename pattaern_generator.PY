print("Welcome to Pattern Generator and Number Analyzer!")

while True:

    print("Menu")
    print("1. Generate Pattern")
    print("2. Analyze Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Invalid number of rows")
            continue

        print("Pattern:")

        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == "2":

        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        if end < start:
            print("Invalid Range")
            continue

        total = 0

        for number in range(start, end + 1):

            if number == 0:
                pass

            if number % 2 == 0:
                print("Number", number, "is Even")
            else:
                print("Number", number, "is Odd")

            total = total + number

        print("Sum of all numbers =", total)

    elif choice == "3":

        print("Thank you for using the Pattern Generator and Number Analyzer.")
        print("Goodbye!")
        break

    else:
        print("Invalid Choice. Please try again.")
