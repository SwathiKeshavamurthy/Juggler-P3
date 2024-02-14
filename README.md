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
        - [Program1: Convert Numbers into Words](#program1-convert-numbers-into-words)
        - [Program2: Get Weather](#program2-get-weather)
        - [Program3: Get Day of Birth](#program3-get-day-of-birth)
        - [Program4: Count All Characters](#program4-count-all-characters)
        - [Program5: Guess a Number](#program5-guess-a-number)
    - [Future Features](#future-features)

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

## Flowchart - Using LUCID

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

### Program1: Convert Numbers into Words
- Description: Program1 allows users to convert numeric input into its word representation. It supports a wide range of numbers up to trillion.
- Usage: Users input a whole number within the range of 1 to trillion, and the program converts it into words. For example, entering "123" would result in "one hundred twenty-three".
- Implementation: The conversion logic is implemented using a Python function that handles various cases based on the magnitude of the input number.

### Program2: Get Weather
- Description: Program2 retrieves current weather information for a specified city or country using the OpenWeatherMap API.
- Usage: Users input the name of a city or country, and the program fetches and displays the current weather conditions, including temperature, humidity, wind speed, and weather description.
- Implementation: The program utilizes the requests library to send HTTP requests to the OpenWeatherMap API and parse the JSON response to extract relevant weather data.

### Program3: Get Day of Birth
- Description: Program3 determines the day of the week based on a person's date of birth.
- Usage: Users input their date of birth in the format "dd-mm-yyyy", and the program calculates and displays the corresponding day of the week (e.g., Monday, Tuesday, etc.).
- Implementation: The program uses Python's datetime module to parse the input date string and extract the day of the week from the resulting datetime object.

### Program4: Count All Characters
- Description: Program4 counts the occurrences of alphabets, numbers, special characters, and spaces in a given text.
- Usage: Users input a phrase or sentence, and the program analyzes the input text to count and display the number of alphabets, numbers, special characters, and spaces present.
- Implementation: The program iterates through each character in the input text and categorizes them into different groups based on their type (alphabet, number, special character, or space), then counts the occurrences of each group.

### Program5: Guess a Number
- Description: Program5 implements a number guessing game where the user tries to guess a secret number within a specified range.
- Usage: Users are prompted to guess a number between 1 and 10, and the program provides feedback based on whether the guess is too high, too low, or correct.
- Implementation: The program generates a random secret number within the specified range and compares the user's guess with the secret number to determine the outcome.

## Future Features
