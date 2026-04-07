# 🏥 AI Medical Voice Agent - Complete Setup & User Guide

## ✨ What's New (Django Conversion)

Your Streamlit application has been **completely converted to Django** with:
- ✅ Professional Bootstrap 5 UI with responsive design
- ✅ All original features preserved and enhanced
- ✅ Database-backed storage (instead of file-based)
- ✅ User authentication system
- ✅ Advanced analytics dashboard
- ✅ Production-ready architecture

---

## 🚀 Quick Start Guide

### Step 1: Access the Application
The Django server is now running on `http://localhost:8000`

### Step 2: Login
Use the default credentials:
- **Username:** admin
- **Password:** admin123

**Or create a new account:**
- Click "Register" on the login page
- Fill in your details
- Create your patient profile

### Step 3: Explore Features

#### 📊 Dashboard
- Overview of your appointments, reports, and prescriptions
- Quick action buttons
- Recent appointments list
- Health tips

#### 🎙️ Voice Consultation
- Ask medical questions to the AI
- Choose consultation mode (General Health, Medicine Info, etc.)
- Select response language
- View chat history
- All conversations are saved

#### 📅 Appointments
- Book appointments with doctors
- Select department and specialization
- Choose consultation type (In-person, Video, Phone)
- Describe symptoms
- Mark as emergency or follow-up
- Cancel appointments
- View upcoming appointments

#### 📄 Medical Reports
- Upload medical documents (PDF, JPG, PNG)
- Categorize by type (Blood Test, X-Ray, MRI, etc.)
- Add notes and dates
- Download reports anytime
- Secure storage

#### 💊 Prescriptions
- Get AI-generated suggestions
- Based on your symptoms
- Educational content with disclaimers
- Download as text file
- Delete old prescriptions
- Featured medicines list

#### 🛒 Pharmacy
- Browse available medicines
- Search and filter
- Add to cart
- Checkout and order
- Track order status

#### 📈 Health Analytics
- View statistics:
  - Total appointments
  - Medical reports count
  - Prescriptions count
- Monthly appointment trends (chart)
- Report type distribution (pie chart)
- Recent activity timeline

---

## 🔐 Account Management

### Changing Password
Currently, use Django admin panel:
1. Go to `http://localhost:8000/admin/`
2. Login with admin credentials
3. Navigate to Users
4. Select your account
5. Change password

### Profile Updates
Coming soon feature - currently edit via admin panel

### Account Deletion
Contact administrator via admin panel

---

## 📋 Feature Details

### Voice Consultation Modes

| Mode | Purpose |
|------|---------|
| General Health | General wellness questions |
| Medicine Info | Information about medications |
| Nutrition & Diet | Dietary advice and nutrition |
| Mental Health Support | Mental wellness guidance |

### Supported Languages
- English 🇬🇧
- हिंदी (Hindi) 🇮🇳
- Español (Spanish) 🇪🇸
- Français (French) 🇫🇷

### Department Specializations
- General Physician
- Cardiologist
- Dermatologist
- Dentist
- Psychiatrist
- Orthopedic
- Pediatrician
- Gynecologist
- ENT Specialist

### Report Types
- Blood Test
- X-Ray
- MRI
- CT Scan
- Ultrasound
- Prescription
- Other

---

## 🔧 Technical Information

### Technology Stack
- **Backend:** Django 6.0.3
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (easily upgradeable to PostgreSQL)
- **JavaScript:** Vanilla JS for interactivity
- **Charts:** Chart.js for data visualization
- **API:** Google Gemini for AI features

### File Locations
- **Database:** `db.sqlite3`
- **Uploaded Files:** `media/` directory
- **Templates:** `templates/healthcare/`
- **Static Files:** `static/` directory
- **Settings:** `medical_voice/settings.py`

### Port Configuration
- **Development Server:** Port 8000
- To change: `python manage.py runserver 8080`

---

## ⚠️ Important Disclaimers

### Medical Information Disclaimer
This application provides **EDUCATIONAL INFORMATION ONLY**:

❌ **NOT a substitute for:**
- Professional medical diagnosis
- Licensed healthcare provider consultation
- Emergency medical services
- Prescription medication guidelines

✅ **Always:**
- Consult a licensed doctor for medical concerns
- Contact emergency services for emergencies
- Verify medical information with professionals
- Never self-diagnose or self-treat serious conditions

### Data Privacy
- All data is stored locally in `db.sqlite3`
- No data is sent to external servers except:
  - Google Gemini API for AI features (with your API key)
  - Cloud services if you deploy to cloud

### File Upload Security
- Only upload files you trust
- Maximum file size recommendations: 10MB
- Supported formats: PDF, JPG, PNG, JPEG

---

## 🛠️ Troubleshooting

### Server Won't Start
**Problem:** Port 8000 already in use
```bash
# Use different port:
python manage.py runserver 8080
```

### Database Issues
**Problem:** Database locked or corrupted
```bash
# Reset database (WARNING: loses all data):
rm db.sqlite3
python manage.py migrate
python setup_db.py
```

### Static Files Missing
**Problem:** CSS/JS not loading
```bash
python manage.py collectstatic --noinput
```

### API Key Error
**Problem:** "Gemini API configuration failed"
1. Get key from: https://makersuite.google.com/app/apikey
2. Update in `healthcare/views.py` line 17:
```python
API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
```

### Login Issues
**Problem:** Can't login with admin credentials
```bash
# Reset password:
python manage.py changepassword admin
```

### Page Not Loading
**Problem:** 404 errors or blank pages
1. Clear browser cache (Ctrl+Shift+Delete)
2. Try incognito/private window
3. Restart Django server

---

## 📊 Database Management

### Access Admin Panel
- URL: `http://localhost:8000/admin/`
- Username: admin
- Password: admin123

### Via Django Shell
```bash
python manage.py shell
```

### View Database Contents
```python
from healthcare.models import *

# View all patients
list(Patient.objects.all())

# View all appointments
list(Appointment.objects.all())

# View medicines
list(Medicine.objects.all())
```

---

## 💾 Backup & Restore

### Backup Database
```bash
# Copy database file
copy db.sqlite3 db.sqlite3.backup
```

### Backup Media Files
```bash
# Copy uploaded files
xcopy media media_backup /E /I
```

### Export Data
```bash
# Create JSON dump
python manage.py dumpdata > backup.json
```

### Restore Data
```bash
# Load from JSON
python manage.py loaddata backup.json
```

---

## 🚀 Deployment Guide

### For Small Scale (Personal/Local)
Current setup is fine for:
- Personal use
- Small clinic
- Testing
- Development

### For Production Deployment

#### 1. Configure Settings
Edit `medical_voice/settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'generate-new-secure-key'
```

#### 2. Use Production Server
Instead of `runserver`, use:
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn medical_voice.wsgi:application --bind 0.0.0.0:8000
```

#### 3. Upgrade Database
```bash
pip install psycopg2-binary
# Update settings.py to use PostgreSQL
```

#### 4. Setup HTTPS
- Use Let's Encrypt (free SSL)
- Configure nginx or Apache as reverse proxy
- Enable HTTPS redirect

#### 5. Environment Variables
Create `.env` file:
```
SECRET_KEY=your-secret-key
DEBUG=False
API_KEY=your-gemini-api-key
DATABASE_URL=postgresql://user:password@localhost/dbname
```

---

## 📞 Support & Tips

### Browser Compatibility
- ✅ Chrome/Chromium (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

### Performance Tips
1. Use Chrome DevTools for debugging
2. Clear cache if issues occur
3. Use incognito for testing
4. Close unused browser tabs

### Development Tips
1. Keep server running in background
2. Check Django console for errors
3. Use browser developer tools (F12)
4. Test in different browsers

### Data Entry Tips
1. Use realistic dates
2. Describe symptoms clearly
3. Upload clear document scans
4. Add notes for better context
5. Keep phone/email updated

---

## 🎓 Learning Resources

### For Users
- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Guide: https://getbootstrap.com/docs/
- Chart.js: https://www.chartjs.org/

### For Developers
- Django Models: https://docs.djangoproject.com/en/6.0/topics/db/models/
- Class-Based Views: https://docs.djangoproject.com/en/6.0/topics/class-based-views/
- Django Admin: https://docs.djangoproject.com/en/6.0/ref/contrib/admin/

---

## ✅ Verification Checklist

After starting the server, verify:
- [ ] Server running without errors (http://localhost:8000)
- [ ] Login page loads (can register or login)
- [ ] Dashboard accessible after login
- [ ] All sidebar links work
- [ ] Can upload files
- [ ] Can create appointments
- [ ] Can ask AI questions
- [ ] Charts load on analytics page
- [ ] Admin panel accessible (/admin/)

---

## 🔄 Restart Instructions

### Stop Server
Press `Ctrl+C` in the terminal where Django is running

### Restart Server
```bash
cd "c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice"
django_env\Scripts\activate
python manage.py runserver
```

---

## 📞 Contact & Support

For issues or questions:
1. Check this guide first
2. Review Django documentation
3. Check terminal for error messages
4. Review browser console (F12)

---

**Last Updated:** March 23, 2026
**Status:** ✅ Active & Running
**Version:** 2.0 (Django Edition)

Enjoy your AI Medical Voice Agent! 🏥✨
