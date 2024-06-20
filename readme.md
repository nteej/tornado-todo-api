# Tornado Todo API with TDD & Best Practises

This is a simple Todo API built using the Tornado web framework in Python with TDD & Best Practises. It supports creating, retrieving, updating, and deleting todo items. The project includes unit tests with full coverage and adheres to best practices for validation, exception handling, and performance optimization.

## Features

- Create a new todo item
- Retrieve all todo items
- Retrieve a specific todo item by ID
- Update a todo item
- Delete a todo item

## Requirements

- Python 3.7+
- Tornado
- SQLAlchemy
- Alembic
- Pytest

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nteej/tornado-todo-api.git
    cd tornado-todo-api
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    alembic upgrade head
    ```

## Running the Application

To start the Tornado application, run:

```bash
python3 app.py
```

## Test API

```bash
curl http://localhost:8888
```

The server will start on http://localhost:8888.

## API Endpoints

1. Get all todos

	-	URL: /todos
	-	Method: GET
	-	Response: JSON array of todo items

2. Get a specific todo

	-	URL: /todos/{id}
	-	Method: GET
	-	Response: JSON object of the requested todo item

3. Create a new todo

	-	URL: /todos
	-	Method: POST
	-	Body: JSON object with title and description
	-	Response: JSON object of the created todo item

4. Update a todo

	-	URL: /todos/{id}
	-	Method: PUT
	-	Body: JSON object with title and description
	-	Response: JSON object of the updated todo item

5. Delete a todo

	-	URL: /todos/{id}
	-	Method: DELETE
	-	Response: Status message

## Running Tests

To run the unit tests, use:

```bash
pytest test_app.py
```

