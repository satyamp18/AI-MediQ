#!/usr/bin/env python
import os
import sys
import django

# Add the project to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_voice.settings')

# Setup Django
django.setup()

from decouple import config
import google.generativeai as genai
import warnings

# Suppress FutureWarning
warnings.filterwarnings('ignore', category=FutureWarning)

print("\n" + "="*60)
print("🔑 MediQ API Key Activation Test")
print("="*60 + "\n")

try:
    # Load API key from .env
    api_key = config('GEMINI_API_KEY')
    print(f"✅ API Key loaded from .env")
    print(f"   Key preview: {api_key[:20]}..." if api_key else "   Key: NOT FOUND")
    
    # Configure Gemini API
    genai.configure(api_key=api_key)
    print(f"\n✅ Gemini API configured successfully")
    
    # List available models to verify connection
    print(f"\n📡 Testing API connection...")
    try:
        models = genai.list_models()
        print(f"\n✅ API Connection: ACTIVE")
        print(f"\n📊 Available Models:")
        for model in models:
            if "gemini" in model.name.lower():
                print(f"   • {model.name}")
    except Exception as e:
        if "429" in str(e) or "quota" in str(e).lower():
            print(f"\n⚠️  API Quota Limit Reached (Free tier limit exceeded)")
            print(f"\n✅ API Connection: ACTIVE (but quota exhausted)")
            print(f"\n💡 Solution:")
            print(f"   1. Upgrade to a paid plan on Google Cloud Console")
            print(f"   2. Wait for the next quota reset (usually after 24 hours)")
            print(f"   3. Or switch to gemini-1.5-flash which has higher free tier limits")
        else:
            raise
    
    print("\n" + "="*60)
    print("✨ Your API Key is successfully activated and connected!")
    print("="*60 + "\n")
    
    sys.exit(0)
    
except Exception as e:
    print(f"\n❌ API Connection: FAILED")
    print(f"\n⚠️  Error Details:")
    print(f"   {str(e)}\n")
    
    print("="*60)
    print("🔧 Troubleshooting:")
    print("="*60)
    print("1. Verify API key is correct in .env file")
    print("2. Check if API key is active on Google AI Studio")
    print("3. Ensure internet connection is working")
    print("4. Try creating a new API key if the current one is expired")
    print("="*60 + "\n")
    
    sys.exit(1)
