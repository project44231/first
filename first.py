import sys

print("Hello World")
# write a main function that prints hello world

def main():
    print("Hello World")
    print_full_name()

if __name__ == "__main__":
    main()

def print_full_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    # validate inputs
    if len(first_name) < 1 or len(last_name) < 1:
        print("Invalid input")
        print_full_name()

    full_name = first_name + " " + last_name
    print(full_name)




    
