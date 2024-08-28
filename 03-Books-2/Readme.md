# FastAPI Book API

This project is a simple FastAPI application for managing a collection of books. It demonstrates basic CRUD (Create, Read, Update, Delete) operations using FastAPI along with Pydantic for data validation and Starlette for HTTP status codes.

## Requirements

- Python 3.7+
- FastAPI
- Pydantic
- Starlette

You can install the necessary packages using pip:

```bash
pip install fastapi pydantic starlette
```

## Code Overview

### Pydantic

Pydantic is used for data validation and settings management. In this project, Pydantic's `BaseModel` is used to define the schema for book requests.

- **`BookRequest`**: This Pydantic model defines the expected format for book data in POST and PUT requests. It includes validation rules such as:
  - `title`: Must be at least 3 characters long.
  - `author`: Must be at least 1 character long.
  - `description`: Must be between 1 and 100 characters long.
  - `rating`: Must be an integer between 1 and 5.
  - `published_date`: Must be an integer between 2000 and 2030.

  Additionally, the `model_config` dictionary provides an example of a valid `BookRequest` payload.

### Starlette

Starlette is a lightweight ASGI framework that FastAPI builds on. It provides utilities like HTTP status codes.

- **`status`**: Used to define HTTP status codes in the route handlers for consistency and readability.

### FastAPI Application

The FastAPI app includes several endpoints for managing books:

- **GET `/books`**: Returns a list of all books.
- **GET `/books/{book_id}`**: Returns a single book by its ID.
- **GET `/books/`**: Returns books filtered by rating.
- **GET `/books/publish/`**: Returns books filtered by published date.
- **POST `/create-book`**: Creates a new book with data provided in the request body.
- **PUT `/books/update_book`**: Updates an existing book with the provided data.
- **DELETE `/books/{book_id}`**: Deletes a book by its ID.

## Example Usage

### Retrieve All Books

```bash
curl -X 'GET' 'http://127.0.0.1:8000/books' -H 'accept: application/json'
```

### Retrieve a Book by ID

```bash
curl -X 'GET' 'http://127.0.0.1:8000/books/1' -H 'accept: application/json'
```

### Create a New Book

```bash
curl -X 'POST' 'http://127.0.0.1:8000/create-book' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "title": "New Book",
  "author": "Author Name",
  "description": "A description of the new book",
  "rating": 4,
  "published_date": 2025
}'
```

### Update an Existing Book

```bash
curl -X 'PUT' 'http://127.0.0.1:8000/books/update_book' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "id": 1,
  "title": "Updated Book Title",
  "author": "Updated Author",
  "description": "Updated description",
  "rating": 5,
  "published_date": 2026
}'
```

### Delete a Book

```bash
curl -X 'DELETE' 'http://127.0.0.1:8000/books/1' -H 'accept: application/json'
```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

Make sure to replace `main` with the name of your Python file if it's different.

## Conclusion

This FastAPI application provides a basic example of managing resources using RESTful APIs, with Pydantic for data validation and Starlette for HTTP utilities. Feel free to extend this application with additional features or enhancements.
```

This `README.md` file provides an overview of the application's functionality, usage examples, and instructions for running the FastAPI app. It also explains how Pydantic and Starlette are used in the project.Certainly! Here's a `README.md` file that explains the use of Pydantic and Starlette in the provided FastAPI code:

```markdown
# FastAPI Book API

This project is a simple FastAPI application for managing a collection of books. It demonstrates basic CRUD (Create, Read, Update, Delete) operations using FastAPI along with Pydantic for data validation and Starlette for HTTP status codes.

## Requirements

- Python 3.7+
- FastAPI
- Pydantic
- Starlette

You can install the necessary packages using pip:

```bash
pip install fastapi pydantic starlette
```

## Code Overview

### Pydantic

Pydantic is used for data validation and settings management. In this project, Pydantic's `BaseModel` is used to define the schema for book requests.

- **`BookRequest`**: This Pydantic model defines the expected format for book data in POST and PUT requests. It includes validation rules such as:
  - `title`: Must be at least 3 characters long.
  - `author`: Must be at least 1 character long.
  - `description`: Must be between 1 and 100 characters long.
  - `rating`: Must be an integer between 1 and 5.
  - `published_date`: Must be an integer between 2000 and 2030.

  Additionally, the `model_config` dictionary provides an example of a valid `BookRequest` payload.

### Starlette

Starlette is a lightweight ASGI framework that FastAPI builds on. It provides utilities like HTTP status codes.

- **`status`**: Used to define HTTP status codes in the route handlers for consistency and readability.

### FastAPI Application

The FastAPI app includes several endpoints for managing books:

- **GET `/books`**: Returns a list of all books.
- **GET `/books/{book_id}`**: Returns a single book by its ID.
- **GET `/books/`**: Returns books filtered by rating.
- **GET `/books/publish/`**: Returns books filtered by published date.
- **POST `/create-book`**: Creates a new book with data provided in the request body.
- **PUT `/books/update_book`**: Updates an existing book with the provided data.
- **DELETE `/books/{book_id}`**: Deletes a book by its ID.

## Example Usage

### Retrieve All Books

```bash
curl -X 'GET' 'http://127.0.0.1:8000/books' -H 'accept: application/json'
```

### Retrieve a Book by ID

```bash
curl -X 'GET' 'http://127.0.0.1:8000/books/1' -H 'accept: application/json'
```

### Create a New Book

```bash
curl -X 'POST' 'http://127.0.0.1:8000/create-book' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "title": "New Book",
  "author": "Author Name",
  "description": "A description of the new book",
  "rating": 4,
  "published_date": 2025
}'
```

### Update an Existing Book

```bash
curl -X 'PUT' 'http://127.0.0.1:8000/books/update_book' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "id": 1,
  "title": "Updated Book Title",
  "author": "Updated Author",
  "description": "Updated description",
  "rating": 5,
  "published_date": 2026
}'
```

### Delete a Book

```bash
curl -X 'DELETE' 'http://127.0.0.1:8000/books/1' -H 'accept: application/json'
```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

Make sure to replace `main` with the name of your Python file if it's different.

## Conclusion

This FastAPI application provides a basic example of managing resources using RESTful APIs, with Pydantic for data validation and Starlette for HTTP utilities. Feel free to extend this application with additional features or enhancements.
