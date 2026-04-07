# 🏥 AI Medical Voice Agent - Django Version

A comprehensive healthcare platform with AI-powered medical consultation, appointment management, medical report storage, prescription suggestions, and online pharmacy services.

## 🌟 Features

### 1. **Authentication & User Management**
- User registration and login
- Secure password hashing
- Patient profile management
- Role-based access control

### 2. **Voice & AI Consultation** 🎙️
- AI-powered medical assistant using Google Gemini API
- Multiple consultation modes:
  - General Health
  - Medicine Info
  - Nutrition & Diet
  - Mental Health Support
- Multi-language support (English, Hindi, Spanish, French)
- Chat history tracking
- Educational disclaimer system

### 3. **Appointment Management** 📅
- Book appointments with doctors
- Multiple consultation types:
  - In-Person
  - Video Call
  - Phone Call
- 9 different specializations
- Emergency and follow-up appointment marking
- Appointment status tracking
- Cancel appointments

### 4. **Medical Reports** 📄
- Secure file upload (PDF, Images)
- Categorized report types:
  - Blood Test
  - X-Ray
  - MRI
  - CT Scan
  - Ultrasound
  - Prescription
  - Other
- Download reports anytime
- Add notes to reports
- Date tracking

### 5. **Prescriptions & Suggestions** 💊
- AI-generated prescription suggestions
- Educational-only content (with disclaimers)
- Symptom-based suggestions
- Download prescriptions as text
- Prescription history

### 6. **Online Pharmacy** 🛒
- Medicine catalog with pricing
- Search and filter medicines
- Add to cart functionality
- Checkout and order management
- Order confirmation
- Stock tracking

### 7. **Health Analytics Dashboard** 📊
- Statistical overview:
  - Total appointments
  - Medical reports count
  - Prescriptions count
- Monthly appointment trends (bar chart)
- Report type distribution (pie chart)
- Recent appointments timeline
- Activity summary

### 8. **Modern UI/UX** 🎨
- Bootstrap 5 responsive design
- Gradient navigation bar
- Sidebar navigation
- Card-based layouts
- Interactive charts using Chart.js
- Mobile-friendly interface
- Smooth animations
- Professional color scheme

## 📋 Project Structure

```
medical voice/
├── manage.py
├── setup_db.py                 # Database initialization script
├── db.sqlite3                  # SQLite database
├── django_env/                 # Virtual environment
├── medical_voice/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── healthcare/                 # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── migrations/
├── templates/
│   └── healthcare/
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── voice_consultation.html
│       ├── appointments.html
│       ├── medical_reports.html
│       ├── prescriptions.html
│       ├── pharmacy.html
│       ├── order_confirmation.html
│       └── health_dashboard.html
├── static/                     # CSS, JS, Images
└── media/                      # User uploads
```

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- pip
- Windows PowerShell

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd "c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice"
```

2. **Create and activate virtual environment:**
```bash
python -m venv django_env
django_env\Scripts\activate.bat
```

3. **Install dependencies:**
```bash
pip install django pillow google-generativeai SpeechRecognition gtts python-multipart
```

4. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Initialize database with sample data:**
```bash
python setup_db.py
```

6. **Create superuser (if not exists):**
```bash
python manage.py createsuperuser
```

7. **Collect static files:**
```bash
python manage.py collectstatic --noinput
```

### Running the Application

```bash
python manage.py runserver
```

Access the application at: **http://localhost:8000**

#### Login Credentials (Default)
- **Username:** admin
- **Password:** admin123

## 🔑 Key URLs

- Home/Dashboard: `http://localhost:8000/dashboard/`
- Voice Consultation: `http://localhost:8000/consultation/`
- Appointments: `http://localhost:8000/appointments/`
- Medical Reports: `http://localhost:8000/reports/`
- Prescriptions: `http://localhost:8000/prescriptions/`
- Pharmacy: `http://localhost:8000/pharmacy/`
- Health Dashboard: `http://localhost:8000/health-dashboard/`
- Admin Panel: `http://localhost:8000/admin/`

## 📊 Database Models

### Patient
- User (OneToOneField)
- Age, Gender, Phone
- Profile Picture
- Created At

### Appointment
- Patient (ForeignKey)
- Department, Doctor Name
- Date, Time
- Consultation Type
- Symptoms
- Emergency/Follow-up flags
- Status tracking

### MedicalReport
- Patient (ForeignKey)
- Name, File
- Report Type
- Report Date
- Notes
- Upload timestamp

### Prescription
- Patient (ForeignKey)
- Symptoms
- Suggestion (AI-generated)
- Created At

### Medicine
- Name, Dosage
- Price
- Description
- Stock status
- Image

### Order & OrderItem
- Patient (ForeignKey)
- Medicines (ManyToManyField)
- Total Price
- Status tracking
- Timestamps

### ConsultationHistory
- Patient (ForeignKey)
- Question, AI Response
- Mode, Language
- Created At

## 🔐 Security Features

- Secure password hashing with Django's built-in authentication
- CSRF protection on all forms
- SQL injection prevention via ORM
- XSS protection via template auto-escaping
- Login required decorators on protected views
- Session management
- HTTPS ready (requires additional configuration for production)

## 🎨 Design Features

### Color Scheme
- **Primary:** Purple gradient (#667eea to #764ba2)
- **Light backgrounds:** #f0f2f5, #f8f9fa
- **Text:** Dark (#212529) on light backgrounds
- **Accents:** Blue (#0d6efd), Green (#198754)

### Responsive Design
- Bootstrap 5 grid system
- Mobile-first approach
- Flexbox layouts
- Media queries for tablets and phones
- Touch-friendly buttons and inputs

### Interactive Elements
- Smooth animations and transitions
- Hover effects on cards
- Loading spinners
- Modal dialogs
- Toast notifications
- Chart visualizations

## 📱 API Endpoints

### AI Consultation
- `POST /api/ask-ai/` - Get AI response to medical question

### Shopping
- `POST /api/add-to-cart/` - Add medicine to cart

## 🤖 AI Integration

- **Provider:** Google Gemini API
- **Models:** gemini-2.5-pro
- **Capabilities:**
  - Medical information provision
  - Symptom analysis
  - Medicine suggestions (educational)
  - Health tips generation

**Note:** Always set your valid Google Gemini API key in `healthcare/views.py`

## 📝 Important Notes

⚠️ **MEDICAL DISCLAIMER:**
This platform provides **educational medical information only**. It is **NOT** a substitute for professional medical advice, diagnosis, or treatment. Always consult with a licensed healthcare provider for:
- Diagnosis and treatment planning
- Prescription medications
- Emergency medical situations
- Chronic disease management

## 🚀 Deployment (Production Ready)

For production deployment:

1. **Update settings.py:**
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS`
   - Set secure secret key
   - Configure HTTPS/SSL

2. **Use production server:**
   - Gunicorn
   - uWSGI
   - Waitress

3. **Database:**
   - Upgrade to PostgreSQL
   - Configure backups

4. **Static files:**
   - Use WhiteNoise or CDN
   - Collect static files

5. **Environment variables:**
   - Use python-decouple or similar
   - Store API keys securely

## 🛠️ Customization

### Adding New Features

1. **New Model:** Add to `healthcare/models.py`
2. **New View:** Add to `healthcare/views.py`
3. **New URL:** Add to `healthcare/urls.py`
4. **New Template:** Create in `templates/healthcare/`

### Styling

Edit `base.html` `<style>` section to customize:
- Colors
- Fonts
- Spacing
- Animations

### Medicines Catalog

Edit `setup_db.py` to add more sample medicines or use Django admin.

## 📞 Support & Maintenance

### Common Issues

1. **API Key Error:**
   - Get key from: https://makersuite.google.com/app/apikey
   - Update in `healthcare/views.py`

2. **Database Issues:**
   - Reset: `python manage.py migrate healthcare zero`
   - Re-migrate: `python manage.py migrate`

3. **Static Files:**
   - Run: `python manage.py collectstatic`

## 🎓 Learning Resources

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/
- Chart.js Documentation: https://www.chartjs.org/docs/latest/
- Google Gemini API: https://ai.google.dev/

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**AI Medical Voice Agent Development Team**
- Converted from Streamlit to Django Framework
- Enhanced UI with Bootstrap 5
- Added comprehensive healthcare features

## 🤝 Contributing

Feel free to fork, modify, and improve this project. Contributions are welcome!

---

**Last Updated:** March 23, 2026
**Status:** ✅ Production Ready
**Version:** 2.0 (Django)
