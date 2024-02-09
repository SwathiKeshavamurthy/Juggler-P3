import os
import requests
import json
import pytz
import datetime
import random
from dotenv import load_dotenv

# WELCOME MEESAGE FUNCTION
def welcome_msg():
    """
    Print banner msg and intro text
    """
    print("\nWelcome")
    print("Juggler multi-program tool.")
    print(
        "\nHere is the list of all 5 programs.\n"
        "1 : Progarm1 - You can convert numbers into words between 1 to Trillion.\n"
        "2 : Progarm2 - You can get the weather information of the city you request.\n"
        "3 : Progarm3 - You can find out the Day of Birth.\n"
        "4 : Progarm4 - You can type a sentence to count all the characters including spaces separately and displayed.\n"
        "5 : Progarm5 - You should guess a number between 1-25.\n"
        )


# TWO FUNCTIONS FOR GET WEATHER PROGRAM"
def get_api_key():
    """
    Get the OpenWeatherMap API key from the environment variable.
    """
    load_dotenv()
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Make sure to set the OPENWEATHERMAP_API_KEY environment variable.")
    return api_key

def get_weather(api_key, city):
    """
    Get the current weather information for a specified city using the OpenWeatherMap API.
    Args:
    - api_key: The API key for accessing the OpenWeatherMap API.
    - city: The name of the city for which weather information is requested.
    Returns:
    - A dictionary containing the weather information.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


# PROGRAM1: CONVERT NUMBERS INTO WORDS FUNCTION
def program1_convert_numbers_to_words():
    """
    Convert a given integer number into its word representation.
    Parameters:
    - number (int): The integer number to be converted into words. Should be within the range.
    Returns:
    - str: The word representation of the input number.
    Raises:
    - ValueError: If the input number is outside the valid range.
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
                    return '\nNumber out of range'

            # Get user input
            user_input = int(input("\nEnter a whole number (1 to trillion): "))

            # Convert the input to words
            result = number_to_words(user_input)

            # Display the result
            print(f"\nNumber in words: {result}")

#Add loop to handle user choice of continuing the same program, returning to the main menu, or exiting the program.

            while True:
                choice = input("\nPress 'c' to continue or 'm' to return to the main menu or 'q' to exit the program: ")
                if choice == 'c':
                    break
                elif choice == 'm':
                    welcome_msg()
                    return
                elif choice == 'q':
                    print("\nExiting program. Goodbye!\n")
                    exit()
                else:
                    print("\nInvalid choice. Please press 'c' to continue or 'm' to return to the main menu or 'q' to exit the program")

        except ValueError:
            print("\nInvalid input. Enter numbers only")


# PROGRAM2: GET WEATHER FUNCTION
def program2_get_weather():
    """
    Get the current weather information for a specified city using the OpenWeatherMap API.
    """
    while True:
        api_key = get_api_key()
        city = input("\nEnter city name: ").strip()
        weather_data = get_weather(api_key, city)

        if weather_data.get('cod') == '404':
            print("\nCity not found. Please check the city name and try again.")
        else: 
            city = weather_data['name']   
            
            # Calculate local time by adding timezone offset
            timezone_offset = datetime.timedelta(seconds=weather_data['timezone'])
            local_time = datetime.datetime.fromtimestamp(weather_data['dt'], datetime.timezone.utc) + timezone_offset
            local_time_str = local_time.strftime('%H:%M:%S')
        
            weather_description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            print(f"Weather in {city}")
            print(f"Date and Time: {local_time}")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")


#Add loop to handle user choice of continuing the same program, returning to the main menu, or exiting the program.

        while True:
            choice = input("\nPress 'c' to continue or 'm' to return to the main menu or 'q' to exit the program: ")
            if choice == 'c':
                break
            elif choice == 'm':
                welcome_msg()
                return
            elif choice == 'q':
                print("\nExiting program. Goodbye!\n")
                exit()
            else:
                print("\nInvalid choice. Please press 'c' to continue or 'm' to return to the main menu or 'q' to exit the program")


# PROGRAM3: GET DAY OF BIRTH FUNCTION
def program3_get_day_of_birth():
    """
    Get the day of the week on which a person was born based on their date of birth.
    Parameters:
    - date_str (str): A string representing the date of birth in the format 'DD-MM-YYYY'.
    Returns:
    - str: The day of the week on which the person was born (e.g., 'Monday', 'Tuesday', etc.).
    Raises:
    - ValueError: If the input date string is not in the correct format or if it represents an invalid date.
    """
    while True:
        def find_day_of_birth(date_str):
            try:
                # Parse the date string into a datetime object
                dob = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        
                # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
                day_of_week = dob.weekday()
        
                # List of days of the week
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
                print(f"The person was born on a {days[day_of_week]}.")
            except ValueError:
                print("Invalid date format. Please enter the date in dd-mm-yyyy format.")

        date_of_birth = input("Enter the date of birth (dd-mm-yyyy): ")
        find_day_of_birth(date_of_birth)

#Add loop to handle user choice of continuing the same program, returning to the main menu, or exiting the program.
       
        while True:
            choice = input("\nPress 'c' to continue or 'm' to return to the main menu or 'q' to exit the program: ")
            if choice == 'c':
                break
            elif choice == 'm':
                welcome_msg()
                return
            elif choice == 'q':
                print("\nExiting program. Goodbye!\n")
                exit()
            else:
                print("\nInvalid choice. Please press 'c' to continue or 'm' to return to the main menu or 'q' to exit the program")


# PROGRAM4: COUNT ALL CHARACTERS INCLUDING SPACES FUNCTION
def program4_count_all_characters():
    """
    Count the occurrences of each character in the given text.
    Parameters:
    - input_text(str): The input text for which character counts are to be calculated.
    Returns:
    - dict: A dictionary containing the count of occurrences of each character in the input text.
    """

    while True:
        def count_characters(input_text):
        # Initialize counters
            alphabet_count = 0
            digit_count = 0
            special_char_count = 0
            space_count = 0

            # Iterate through each character in the input
            for char in input_text:
                if char.isalpha():
                    alphabet_count += 1
                elif char.isdigit():
                    digit_count += 1
                elif char.isspace():
                    space_count += 1
                else:
                    special_char_count += 1

            return alphabet_count, digit_count, special_char_count, space_count


        # Get user input
        user_input = input("Type a phrase or sentence: ")

        # Count characters
        alphabet_count, digit_count, special_char_count, space_count = count_characters(user_input)

        # Display the results
        print(f"Alphabets: {alphabet_count}")
        print(f"Numbers: {digit_count}")
        print(f"Special Characters: {special_char_count}")
        print(f"Spaces: {space_count}")      

#Add loop to handle user choice of continuing the same program, returning to the main menu, or exiting the program.
       
        while True:
            choice = input("\nPress 'c' to continue or 'm' to return to the main menu or 'q' to exit the program: ")
            if choice == 'c':
                break
            elif choice == 'm':
                welcome_msg()
                return
            elif choice == 'q':
                print("\nExiting program. Goodbye!\n")
                exit()
            else:
                print("\nInvalid choice. Please press 'c' to continue or 'm' to return to the main menu or 'q' to exit the program")


# PROGRAM5: GUEES A NUMBER FUNCTION
def program5_guess_a_number():
    """
    Guess a number game where the user tries to guess a secret number.
    Parameters:
    - target_number (int): The secret number that the user needs to guess.
    Returns:
    - str: A message indicating whether the user guessed the number correctly or not.
    """
    while True:
        def guess_a_number(lower_limit, upper_limit):
            # Generate a random number within the specified range
            target_number = random.randint(lower_limit, upper_limit)
            attempts = 0

            while True:
                guess = int(input(f"Guess a number between {lower_limit} and {upper_limit}: "))
        
                # Increment the number of attempts
                attempts += 1

                # Check if the guess is correct
                if guess == target_number:
                    print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
                    break
                elif guess < target_number:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")

        lower_limit = 1
        upper_limit = 25

        # Call the function to start the program
        guess_a_number(lower_limit, upper_limit)

#Add loop to handle user choice of continuing the same program, returning to the main menu, or exiting the program.
       
        while True:
            choice = input("\nPress 'c' to continue or 'm' to return to the main menu or 'q' to exit the program: ")
            if choice == 'c':
                break
            elif choice == 'm':
                welcome_msg()
                return
            elif choice == 'q':
                print("\nExiting program. Goodbye!\n")
                exit()
            else:
                print("\nInvalid choice. Please press 'c' to continue or 'm' to return to the main menu or 'q' to exit the program")


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