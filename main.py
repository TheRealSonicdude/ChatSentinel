# Press the green button in the gutter to run the script.
choice = 0

def reset_choice():
    choice = 0

if __name__ == '__main__':

    print("Welcome to Chat Sentinel.")

    while True:
        print("Please select an option.")
        print("1 - Load Chat Log")
        print("2 - Configure Keywords")
        print("3 - Generate Report")
        print("4 - Fetch Data From URL")
        print("5 - Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("1")
                reset_choice()
            case 2:
                print("2")
                reset_choice()
            case 3:
                print("3")
                reset_choice()
            case 4:
                print("4")
                reset_choice()
            case 5:
                print("5")
                print("You have exited the program.")
                print("To use the program again, press 'Run'.")
                break