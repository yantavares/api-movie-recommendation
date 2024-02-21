# Movie Chatbot API Documentation

* Note * This is a fork from the original project maintained by [me](https://github.com/yantavares), [GuilhermeGonSoares](https://github.com/GuilhermeGonSoares) and [Mathweuzz](https://github.com/Mathweuzz).

The Chat API, powered by an advanced AI, enables the creation, retrieval, updating, and deletion of chat sessions and messages about movies within an application. This AI-driven approach enhances the interaction capabilities of the API, offering more dynamic and intelligent responses based on user inputs and contexts. Detailed documentation about the AI, including its architecture, training methods, and capabilities, can be found at the [Movie-chatbot-AI GitHub repository](https://github.com/Mathweuzz/Movie-chatbot-AI).

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
- **Request Body:** Optionally specify initial parameters or participants.
- **Response:** Returns details of the newly created chat session, facilitated by AI.

### Get All Chats

- **Method:** GET
- **URL:** `/chat/`
- **Response:** Returns an array of all chat sessions.

### Get Specific Chat

- **Method:** GET
- **URL:** `/chat/{chat_id}`
- **URL Parameters:** `chat_id` is the unique identifier of the chat.
- **Response:** Returns details of the specified chat session, with AI-enhanced insights.

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
- **Response:** Returns an array of messages from the specified chat session, enriched by AI.

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
- **Response:** Returns details of the newly created message, processed through AI for contextual understanding.

## Authentication

All requests to the Chat API require authentication. Include an `Authorization` header with a valid API token in each request.

**Example Header:**

```
Authorization: Bearer YOUR_API_TOKEN
```

## Error Handling

The API uses standard HTTP response codes for success or failure notifications. Errors return a JSON response with error details.
