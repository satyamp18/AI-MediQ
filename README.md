# 🏥 MediQ - AI Healthcare Platform# 🏥 MediQ - AI-Powered Healthcare Platform# 🏥 MediQ - AI-Powered Healthcare Platform



A modern, AI-powered healthcare application built with Django. Get instant medical guidance, book appointments, manage prescriptions, and order medicines - all in one place!



![Django](https://img.shields.io/badge/Django-6.0.3-darkgreen)![Django](https://img.shields.io/badge/Django-6.0.3-darkgreen)![Django](https://img.shields.io/badge/Django-6.0.3-darkgreen)

![Python](https://img.shields.io/badge/Python-3.13+-blue)

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)![Python](https://img.shields.io/badge/Python-3.13+-blue)![Python](https://img.shields.io/badge/Python-3.13+-blue)

![License](https://img.shields.io/badge/License-MIT-green)

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)

---

![SQLite](https://img.shields.io/badge/SQLite-3-lightblue)![SQLite](https://img.shields.io/badge/SQLite-3-lightblue)

## ✨ Key Features

![Gemini API](https://img.shields.io/badge/Google%20Gemini-AI-blue)![License](https://img.shields.io/badge/License-MIT-green)

### 💬 AI Chat Consultant

- Chat with AI powered by Google Gemini![License](https://img.shields.io/badge/License-MIT-green)![Status](https://img.shields.io/badge/Status-Active-brightgreen)

- Get instant medical suggestions

- View consultation history![Status](https://img.shields.io/badge/Status-Active-brightgreen)

- Real-time responses

---

### 🏥 Appointment Booking

- Book appointments easily---

- Choose department and doctor

- Select consultation type (In-person, Video, Phone)## 📋 Table of Contents

- Track appointment status

- Emergency appointment option## 📋 Table of Contents



### 💊 Online Pharmacy- [Overview](#overview)

- Browse available medicines

- Search by medicine name- [Overview](#overview)- [Features](#features)

- Add to cart and checkout

- Track your orders- [Features](#features)- [Tech Stack](#tech-stack)

- Real-time stock availability

- [Tech Stack](#tech-stack)- [Project Structure](#project-structure)

### 📋 Prescription Management

- Get AI-generated prescription suggestions- [Project Structure](#project-structure)- [Installation](#installation)

- Download prescriptions

- View prescription history- [Installation](#installation)- [Configuration](#configuration)

- Medicine recommendations

- [Configuration](#configuration)- [Usage](#usage)

### 📋 Medical Records

- Upload health reports (PDF, Images)- [Usage](#usage)- [Database Schema](#database-schema)

- Organize medical documents

- Download files anytime- [Database Schema](#database-schema)- [API Endpoints](#api-endpoints)

- Categorize reports (Lab, X-ray, etc.)

- [API Endpoints](#api-endpoints)- [Screenshots](#screenshots)

### 📊 Health Dashboard

- View your health statistics- [Troubleshooting](#troubleshooting)- [Contributing](#contributing)

- See appointment history

- Track medical records- [Contributing](#contributing)- [License](#license)

- Interactive charts and graphs

- [License](#license)

### 🛒 Shopping & Orders

- Add medicines to cart---

- Checkout easily

- View order confirmation---

- Track order status

## 🎯 Overview

---

## 🎯 Overview

## 🛠️ Technology Used

**MediQ** is a comprehensive AI-powered healthcare platform built with Django that revolutionizes patient care management. It combines modern web technologies with artificial intelligence to provide:

- **Backend:** Django 6.0.3 (Python web framework)

- **Database:** SQLite3 (can upgrade to PostgreSQL)**MediQ** is a comprehensive AI-powered healthcare platform built with Django that revolutionizes patient care management. It combines modern web technologies with artificial intelligence to provide:

- **Frontend:** Bootstrap 5.3.0, HTML, CSS, JavaScript

- **AI:** Google Gemini 2.5 Flash API- 🤖 **AI-Powered Consultations** using Google Gemini API

- **Charts:** Chart.js for visualizations

- **Authentication:** Django Session-based- 🤖 **AI-Powered Consultations** using Google Gemini 2.5 Flash API- 📅 **Smart Appointment Management**



---- 📅 **Smart Appointment Management**- 💊 **Online Pharmacy Integration**



## 📋 Quick Setup- 💊 **Online Pharmacy Integration**- 📊 **Health Analytics Dashboard**



### Prerequisites- 📊 **Health Analytics Dashboard**- 🗣️ **Voice Consultation Support**

- Python 3.13+

- pip (package manager)- 🗣️ **Voice & Text Consultation Support**- 📄 **Medical Record Management**

- Git

- 📄 **Medical Record Management**

### Installation (5 Steps)

- 🛒 **Shopping Cart & Order System**The platform is designed to bridge the gap between patients and healthcare providers while leveraging cutting-edge AI technology for personalized medical guidance.

**Step 1: Clone Repository**

```bash

git clone https://github.com/satyamp18/AI-MediQ.git

cd AI-MediQThe platform is designed to bridge the gap between patients and healthcare providers while leveraging cutting-edge AI technology for personalized medical guidance.---

```



**Step 2: Create Virtual Environment**

```bash---## ✨ Features

# Windows

python -m venv django_env

.\django_env\Scripts\activate

## ✨ Features### 🔐 Authentication & User Management

# macOS/Linux

python3 -m venv django_env- User registration with email validation

source django_env/bin/activate

```### 🔐 Authentication & User Management- Secure login/logout functionality



**Step 3: Install Dependencies**- User registration with secure authentication- Role-based access control (Patient/Admin)

```bash

pip install -r requirements.txt- Login/logout functionality with session management- Profile management

```

- Role-based access control (Patient/Admin)- Session-based authentication

**Step 4: Setup Environment File**

Create `.env` file in project root:- Profile management and updates

```

GEMINI_API_KEY=your_api_key_here- Password hashing with PBKDF2### 🤖 AI Consultation System

DEBUG=True

SECRET_KEY=your-secret-key-here- **Voice & Text Chat Interface** - Real-time communication with AI assistant

```

### 🤖 AI Consultation System- **Google Gemini Integration** - Advanced natural language processing

**Step 5: Run Application**

```bash- **Real-time Chat Interface** - Communicate with AI assistant- **Consultation History** - Track all previous consultations

python manage.py migrate          # Create database

python manage.py createsuperuser  # Create admin account- **Google Gemini Integration** - Advanced natural language processing- **Multi-language Support** - Support for multiple languages

python manage.py runserver        # Start server

```- **Consultation History** - Track all previous interactions- **Graceful Error Handling** - Fallback responses for API failures



Open browser: **http://localhost:8000**- **Quota-Aware** - Handles API limits gracefully- **Context-Aware Responses** - Personalized medical guidance



---- **Context-Aware Responses** - Personalized medical guidance



## 🔑 Get Gemini API Key- **Error Handling** - Fallback responses for API failures### 📅 Appointment Management



1. Go to [Google AI Studio](https://aistudio.google.com/)- Book appointments with doctors

2. Click "Get API Key"

3. Create new API key### 📅 Appointment Management- Department/specialty selection (9 departments)

4. Copy and paste in `.env` file

- Book appointments with flexible scheduling- Appointment scheduling with date & time

---

- Department selection (General, Cardiology, Dermatology, etc.)- Consultation type selection (In-person/Video/Phone)

## 📖 How to Use

- Consultation type options (In-person, Video, Phone)- Emergency appointment flagging

### Register & Login

1. Go to Registration page- Emergency appointment flagging- Follow-up appointment tracking

2. Create account with email and password

3. Login with credentials- Appointment status tracking (Pending, Confirmed, Completed, Cancelled)- Appointment status management (Pending/Confirmed/Completed/Cancelled)



### Use AI Consultant- View complete appointment history- View appointment history

1. Go to "AI Consultation" page

2. Type your health question- Follow-up appointment support

3. Get instant AI response

4. View chat history### 💊 Online Pharmacy



### Book Appointment### 💊 Online Pharmacy- Browse medicine catalog

1. Click "Appointments"

2. Fill appointment form- Browse comprehensive medicine catalog- Advanced search functionality

3. Select date and time

4. Choose consultation type- Advanced search and filtering- Medicine pricing and dosage information

5. Submit

- Real-time stock availability tracking- Stock availability tracking

### Order Medicine

1. Go to "Pharmacy"- Detailed medicine information (dosage, price, description)- Shopping cart system

2. Search medicine name

3. Add to cart- Shopping cart functionality- Order management

4. Proceed to checkout

5. View order confirmation- Order management and tracking- Order confirmation and tracking



### Upload Medical Records- Order confirmation system- Multiple medicine order handling

1. Go to "Medical Reports"

2. Click "Upload Report"

3. Select file (PDF/Image)

4. Add description### 📋 Medical Records Management### 📋 Medical Records Management

5. Save

- Upload medical reports (PDF, Images)- Upload medical reports (PDF, Images)

---

- Report categorization (Lab Reports, X-rays, CT Scans, etc.)- Report categorization (Lab Reports, X-rays, CT Scans, etc.)

## 🗄️ Database Models

- Organize and retrieve medical documents- Report metadata storage

| Model | Purpose |

|-------|---------|- Download medical files- Download medical documents

| **Patient** | Store user health profile |

| **Appointment** | Manage doctor appointments |- Report metadata storage- Report organization and search

| **Medicine** | Medicine catalog |

| **Order** | Track medicine orders |

| **Prescription** | Store prescription suggestions |

| **MedicalReport** | Store uploaded documents |### 💊 Prescription Management### 💊 Prescription Management

| **ConsultationHistory** | Track AI conversations |

- AI-generated prescription suggestions- AI-generated prescription suggestions

---

- Symptom-based recommendations- Prescription history tracking

## 🌐 Main Pages

- Prescription history tracking- Download prescriptions as PDF

| Page | URL | What You Can Do |

|------|-----|-----------------|- Download prescriptions as PDF- Medicine linking to prescriptions

| Home | / | View welcome page |

| Login | /login/ | Sign in to account |- Medicine linking to prescriptions- Symptom-based recommendations

| Register | /register/ | Create new account |

| Dashboard | /dashboard/ | View health overview |

| AI Chat | /consultation/ | Chat with AI assistant |

| Appointments | /appointments/ | Book/view appointments |### 📊 Health Analytics Dashboard### 📊 Health Analytics Dashboard

| Pharmacy | /pharmacy/ | Browse & order medicines |

| Prescriptions | /prescriptions/ | View AI suggestions |- Interactive charts and graphs (Chart.js)- Patient health metrics visualization

| Medical Reports | /medical-reports/ | Upload/download reports |

| Health Analytics | /health-dashboard/ | View charts & stats |- Appointment statistics- Interactive charts and graphs (Chart.js)



---- Medical record overview- Appointment statistics



## 🎨 UI Features- Health trend analysis- Medical record tracking



- ✅ Dark professional theme- Comprehensive health journey tracking- Health trend analysis

- ✅ Cyan/Teal color scheme

- ✅ Mobile responsive design- Comprehensive overview of health journey

- ✅ Easy navigation

- ✅ Fast loading### 🎨 Modern UI/UX

- ✅ Modern buttons and cards

- Fully responsive design (Mobile, Tablet, Desktop)### 🎨 Modern UI/UX

---

- Professional dark theme with cyan/teal accents- Responsive design (Mobile, Tablet, Desktop)

## 📁 Folder Structure

- Bootstrap 5.3.0 styling- Modern blue/teal color scheme

```

AI-MediQ/- Bootstrap Icons 1.10.0- Bootstrap 5.3.0 styling

├── manage.py              # Django command

├── requirements.txt       # Dependencies- Smooth animations and transitions- Bootstrap Icons integration

├── README.md             # This file

├── .env                  # Environment variables (create yourself)- Intuitive navigation- Smooth animations and transitions

│

├── medical_voice/        # Project settings- Dark mode ready components

│   ├── settings.py

│   ├── urls.py---- Intuitive navigation

│   └── wsgi.py

│

├── healthcare/           # Main application

│   ├── models.py         # Database models## 🛠️ Tech Stack---

│   ├── views.py          # Page logic

│   ├── urls.py           # Page routes

│   └── admin.py          # Admin panel setup

│### Backend## 🛠️ Tech Stack

├── templates/            # HTML pages

│   └── healthcare/- **Framework:** Django 6.0.3

│       ├── base.html

│       ├── dashboard.html- **Database:** SQLite3 (Production-ready with PostgreSQL migration support)### Backend

│       ├── voice_consultation.html

│       ├── appointments.html- **Python Version:** 3.13+- **Framework:** Django 6.0.3

│       ├── pharmacy.html

│       ├── prescriptions.html- **ORM:** Django Object-Relational Mapping- **Database:** SQLite3 (Easily upgradeable to PostgreSQL)

│       ├── medical_reports.html

│       └── ...- **Python Version:** 3.13+

│

└── django_env/          # Virtual environment### Frontend- **ORM:** Django ORM

```

- **CSS Framework:** Bootstrap 5.3.0

---

- **JavaScript:** Vanilla JS with AJAX### Frontend

## 🔒 Security

- **Charts:** Chart.js for data visualization- **CSS Framework:** Bootstrap 5.3.0

- ✅ Secure login & registration

- ✅ Password encryption- **Icons:** Bootstrap Icons 1.10.0- **JavaScript:** Vanilla JS + AJAX

- ✅ CSRF protection

- ✅ SQL injection prevention- **Templating:** Django Template Language (DTL)- **Charts:** Chart.js for data visualization

- ✅ API key protection (in .env)

- **Icons:** Bootstrap Icons 1.10.0

---

### APIs & Services- **Templating:** Django Template Language

## 🚀 Run Application

- **AI Engine:** Google Generative AI (Gemini 2.5 Flash)

```bash

# Activate virtual environment- **Environment Management:** python-decouple### APIs & Services

# Windows: .\django_env\Scripts\activate

# macOS/Linux: source django_env/bin/activate- **Image Processing:** Pillow- **AI:** Google Generative AI (Gemini)



python manage.py runserver- **Environment Management:** python-decouple

```

### Development & Deployment- **File Handling:** Pillow

Then open: **http://localhost:8000**

- **Version Control:** Git

---

- **Package Manager:** pip### Development Tools

## 🐛 Common Problems & Solutions

- **Virtual Environment:** venv- **Version Control:** Git

| Problem | Solution |

|---------|----------|- **Web Server Ready:** WSGI/ASGI compatible- **Package Manager:** pip

| **"Module not found"** | Activate virtual environment & install requirements |

| **"API key invalid"** | Check .env file has correct key from Google AI Studio |- **Virtual Environment:** venv

| **"Port 8000 in use"** | Run `python manage.py runserver 8001` |

| **"Database error"** | Run `python manage.py migrate` |---



------



## 📚 Default Admin Account## 📁 Project Structure



```## 📁 Project Structure

Username: admin

Password: (set during createsuperuser)```

```

AI-MediQ/```

Access at: **http://localhost:8000/admin**

├── manage.py                    # Django management scriptmedical_voice/

---

├── requirements.txt             # Python dependencies├── manage.py                          # Django management script

## 🤝 Want to Contribute?

├── README.md                    # Documentation├── db.sqlite3                        # SQLite database

1. Fork the repository

2. Create feature branch: `git checkout -b feature/your-feature`├── .env.example                 # Environment template├── README.md                         # This file

3. Make changes

4. Commit: `git commit -m "Add feature"`├── .gitignore                   # Git ignore rules├── SETUP_GUIDE.md                    # Setup instructions

5. Push: `git push origin feature/your-feature`

6. Create Pull Request│├── API_KEYS_SETUP.md                 # API key configuration



---├── medical_voice/               # Main project settings├── API_KEY_FIX.md                    # API troubleshooting



## 📄 License│   ├── settings.py              # Django configuration├── requirements_django.txt           # Python dependencies



MIT License - Free to use and modify│   ├── urls.py                  # Project URL routing├── .env                              # Environment variables (not in repo)



---│   ├── asgi.py                  # ASGI configuration├── .gitignore                        # Git ignore rules



## 👤 Author│   ├── wsgi.py                  # WSGI configuration│



**Satyam Pandey**│   └── __init__.py├── medical_voice/                    # Main project settings

- GitHub: [@satyamp18](https://github.com/satyamp18)

- Repository: [AI-MediQ](https://github.com/satyamp18/AI-MediQ)││   ├── settings.py                   # Django settings



---├── healthcare/                  # Main application│   ├── urls.py                       # Project URL configuration



## 💬 Support & Issues│   ├── models.py                # 8 Database models│   ├── asgi.py                       # ASGI configuration



- 🐛 Found a bug? [Report here](https://github.com/satyamp18/AI-MediQ/issues)│   ├── views.py                 # 24+ View functions│   ├── wsgi.py                       # WSGI configuration

- 💡 Have an idea? [Suggest here](https://github.com/satyamp18/AI-MediQ/discussions)

- ⭐ Like the project? Star it on GitHub!│   ├── urls.py                  # App URL patterns│   └── __init__.py



---│   ├── admin.py                 # Django admin setup│



<div align="center">│   ├── apps.py                  # App configuration├── healthcare/                       # Main application



### Made with ❤️ for better healthcare│   ├── migrations/              # Database migrations│   ├── models.py                     # 8 Django models



**[GitHub](https://github.com/satyamp18/AI-MediQ)** | **[Report Issue](https://github.com/satyamp18/AI-MediQ/issues)** | **[Suggest Feature](https://github.com/satyamp18/AI-MediQ/discussions)**│   │   └── 0001_initial.py│   ├── views.py                      # 24+ view functions



</div>│   └── __pycache__/│   ├── urls.py                       # App URL patterns


││   ├── admin.py                      # Django admin configuration

├── templates/                   # HTML templates│   ├── apps.py

│   └── healthcare/│   ├── migrations/                   # Database migrations

│       ├── base.html            # Master template with navbar/sidebar│   │   └── 0001_initial.py

│       ├── login.html           # User login page│   └── __pycache__/

│       ├── register.html        # User registration page│

│       ├── dashboard.html       # Main patient dashboard├── templates/                        # HTML templates

│       ├── voice_consultation.html  # AI chat interface│   └── healthcare/

│       ├── appointments.html    # Appointment booking/management│       ├── base.html                 # Master template

│       ├── medical_reports.html # Medical records management│       ├── login.html                # Login page

│       ├── prescriptions.html   # Prescriptions with AI suggestions│       ├── register.html             # Registration page

│       ├── pharmacy.html        # Medicine store│       ├── dashboard.html            # Main dashboard

│       ├── order_confirmation.html  # Order success page│       ├── voice_consultation.html   # AI chat interface

│       └── health_dashboard.html    # Analytics dashboard│       ├── appointments.html         # Appointment management

││       ├── medical_reports.html      # Medical records

└── django_env/                  # Virtual environment (not in git)│       ├── prescriptions.html        # Prescriptions

    ├── Scripts/│       ├── pharmacy.html             # Medicine store

    ├── Lib/│       ├── order_confirmation.html   # Order success page

    └── pyvenv.cfg│       └── health_dashboard.html     # Analytics dashboard

```│

└── django_env/                       # Virtual environment

---    ├── Scripts/

    ├── Lib/

## 🚀 Quick Start    └── pyvenv.cfg

```

### Prerequisites

- Python 3.13 or higher---

- pip (Python package manager)

- Git## 🚀 Installation

- Google Gemini API Key

### Prerequisites

### Step 1: Clone the Repository- Python 3.13 or higher

```bash- pip (Python package manager)

git clone https://github.com/satyamp18/AI-MediQ.git- Git

cd AI-MediQ- Virtual environment support

```

### Step 1: Clone the Repository

### Step 2: Create & Activate Virtual Environment```bash

```bashgit clone https://github.com/satyamp18/AI-MediQ.git

# Windowscd AI-MediQ

python -m venv django_env```

.\django_env\Scripts\activate

### Step 2: Create Virtual Environment

# macOS/Linux```bash

python3 -m venv django_env# Windows

source django_env/bin/activatepython -m venv django_env

```.\django_env\Scripts\activate



### Step 3: Install Dependencies# macOS/Linux

```bashpython3 -m venv django_env

pip install -r requirements.txtsource django_env/bin/activate

``````



### Step 4: Create Environment Configuration### Step 3: Install Dependencies

```bash```bash

# Create .env file in project rootpip install -r requirements_django.txt

notepad .env  # Windows```

nano .env     # macOS/Linux

```### Step 4: Configure Environment Variables

```bash

Add the following to `.env`:# Create .env file in project root

```envcopy .env.example .env  # Windows

# API Configurationcp .env.example .env    # macOS/Linux

GEMINI_API_KEY=your_gemini_api_key_here```



# Django ConfigurationEdit `.env` and add your API key:

DEBUG=True```

SECRET_KEY=django-insecure-your-secret-key-hereGEMINI_API_KEY=your_api_key_here

ALLOWED_HOSTS=localhost,127.0.0.1DEBUG=True

```SECRET_KEY=your_secret_key

```

### Step 5: Apply Database Migrations

```bash### Step 5: Apply Database Migrations

python manage.py migrate```bash

```python manage.py migrate

```

### Step 6: Create Superuser (Admin Account)

```bash### Step 6: Create Superuser (Admin)

python manage.py createsuperuser```bash

# Enter username, email, and password when promptedpython manage.py createsuperuser

```# Follow prompts to create admin account

```

### Step 7: Run Development Server

```bash### Step 7: Load Sample Data (Optional)

python manage.py runserver```bash

```python manage.py loaddata sample_medicines  # If available

```

Your application will be available at: **http://localhost:8000**

### Step 8: Run Development Server

---```bash

python manage.py runserver

## ⚙️ Configuration```



### Get Your Gemini API KeyServer will start at: **http://localhost:8000**



1. Visit [Google AI Studio](https://aistudio.google.com/)---

2. Click "Get API Key" button

3. Select "Create API Key" → "Create API key in new project"## ⚙️ Configuration

4. Copy the generated API key

5. Add it to your `.env` file as `GEMINI_API_KEY`### Environment Variables

Create a `.env` file in the project root:

### Environment Variables Reference

```env

```env# API Configuration

# RequiredGEMINI_API_KEY=sk-xxxxxxxxxxxxx

GEMINI_API_KEY=sk-xxxxxxxxxxxxx

# Django Configuration

# Django (Optional but recommended)DEBUG=True

DEBUG=TrueSECRET_KEY=your-secret-key-here

SECRET_KEY=your-very-secret-key-minimum-50-charsALLOWED_HOSTS=localhost,127.0.0.1

ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database

# Database (SQLite by default)DB_NAME=db.sqlite3

DB_ENGINE=django.db.backends.sqlite3DB_ENGINE=django.db.backends.sqlite3

DB_NAME=db.sqlite3

```# Email (Optional)

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

### Important Notes```

- ⚠️ Keep `.env` file private - never commit it to git

- ⚠️ Change `SECRET_KEY` for production### Get Your Gemini API Key

- ⚠️ Set `DEBUG=False` for production1. Visit [Google AI Studio](https://aistudio.google.com/)

- ⚠️ Update `ALLOWED_HOSTS` with your domain2. Click "Get API Key"

3. Create a new API key

---4. Copy and paste into `.env` file



## 📖 Usage Guide**Detailed guide:** See [API_KEYS_SETUP.md](API_KEYS_SETUP.md)



### First Time Users---



1. **Register an Account**## 📖 Usage

   - Go to http://localhost:8000/register/

   - Fill in username, email, and password### Access the Application

   - Click "Register"

| Page | URL | Access |

2. **Login**|------|-----|--------|

   - Go to http://localhost:8000/login/| Home | http://localhost:8000 | Public |

   - Enter your credentials| Login | http://localhost:8000/login/ | Public |

   - Click "Login"| Register | http://localhost:8000/register/ | Public |

| Dashboard | http://localhost:8000/dashboard/ | Authenticated |

3. **Explore Dashboard**| AI Consultation | http://localhost:8000/voice-consultation/ | Authenticated |

   - View your health metrics| Appointments | http://localhost:8000/appointments/ | Authenticated |

   - Check recent appointments| Medical Reports | http://localhost:8000/medical-reports/ | Authenticated |

   - See medical records count| Prescriptions | http://localhost:8000/prescriptions/ | Authenticated |

| Pharmacy | http://localhost:8000/pharmacy/ | Authenticated |

### Access Different Sections| Health Analytics | http://localhost:8000/health-dashboard/ | Authenticated |

| Admin Panel | http://localhost:8000/admin/ | Admin Only |

| Feature | URL | Access Level |

|---------|-----|--------------|### Default Admin Credentials

| Home | http://localhost:8000/ | Public |```

| Login | http://localhost:8000/login/ | Public |Username: admin

| Register | http://localhost:8000/register/ | Public |Password: admin123

| Dashboard | http://localhost:8000/dashboard/ | Authenticated |```

| AI Consultation | http://localhost:8000/consultation/ | Authenticated |

| Appointments | http://localhost:8000/appointments/ | Authenticated |⚠️ **Change password immediately in production!**

| Medical Reports | http://localhost:8000/medical-reports/ | Authenticated |

| Prescriptions | http://localhost:8000/prescriptions/ | Authenticated |### Sample User Registration

| Pharmacy | http://localhost:8000/pharmacy/ | Authenticated |1. Go to http://localhost:8000/register/

| Health Analytics | http://localhost:8000/health-dashboard/ | Authenticated |2. Fill in username, email, password

| Admin Panel | http://localhost:8000/admin/ | Admin Only |3. Click "Register"

4. Login with your credentials

### Default Admin Credentials (First Time)5. Start using features!

```

Username: admin---

Password: (whatever you set during createsuperuser)

```## 🗄️ Database Schema



⚠️ **IMPORTANT:** Change the admin password immediately!### Models



---#### 1. **Patient**

```python

## 🗄️ Database Models- User (OneToOneField)

- age (IntegerField)

### Patient- gender (CharField)

- User reference (OneToOne)- phone (CharField)

- Age, gender, phone number- profile_picture (ImageField)

- Profile picture- created_at (DateTimeField)

- Creation timestamp```



### Appointment#### 2. **Appointment**

- Patient reference```python

- Department selection- patient (ForeignKey → Patient)

- Doctor name- department (CharField - 9 choices)

- Date, time, and consultation type- doctor_name (CharField)

- Symptoms description- appointment_date (DateField)

- Emergency and follow-up flags- appointment_time (TimeField)

- Status tracking- consultation_type (CharField - 3 choices)

- symptoms (TextField)

### MedicalReport- is_emergency (BooleanField)

- Patient reference- is_followup (BooleanField)

- File upload with PDF/image support- status (CharField - 4 states)

- Report type categorization- created_at, updated_at (DateTimeField)

- Report date and notes```

- Upload timestamp

#### 3. **MedicalReport**

### Prescription```python

- Patient reference- patient (ForeignKey → Patient)

- Symptoms input- name (CharField)

- AI-generated suggestion- file (FileField)

- Creation timestamp- report_type (CharField - 7 categories)

- report_date (DateField)

### ConsultationHistory- notes (TextField)

- Patient reference- uploaded_at (DateTimeField)

- Question and AI response```

- Consultation mode and language

- Timestamp#### 4. **Prescription**

```python

### Medicine- patient (ForeignKey → Patient)

- Name, dosage, price- symptoms (TextField)

- Description- suggestion (TextField - AI-generated)

- Stock availability- created_at (DateTimeField)

- Product image```



### Order#### 5. **ConsultationHistory**

- Patient reference```python

- Medicine items (ManyToMany)- patient (ForeignKey → Patient)

- Total price- question (TextField)

- Order status- ai_response (TextField)

- Timestamps- mode (CharField)

- language (CharField)

### OrderItem- created_at (DateTimeField)

- Order reference```

- Medicine reference

- Quantity and price#### 6. **Medicine**

```python

---- name (CharField)

- dosage (CharField)

## 🔌 Main API Endpoints- price (DecimalField)

- description (TextField)

### Authentication- in_stock (BooleanField)

```- image (ImageField)

POST   /register/              Create new user account```

POST   /login/                 User login

GET    /logout/                User logout#### 7. **Order**

``````python

- patient (ForeignKey → Patient)

### Dashboard- medicines (ManyToMany → Medicine through OrderItem)

```- total_price (DecimalField)

GET    /dashboard/             View main dashboard- status (CharField - 5 states)

```- created_at, updated_at (DateTimeField)

```

### AI Consultation

```#### 8. **OrderItem**

GET    /consultation/          Chat interface```python

POST   /ask-ai/                Send message to AI (JSON API)- order (ForeignKey → Order)

```- medicine (ForeignKey → Medicine)

- quantity (IntegerField)

### Appointments- price (DecimalField)

``````

GET    /appointments/          List and book appointments

POST   /appointments/          Create new appointment---

GET    /cancel-appointment/<id>/  Cancel appointment

```## 🔌 API Endpoints



### Medical Records### Authentication

```- `POST /register/` - User registration

GET    /medical-reports/       List medical reports- `POST /login/` - User login

POST   /medical-reports/       Upload new report- `GET /logout/` - User logout

GET    /download-report/<id>/  Download report file

DELETE /medical-reports/<id>/  Delete report### Dashboard

```- `GET /dashboard/` - Main dashboard with metrics



### Prescriptions### Consultations

```- `GET /voice-consultation/` - Chat interface

GET    /prescriptions/         List prescriptions- `POST /ask-ai/` - Send question to AI (JSON API)

POST   /prescriptions/         Generate AI suggestion

GET    /download-prescription/<id>/  Download prescription### Appointments

```- `GET /appointments/` - List and book appointments

- `POST /appointments/` - Create appointment

### Pharmacy- `GET /cancel-appointment/<id>/` - Cancel appointment

```

GET    /pharmacy/              Browse medicines### Medical Records

POST   /add-to-cart/           Add medicine to cart (JSON)- `GET /medical-reports/` - List reports

GET    /checkout/              Checkout page- `POST /medical-reports/` - Upload report

POST   /checkout/              Process order- `GET /download-report/<id>/` - Download report

```

### Prescriptions

### Analytics- `GET /prescriptions/` - List prescriptions

```- `GET /download-prescription/<id>/` - Download prescription

GET    /health-dashboard/      View health analytics

```### Pharmacy

- `GET /pharmacy/` - Browse medicines

### Admin- `POST /add-to-cart/` - Add to cart (JSON)

```- `GET /checkout/` - Checkout page

GET    /admin/                 Django admin panel- `POST /checkout/` - Process order

```

### Health Analytics

---- `GET /health-dashboard/` - Analytics dashboard



## 🎨 UI/UX Design---



### Color Scheme## 🎨 UI/UX Features

- **Primary Accent:** #00d4ff (Cyan Blue)

- **Secondary Accent:** #0096c7 (Teal)### Color Scheme

- **Dark Background:** #0f0f1e (Deep Dark)- **Primary:** Blue/Teal (#00b4d8 → #0096c7)

- **Card Background:** #1a1a2e (Card Dark)- **Accent:** Light Blue (#f0f9ff)

- **Text Primary:** #ffffff (White)- **Text:** Dark Gray (#212529)

- **Text Secondary:** #b0b0b0 (Gray)- **Borders:** Subtle Blue (#00b4d8)



### Design Features### Responsive Design

- ✅ Mobile-first responsive design- ✅ Mobile-first approach

- ✅ Smooth hover and transition effects- ✅ Tablet optimization

- ✅ Accessible color contrasts- ✅ Desktop experience

- ✅ Intuitive navigation- ✅ Touch-friendly buttons

- ✅ Professional dark theme- ✅ Collapsible navigation

- ✅ Consistent component styling

### Components

---- Modern card layouts with hover effects

- Animated transitions

## 🔒 Security Features- Progress indicators

- Toast notifications

- ✅ CSRF Protection on all forms- Modal dialogs

- ✅ SQL Injection Prevention (Django ORM)- Form validation

- ✅ XSS Protection (Template escaping)

- ✅ Secure Password Hashing (PBKDF2)---

- ✅ Session-based Authentication

- ✅ Environment Variable Protection## 📊 Screenshots

- ✅ API Key Encryption in .env

- ✅ Input Validation on all forms### Dashboard

- ✅ Permission-based Access ControlClean overview with appointment count, medical reports, and prescriptions metrics.



---### AI Consultation

Real-time chat interface with message history and AI responses.

## 🐛 Troubleshooting

### Appointment Booking

### Common Issues & SolutionsEasy-to-use form with department selection, date/time picker, and consultation type.



**Q: "ModuleNotFoundError: No module named 'google.generativeai'"**### Pharmacy

```bashBrowse medicines with search, pricing, and shopping cart functionality.

pip install google-generativeai

```### Health Analytics

Interactive charts showing health trends and statistics.

**Q: "Error: 400 API key not valid"**

- Verify API key in .env file---

- Check API key is active in Google AI Studio

- Ensure no extra spaces in .env## 🔒 Security Features



**Q: "Port 8000 already in use"**- ✅ CSRF Protection

```bash- ✅ SQL Injection Prevention (Django ORM)

python manage.py runserver 8001- ✅ XSS Protection

```- ✅ Secure Password Hashing (PBKDF2)

- ✅ Session-based Authentication

**Q: "Database migration errors"**- ✅ Environment Variable Protection (.env in .gitignore)

```bash- ✅ API Key Encryption

python manage.py migrate --fake-initial- ✅ Input Validation

```- ✅ Rate Limiting Ready



**Q: "Module not found after installation"**---

```bash

# Ensure virtual environment is activated## 🚀 Deployment

# Windows

.\django_env\Scripts\activate### Prepare for Production

1. Set `DEBUG=False` in settings.py

# macOS/Linux2. Update `ALLOWED_HOSTS` with your domain

source django_env/bin/activate3. Use strong `SECRET_KEY`

```4. Set up environment variables on server

5. Use PostgreSQL instead of SQLite

**Q: "Cannot connect to AI - quota exceeded"**

- Gemini 2.5 Flash has generous free tier### Deploy on Heroku

- Check your API usage in Google AI Studio```bash

- Consider upgrading billing# Install Heroku CLI

heroku login

**Q: "Changes not reflecting after editing templates"**heroku create your-app-name

- Django auto-reloads on code changesgit push heroku main

- Check server console for errorsheroku run python manage.py migrate

- Try Ctrl+C to stop and restart serverheroku run python manage.py createsuperuser

```

---

### Deploy on PythonAnywhere

## 📈 Performance Optimization1. Create account on PythonAnywhere

2. Upload code via git

### Recommendations3. Configure virtual environment

- Use PostgreSQL instead of SQLite for production4. Set up web app configuration

- Enable caching with Redis5. Configure environment variables

- Use Gunicorn/uWSGI for production server

- Implement CDN for static files---

- Add database indexes on frequently queried fields

## 🐛 Troubleshooting

### For Large Datasets

```python### Common Issues

# Use select_related for ForeignKey

appointments = Appointment.objects.select_related('patient')**Issue: "ModuleNotFoundError: No module named 'google.generativeai'"**

```bash

# Use prefetch_related for ManyToManypip install google-generativeai

orders = Order.objects.prefetch_related('medicines')```



# Use pagination for large result sets**Issue: "Error: 400 API key not valid"**

from django.core.paginator import Paginator- Check `.env` file has correct API key

```- Verify API key is active on Google AI Studio

- See [API_KEY_FIX.md](API_KEY_FIX.md) for detailed help

---

**Issue: "Port 8000 already in use"**

## 🚀 Deployment```bash

python manage.py runserver 8001

### Heroku Deployment```

```bash

# Install Heroku CLI and login**Issue: Database migration errors**

heroku login```bash

python manage.py migrate --fake-initial

# Create app```

heroku create your-mediq-app

For more help, see [API_KEY_FIX.md](API_KEY_FIX.md) and [API_KEYS_SETUP.md](API_KEYS_SETUP.md)

# Add environment variables

heroku config:set GEMINI_API_KEY=your_key_here---



# Push and migrate## 📚 Documentation

git push heroku main

heroku run python manage.py migrate- [Setup Guide](SETUP_GUIDE.md) - Detailed setup instructions

heroku run python manage.py createsuperuser- [API Keys Setup](API_KEYS_SETUP.md) - How to configure API keys

```- [API Key Troubleshooting](API_KEY_FIX.md) - Solving API issues

- [Django Documentation](https://docs.djangoproject.com/) - Official Django docs

### Production Checklist

- [ ] Set `DEBUG=False` in settings.py---

- [ ] Update `SECRET_KEY` with strong random value

- [ ] Set proper `ALLOWED_HOSTS`## 🤝 Contributing

- [ ] Use PostgreSQL instead of SQLite

- [ ] Enable HTTPS/SSLWe welcome contributions! Here's how to help:

- [ ] Set up proper error logging

- [ ] Configure static files serving### Fork & Clone

- [ ] Set up backup strategy```bash

- [ ] Monitor API usagegit clone https://github.com/yourusername/AI-MediQ.git

- [ ] Use environment variables for all secretscd AI-MediQ

git checkout -b feature/your-feature-name

---```



## 📚 Additional Resources### Make Changes

1. Create a feature branch

- [Django Documentation](https://docs.djangoproject.com/)2. Make your improvements

- [Google Generative AI Docs](https://ai.google.dev/docs)3. Test thoroughly

- [Bootstrap Documentation](https://getbootstrap.com/docs/)4. Keep commits clean and descriptive

- [Python Documentation](https://docs.python.org/3/)

### Submit Pull Request

---```bash

git add .

## 🤝 Contributinggit commit -m "Add: Description of your feature"

git push origin feature/your-feature-name

We welcome contributions! Here's how:```



### Steps to Contribute### Guidelines

1. Fork the repository- Follow PEP 8 style guide

2. Create feature branch: `git checkout -b feature/amazing-feature`- Write clear commit messages

3. Make your changes- Add docstrings to functions

4. Commit: `git commit -m 'Add amazing feature'`- Test your code

5. Push: `git push origin feature/amazing-feature`- Update documentation

6. Submit Pull Request

---

### Guidelines

- Follow PEP 8 style guide## 📋 Roadmap

- Write clear commit messages

- Add docstrings to functions### Current Version (v1.0)

- Test your changes thoroughly- ✅ AI Consultation System

- Update documentation- ✅ Appointment Management

- ✅ Pharmacy System

---- ✅ Medical Records

- ✅ Health Analytics

## 📋 Roadmap

### Upcoming Features (v2.0)

### Version 1.0 ✅ (Current)- 🔜 Video Consultation Integration

- ✅ AI Consultation System- 🔜 Prescription Auto-Fulfillment

- ✅ Appointment Management- 🔜 Insurance Integration

- ✅ Pharmacy System- 🔜 Mobile App (React Native)

- ✅ Medical Records- 🔜 Real-time Notifications

- ✅ Health Analytics- 🔜 Advanced Analytics

- ✅ Dark Mode UI- 🔜 Payment Gateway Integration

- ✅ Responsive Design- 🔜 Multi-language Support



### Version 2.0 (Planned)---

- 🔜 Video Consultation Integration

- 🔜 Payment Gateway (Razorpay/Stripe)## 📄 License

- 🔜 Insurance Integration

- 🔜 Mobile App (React Native)This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

- 🔜 Real-time Notifications

- 🔜 Prescription Auto-Fulfillment```

- 🔜 Advanced AnalyticsMIT License

- 🔜 Multi-language Support

Permission is hereby granted, free of charge, to any person obtaining a copy

---of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

## 📄 Licenseto use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

This project is licensed under the MIT License - see the LICENSE file for details.furnished to do so, subject to the following conditions:



```The above copyright notice and this permission notice shall be included in all

MIT Licensecopies or substantial portions of the Software.

```

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal---

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell## 👥 Authors

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:- **Developer:** Satyam Pandey

- **GitHub:** [@satyamp18](https://github.com/satyamp18)

The above copyright notice and this permission notice shall be included in all- **Repository:** [AI-MediQ](https://github.com/satyamp18/AI-MediQ)

copies or substantial portions of the Software.

```---



---## 📞 Support & Contact



## 👥 Author- 📧 Email: support@mediq.local

- 💬 Issues: [GitHub Issues](https://github.com/satyamp18/AI-MediQ/issues)

**Satyam Pandey**- 📝 Discussions: [GitHub Discussions](https://github.com/satyamp18/AI-MediQ/discussions)

- 📧 GitHub: [@satyamp18](https://github.com/satyamp18)

- 📦 Repository: [AI-MediQ](https://github.com/satyamp18/AI-MediQ)---



---## 🙏 Acknowledgments



## 📞 Support- **Django Team** - For the amazing web framework

- **Google AI** - For Gemini API access

- 🐛 **Report Issues:** [GitHub Issues](https://github.com/satyamp18/AI-MediQ/issues)- **Bootstrap** - For the UI framework

- 💬 **Discussions:** [GitHub Discussions](https://github.com/satyamp18/AI-MediQ/discussions)- **Chart.js** - For visualization library

- ⭐ **Star the Project:** [AI-MediQ](https://github.com/satyamp18/AI-MediQ)- **Community** - For support and feedback



------



## 🙏 Acknowledgments## 📈 Project Statistics



- **Django Team** - Amazing web framework- **Total Models:** 8

- **Google AI** - Gemini API access- **Total Views:** 24+

- **Bootstrap** - Responsive UI framework- **Total Templates:** 11

- **Chart.js** - Data visualization- **Lines of Code:** 3000+

- **Open Source Community** - Support and inspiration- **API Endpoints:** 20+

- **Test Coverage:** Growing

---

---

<div align="center">

<div align="center">

### ⭐ If you find this project helpful, please give it a star!

### ⭐ If you found this project helpful, please give it a star!

**[⭐ Star on GitHub](https://github.com/satyamp18/AI-MediQ)** | **[🐛 Report Issues](https://github.com/satyamp18/AI-MediQ/issues)** | **[💡 Suggest Features](https://github.com/satyamp18/AI-MediQ/discussions)**

[⭐ Star on GitHub](https://github.com/satyamp18/AI-MediQ) | [🐛 Report Issues](https://github.com/satyamp18/AI-MediQ/issues) | [💡 Suggest Features](https://github.com/satyamp18/AI-MediQ/discussions)

Made with ❤️ by [Satyam Pandey](https://github.com/satyamp18)

Made with ❤️ by [Satyam Pandey](https://github.com/satyamp18)

</div>

</div>
