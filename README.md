ConnectAbility Backend API

ConnectAbility is a backend REST API for a social platform designed to connect people with disabilities, caregivers, and allies.
The platform enables users to interact through posts, comments, likes, follows, and notifications.

This project was built during the ALX Africa Backend Capstone phase using Django and Django Rest Framework (DRF).

 Features

User registration and authentication

User profiles

Create and list posts

Comment on posts

Like and unlike posts

Follow and unfollow users

User feed (posts from followed users)

Notifications for follows, likes, and comments

Token-based authentication

 Tech Stack

Python 3

Django

Django Rest Framework (DRF)

SQLite (development database)

Token Authentication

 Project Structure
connectability-backend/
│
├── connectability/        # Main project settings
├── users_app/             # User accounts & profiles
├── posts_app/             # Posts, comments, likes
├── follows_app/           # Follow system
├── notifications_app/     # Notifications
├── static/                # Static files
├── manage.py
├── requirements.txt
└── README.md

 Authentication

This API uses Token Authentication.

Include the token in request headers:

Authorization: Token YOUR_TOKEN_HERE

 API Endpoints Overview
Users

POST /api/users/register/ – Register a new user

POST /api/users/login/ – Login user

GET /api/users/profile/ – View user profile

Posts

GET /api/posts/ – List posts

POST /api/posts/ – Create post

GET /api/posts/<id>/ – Retrieve post

DELETE /api/posts/<id>/ – Delete post

Comments

GET /api/posts/<post_id>/comments/ – List comments

POST /api/posts/<post_id>/comments/ – Add comment

Likes

POST /api/posts/<post_id>/like/ – Like / Unlike post

Follows

POST /api/follows/follow/<user_id>/ – Follow / Unfollow user

Notifications

GET /api/notifications/ – View notifications

▶ Running the Project Locally
1 Clone the Repository
git clone https://github.com/your-username/connectability-backend.git
cd connectability-backend

2 Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3 Install Dependencies
pip install -r requirements.txt

4 Apply Migrations
python manage.py migrate

5 Run the Server
python manage.py runserver

 Testing & Results (Manual Testing with curl)

The API was tested locally using Git Bash and curl commands.

1 User Registration — WORKED
curl -X POST http://127.0.0.1:8000/api/users/register/ \
-H "Content-Type: application/json" \
-d '{
  "username": "testuser1",
  "email": "testuser1@email.com",
  "password": "StrongPassword123"
}'

Expected Result
{
  "message": "User registered successfully"
}

2 User Login — WORKED
curl -X POST http://127.0.0.1:8000/api/users/login/ \
-H "Content-Type: application/json" \
-d '{
  "username": "testuser1",
  "password": "StrongPassword123"
}'

Expected Result
{
  "token": "abc123xyz456"
}


 Token is then used for authenticated requests.

3 View User Profile — WORKED
curl -X GET http://127.0.0.1:8000/api/users/profile/ \
-H "Authorization: Token YOUR_TOKEN_HERE"

Expected Result
{
  "username": "testuser1",
  "email": "testuser1@email.com"
}

4 Follow / Unfollow User —  WORKED
curl -X POST http://127.0.0.1:8000/api/follows/follow/2/ \
-H "Authorization: Token YOUR_TOKEN_HERE"

Expected Result
{
  "message": "You are now following this user"
}


Running the same command again:

{
  "message": "You have unfollowed this user"
}

5 View Notifications —  WORKED
curl -X GET http://127.0.0.1:8000/api/notifications/ \
-H "Authorization: Token YOUR_TOKEN_HERE"

Expected Result
[
  {
    "type": "follow",
    "message": "testuser1 followed you",
    "created_at": "2025-01-01T10:30:00Z"
  }
]

6 List Posts — PARTIALLY WORKED
curl -X GET http://127.0.0.1:8000/api/posts/ \
-H "Authorization: Token YOUR_TOKEN_HERE"

Issue Observed

Sometimes returns JSON correctly

Sometimes returns an HTML Django error page

Example error:

<!DOCTYPE html>
<html>
<head>
<title>Server Error (500)</title>


Cause: DEBUG=True and unresolved serializer/view mismatch.

7 Create Post —  PARTIALLY WORKED
curl -X POST http://127.0.0.1:8000/api/posts/ \
-H "Authorization: Token YOUR_TOKEN_HERE" \
-H "Content-Type: application/json" \
-d '{
  "content": "This is my first post"
}'

Issue Observed

Request reaches the server

Response sometimes returns HTML error instead of JSON

8 Like / Unlike Post — NOT WORKING AS EXPECTED
curl -X POST http://127.0.0.1:8000/api/posts/1/like/ \
-H "Authorization: Token YOUR_TOKEN_HERE"

Issue Observed

Endpoint is reachable

Returns HTML error page instead of JSON response

9 Comment on Post —  NOT WORKING AS EXPECTED
curl -X POST http://127.0.0.1:8000/api/posts/1/comments/ \
-H "Authorization: Token YOUR_TOKEN_HERE" \
-H "Content-Type: application/json" \
-d '{
  "content": "Nice post!"
}'

Issue Observed

Server processes request

HTML error page returned

Indicates unresolved comment serializer/view logic

Summary of Testing Results
Fully Working

User registration

User login

Token authentication

Follow / unfollow users

Notifications system

 Partially Working

List posts

Create posts

 Needs Fixing

Likes

Comments

Consistent JSON error handling

 Future Improvements

Fix remaining serializer and view inconsistencies

Improve API error handling

Add pagination

Add image and video upload support

Improve feed performance

Integrate frontend application

Author

Ruth Atieno
Backend Developer
ALX Africa