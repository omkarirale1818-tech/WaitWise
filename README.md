# WaitWise - Queue Management System

#### Video Demo: https://youtu.be/tZXgllPmU

## Description

WaitWise is a queue management system developed using Python as my CS50P final project. The main purpose of this project is to make customer queue management easier and more organized. In places such as food stalls, small shops, and service counters, customers often have to wait for their turn. Managing the queue manually can sometimes create confusion. WaitWise helps solve this problem by generating tokens, displaying waiting customers, and estimating their waiting time.

I developed this project to apply the Python concepts I learned during CS50's Introduction to Programming with Python course. While working on it, I practiced using functions, lists, dictionaries, file handling, exception handling, JSON, and modules.

## Features

**1. Add Customers and Generate Tokens**

The program allows the user to enter a customer's name and the service they require. It generates a token number for each new customer and stores the customer's information in a list.

**2. View the Waiting Queue**

The program displays customers whose status is waiting. This helps the user understand which customers are still waiting for their turn.

**3. Serve the Next Customer**

The user can serve the next customer in the queue. The program updates the customer's status and records the service time so that the information can be used for future waiting-time calculations.

**4. Estimate Waiting Time**

WaitWise estimates how long a customer may need to wait before receiving service. It uses previous service-time information when available. If there is not enough service history, it uses a default estimated service time. The actual waiting time may differ from the estimate.

**5. Search for Customers**

The program allows the user to search for customers using their name or token number. This makes it easier to find a particular customer's information without checking the entire queue manually.

**6. View Queue Statistics**

The program displays basic statistics about the queue. These statistics help the user understand the current queue and information collected from completed services.

**7. Save Customer Data**

WaitWise uses a JSON file to store customer information. This allows the program to load previously saved data when it runs again instead of losing all information when the program closes.

## Technologies Used

- **Python:** Used to develop the main application and its functions.
- **JSON:** Used to save and load customer information.
- **datetime:** Used to record date and time information.
- **statistics:** Used to calculate average service times.
- **pytest:** Used to test the program's functions.

## Files in the Project

- `project.py` contains the main program, menu, and functions for managing customers, tokens, waiting times, searching, and statistics.
- `test_project.py` contains automated tests written using pytest.
- `requirements.txt` lists the external Python packages required by the project.
- `customers.json` stores customer data when the program uses JSON file storage.

## How to Run the Project

First, install the required packages by running:

```bash
python -m pip install -r requirements.txt
```

Next, start the program:

```bash
python project.py
```

To run the automated tests, use:

```bash
python -m pytest -v
```

## What I Learned

While developing WaitWise, I learned how to organize a Python program into separate functions and how to work with lists and dictionaries. I also gained practical experience with JSON file handling, calculating averages, managing customer records, and testing functions with pytest. This project helped me understand how different Python concepts can be combined to build a useful application.

## Limitations

The waiting time shown by WaitWise is only an estimate based on available service-time information. The actual waiting time depends on how long each service takes. The project is designed as a simple Python application and does not currently provide a web-based interface or a database server.
