def welcome_msg():
    """
    Print banner msg and intro text
    """
    print("Welcome")
    print("This is a Juggler multi-program tool.")
    print(
        "Program1-You can convert numbers into words between 1 to Trillion.\n"
        "Program2-You can get the weather information of the city you request.\n"
        "Program3-You can find out the Day of Birth.\n"
        "Program4-You can type a sentence to count all the characters with spaces separately and displayed.\n"
        "Program5-You should guess a number between 1-10.\n")

# Calling the function to display the welcome message
welcome_msg()

def program1_convert_numbers():
    #program1 code
    print('entered program1')
    pass

def program2_get_weather():
    #program2 code
    print('entered program2')
    pass

def program3_get_day_of_birth():
    #program3 code
    print('entered program3')
    pass

def program4_count_all_characters():
    #program4 code
    print('entered program4')
    pass

def program5_guess_a_number():
    #program5 code
    print('entered program5')
    pass

def main():
    welcome_msg()
    program_choice = input("Please choose a program and type a number between (1-5): ")

    if program_choice == '1':
        program1_convert_numbers()
    elif program_choice == '2':
        program2_get_weather()
    elif program_choice == '3':
        program3_get_day_of_birth()
    elif program_choice == '4':
        program4_count_all_characters()
    elif program_choice == '5':
        program5_guess_a_number()
    else:
        print("Invalid choice. Please choose a program between 1 to 5.")

if __name__ == "__main__":
    main()