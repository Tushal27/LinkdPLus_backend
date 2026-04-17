<div align="center">

# 🔗 LinkdPlus — Backend

**A production-grade social networking REST API built with Django REST Framework**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-REST_Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)

🌐 **Live Frontend →** [linkd-plus-frontend.vercel.app](https://linkd-plus-frontend.vercel.app)
📦 **Frontend Repo →** [LinkdPlus-Frontend](https://github.com/Tushal27/LinkdPlus-Frontend)

</div>

---

## 📖 About

LinkdPlus is a full-stack career social networking platform — built to give professionals a focused space to share updates, connect, and engage. This repo is the Django REST Framework backend, handling all API logic, authentication, and data.

The project is **live and serving real users.** It was built entirely solo — from DB schema design to deployment on Render.

---

## 🏗️ System Architecture

```mermaid
graph TB
    Client["🌐 React Frontend<br/>(Vercel)"]
    
    subgraph Backend ["⚙️ Django REST API (Render)"]
        Auth["accounts app<br/>JWT Auth / Profiles"]
        Posts["posts app<br/>Feed / Likes / Comments"]
        Contact["contactme app<br/>Messaging"]
    end

    subgraph Data ["💾 Data Layer"]
        DB["PostgreSQL<br/>Database"]
        Media["Cloudinary<br/>Media Storage"]
    end

    Client -->|"HTTP + JWT"| Auth
    Client -->|"HTTP + JWT"| Posts
    Client -->|"HTTP + JWT"| Contact
    Auth --> DB
    Posts --> DB
    Contact --> DB
    Auth --> Media
    Posts --> Media
```

---

## 🔄 Authentication Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Django API
    participant DB as PostgreSQL

    U->>F: Enter credentials
    F->>B: POST /api/accounts/login/
    B->>DB: Validate user
    DB-->>B: User object
    B-->>F: Access token + Refresh token
    F->>F: Store tokens in localStorage
    
    Note over F,B: Subsequent requests
    F->>B: GET /api/posts/ + Authorization: Bearer <token>
    B->>B: Validate JWT
    B-->>F: Protected data
    
    Note over F,B: Token refresh
    F->>B: POST /api/token/refresh/
    B-->>F: New access token
```

---

## 🗄️ Database Schema

```mermaid
erDiagram
    USER {
        int id PK
        string username
        string email
        string password_hash
        string bio
        string profile_pic
        datetime created_at
    }
    POST {
        int id PK
        int author_id FK
        string content
        string image
        datetime created_at
    }
    LIKE {
        int id PK
        int user_id FK
        int post_id FK
        string type
    }
    COMMENT {
        int id PK
        int user_id FK
        int post_id FK
        string content
        datetime created_at
    }
    MESSAGE {
        int id PK
        int sender_id FK
        int receiver_id FK
        string content
        datetime sent_at
    }

    USER ||--o{ POST : "creates"
    USER ||--o{ LIKE : "gives"
    USER ||--o{ COMMENT : "writes"
    USER ||--o{ MESSAGE : "sends"
    POST ||--o{ LIKE : "receives"
    POST ||--o{ COMMENT : "has"
```

---

## 🚀 API Endpoints

### Authentication — `/api/accounts/`
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/register/` | Register new user |
| `POST` | `/login/` | Login, returns JWT tokens |
| `POST` | `/token/refresh/` | Refresh access token |
| `GET` | `/profile/<id>/` | Get user profile |
| `PUT` | `/profile/update/` | Update profile + photo |

### Posts — `/api/posts/`
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Get all posts (feed) |
| `POST` | `/` | Create new post |
| `GET` | `/<id>/` | Get single post |
| `DELETE` | `/<id>/` | Delete post |
| `POST` | `/<id>/like/` | Like / unlike post |
| `POST` | `/<id>/comment/` | Add comment |
| `GET` | `/<id>/comments/` | Get all comments |

### Contact — `/api/contactme/`
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/send/` | Send message |
| `GET` | `/inbox/` | Get received messages |

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Django 4.x + Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Database | PostgreSQL |
| Media | Cloudinary |
| Deployment | Render (with `build.sh` + `Procfile`) |
| Runtime | Python 3.11 |

---

## 🛠️ Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/Tushal27/LinkdPLus_backend.git
cd LinkdPLus_backend

# 2. Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Fill in: SECRET_KEY, DATABASE_URL, CLOUDINARY_URL

# 5. Run migrations
python manage.py migrate

# 6. Start server
python manage.py runserver
```

### Environment Variables
```env
SECRET_KEY=your_django_secret_key
DATABASE_URL=postgres://...
CLOUDINARY_CLOUD_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 📁 Project Structure

```
LinkdPLus_backend/
├── accounts/          # User auth, registration, profiles
├── posts/             # Feed, likes, comments
├── contactme/         # Messaging
├── LinkedInapp_Backend/  # Django project settings
├── manage.py
├── requirements.txt
├── Procfile           # Render deployment
├── build.sh           # Render build script
└── runtime.txt        # Python version pin
```

---

<div align="center">

Built with ❤️ by [Tushal J](https://github.com/Tushal27) · [LinkedIn](https://linkedin.com/in/tushal-j)

</div>
