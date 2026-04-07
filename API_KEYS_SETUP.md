# 🔐 API Keys Setup Guide - MediQ

## How to Setup Your API Keys

### **Step 1: Get Your Gemini API Key**

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click on **"Create API Key"** button
3. Select your project or create a new one
4. Copy the generated API key

### **Step 2: Configure Environment Variables**

The project uses a `.env` file for secure API key management.

#### **Option A: Quick Setup (Development)**

1. Open the `.env` file in your project root:
   ```
   c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice\.env
   ```

2. Replace `YOUR_GEMINI_API_KEY_HERE` with your actual API key:
   ```env
   GEMINI_API_KEY=AIzaSyDCItj-ivH_jq4jW46uZjpbJ9wcaS37Mcs
   ```

3. Save the file (Ctrl+S)

4. Restart the Django server:
   ```powershell
   cd "c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice"
   django_env\Scripts\python manage.py runserver 8000
   ```

#### **Option B: Using System Environment Variables (Production)**

**On Windows PowerShell:**
```powershell
[System.Environment]::SetEnvironmentVariable("GEMINI_API_KEY","YOUR_API_KEY_HERE",[System.EnvironmentVariableTarget]::User)
```

**Then restart your terminal and Django server.**

---

### **Step 3: Verify Configuration**

1. Start your Django server:
   ```powershell
   cd "c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice"
   django_env\Scripts\python manage.py runserver 8000
   ```

2. Open browser and navigate to: `http://localhost:8000`

3. Go to **"Voice Consultation"** and test the AI feature

4. If AI responses appear, your API key is working! ✅

---

## 🔑 API Key Locations

| Configuration | File | Type |
|---|---|---|
| **Development** | `.env` | Environment File |
| **Production** | System Variables | OS Environment |
| **Code** | `healthcare/views.py` | Line 22-26 |

---

## ⚠️ Security Best Practices

### **DO:**
✅ Keep API keys in `.env` file  
✅ Add `.env` to `.gitignore`  
✅ Use different keys for different environments  
✅ Rotate keys periodically  
✅ Use environment variables in production  

### **DON'T:**
❌ Hardcode API keys in Python files  
❌ Commit `.env` file to Git  
❌ Share API keys in emails or chat  
❌ Use the same key for dev and production  
❌ Log API keys in error messages  

---

## 📋 Configuration Files

### **.env File** (Development)
```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
DB_NAME=db.sqlite3
DEBUG=True
SECRET_KEY=your-secret-key
```

### **.gitignore** (Protection)
Ensures `.env` is never committed to Git:
```
.env
.env.local
*.log
__pycache__/
```

---

## 🧪 Testing Your API Key

### **Test 1: Direct Python Test**
```powershell
cd "c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice"
django_env\Scripts\python manage.py shell
```

Then in Python shell:
```python
from decouple import config
api_key = config('GEMINI_API_KEY')
print(api_key)  # Should show your API key
```

### **Test 2: Web Interface Test**
1. Login to your MediQ app
2. Go to "Voice Consultation"
3. Ask a health question
4. If you get an AI response, API is working ✅

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| **"API Key not found"** | Check `.env` file exists in project root |
| **"Invalid API Key"** | Verify key is correct and not expired |
| **"Module decouple not found"** | Run `pip install python-decouple` |
| **AI not responding** | Check API quota on Google AI Studio |
| **GEMINI_API_KEY not reading** | Restart terminal/Django server |

---

## 📚 Related Files

- **Main Configuration**: `healthcare/views.py` (Lines 22-26)
- **Environment Template**: `.env`
- **Git Protection**: `.gitignore`
- **Django Settings**: `medical_voice/settings.py`

---

## 🚀 Next Steps

1. ✅ Get your API key from Google AI Studio
2. ✅ Add it to `.env` file
3. ✅ Restart Django server
4. ✅ Test Voice Consultation feature
5. ✅ Deploy to production with system environment variables

---

**Last Updated**: March 26, 2026  
**Application**: MediQ
