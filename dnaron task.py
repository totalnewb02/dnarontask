def check_even_odd(your_number):
    your_number = int(your_number)
    if your_number % 2 == 0:
        return f'{your_number} is even number'
    else:
        return f'{your_number} is an odd number.'

# This keeps your manual input working normally when you run this file directly
if __name__ == '__main__':
    user_input = input('enter your number.')
    print(check_even_odd(user_input))