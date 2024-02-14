# <h1 align="center">JUGGLER Multi-Program Tool</h1>
<h2>Welcome</h2>

view the live project [CLICK HERE!](https://juggler-p3-8ea65e7afcc7.herokuapp.com/)

![Am I Responsive Image](documentation/readme-images/amiresponsive.JPG)

# Introduction

 [Juggler website](https://juggler-p3-8ea65e7afcc7.herokuapp.com/), This Python script is designed to be a versatile utility, offering users a suite of handy programs to perform various tasks efficiently. Whether you need to convert numbers into words, check the weather forecast, determine the day of the week for a specific date(find the day of birth), count characters in a text, or simply play a number guessing game, the Juggler has got you covered!
 
 # Table of Contents

- [Juggler](#juggler-multi-program-tool)
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [User Goals and Stories (UX)](#user-goals-and-stories-ux)
    - [The user's goals](#user-goals)
    - [The user's stories](#user-stories)
- [Owner Goals and Stories (UX)](#owner-goals-and-stories-ux)
    - [The owner's goals](#owner-goals)
    - [The owner's stories](#owner-stories)
- [Design of the website](#design-of-the-website)
    -[Flowchart - Using LUCID](#flowchart---using-lucid)
    -[Colors - Using COLORAMA](#colors---using-colorama)
    -[Text](#text)
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Juggler Main Function](#juggler-main-function)
        - [Program1: Convert Numbers into Words](#program1-convert-numbers-into-words)        
        - [Program2: Get Weather](#program2-get-weather)
        - [Program3: Get Day of Birth](#program3-get-day-of-birth)
        - [Program4: Count All Characters](#program4-count-all-characters)
        - [Program5: Guess a Number](#program5-guess-a-number)
    - [Future Features](#future-features)
        - [Existing Program Enhancement Ideas](#existing-program-enhancement-ideas)
        - [Addition of New Future Program Enhancement Ideas](#addition-of-new-future-program-enhancement-ideas)
- [Languages Used](#languages-used)
- [Technologies Used](#technologies-used)
- [Tools Used](#tools-used)
    - [Python Libraries](#python-libraries)
    - [Other Tools](#other-tools)
- [Classes and Functions in Juggler](#classes-and-functions-in-juggler)

# User Goals and Stories (UX)

## User Goals:

- Perform Various Tasks: Users aim to efficiently perform a variety of tasks, such as converting numbers into words, checking the weather, finding the day of the week for a specific date, counting characters in a text, and playing a number guessing game.
- Access Conveniently: Users want to access and use the tool conveniently, without the need for complex setups or installations.
- Understand Program Functions: Users seek clarity on the functions of each program offered by the tool, enabling them to choose the appropriate program for their needs.
- Interact Intuitively: Users expect an intuitive and user-friendly interface that allows them to interact with the programs seamlessly.
- Receive Feedback and Guidance: Users appreciate feedback and guidance within the tool, including error messages, prompts for input, and clear instructions on how to use each program.

## User Stories:

- As a user, I want to convert numbers into words, so I can easily represent numeric values in text format.
- As a user, I want to check the weather for a specific city, so I can plan my activities accordingly.
- As a user, I want to find out the day of the week for a particular date, so I can recall important events or schedule appointments.
- As a user, I want to count characters in a sentence or phrase, to analyze text data or verify the length of a message.
- As a user, I want to play a number guessing game, for entertainment and to challenge my guessing skills.
- As a user, I want to navigate between different programs easily, so I can switch tasks without hassle.
- As a user, I want to receive clear instructions and feedback from the tool, to understand how to interact with each program effectively.
- As a user, I want to have a smooth and error-free experience, without encountering technical issues or confusing errors.

# Owner Goals and Stories (UX)

## Owner Goals

- Provide Value: The website owner aims to offer a valuable resource for users by providing a suite of versatile programs that cater to various needs and interests.
- Increase Engagement: The website owner seeks to increase user engagement by offering interactive and entertaining programs that encourage users to spend more time on the site.
- Drive Traffic: The website owner wants to attract more visitors to the site by offering unique and useful tools that differentiate the site from competitors.

## Owner Stories:

- As a website owner, I want to offer a diverse range of utility programs, so users can find solutions to their needs conveniently on my site.
- As a website owner, I want to create an engaging and interactive experience for users, encouraging them to explore different programs and features on the site.
- As a website owner, I want to ensure the site is user-friendly and accessible, catering to users of all skill levels and backgrounds.

# Design of the website

## Flowchart - Using [LUCID](https://www.lucidchart.com/)

- The flowchart outlines the process flow for a multi-program tool called "Juggler."
- The flowchart depicts the main menu and the various programs available within the Juggler tool. Each program is represented as a separate process with its own set of functionalities.

![flowchart](documentation/readme-images/flowchart.png)

## Colors - Using COLORAMA

- Colorama is a Python library designed to simplify the process of adding colored text and styling to terminal output. It provides an easy-to-use interface for printing colored text in the terminal, making command-line interfaces (CLI) more visually appealing and easier to read.

- Installation
You can install Colorama using pip, the Python package manager. Simply run the following command in your terminal: pip install colorama

![colorama1](documentation/readme-images/colorama1.JPG)

![colorama2](documentation/readme-images/colorama2.JPG)

## Text

Most of the text is written  by the author.
Some text for README.md is taken from Google and is rephrased by the author.

# Features

## Existing Features

### Juggler Main Function
The main() function in Juggler serves as the entry point and central control mechanism for the entire multi-program tool. 
The main() function is responsible for displaying the welcome message, presenting the user with program choices, and handling user input to execute the selected program functionalities. It serves as the backbone of the Juggler tool, coordinating the flow of operations and interactions with the user.
![main](documentation/readme-images/main.JPG)


### Program1: Convert Numbers into Words
- Description: Program1 allows users to convert numeric input into its word representation. It supports a wide range of numbers up to trillion.
- Usage: Users input a whole number within the range of 1 to trillion, and the program converts it into words. For example, entering "123" would result in "one hundred twenty-three".
- Implementation: The conversion logic is implemented using a Python function that handles various cases based on the magnitude of the input number.
![program1](documentation/readme-images/p1.JPG)

### Program2: Get Weather
- Description: Program2 retrieves current weather information for a specified city or country using the OpenWeatherMap API.
- Usage: Users input the name of a city or country, and the program fetches and displays the current weather conditions, including temperature, humidity, wind speed, and weather description.
- Implementation: The program utilizes the requests library to send HTTP requests to the OpenWeatherMap API and parse the JSON response to extract relevant weather data.
![program2](documentation/readme-images/p2.JPG)

### Program3: Get Day of Birth
- Description: Program3 determines the day of the week based on a person's date of birth.
- Usage: Users input their date of birth in the format "dd-mm-yyyy", and the program calculates and displays the corresponding day of the week (e.g., Monday, Tuesday, etc.).
- Implementation: The program uses Python's datetime module to parse the input date string and extract the day of the week from the resulting datetime object.
![program3](documentation/readme-images/p3.JPG)

### Program4: Count All Characters
- Description: Program4 counts the occurrences of alphabets, numbers, special characters, and spaces in a given text.
- Usage: Users input a phrase or sentence, and the program analyzes the input text to count and display the number of alphabets, numbers, special characters, and spaces present.
- Implementation: The program iterates through each character in the input text and categorizes them into different groups based on their type (alphabet, number, special character, or space), then counts the occurrences of each group.
![program4](documentation/readme-images/p4.JPG)

### Program5: Guess a Number
- Description: Program5 implements a number guessing game where the user tries to guess a secret number within a specified range.
- Usage: Users are prompted to guess a number between 1 and 10, and the program provides feedback based on whether the guess is too high, too low, or correct.
- Implementation: The program generates a random secret number within the specified range and compares the user's guess with the secret number to determine the outcome.
![program5](documentation/readme-images/p5.JPG)

## Future Features

### Existing Program Enhancement Ideas:

**Program1: Convert Numbers into Words.**
- Support Negative Numbers: Enable converting negative numbers into words.
- Decimal Numbers: Allow conversion of decimal numbers (e.g., 123.45) into words.

**Program2: Get Weather**

- More Details: Provide additional weather details like hourly forecasts.
- Location Detection: Automatically detect the user's location to fetch weather information.

**Program3: Get Day of Birth**

- Age Calculation: Add the option to calculate the user's age from their birthdate.

**Program4: Count All Characters**

- Text Classification: Categorize input text into predefined categories.

**Program5: Guess a Number**

- Difficulty Levels: Offer different difficulty levels with varied ranges or complexity.
- Multiplayer Mode: Allow multiple users to guess the number simultaneously.

### Addition of New Future Program Enhancement Ideas:

Addition of new programs could further enrich the functionality and usability of the Juggler tool. This features aim to expand the capabilities of Juggler, providing users with more diverse and advanced tools for text manipulation, data analysis, and other tasks. Example: Text Encryption/Decryption, Data Visualization.

# Languages Used

- [PYTHON](https://www.python.org/) used as the back-end programming language.
Python is a primary programming language used for developing the core functionality of the Juggler tool. It offers simplicity, readability, and a vast ecosystem of libraries and frameworks that facilitate rapid development.
- [HTML5](https://en.wikipedia.org/wiki/HTML5) (Hypertext Markup Language) or HTML, was used to design the basic website. 
HTML was already implemented in the [CODEINSTITUTE TEMPLATE](https://github.com/Code-Institute-Org/p3-template). This template is used for building Jugger Tool. I have made few changes as color and terminal width.

# Technologies Used

- [GitHub](https://github.com/). It provides version control using Git, enabling developers to track changes to their codebase, collaborate with others, and manage their projects efficiently.
- [GitPod](https://www.gitpod.io/). Gitpod is an online integrated development environment (IDE) that allows developers to write, review, and manage code directly within a web browser.
- [Heroku](https://www.heroku.com/). Heroku is a cloud platform as a service (PaaS) that enables developers to build, deploy, and manage web applications quickly and easily. It supports multiple programming languages, including Ruby, Node.js, Python, Java, PHP, and Go, allowing developers to work with their preferred tools and frameworks. 

# Tools Used

## Python Libraries

- [Requests Library](https://pypi.org/project/requests/)
The Requests library is utilized in Juggler for making HTTP requests to external APIs, such as the OpenWeatherMap API for retrieving weather information. It simplifies the process of sending and receiving data over the web.
- [Colorama Library](https://pypi.org/project/colorama/)
Colorama is a Python library used for adding colored text and styling to the command-line interface of the Juggler tool. It enhances the visual appeal and user experience by providing colored output for different messages and prompts.
- [Dotenv Library](https://pypi.org/project/python-dotenv/)
Dotenv is employed for loading environment variables from a .env file into the Juggler application. It enables configuration settings, such as API keys or sensitive information, to be stored separately from the main codebase and easily managed.

## Other Tools

- [Am I Responsive](https://ui.dev/amiresponsive) was used to get a responsive image for README.
- [OpenWeatherMap](https://openweathermap.org/) was used to retrieve current weather information for any city or country. 

# Classes and Functions in Juggler

- `get_api_key()`
   -  Retrieves the API key for accessing the OpenWeatherMap API.
- `get_weather(api_key, city)`
   - Fetches current weather information for a specified city using the OpenWeatherMap API.
- `number_to_words(number)`
    - Converts a given integer number into its word representation.
- `get_day_of_birth(date_str)`
    - Determines the day of the week a person was born based on their date of birth.
- `count_characters(input_text)`
    - Counts the occurrences of each character in the input text.
- `guess_a_number(lower_limit, upper_limit)`
    - Plays the number guessing game where the user tries to guess a secret number within a specified range.
- `welcome_msg()`
    - Displays the welcome message and introduction text when the Juggler tool is launched.
- `clear_terminal()`
    - Clears the terminal screen.
- `handle_user_choice()`
    - Handles user choice for continuing, returning to the main menu, or exiting the program.
- `main()`
    - Main function that orchestrates the execution of different programs within the Juggler tool.

# Imports in Juggler

- `os`- Provides a portable way to interact with the operating system.
- `requests` - Enables sending HTTP requests to web servers and receiving responses.
- `json` - Provides functions for encoding and decoding JSON data, of Python objects to and from JSON format.
- `pytz`- Provides timezone information.
- `datetime` - Provides classes for working with date and time values, including the creation, manipulation, and formatting of datetime objects.
- `time` - Provides functions for working with time values, including sleeping, measuring time intervals, and accessing the current system time.
- `random` - Provides functions for generating pseudo-random numbers, allowing the creation of randomized elements in programs.
- `dotenv` - Loads environment variables from a .env file into the environment.
- `colorama` - Provides cross-platform support for colored terminal text.