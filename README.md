# ConnectAbility Backend API

ConnectAbility is a backend REST API for a social platform designed to connect people with disabilities, caregivers, and allies.  
The platform supports user accounts, posts, comments, likes, follows, and notifications.

This project is built using **Django** and **Django Rest Framework (DRF)**.

---

##  Features

- User registration and authentication
- User profiles
- Create, list, and delete posts
- Comment on posts
- Like and unlike posts
- Follow and unfollow users
- User feed (posts from followed users)
- Notifications for follows, likes, and comments
- Token-based authentication

---

## 🛠 Tech Stack

- Python 3
- Django
- Django Rest Framework
- SQLite (development)
- Token Authentication
- Render (deployment)

---

##  Project Structure

```text
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

POST /api/users/register/ – Register user

POST /api/users/login/ – Login user

GET /api/users/profile/ – View profile

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

5 Run Server
python manage.py runserver

Testing (Using Curl Example)

Create a post:

curl -X POST http://127.0.0.1:8000/api/posts/ \
-H "Authorization: Token YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{"content": "My first post"}'

 Known Issues

Some endpoints may return HTML error pages during development when DEBUG=True.

These issues are under active debugging and improvement.

 Future Improvements

Improve error handling

Add pagination

Add image/video upload support

Improve feed performance

Frontend integration

 Author

Ruth Atieno
Backend Developer
ALX Africa