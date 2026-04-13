# 🏥 MediQ - AI-Powered Healthcare Platform🏥 MediQ – AI-Powered Healthcare Platform



A modern, AI-driven healthcare application built with Django. Get instant medical guidance, book appointments, manage prescriptions, and order medicines - all in one place!🚀 Introduction



![Django](https://img.shields.io/badge/Django-6.0.3-darkgreen)MediQ is a full-stack AI-powered healthcare platform built using Django that simplifies patient care by integrating AI consultation, appointment management, online pharmacy, and medical records into a single system.

![Python](https://img.shields.io/badge/Python-3.13+-blue)

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)The platform leverages Google Gemini AI to provide real-time, context-aware medical assistance, helping bridge the gap between patients and healthcare services with a seamless digital experience.

![AI](https://img.shields.io/badge/AI-Google%20Gemini-blue)

![License](https://img.shields.io/badge/License-MIT-green)🎯 Key Highlights:-



---AI-driven healthcare assistance

End-to-end patient workflow (consult → appointment → prescription → order → records)

## 🚀 IntroductionScalable full-stack architecture

Secure and user-friendly system

MediQ is a comprehensive healthcare platform that brings together AI consultation, appointment booking, online pharmacy, and medical records management. Using Google Gemini AI, it provides real-time medical guidance while maintaining a seamless, secure user experience.

✨ Features:-

---

🤖 AI Consultation System

## ✨ Key FeaturesReal-time AI chat for medical guidance

Context-aware and personalized responses

### 🤖 AI Consultation SystemConsultation history tracking

- Chat with AI for instant medical guidanceVoice & text-based interaction

- Real-time, context-aware responses📅 Appointment Management

- Consultation history trackingBook appointments with doctors

- 24/7 availabilityMultiple consultation modes (In-person, Video, Phone)

Emergency & follow-up options

### 📅 Appointment ManagementAppointment status tracking

- Easy appointment booking💊 Online Pharmacy

- Choose doctor and departmentBrowse and search medicines

- Multiple consultation modes (In-person, Video, Phone)Add to cart and checkout system

- Track appointment statusOrder tracking and management

- Emergency & follow-up optionsReal-time stock availability

📄 Medical Records Management

### 💊 Online PharmacyUpload health reports (PDFs, images)

- Browse 15+ medicinesCategorize reports (Lab, X-ray, etc.)

- Advanced search functionalitySecure storage and easy retrieval

- Shopping cart systemDownload anytime

- Easy checkout & payment📋 Prescription System

- Real-time stock availabilityAI-generated prescription suggestions

- Order trackingSymptom-based recommendations

Prescription history tracking

### 📄 Medical Records📊 Health Analytics Dashboard

- Upload health reports (PDF, Images)Interactive charts and visualizations

- Categorize by type (Lab, X-ray, Scan, etc.)Health trends and statistics

- Secure storageAppointment & medical history insights

- Easy download & retrieval🔐 Authentication & Security

Secure login & registration system

### 📋 PrescriptionsRole-based access (Patient/Admin)

- AI-generated prescription suggestionsPassword hashing (PBKDF2)

- Symptom-based recommendationsCSRF, XSS, SQL Injection protection

- Download prescriptionsEnvironment-based API key security

- Prescription history

🛠️ Tech Stack:-

### 📊 Health Dashboard

- Interactive charts & graphsBackend

- Health statistics overviewDjango (Python)

- Appointment historyDjango ORM

- Medical record trackingFrontend

- Visual health trendsHTML, CSS, Bootstrap

JavaScript (AJAX)

### 🔐 Security FeaturesDatabase

- Secure login & registrationSQLite (PostgreSQL-ready for production)

- Password encryption (PBKDF2)AI Integration

- CSRF, XSS, SQL injection protectionGoogle Gemini API

- Environment-based API key managementVisualization

Chart.js

---

🌐 Core Modules:-

## 🛠️ Technology Stack

AI Consultation

| Component | Technology |Appointment Booking

|-----------|-----------|Pharmacy & Orders

| **Backend** | Django 6.0.3 (Python) |Medical Records

| **Frontend** | Bootstrap 5.3.0, HTML, CSS, JavaScript |Prescriptions

| **Database** | SQLite3 (PostgreSQL-ready) |Health Dashboard

| **AI Engine** | Google Gemini 2.5 Flash API |

| **Charts** | Chart.js for visualization |🎨 UI/UX Highlights

| **Authentication** | Django Session-based |Fully responsive design (Mobile + Desktop)

Modern and clean interface

---Smooth navigation and user experience

🚀 Future Enhancements

## 📋 Quick SetupVideo consultation system

Payment gateway integration

### PrerequisitesMobile app (React Native)

- Python 3.13+Advanced analytics & notifications

- pip (package manager)👨‍💻 Author

- Git

Satyam Pandey

### Installation (5 Easy Steps)GitHub: https://github.com/satyamp18

**Step 1: Clone Repository**
```bash
git clone https://github.com/satyamp18/AI-MediQ.git
cd AI-MediQ
```

**Step 2: Create Virtual Environment**
```bash
# Windows
python -m venv django_env
.\django_env\Scripts\activate

# macOS/Linux
python3 -m venv django_env
source django_env/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Setup Database & Create .env File**
```bash
python manage.py migrate
python manage.py createsuperuser  # Create admin account
```

Create `.env` in project root:
```env
GEMINI_API_KEY=your_api_key_here
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Step 5: Run Server**
```bash
python manage.py runserver
```

Open: **http://localhost:8000**

---

## 🔑 Get Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Click "Get API Key"
3. Create new API key
4. Add to `.env` file as `GEMINI_API_KEY`

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

## 🗄️ Database Models

| Model | Purpose |
|-------|---------|
| Patient | User health profile |
| Appointment | Doctor appointments |
| Medicine | Medicine catalog |
| Order | Medicine orders |
| Prescription | AI suggestions |
| MedicalReport | Health documents |
| ConsultationHistory | AI conversations |

---

## 🌐 Main Pages & URLs

| Page | URL | Features |
|------|-----|----------|
| Home | `/` | Welcome page |
| Register | `/register/` | Create account |
| Login | `/login/` | Sign in |
| Dashboard | `/dashboard/` | Health overview |
| AI Chat | `/consultation/` | AI assistant |
| Appointments | `/appointments/` | Book appointments |
| Pharmacy | `/pharmacy/` | Browse & order medicines |
| Prescriptions | `/prescriptions/` | AI suggestions |
| Medical Reports | `/medical-reports/` | Upload documents |
| Health Dashboard | `/health-dashboard/` | Analytics & charts |
| Admin Panel | `/admin/` | Admin control |

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

## 🐛 Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| **"Module not found"** | Activate virtual environment & run `pip install -r requirements.txt` |
| **"API key invalid"** | Create `.env` file with valid `GEMINI_API_KEY` |
| **"Port 8000 in use"** | Run `python manage.py runserver 8001` |
| **"Database error"** | Run `python manage.py migrate` |
| **"No medicines showing"** | Run `python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_voice.settings'); django.setup(); exec(open('add_medicines.py').read())"` |

---

## 📚 Admin Access

**Default Admin Credentials:**
```
Username: admin
Password: (set during createsuperuser)
```

Access: **http://localhost:8000/admin**

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

## 🚀 Future Enhancements

- 🔜 Video consultation system
- 🔜 Payment gateway integration (Stripe/Razorpay)
- 🔜 Mobile app (React Native)
- 🔜 Real-time notifications
- 🔜 Advanced analytics
- 🔜 Multi-language support
- 🔜 Prescription auto-fulfillment

---

## 📄 License

MIT License - Free to use and modify

---

## 👤 Author

**Satyam Pandey**
- GitHub: [@satyamp18](https://github.com/satyamp18)
- Repository: [AI-MediQ](https://github.com/satyamp18/AI-MediQ)

---

## 💬 Support & Feedback

- 🐛 **Report Issues:** [GitHub Issues](https://github.com/satyamp18/AI-MediQ/issues)
- 💡 **Suggest Features:** [GitHub Discussions](https://github.com/satyamp18/AI-MediQ/discussions)
- ⭐ **Star the Project:** Show your support!

---

<div align="center">

### ❤️ Made with passion for better healthcare

**[GitHub](https://github.com/satyamp18/AI-MediQ)** | **[Report Issue](https://github.com/satyamp18/AI-MediQ/issues)** | **[Suggest Feature](https://github.com/satyamp18/AI-MediQ/discussions)**

If you find this project helpful, please give it a ⭐ on GitHub!

</div>
