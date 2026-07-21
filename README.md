# 🩺 MediQ – AI-Powered Healthcare Platform

An AI-powered healthcare platform built with **Python, Django, SQLite, and Google Gemini AI** that enables users to consult an AI assistant, book medical appointments, order medicines, manage medical records, and monitor their healthcare journey from a single web application.

> **Disclaimer:** MediQ provides general educational health information only and is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.

---

# ✨ Overview

**MediQ** is a full-stack healthcare platform designed to simplify access to essential healthcare services through an intuitive and secure web application. By integrating **Google Gemini AI** with Django, the platform provides AI-assisted health guidance while allowing users to schedule appointments, manage medical records, receive educational prescription suggestions, and purchase medicines online.

The application focuses on delivering a seamless patient experience by bringing consultation, appointment management, pharmacy services, and health record management together in one centralized platform.

---

# 🌟 Key Highlights

* 🤖 AI-powered healthcare assistant using Google Gemini
* 📅 Appointment booking across multiple medical departments
* 💊 Integrated online pharmacy with order tracking
* 📄 Secure medical record management
* 📋 AI-assisted educational prescription suggestions
* 📊 Personalized health dashboard
* 🌍 Multi-language AI responses
* 🔐 Secure authentication and data protection

---

# 🚀 Features

## 🤖 AI Consultation

* AI-powered medical guidance using Google Gemini
* Multiple consultation modes:

  * General Health
  * Medicine Information
  * Nutrition & Diet
  * Mental Health Support
* Multi-language support
* Consultation history

---

## 📅 Appointment Management

* Book appointments across multiple departments
* In-Person, Video, and Phone consultations
* Emergency and follow-up appointments
* Appointment status tracking

Departments include:

* General Medicine
* Cardiology
* Dermatology
* Dental
* Orthopedics
* Pediatrics
* Psychiatry
* Gynecology
* ENT

---

## 💊 Online Pharmacy

* Browse available medicines
* Live stock availability
* Shopping cart
* Order placement
* Order tracking

---

## 📄 Medical Records

* Upload reports and medical documents
* Store lab reports, X-rays, MRI and CT scans
* Categorized record management
* Download reports anytime

---

## 📋 AI-Assisted Prescriptions

* Educational medicine suggestions
* Prescription history
* Download prescription records

---

## 📊 Health Dashboard

* Appointment statistics
* Prescription overview
* Medical record summary
* Health activity analytics

---

## 🔐 Security

* Django Authentication System
* Password Hashing (PBKDF2)
* CSRF Protection
* SQL Injection Protection
* XSS Protection
* Environment-based API Key Management

---

# 🛠️ Tech Stack

| Category       | Technology                       |
| -------------- | -------------------------------- |
| Backend        | Python, Django                   |
| Frontend       | HTML, CSS, Bootstrap, JavaScript |
| Database       | SQLite                           |
| AI Integration | Google Gemini API                |
| Authentication | Django Session Authentication    |

---

# 📁 Project Structure

```text
MediQ/
├── manage.py
├── requirements.txt
├── .env
│
├── config/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                   # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   └── core/
│       ├── base.html
│       ├── dashboard.html
│       ├── voice_consultation.html
│       ├── appointments.html
│       ├── pharmacy.html
│       ├── prescriptions.html
│       └── health_dashboard.html
│
└── venv/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/MediQ.git

cd MediQ
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key
DEBUG=True
GEMINI_API_KEY=your_api_key
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 5. Apply Database Migrations

```bash
python manage.py migrate
```

---

## 6. Create an Admin User

```bash
python manage.py createsuperuser
```

---

## 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

# 🔑 Google Gemini API Setup

1. Visit **Google AI Studio**
2. Generate a new API Key
3. Copy the API key
4. Paste it into the `.env` file

```env
GEMINI_API_KEY=your_api_key
```

---

# 📌 Application Routes

| Feature          | Route                |
| ---------------- | -------------------- |
| AI Consultation  | `/consultation/`     |
| Appointments     | `/appointments/`     |
| Pharmacy         | `/pharmacy/`         |
| Medical Records  | `/reports/`          |
| Prescriptions    | `/prescriptions/`    |
| Health Dashboard | `/health-dashboard/` |
| Admin Panel      | `/admin/`            |

---

# 📖 Usage

1. Register a new account.
2. Log in to your dashboard.
3. Consult the AI assistant for general health guidance.
4. Book appointments with your preferred department.
5. Browse and order medicines from the pharmacy.
6. Upload and manage your medical records.
7. View appointments, prescriptions, and reports from the Health Dashboard.

---

# 🐞 Troubleshooting

| Issue                          | Solution                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------- |
| Django module not found        | Activate the virtual environment and install dependencies using `pip install -r requirements.txt` |
| Google Gemini module not found | Install using `pip install google-genai`                                                          |
| Invalid API Key                | Verify the `GEMINI_API_KEY` value in the `.env` file                                              |
| Port already in use            | Run `python manage.py runserver 8001`                                                             |
| AI quota exceeded              | Wait a few minutes and try again                                                                  |

---

# 🚀 Future Enhancements

* Video consultation support
* Payment gateway integration
* Email and SMS notifications
* PostgreSQL database support
* Advanced health analytics
* Mobile application
* AI-powered health recommendations

---

# 🤝 Contributing

Contributions are welcome.

```bash
git checkout -b feature/your-feature

git commit -m "Add your feature"

git push origin feature/your-feature
```

After pushing your changes, open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Satyam Pandey**

Final Year B.Tech (Computer Science)

Python • Django • Backend Development • Machine Learning

---

⭐ **If you found this project helpful, consider giving it a Star!**
