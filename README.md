# 🏥 MediQ – AI-Powered Healthcare Platform



An AI-powered healthcare app built with Django. Chat with AI, book appointments, order medicines, and manage medical records.


A modern, AI-driven healthcare application built with Django. Get instant medical guidance, book appointments, manage prescriptions, and order medicines - all in one place!🚀 Introduction

MediQ is a full-stack AI-powered healthcare platform built using Django that simplifies patient care by integrating AI consultation, appointment management, online pharmacy, and medical records into a single system.



## ✨ Features!



- 🤖 **AI Chat** - Get instant medical guidance!The platform leverages Google Gemini AI to provide real-time, context-aware medical assistance, helping bridge the gap between patients and healthcare services with a seamless digital experience.

- 📅 **Appointments** - Book doctor appointments

- 💊 **Pharmacy** - Browse & order 15+ medicines!

- 📄 **Medical Records** - Upload health documents

- 📊 **Dashboard** - View health analytics!

- 📋 **Prescriptions** - AI-generated suggestions



---

---AI-driven healthcare assistance

## 🚀 Quick Setup

End-to-end patient workflow (consult → appointment → prescription → order → records)

### Prerequisites

- Python 3.13+## 🚀 IntroductionScalable full-stack architecture

- Git

Secure and user-friendly system

### Installation

MediQ is a comprehensive healthcare platform that brings together AI consultation, appointment booking, online pharmacy, and medical records management. Using Google Gemini AI, it provides real-time medical guidance while maintaining a seamless, secure user experience.

```bash

# Clone✨ Features:-

cd AI-MediQ---


# Install & setup

pip install -r requirements.txt### 🤖 AI Consultation SystemConsultation history tracking

python manage.py migrate

python manage.py createsuperuser- Chat with AI for instant medical guidanceVoice & text-based interaction

```

- Real-time, context-aware responses📅 Appointment Management

### Create `.env` file

```env- Consultation history trackingBook appointments with doctors

GEMINI_API_KEY=your_api_key_here

DEBUG=True- 24/7 availabilityMultiple consultation modes (In-person, Video, Phone)

SECRET_KEY=your-secret-key

ALLOWED_HOSTS=localhost,127.0.0.1Emergency & follow-up options

```

### 📅 Appointment ManagementAppointment status tracking

### Run

```bash- Easy appointment booking💊 Online Pharmacy

python manage.py runserver

```- Choose doctor and departmentBrowse and search medicines



Open: **http://localhost:8000**- Multiple consultation modes (In-person, Video, Phone)Add to cart and checkout system



---- Track appointment statusOrder tracking and management



## 🔑 Get API Key- Emergency & follow-up optionsReal-time stock availability



1. Visit [Google AI Studio](https://aistudio.google.com/)📄 Medical Records Management

2. Click "Get API Key"

3. Add to `.env` as `GEMINI_API_KEY`### 💊 Online PharmacyUpload health reports (PDFs, images)



---- Browse 15+ medicinesCategorize reports (Lab, X-ray, etc.)



## 📱 Main Features- Advanced search functionalitySecure storage and easy retrieval



| Feature | URL |- Shopping cart systemDownload anytime

|---------|-----|

| AI Chat | /consultation/ |- Easy checkout & payment📋 Prescription System

| Pharmacy | /pharmacy/ |

| Appointments | /appointments/ |- Real-time stock availabilityAI-generated prescription suggestions

| Medical Reports | /medical-reports/ |

| Prescriptions | /prescriptions/ |- Order trackingSymptom-based recommendations

| Dashboard | /dashboard/ |

| Admin | /admin/ |Prescription history tracking



---### 📄 Medical Records📊 Health Analytics Dashboard



## 🛠️ Tech Stack- Upload health reports (PDF, Images)Interactive charts and visualizations



- **Backend:** Django 6.0.3- Categorize by type (Lab, X-ray, Scan, etc.)Health trends and statistics

- **Frontend:** Bootstrap 5.3.0, HTML, CSS, JS

- **Database:** SQLite3- Secure storageAppointment & medical history insights

- **AI:** Google Gemini API

- Easy download & retrieval🔐 Authentication & Security

---

Secure login & registration system

## 📁 Structure

### 📋 PrescriptionsRole-based access (Patient/Admin)

```

AI-MediQ/- AI-generated prescription suggestionsPassword hashing (PBKDF2)

├── manage.py

├── requirements.txt- Symptom-based recommendationsCSRF, XSS, SQL Injection protection

├── README.md

├── .env (create yourself)- Download prescriptionsEnvironment-based API key security

├── medical_voice/          # Project settings

├── healthcare/             # Main app- Prescription history

├── templates/              # HTML pages

└── django_env/             # Virtual environment🛠️ Tech Stack:-

```

### 📊 Health Dashboard

---

- Interactive charts & graphsBackend

## 🐛 Common Issues

- Health statistics overviewDjango (Python)

| Issue | Fix |

|-------|-----|- Appointment historyDjango ORM

| Module not found | Activate venv & `pip install -r requirements.txt` |

| API key invalid | Create `.env` with valid `GEMINI_API_KEY` |- Medical record trackingFrontend

| Port 8000 in use | `python manage.py runserver 8001` |

| No medicines | Run `python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_voice.settings'); django.setup(); exec(open('add_medicines.py').read())"` |- Visual health trendsHTML, CSS, Bootstrap



---JavaScript (AJAX)



## 📚 Default Admin### 🔐 Security FeaturesDatabase



```- Secure login & registrationSQLite (PostgreSQL-ready for production)

Username: admin

Password: (set during createsuperuser)- Password encryption (PBKDF2)AI Integration

```

- CSRF, XSS, SQL injection protectionGoogle Gemini API

Access: **http://localhost:8000/admin**

- Environment-based API key managementVisualization

---

Chart.js



---AI Consultation



## 📄 License| Component | Technology |Appointment Booking



MIT License - Free to use|-----------|-----------|Pharmacy & Orders




## 👤 Author| **Frontend** | Bootstrap 5.3.0, HTML, CSS, JavaScript |Prescriptions



**Satyam Pandey** - [@satyamp18](https://github.com/satyamp18)| **Database** | SQLite3 (PostgreSQL-ready) |Health Dashboard



---| **AI Engine** | Google Gemini 2.5 Flash API |



<div align="center">| **Charts** | Chart.js for visualization |🎨 UI/UX Highlights



**[GitHub](https://github.com/satyamp18/AI-MediQ)** | **[Issues](https://github.com/satyamp18/AI-MediQ/issues)** | **[Star ⭐](https://github.com/satyamp18/AI-MediQ)**| **Authentication** | Django Session-based |Fully responsive design (Mobile + Desktop)



</div>Modern and clean interface


---Smooth navigation and user experience

🚀 Future Enhancements

## 📋 Quick SetupVideo consultation system

Payment gateway integration

### PrerequisitesMobile app (React Native)

- Python 3.13+Advanced analytics & notifications

- pip (package manager)👨‍💻 Author

- Git

Satyam Pandey


Open: **http://localhost:8000**

---

## 📖 How to Use

### 1. Register & Login
- Go to `/register/` to create account
- Login with your credentials

### 2. Use AI Consultant
- Navigate to "AI Consultation"
- Type your health question
- Get instant AI response
- View chat history

### 3. Book Appointment
- Click "Appointments"
- Fill form with symptoms
- Select date, time, and doctor
- Choose consultation type
- Submit booking

### 4. Order Medicine
- Go to "Pharmacy"
- Search or browse medicines
- Add to cart
- Proceed to checkout
- Confirm order

### 5. Upload Medical Records
- Go to "Medical Reports"
- Click "Upload Report"
- Select file (PDF/Image)
- Add description & category
- Save

### 6. View Health Dashboard
- Click "Health Dashboard"
- See statistics & charts
- Track appointments
- Monitor medical records

---


## 📁 Project Structure

```
AI-MediQ/
├── manage.py                 # Django command
├── requirements.txt          # Dependencies
├── README.md                # Documentation
├── .env                     # Environment config (create yourself)
│
├── medical_voice/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── healthcare/              # Main app
│   ├── models.py           # 8 Database models
│   ├── views.py            # 24+ Views
│   ├── urls.py             # Routes
│   └── admin.py            # Admin setup
│
├── templates/              # HTML pages
│   └── healthcare/
│       ├── base.html
│       ├── dashboard.html
│       ├── voice_consultation.html
│       ├── appointments.html
│       ├── pharmacy.html
│       ├── prescriptions.html
│       ├── medical_reports.html
│       └── health_dashboard.html
│
└── django_env/             # Virtual environment
```

---

## 🎨 UI/UX Features

✅ Fully responsive (Mobile + Desktop)  
✅ Modern dark theme with cyan/teal accents  
✅ Smooth animations & transitions  
✅ Intuitive navigation  
✅ Professional design  
✅ Fast loading  

---


---



## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Make changes and test
4. Commit: `git commit -m "Add feature description"`
5. Push: `git push origin feature/your-feature`
6. Create Pull Request

---

## 👤 Author

**Satyam Pandey**
- GitHub: [@satyamp18](https://github.com/satyamp18)
- Repository: [AI-MediQ](https://github.com/satyamp18/AI-MediQ)


---

<div align="center">

### ❤️ Made with passion for better healthcare

**[GitHub](https://github.com/satyamp18/AI-MediQ)** | **[Report Issue](https://github.com/satyamp18/AI-MediQ/issues)** | **[Suggest Feature](https://github.com/satyamp18/AI-MediQ/discussions)**

If you find this project helpful, please give it a ⭐ on GitHub!

</div>
