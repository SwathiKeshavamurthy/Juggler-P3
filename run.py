def welcome_msg():
    """
    Print banner msg and intro text
    """
    print("Welcome")
    print("Juggler multi-program tool.")
    print(
        "Here is the list of all 5 programs.\n"
        "1 : Progarm1 - You can convert numbers into words between 1 to Trillion.\n"
        "2 : Progarm2 - You can get the weather information of the city you request.\n"
        "3 : Progarm3 - You can find out the Day of Birth.\n"
        "4 : Progarm4 - You can type a sentence to count all the characters including spaces separately and displayed.\n"
        "5 : Progarm5 - You should guess a number between 1-10.\n"
        )


def program1_convert_numbers_to_words():
    """
    Convert a given integer number into its word representation.
    """
    while True:
        try:
            def number_to_words(number):
                word_to_num = {
                    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                    70: 'seventy', 80: 'eighty', 90: 'ninety'
                }

                if 0 <= number < 20:
                    return word_to_num[number]
                elif 20 <= number < 100:
                    return word_to_num[number // 10 * 10] + ('' if number % 10 == 0 else ' ' + word_to_num[number % 10])
                elif 100 <= number < 1000:
                    return word_to_num[number // 100] + ' hundred' + (' and ' + number_to_words(number % 100) if number % 100 != 0 else '')
                elif 1000 <= number < 1000000:
                    return number_to_words(number // 1000) + ' thousand' + (' ' + number_to_words(number % 1000) if number % 1000 != 0 else '')
                elif 1000000 <= number < 1000000000:
                    return number_to_words(number // 1000000) + ' million' + (' ' + number_to_words(number % 1000000) if number % 1000000 != 0 else '')
                elif 1000000000 <= number < 1000000000000:
                    return number_to_words(number // 1000000000) + ' billion' + (' ' + number_to_words(number % 1000000000) if number % 1000000000 != 0 else '')
                elif 1000000000000 <= number < 1000000000000000:
                    return number_to_words(number // 1000000000000) + ' trillion' + (' ' + number_to_words(number % 1000000000000) if number % 1000000000000 != 0 else '')
                else:
                    return 'Number out of range'

            # Get user input
            user_input = int(input("Enter a whole number (1 to trillion): "))

            # Convert the input to words
            result = number_to_words(user_input)

            # Display the result
            print(f"Number in words: {result}")

            while True:
                choice = input("Press 'c' to continue or 'm' to return to the main menu or 'q' to exit the program: ")
                if choice == 'c':
                    break
                elif choice == 'm':
                    welcome_msg()
                    return
                elif choice == 'q':
                    print("Exiting program. Goodbye!")
                    exit()
                else:
                    print("Invalid choice. Please press 'c' to continue or 'm' to return to the main menu or 'q' to exit the program")

        except ValueError:
            print("Invalid input. Enter numbers only")


def program2_get_weather():
    """
    Get the current weather information for a specified city using the OpenWeatherMap API.
    """

    print('entered program2')
    pass


def program3_get_day_of_birth():
    """
    Get the day of the week on which a person was born based on their date of birth.
    """

    print('entered program3')
    pass


def program4_count_all_characters():
    """
    Count the occurrences of each character in the given text.
    """

    print('entered program4')
    pass


def program5_guess_a_number():
    """
    Guess a number game where the user tries to guess a secret number.
    """

    print('entered program5')
    pass


def main():
    # Calling the function to display the welcome message
    welcome_msg()

    while True:
        program_choice = input("Please choose a program and type a number between (1-5): ")

        if program_choice == '1':
            # Calling the function when the choice is 1
             program1_convert_numbers_to_words()
        elif program_choice == '2':
            # Calling the function when the choice is 2
            program2_get_weather()
        elif program_choice == '3':
            # Calling the function when the choice is 3
            program3_get_day_of_birth()
        elif program_choice == '4':
            # Calling the function when the choice is 4
            program4_count_all_characters()
        elif program_choice == '5':
            # Calling the function when the choice is 5
            program5_guess_a_number()
        else:
            print("Invalid choice. Please choose a program between 1 to 5.")

if __name__ == "__main__":
    main()