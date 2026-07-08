<div align="center">

# 🩺 MediQ

### AI-Powered Healthcare Platform

**Chat with AI. Book appointments. Order medicines. Manage your health — all in one place.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-AI-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## ✨ Overview

**MediQ** is a full-stack healthcare platform built with Django that brings AI-powered medical guidance, appointment booking, an online pharmacy, and medical records management into one seamless experience.

Powered by **Google Gemini AI**, MediQ helps bridge the gap between patients and healthcare services — giving people fast, reliable, general health information while keeping the full patient journey (consult → book → prescribe → order → track) in a single system.

> ⚠️ **Disclaimer:** MediQ provides general educational health information only. It is **not** a substitute for professional medical diagnosis, advice, or treatment. Always consult a licensed healthcare provider.

---

## 🚀 Features

### 🤖 AI Consultation
- Real-time, context-aware medical guidance via Google Gemini
- Multiple consultation modes — General Health, Medicine Info, Nutrition & Diet, Mental Health Support
- Multi-language responses (English, Hindi, Spanish, French)
- Full consultation history, saved and searchable

### 📅 Appointment Management
- Book appointments across 9 departments (General, Cardiology, Dermatology, Dental, Psychiatry, Orthopedics, Pediatrics, Gynecology, ENT)
- In-Person, Video, or Phone consultation types
- Emergency & follow-up flags
- Status tracking — Pending, Confirmed, Completed, Cancelled

### 💊 Online Pharmacy
- Browse 15+ medicines with live stock status
- Cart-based shopping experience
- Order tracking from checkout to delivery

### 📄 Medical Records
- Upload lab reports, X-rays, MRIs, CT scans & more
- Categorized storage with notes
- Download anytime

### 📋 AI-Assisted Prescriptions
- Symptom-based, educational medicine suggestions
- Full prescription history with downloadable records

### 📊 Health Dashboard
- Visual stats on appointments, records & prescriptions
- Monthly trends and report-type breakdowns

### 🔐 Security
- Session-based authentication
- Password hashing (PBKDF2)
- CSRF, XSS & SQL injection protection
- Environment-based API key management

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 6.0 (Python) |
| **Frontend** | HTML, CSS, Bootstrap, JavaScript |
| **Database** | SQLite (PostgreSQL-ready) |
| **AI Engine** | Google Gemini API (`google-genai`) |
| **Auth** | Django session-based authentication |

---

## 📁 Project Structure

```
MediQ/
├── manage.py
├── requirements.txt
├── .env                    # create yourself (see below)
│
├── config/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                   # Main application
│   ├── models.py           # Patient, Appointment, Prescription, Medicine, Order...
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
└── venv/                   # virtual environment
```

---

## ⚡ Quick Setup

### Prerequisites
- Python 3.12+
- pip
- Git

### Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd MediQ

# 2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

```bash
# 5. Run migrations
python manage.py migrate

# 6. Create an admin account
python manage.py createsuperuser

# 7. Launch the server
python manage.py runserver
```

Open **http://localhost:8000** 🎉

---

## 🔑 Get a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Click **Get API Key**
3. Paste it into your `.env` file as `GEMINI_API_KEY`

---

## 📱 Route Map

| Feature | URL |
|---|---|
| AI Consultation | `/consultation/` |
| Pharmacy | `/pharmacy/` |
| Appointments | `/appointments/` |
| Medical Reports | `/reports/` |
| Prescriptions | `/prescriptions/` |
| Health Dashboard | `/health-dashboard/` |
| Admin Panel | `/admin/` |

---

## 📖 How to Use

1. **Register** at `/register/` and log in
2. **Ask the AI** — head to AI Consultation, pick a mode & language, and type your question
3. **Book an appointment** — choose department, doctor, date & consultation type
4. **Order medicine** — browse the pharmacy, add to cart, and check out
5. **Upload records** — attach lab reports/scans with category & notes
6. **Track everything** on your personalized Health Dashboard

---

## 🐛 Troubleshooting

| Issue | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'django'` | Activate your virtual environment, then `pip install -r requirements.txt` |
| `ModuleNotFoundError: No module named 'google'` | `pip install google-genai` |
| AI response shows a quota/unavailable warning | Gemini API is temporarily rate-limited or under high demand — wait a few minutes and retry |
| Invalid API key warning | Double-check `GEMINI_API_KEY` in `.env` — it shouldn't be the placeholder value |
| Port 8000 already in use | `python manage.py runserver 8001` |

---

## 🎨 Design Philosophy

- Fully responsive — mobile & desktop
- Dark theme with cyan/teal accents
- Smooth transitions and clean navigation
- Fast, minimal-friction workflows across every feature

---

## 🔮 Roadmap

- [ ] Video consultation integration
- [ ] Payment gateway for pharmacy checkout
- [ ] Mobile app (React Native)
- [ ] Advanced analytics & smart notifications

---

## 🤝 Contributing

Contributions are welcome!

```bash
git checkout -b feature/your-feature
# make your changes
git commit -m "Add: your feature description"
git push origin feature/your-feature
```

Then open a Pull Request 🚀

---

## 📄 License

Released under the **MIT License** — free to use, modify, and distribute.

---

<div align="center">

### 👤 Author

**Satyam Pandey**

⭐ If you found this project useful, consider giving it a star!

</div>
