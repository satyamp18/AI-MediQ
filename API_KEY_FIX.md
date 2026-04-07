# 🔑 API Key Fix Guide - MediQ

## Error: "API key not valid"

### **Root Cause**
The Gemini API key in your `.env` file is invalid, expired, or not properly configured.

---

## ✅ **Solution: Get a Valid API Key**

### **Step 1: Go to Google AI Studio**
```
https://aistudio.google.com/app/apikey
```

### **Step 2: Create or Copy Your API Key**

**If creating new:**
1. Click **"Create API Key"** button
2. Select your Google Cloud Project (or create new)
3. Accept the terms
4. Copy the generated key

**Your API key looks like:**
```
AIzaSyDnW2w7tX8hP9kL5mN2qR7sT3uV6wX9yZ
```

### **Step 3: Update `.env` File**

1. Open file in VS Code:
   ```
   c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice\.env
   ```

2. Find this line:
   ```env
   GEMINI_API_KEY=YOUR_VALID_API_KEY_HERE
   ```

3. Replace with your actual key:
   ```env
   GEMINI_API_KEY=AIzaSyDnW2w7tX8hP9kL5mN2qR7sT3uV6wX9yZ
   ```

4. **Save file** (Ctrl+S)

### **Step 4: Restart Django Server**

```powershell
cd "c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice"
django_env\Scripts\python manage.py runserver 8000
```

---

## 🧪 **Testing the Fix**

### **Test 1: Check Server Starts**
When you see this message, API key is being read:
```
Starting development server at http://127.0.0.1:8000/
System check identified no issues (0 silenced).
```

### **Test 2: Test AI Feature**
1. Open: `http://localhost:8000`
2. Login with: `admin` / `admin123`
3. Go to: **"Voice Consultation"**
4. Ask a health question
5. If you get a response, ✅ API key works!

### **Test 3: Check .env Content**
```powershell
cd "c:\Users\Satyam Pandey\OneDrive\Desktop\medical voice"
Get-Content .env | Select-String "GEMINI_API_KEY"
```
Should show your actual key (not `YOUR_VALID_API_KEY_HERE`)

---

## ⚠️ **Common Issues & Fixes**

| Issue | Fix |
|-------|-----|
| **Still getting 400 error** | Double-check API key is correct and copy-pasted exactly |
| **API key shows as `YOUR_VALID_API_KEY_HERE`** | You didn't replace the placeholder - edit `.env` again |
| **Changes not taking effect** | Restart Django server after saving `.env` |
| **"Module decouple not found"** | Run: `pip install python-decouple` |
| **API key expired** | Generate a new key from Google AI Studio |

---

## 🔐 **API Key Requirements**

Your Gemini API key must:
- ✅ Be generated from Google AI Studio (not Google Cloud Console)
- ✅ Have "Generative Language API" enabled
- ✅ Be in valid format (starts with `AIza`)
- ✅ Not be expired
- ✅ Have API quota remaining

---

## 📝 **File Locations**

| File | Purpose |
|------|---------|
| `.env` | API key storage |
| `healthcare/views.py` | API key usage |
| `.gitignore` | Protects `.env` from Git |

---

## 🚀 **After Fix**

Once your API key is valid:

1. ✅ AI Voice Consultation works
2. ✅ Medical questions are answered
3. ✅ Prescriptions can be generated
4. ✅ Health analytics work
5. ✅ No more 400 API errors

---

## 📞 **Still Having Issues?**

Try these steps in order:
1. Verify API key at: https://aistudio.google.com/app/apikey
2. Make sure key hasn't expired (recent keys are valid)
3. Clear any spaces or extra characters in `.env`
4. Restart terminal/server completely
5. Check Django logs for more details

---

**Last Updated**: March 26, 2026  
**Application**: MediQ
