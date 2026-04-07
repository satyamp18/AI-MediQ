# 🏥 MediQ - AI-Powered Healthcare Platform

![Django](https://img.shields.io/badge/Django-6.0.3-darkgreen)
![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)
![SQLite](https://img.shields.io/badge/SQLite-3-lightblue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**MediQ** is a comprehensive AI-powered healthcare platform built with Django that revolutionizes patient care management. It combines modern web technologies with artificial intelligence to provide:

- 🤖 **AI-Powered Consultations** using Google Gemini API
- 📅 **Smart Appointment Management**
- 💊 **Online Pharmacy Integration**
- 📊 **Health Analytics Dashboard**
- 🗣️ **Voice Consultation Support**
- 📄 **Medical Record Management**

The platform is designed to bridge the gap between patients and healthcare providers while leveraging cutting-edge AI technology for personalized medical guidance.

---

## ✨ Features

### 🔐 Authentication & User Management
- User registration with email validation
- Secure login/logout functionality
- Role-based access control (Patient/Admin)
- Profile management
- Session-based authentication

### 🤖 AI Consultation System
- **Voice & Text Chat Interface** - Real-time communication with AI assistant
- **Google Gemini Integration** - Advanced natural language processing
- **Consultation History** - Track all previous consultations
- **Multi-language Support** - Support for multiple languages
- **Graceful Error Handling** - Fallback responses for API failures
- **Context-Aware Responses** - Personalized medical guidance

### 📅 Appointment Management
- Book appointments with doctors
- Department/specialty selection (9 departments)
- Appointment scheduling with date & time
- Consultation type selection (In-person/Video/Phone)
- Emergency appointment flagging
- Follow-up appointment tracking
- Appointment status management (Pending/Confirmed/Completed/Cancelled)
- View appointment history

### 💊 Online Pharmacy
- Browse medicine catalog
- Advanced search functionality
- Medicine pricing and dosage information
- Stock availability tracking
- Shopping cart system
- Order management
- Order confirmation and tracking
- Multiple medicine order handling

### 📋 Medical Records Management
- Upload medical reports (PDF, Images)
- Report categorization (Lab Reports, X-rays, CT Scans, etc.)
- Report metadata storage
- Download medical documents
- Report organization and search

### 💊 Prescription Management
- AI-generated prescription suggestions
- Prescription history tracking
- Download prescriptions as PDF
- Medicine linking to prescriptions
- Symptom-based recommendations

### 📊 Health Analytics Dashboard
- Patient health metrics visualization
- Interactive charts and graphs (Chart.js)
- Appointment statistics
- Medical record tracking
- Health trend analysis
- Comprehensive overview of health journey

### 🎨 Modern UI/UX
- Responsive design (Mobile, Tablet, Desktop)
- Modern blue/teal color scheme
- Bootstrap 5.3.0 styling
- Bootstrap Icons integration
- Smooth animations and transitions
- Dark mode ready components
- Intuitive navigation

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 6.0.3
- **Database:** SQLite3 (Easily upgradeable to PostgreSQL)
- **Python Version:** 3.13+
- **ORM:** Django ORM

### Frontend
- **CSS Framework:** Bootstrap 5.3.0
- **JavaScript:** Vanilla JS + AJAX
- **Charts:** Chart.js for data visualization
- **Icons:** Bootstrap Icons 1.10.0
- **Templating:** Django Template Language

### APIs & Services
- **AI:** Google Generative AI (Gemini)
- **Environment Management:** python-decouple
- **File Handling:** Pillow

### Development Tools
- **Version Control:** Git
- **Package Manager:** pip
- **Virtual Environment:** venv

---

## 📁 Project Structure

```
medical_voice/
├── manage.py                          # Django management script
├── db.sqlite3                        # SQLite database
├── README.md                         # This file
├── SETUP_GUIDE.md                    # Setup instructions
├── API_KEYS_SETUP.md                 # API key configuration
├── API_KEY_FIX.md                    # API troubleshooting
├── requirements_django.txt           # Python dependencies
├── .env                              # Environment variables (not in repo)
├── .gitignore                        # Git ignore rules
│
├── medical_voice/                    # Main project settings
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Project URL configuration
│   ├── asgi.py                       # ASGI configuration
│   ├── wsgi.py                       # WSGI configuration
│   └── __init__.py
│
├── healthcare/                       # Main application
│   ├── models.py                     # 8 Django models
│   ├── views.py                      # 24+ view functions
│   ├── urls.py                       # App URL patterns
│   ├── admin.py                      # Django admin configuration
│   ├── apps.py
│   ├── migrations/                   # Database migrations
│   │   └── 0001_initial.py
│   └── __pycache__/
│
├── templates/                        # HTML templates
│   └── healthcare/
│       ├── base.html                 # Master template
│       ├── login.html                # Login page
│       ├── register.html             # Registration page
│       ├── dashboard.html            # Main dashboard
│       ├── voice_consultation.html   # AI chat interface
│       ├── appointments.html         # Appointment management
│       ├── medical_reports.html      # Medical records
│       ├── prescriptions.html        # Prescriptions
│       ├── pharmacy.html             # Medicine store
│       ├── order_confirmation.html   # Order success page
│       └── health_dashboard.html     # Analytics dashboard
│
└── django_env/                       # Virtual environment
    ├── Scripts/
    ├── Lib/
    └── pyvenv.cfg
```

---

## 🚀 Installation

### Prerequisites
- Python 3.13 or higher
- pip (Python package manager)
- Git
- Virtual environment support

### Step 1: Clone the Repository
```bash
git clone https://github.com/satyamp18/AI-MediQ.git
cd AI-MediQ
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv django_env
.\django_env\Scripts\activate

# macOS/Linux
python3 -m venv django_env
source django_env/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements_django.txt
```

### Step 4: Configure Environment Variables
```bash
# Create .env file in project root
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
```

Edit `.env` and add your API key:
```
GEMINI_API_KEY=your_api_key_here
DEBUG=True
SECRET_KEY=your_secret_key
```

### Step 5: Apply Database Migrations
```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### Step 7: Load Sample Data (Optional)
```bash
python manage.py loaddata sample_medicines  # If available
```

### Step 8: Run Development Server
```bash
python manage.py runserver
```

Server will start at: **http://localhost:8000**

---

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
# API Configuration
GEMINI_API_KEY=sk-xxxxxxxxxxxxx

# Django Configuration
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=db.sqlite3
DB_ENGINE=django.db.backends.sqlite3

# Email (Optional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Get Your Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Click "Get API Key"
3. Create a new API key
4. Copy and paste into `.env` file

**Detailed guide:** See [API_KEYS_SETUP.md](API_KEYS_SETUP.md)

---

## 📖 Usage

### Access the Application

| Page | URL | Access |
|------|-----|--------|
| Home | http://localhost:8000 | Public |
| Login | http://localhost:8000/login/ | Public |
| Register | http://localhost:8000/register/ | Public |
| Dashboard | http://localhost:8000/dashboard/ | Authenticated |
| AI Consultation | http://localhost:8000/voice-consultation/ | Authenticated |
| Appointments | http://localhost:8000/appointments/ | Authenticated |
| Medical Reports | http://localhost:8000/medical-reports/ | Authenticated |
| Prescriptions | http://localhost:8000/prescriptions/ | Authenticated |
| Pharmacy | http://localhost:8000/pharmacy/ | Authenticated |
| Health Analytics | http://localhost:8000/health-dashboard/ | Authenticated |
| Admin Panel | http://localhost:8000/admin/ | Admin Only |

### Default Admin Credentials
```
Username: admin
Password: admin123
```

⚠️ **Change password immediately in production!**

### Sample User Registration
1. Go to http://localhost:8000/register/
2. Fill in username, email, password
3. Click "Register"
4. Login with your credentials
5. Start using features!

---

## 🗄️ Database Schema

### Models

#### 1. **Patient**
```python
- User (OneToOneField)
- age (IntegerField)
- gender (CharField)
- phone (CharField)
- profile_picture (ImageField)
- created_at (DateTimeField)
```

#### 2. **Appointment**
```python
- patient (ForeignKey → Patient)
- department (CharField - 9 choices)
- doctor_name (CharField)
- appointment_date (DateField)
- appointment_time (TimeField)
- consultation_type (CharField - 3 choices)
- symptoms (TextField)
- is_emergency (BooleanField)
- is_followup (BooleanField)
- status (CharField - 4 states)
- created_at, updated_at (DateTimeField)
```

#### 3. **MedicalReport**
```python
- patient (ForeignKey → Patient)
- name (CharField)
- file (FileField)
- report_type (CharField - 7 categories)
- report_date (DateField)
- notes (TextField)
- uploaded_at (DateTimeField)
```

#### 4. **Prescription**
```python
- patient (ForeignKey → Patient)
- symptoms (TextField)
- suggestion (TextField - AI-generated)
- created_at (DateTimeField)
```

#### 5. **ConsultationHistory**
```python
- patient (ForeignKey → Patient)
- question (TextField)
- ai_response (TextField)
- mode (CharField)
- language (CharField)
- created_at (DateTimeField)
```

#### 6. **Medicine**
```python
- name (CharField)
- dosage (CharField)
- price (DecimalField)
- description (TextField)
- in_stock (BooleanField)
- image (ImageField)
```

#### 7. **Order**
```python
- patient (ForeignKey → Patient)
- medicines (ManyToMany → Medicine through OrderItem)
- total_price (DecimalField)
- status (CharField - 5 states)
- created_at, updated_at (DateTimeField)
```

#### 8. **OrderItem**
```python
- order (ForeignKey → Order)
- medicine (ForeignKey → Medicine)
- quantity (IntegerField)
- price (DecimalField)
```

---

## 🔌 API Endpoints

### Authentication
- `POST /register/` - User registration
- `POST /login/` - User login
- `GET /logout/` - User logout

### Dashboard
- `GET /dashboard/` - Main dashboard with metrics

### Consultations
- `GET /voice-consultation/` - Chat interface
- `POST /ask-ai/` - Send question to AI (JSON API)

### Appointments
- `GET /appointments/` - List and book appointments
- `POST /appointments/` - Create appointment
- `GET /cancel-appointment/<id>/` - Cancel appointment

### Medical Records
- `GET /medical-reports/` - List reports
- `POST /medical-reports/` - Upload report
- `GET /download-report/<id>/` - Download report

### Prescriptions
- `GET /prescriptions/` - List prescriptions
- `GET /download-prescription/<id>/` - Download prescription

### Pharmacy
- `GET /pharmacy/` - Browse medicines
- `POST /add-to-cart/` - Add to cart (JSON)
- `GET /checkout/` - Checkout page
- `POST /checkout/` - Process order

### Health Analytics
- `GET /health-dashboard/` - Analytics dashboard

---

## 🎨 UI/UX Features

### Color Scheme
- **Primary:** Blue/Teal (#00b4d8 → #0096c7)
- **Accent:** Light Blue (#f0f9ff)
- **Text:** Dark Gray (#212529)
- **Borders:** Subtle Blue (#00b4d8)

### Responsive Design
- ✅ Mobile-first approach
- ✅ Tablet optimization
- ✅ Desktop experience
- ✅ Touch-friendly buttons
- ✅ Collapsible navigation

### Components
- Modern card layouts with hover effects
- Animated transitions
- Progress indicators
- Toast notifications
- Modal dialogs
- Form validation

---

## 📊 Screenshots

### Dashboard
Clean overview with appointment count, medical reports, and prescriptions metrics.

### AI Consultation
Real-time chat interface with message history and AI responses.

### Appointment Booking
Easy-to-use form with department selection, date/time picker, and consultation type.

### Pharmacy
Browse medicines with search, pricing, and shopping cart functionality.

### Health Analytics
Interactive charts showing health trends and statistics.

---

## 🔒 Security Features

- ✅ CSRF Protection
- ✅ SQL Injection Prevention (Django ORM)
- ✅ XSS Protection
- ✅ Secure Password Hashing (PBKDF2)
- ✅ Session-based Authentication
- ✅ Environment Variable Protection (.env in .gitignore)
- ✅ API Key Encryption
- ✅ Input Validation
- ✅ Rate Limiting Ready

---

## 🚀 Deployment

### Prepare for Production
1. Set `DEBUG=False` in settings.py
2. Update `ALLOWED_HOSTS` with your domain
3. Use strong `SECRET_KEY`
4. Set up environment variables on server
5. Use PostgreSQL instead of SQLite

### Deploy on Heroku
```bash
# Install Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Deploy on PythonAnywhere
1. Create account on PythonAnywhere
2. Upload code via git
3. Configure virtual environment
4. Set up web app configuration
5. Configure environment variables

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'google.generativeai'"**
```bash
pip install google-generativeai
```

**Issue: "Error: 400 API key not valid"**
- Check `.env` file has correct API key
- Verify API key is active on Google AI Studio
- See [API_KEY_FIX.md](API_KEY_FIX.md) for detailed help

**Issue: "Port 8000 already in use"**
```bash
python manage.py runserver 8001
```

**Issue: Database migration errors**
```bash
python manage.py migrate --fake-initial
```

For more help, see [API_KEY_FIX.md](API_KEY_FIX.md) and [API_KEYS_SETUP.md](API_KEYS_SETUP.md)

---

## 📚 Documentation

- [Setup Guide](SETUP_GUIDE.md) - Detailed setup instructions
- [API Keys Setup](API_KEYS_SETUP.md) - How to configure API keys
- [API Key Troubleshooting](API_KEY_FIX.md) - Solving API issues
- [Django Documentation](https://docs.djangoproject.com/) - Official Django docs

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

### Fork & Clone
```bash
git clone https://github.com/yourusername/AI-MediQ.git
cd AI-MediQ
git checkout -b feature/your-feature-name
```

### Make Changes
1. Create a feature branch
2. Make your improvements
3. Test thoroughly
4. Keep commits clean and descriptive

### Submit Pull Request
```bash
git add .
git commit -m "Add: Description of your feature"
git push origin feature/your-feature-name
```

### Guidelines
- Follow PEP 8 style guide
- Write clear commit messages
- Add docstrings to functions
- Test your code
- Update documentation

---

## 📋 Roadmap

### Current Version (v1.0)
- ✅ AI Consultation System
- ✅ Appointment Management
- ✅ Pharmacy System
- ✅ Medical Records
- ✅ Health Analytics

### Upcoming Features (v2.0)
- 🔜 Video Consultation Integration
- 🔜 Prescription Auto-Fulfillment
- 🔜 Insurance Integration
- 🔜 Mobile App (React Native)
- 🔜 Real-time Notifications
- 🔜 Advanced Analytics
- 🔜 Payment Gateway Integration
- 🔜 Multi-language Support

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👥 Authors

- **Developer:** Satyam Pandey
- **GitHub:** [@satyamp18](https://github.com/satyamp18)
- **Repository:** [AI-MediQ](https://github.com/satyamp18/AI-MediQ)

---

## 📞 Support & Contact

- 📧 Email: support@mediq.local
- 💬 Issues: [GitHub Issues](https://github.com/satyamp18/AI-MediQ/issues)
- 📝 Discussions: [GitHub Discussions](https://github.com/satyamp18/AI-MediQ/discussions)

---

## 🙏 Acknowledgments

- **Django Team** - For the amazing web framework
- **Google AI** - For Gemini API access
- **Bootstrap** - For the UI framework
- **Chart.js** - For visualization library
- **Community** - For support and feedback

---

## 📈 Project Statistics

- **Total Models:** 8
- **Total Views:** 24+
- **Total Templates:** 11
- **Lines of Code:** 3000+
- **API Endpoints:** 20+
- **Test Coverage:** Growing

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

[⭐ Star on GitHub](https://github.com/satyamp18/AI-MediQ) | [🐛 Report Issues](https://github.com/satyamp18/AI-MediQ/issues) | [💡 Suggest Features](https://github.com/satyamp18/AI-MediQ/discussions)

Made with ❤️ by [Satyam Pandey](https://github.com/satyamp18)

</div>
