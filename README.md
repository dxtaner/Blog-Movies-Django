# 🎬 Django Film Application

This is a film sharing platform built with Django. Users can register, log in, add films, update or delete them, and leave comments.

---

## 📁 Project Structure

The project includes two main Django apps:

- **user**: Manages user authentication (register, login, logout).
- **filmapp**: Handles all film-related operations and commenting.

---

## 🔑 User App (`user`)

| URL Path     | View Function      | Description             |
|--------------|--------------------|-------------------------|
| `/register/` | `views.register`   | User registration       |
| `/login/`    | `views.userLogin`  | User login              |
| `/logout/`   | `views.userLogout` | User logout             |

---

## 🎥 Film App (`filmapp`)

| URL Path              | View Function         | Description                        |
|-----------------------|------------------------|------------------------------------|
| `/dashboard/`         | `views.dasboard`       | Dashboard for managing user films  |
| `/addfilm/`           | `views.addfilm`        | Add a new film                     |
| `/film/<int:id>`      | `views.detail`         | View details of a specific film    |
| `/update/<int:id>`    | `views.updateFilm`     | Update an existing film            |
| `/delete/<int:id>`    | `views.deleteFilm`     | Delete a film                      |
| `/`                   | `views.filmler`        | List all films                     |
| `/comment/<int:id>`   | `views.addComment`     | Add a comment to a film            |

---

## ⚙️ Installation & Setup

```bash
# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

--- 
## 🧪 Features

- ✅ **User registration, login, and logout**
- 🎬 **Create, read, update, and delete (CRUD) films**
- 💬 **Comment system for films**
- 🔐 **Protected views for authenticated users**
- 📁 **Clean and modular URL management**

---

## 📌 Notes

- The path `/dasboard/` may contain a typo. Consider renaming it to `/dashboard/`.

### Potential Improvements:

- Add user profile pages  
- Categorize films (genre-based)  
- Like/dislike system  
- REST API support with Django REST Framework  

---

## 👨‍💻 Developer

**Taner Özer**  
GitHub: [@dxtaner](https://github.com/dxtaner)  
Email: [tanerozer16@gmail.com](mailto:tanerozer16@gmail.com)

