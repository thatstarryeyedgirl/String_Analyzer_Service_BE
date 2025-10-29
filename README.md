# String_Analyzer_Service_BE

Welcome to **String Analyzer Service!!**  
This project is a **Django RESTful API** that analyzes strings and stores their computed properties in a database.

## Overview  

The **String Analyzer Service** accepts a string input and computes several properties about it, including:  
**length** — Number of characters in the string  
**is_palindrome** — Whether the string reads the same forwards and backwards (case-insensitive)  
**unique_characters** — Number of distinct characters  
**word_count** — Number of words separated by spaces  
**sha256_hash** — Unique SHA-256 hash identifier for the string  
**character_frequency_map** — How many times each character appears

Each analyzed string is stored in the database with its computed properties.

## Endpoints  

### 1. Create / Analyze String
**POST** `/string-analyzer/create/`
- **json**
{
"value": "string to analyze"
}
- Success Response (201 Created)
- Error Response (409 Conflict)

### 2. Get Specific String
**GET** `/string-analyzer/retrieve/<str:value>/`

- Success Response (200 OK)
- Error Response (404 Not Found)

### 3. Get All Strings with Filtering
**GET** `/string-analyzer/list/?is_palindrome=true&min_length=5&max_length=20&word_count=2&contains_character=a`

- Success Response (200 OK)
- Error Response (400 Bad Request)

### 4. Natural Language Filtering
**GET** `/string-analyzer/filter-by-natural-language/?query=all%20single%20word%20palindromic%20string`

- Success Response (200 OK)
- Error Response (400 Bad Request)

### 5. Delete String
**DELETE** `string-analyzer/delete/<str:value>/`

- Success Response (204 No Content)
- Error Responses (404 Not Found)

## Tech Stack
- **Backend Framework:** Django & Django REST Framework (DRF)
- **Database:** PostgreSQL (for development)
- **Language:** Python 3.12.10
- **Environment Management:** `.env`

## Postman Documentation
The String Analyzer Service API is fully documented in Postman to simplify testing and interaction with all available endpoints.
The collection includes examples for creating, retrieving, filtering, and deleting analyzed strings, as well as natural language filtering.

Each request contains preconfigured methods, headers, sample payloads, and example responses to help you understand how the API behaves.
- **Postman Link:** `https://documenter.getpostman.com/view/48778720/2sB3Wnv1it`
