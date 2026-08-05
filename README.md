# API Data Explorer

## Project Description

API Data Explorer is a Python application that retrieves data from a public REST API using the **Requests** library. The project allows users to view, search, filter, and export API data into a CSV file through a simple menu-driven interface.

## Features

* Fetch data from a public REST API
* Display the first 10 posts
* Search posts by title
* Filter posts by User ID
* Save API data to a CSV file
* Handle connection and request errors

## Technologies Used

* Python 3
* Requests Library
* JSON
* CSV

## Project Structure

```
API-Data-Explorer/
│── main.py
│── api_service.py
│── utils.py
│── requirements.txt
│── README.md
```

## API Used

https://jsonplaceholder.typicode.com/posts

## Installation

1. Open the project folder in VS Code.
2. Install the required package:

```
pip install requests
```

## How to Run

Run the following command:

```
python main.py
```

## Menu Options

1. View First 10 Posts
2. Search Post by Title
3. Filter Posts by User ID
4. Save Posts to CSV
5. Exit

## Output

The application displays API data on the screen and can save all posts to a file named `posts.csv`.



