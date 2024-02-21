# Movie Chatbot API Documentation

The Chatbot API enables the creation, retrieval, updating, and deletion of chatbot sessions and messages within an application.

## Base URL

`http://localhost:8000/api`

## Endpoints Overview

### Chat Endpoints

- **Create New Chat**
- **Get All Chats**
- **Get Specific Chat**
- **Change Chat Title**
- **Delete All Chats**

### Message Endpoints

- **Get All Messages from Chat**
- **Post New Message**

## Endpoint Details

### Create New Chat

- **Method:** POST
- **URL:** `/chat/`
- **Request Body:**
  - None required for creation; optionally, specify initial parameters or participants.
- **Response:** Returns details of the newly created chat session.

### Get All Chats

- **Method:** GET
- **URL:** `/chat/`
- **Response:** Returns an array of all chat sessions.

### Get Specific Chat

- **Method:** GET
- **URL:** `/chat/{chat_id}`
- **URL Parameters:** `chat_id` is the unique identifier of the chat.
- **Response:** Returns details of the specified chat session.

### Change Chat Title

- **Method:** PATCH
- **URL:** `/chat/{chat_id}`
- **URL Parameters:** `chat_id` is the unique identifier of the chat.
- **Request Body:**
  ```json
  {
    "title": "New Chat Title"
  }
  ```
- **Response:** Returns updated details of the chat session.

### Delete All Chats

- **Method:** DELETE
- **URL:** `/chat/`
- **Response:** Confirmation of deletion.

### Get All Messages from Chat

- **Method:** GET
- **URL:** `/chat/{chat_id}/messages`
- **URL Parameters:** `chat_id` is the unique identifier of the chat.
- **Response:** Returns an array of messages from the specified chat session.

### Post New Message

- **Method:** POST
- **URL:** `/chat/{chat_id}/messages`
- **URL Parameters:** `chat_id` is the unique identifier of the chat.
- **Request Body:**
  ```json
  {
    "content": "Your message content here"
  }
  ```
- **Response:** Returns details of the newly created message and the answer from the AI.

## Authentication

All requests to the Chat API require authentication. Ensure to include an `Authorization` header with a valid API token in each request.

**Example Header:**

```
Authorization: Bearer YOUR_API_TOKEN
```

## Error Handling

The API uses standard HTTP response codes to indicate the success or failure of requests. In the case of errors, a JSON response will be returned with details about the error.

