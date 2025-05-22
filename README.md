

# 🛒 GreatKart – E-commerce Web Application

**GreatKart** is a full-featured Django-based e-commerce web application designed for selling products online with a user-friendly interface, robust backend functionality, and essential features like product browsing, cart management, checkout, and user accounts.

---

## 📦 Features

- 🔐 User registration, login, logout, and password reset
- 🛍️ Product browsing by category, brand, and search
- 🛒 Shopping cart with quantity management
- 💳 Checkout with order review and payment (mock)
- 📦 Order summary and history
- 🌐 Responsive frontend using Bootstrap
- ⚙️ Admin dashboard to manage products, categories, and orders

---

## 🧰 Tech Stack

- **Backend:** Django 3.x
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (development)
- **Others:** Django messages, media file uploads, custom template tags

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.6+
- pip (Python package installer)
- Virtualenv (recommended)

### 📥 Installation

```bash
# Clone the project
git clone https://github.com/your-username/greatkart.git
cd greatkart

# Set up virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser

# Run development server
python manage.py runserver


⸻

📁 Project Structure

greatkart/
├── accounts/            # User authentication
├── carts/               # Cart management
├── category/            # Product categories
├── orders/              # Order placement and history
├── store/               # Product listings
├── static/              # Static files (CSS, JS)
├── templates/           # HTML templates
├── media/               # Uploaded images
├── greatkart/           # Project settings
└── manage.py            # Django management script


⸻

🧪 Test Credentials (if any)
	•	Admin: admin@example.com / adminpassword
	•	User: user@example.com / userpassword

⸻

📸 Screenshots

(Add relevant UI screenshots here)

⸻

📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

⸻

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Let me know if you want it personalized (e.g., GitHub URL, real admin/user credentials, etc.).
