# user_input = input("Enter a number: ")

# if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
#     print(f"The input '{user_input}' is an integer.")
# elif user_input.replace('.', '', 1).isdigit() or (user_input.startswith('-') and user_input[1:].replace('.', '', 1).isdigit()):
#     print(f"The input '{user_input}' is a float.")
# else:
#     print(f"The input '{user_input}' is neither an integer nor a float.")


user_input = input("Enter a number: ")

try:
    # Try converting to integer
    num = int(user_input)
    print("It's an integer.")
except ValueError:
    try:
        # If int fails, try converting to float
        num = float(user_input)
        print("It's a float.")
    except ValueError:
        print("It's not a number.")