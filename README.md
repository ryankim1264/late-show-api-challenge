Late Show API Challenge

A Flask-based RESTful API for managing late night talk show guests, episodes, and appearances.

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### Clone the Repo

```bash
git clone https://github.com/yourusername/late-show-api-challenge.git
cd late-show-api-challenge

Create Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate 

 How to Run
Create and Migrate Database

createdb late_show_db
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the Database

python3 -m server.seed
Run the App

flask run
Runs on: http://localhost:5000

 Authentication Flow
Register

POST /register
Body:


{
  "username": "yourname",
  "password": "yourpassword"
}
Login

POST /login
Body:


{
  "username": "yourname",
  "password": "yourpassword"
}
Response:


{
  "token": "your_jwt_token"
}

Authenticated Requests
Use this header in protected routes:
Authorization: Bearer your_jwt_token
  API Routes
Method	Endpoint	Description	Auth Required
POST	/register	Register new user	
POST	/login	Login + JWT	
GET	/episodes	List all episodes	
GET	/episodes/<id>	Get episode by ID	
GET	/guests	List all guests
GET	/guests/<id>	Get guest by ID	

Example: GET /episodes
Header:


Authorization: Bearer your_jwt_token
Response:


[
  {
    "id": 1,
    "date": "2023-06-01",
    "number": 177,
    "appearances": [
      {
        "id": 1,
        "rating": 5,
        "guest": {
          "id": 1,
          "name": "Kimutai Ryan",
          "occupation": "Artist"
        }
      }
    ]
  }
]
