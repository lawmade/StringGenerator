import random
import string

def generate_strings(count):
    chars = string.ascii_lowercase + string.digits  # a-z and 0-9
    for _ in range(count):
        result = ''.join(random.choice(chars) for _ in range(5))
        print(result)

def main():
    while True:
        try:
            num = int(input("How many would you like to Generate? (1-50): "))
            if 1 <= num <= 50:
                generate_strings(num)
            else:
                print("Please enter a number between 1 and 50.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # After generating, ask if they want to run again
        while True:
            print("\nPress 1 to regenerate, or 0 to exit.")
            choice = input("Your choice: ")
            if choice == '1':
                break  # Go back to the start of the loop
            elif choice == '0':
                print("Goodbye!")
                return
            else:
                print("Invalid input. Please press 1 or 0.")

if __name__ == "__main__":
    main()
