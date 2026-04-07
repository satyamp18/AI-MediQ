from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from django.utils import timezone
from django.core.files.storage import default_storage
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)
import google.generativeai as genai
from datetime import datetime
import json
from decouple import config
import os

from .models import Patient, Appointment, MedicalReport, Prescription, ConsultationHistory, Medicine, Order, OrderItem

# Initialize Gemini API with environment variable
API_KEY = config('GEMINI_API_KEY', default='YOUR_GEMINI_API_KEY_HERE')
try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Warning: Could not configure Gemini API - {str(e)}")


# ===== AUTHENTICATION =====
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password != password_confirm:
            return render(request, 'healthcare/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'healthcare/register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Create patient profile
        Patient.objects.create(user=user)
        
        login(request, user)
        return redirect('dashboard')
    
    return render(request, 'healthcare/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'healthcare/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'healthcare/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ===== DASHBOARD =====
@login_required(login_url='login')
def dashboard(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient).count()
    reports = MedicalReport.objects.filter(patient=patient).count()
    prescriptions = Prescription.objects.filter(patient=patient).count()
    
    recent_appointments = Appointment.objects.filter(patient=patient)[:5]
    
    context = {
        'patient': patient,
        'total_appointments': appointments,
        'total_reports': reports,
        'total_prescriptions': prescriptions,
        'recent_appointments': recent_appointments,
    }
    
    return render(request, 'healthcare/dashboard.html', context)


# ===== VOICE CONSULTATION =====
@login_required(login_url='login')
def voice_consultation(request):
    patient = Patient.objects.get(user=request.user)
    consultation_history = ConsultationHistory.objects.filter(patient=patient)[:10]
    
    context = {
        'consultation_history': consultation_history,
    }
    
    return render(request, 'healthcare/voice_consultation.html', context)


@login_required(login_url='login')
@require_POST
def ask_ai(request):
    try:
        data = json.loads(request.body)
        question = data.get('question')
        mode = data.get('mode', 'General Health')
        language = data.get('language', 'en')
        
        # Call Gemini API
        try:
            model = genai.GenerativeModel("gemini-2.5-pro")
            prompt = (
                f"You are a medical information assistant (mode: {mode}).\n"
                "Provide safe, factual, and general health guidance. DO NOT diagnose or prescribe medications.\n"
                f"User question: {question}\n\nPlease respond clearly and concisely."
            )
            resp = model.generate_content(prompt)
            ai_response = resp.text if hasattr(resp, "text") else str(resp)
        except Exception as api_error:
            # Fallback response if API fails
            if "API key" in str(api_error) or "400" in str(api_error):
                ai_response = (
                    "⚠️ API Configuration Issue: The Gemini API key appears to be invalid or not configured. "
                    "Please add a valid API key to your .env file and restart the server.\n\n"
                    "For now, here's general guidance: "
                    "Always consult with a licensed healthcare professional for medical concerns. "
                    "Maintain a healthy lifestyle with regular exercise, balanced diet, and adequate sleep."
                )
            else:
                raise
        
        # Save to database
        patient = Patient.objects.get(user=request.user)
        ConsultationHistory.objects.create(
            patient=patient,
            question=question,
            ai_response=ai_response,
            mode=mode,
            language=language
        )
        
        return JsonResponse({'success': True, 'response': ai_response})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


# ===== MEDICAL REPORTS =====
@login_required(login_url='login')
def medical_reports(request):
    patient = Patient.objects.get(user=request.user)
    reports = MedicalReport.objects.filter(patient=patient)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        report_type = request.POST.get('report_type')
        report_date = request.POST.get('report_date')
        notes = request.POST.get('notes')
        file = request.FILES.get('file')
        
        if file:
            MedicalReport.objects.create(
                patient=patient,
                name=name,
                file=file,
                report_type=report_type,
                report_date=report_date,
                notes=notes
            )
            return redirect('medical_reports')
    
    context = {
        'reports': reports,
        'report_types': MedicalReport.REPORT_TYPES,
    }
    
    return render(request, 'healthcare/medical_reports.html', context)


@login_required(login_url='login')
def download_report(request, report_id):
    patient = Patient.objects.get(user=request.user)
    report = get_object_or_404(MedicalReport, id=report_id, patient=patient)
    return FileResponse(report.file.open('rb'), as_attachment=True, filename=report.file.name)


# ===== APPOINTMENTS =====
@login_required(login_url='login')
def appointments(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient)
    
    if request.method == 'POST':
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        consultation_type = request.POST.get('consultation_type')
        symptoms = request.POST.get('symptoms')
        is_emergency = request.POST.get('is_emergency') == 'on'
        is_followup = request.POST.get('is_followup') == 'on'
        
        Appointment.objects.create(
            patient=patient,
            department=department,
            doctor_name=doctor_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            consultation_type=consultation_type,
            symptoms=symptoms,
            is_emergency=is_emergency,
            is_followup=is_followup,
        )
        return redirect('appointments')
    
    context = {
        'appointments': appointments,
        'departments': Appointment.DEPARTMENT_CHOICES,
        'consultation_types': Appointment.CONSULTATION_CHOICES,
    }
    
    return render(request, 'healthcare/appointments.html', context)


@login_required(login_url='login')
def cancel_appointment(request, appointment_id):
    patient = Patient.objects.get(user=request.user)
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=patient)
    appointment.status = 'CANCELLED'
    appointment.save()
    return redirect('appointments')


# ===== PRESCRIPTIONS =====
@login_required(login_url='login')
def prescriptions(request):
    patient = Patient.objects.get(user=request.user)
    prescriptions = Prescription.objects.filter(patient=patient)
    
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        if symptoms:
            try:
                model = genai.GenerativeModel("gemini-2.5-pro")
                prompt = f"Suggest general over-the-counter medicines and home remedies for: {symptoms}. Keep it educational only, concise."
                resp = model.generate_content(prompt)
                suggestion = resp.text if hasattr(resp, "text") else str(resp)
                
                Prescription.objects.create(
                    patient=patient,
                    symptoms=symptoms,
                    suggestion=suggestion
                )
                return redirect('prescriptions')
            except Exception as e:
                return render(request, 'healthcare/prescriptions.html', {
                    'prescriptions': prescriptions,
                    'error': f'Error: {str(e)}'
                })
    
    context = {
        'prescriptions': prescriptions,
        'medicines': Medicine.objects.filter(in_stock=True)[:6],
    }
    
    return render(request, 'healthcare/prescriptions.html', context)


@login_required(login_url='login')
def delete_prescription(request, prescription_id):
    patient = Patient.objects.get(user=request.user)
    prescription = get_object_or_404(Prescription, id=prescription_id, patient=patient)
    prescription.delete()
    return redirect('prescriptions')


@login_required(login_url='login')
def download_prescription(request, prescription_id):
    patient = Patient.objects.get(user=request.user)
    prescription = get_object_or_404(Prescription, id=prescription_id, patient=patient)
    
    txt = f"""PRESCRIPTION
For: {patient.user.first_name} {patient.user.last_name}
Created: {prescription.created_at.strftime('%Y-%m-%d %H:%M')}

SYMPTOMS:
{prescription.symptoms}

SUGGESTION (Educational Only):
{prescription.suggestion}

⚠ This is educational content only. Not a medical prescription."""
    
    response = FileResponse(iter([txt.encode('utf-8')]), content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="prescription_{prescription_id}.txt"'
    return response


# ===== PHARMACY & ORDERS =====
@login_required(login_url='login')
def pharmacy(request):
    medicines = Medicine.objects.filter(in_stock=True)
    context = {
        'medicines': medicines,
    }
    return render(request, 'healthcare/pharmacy.html', context)


@login_required(login_url='login')
@require_POST
def add_to_cart(request):
    try:
        data = json.loads(request.body)
        medicine_id = data.get('medicine_id')
        quantity = int(data.get('quantity', 1))
        
        medicine = Medicine.objects.get(id=medicine_id)
        
        cart = request.session.get('cart', {})
        if str(medicine_id) in cart:
            cart[str(medicine_id)]['quantity'] += quantity
        else:
            cart[str(medicine_id)] = {
                'name': medicine.name,
                'price': str(medicine.price),
                'quantity': quantity
            }
        
        request.session['cart'] = cart
        
        return JsonResponse({'success': True, 'cart_count': sum(item['quantity'] for item in cart.values())})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


@login_required(login_url='login')
def checkout(request):
    patient = Patient.objects.get(user=request.user)
    cart = request.session.get('cart', {})
    
    if not cart:
        return redirect('pharmacy')
    
    # Create order
    total_price = 0
    order = Order.objects.create(patient=patient)
    
    for medicine_id_str, item in cart.items():
        medicine = Medicine.objects.get(id=int(medicine_id_str))
        quantity = item['quantity']
        price = float(item['price']) * quantity
        total_price += price
        
        OrderItem.objects.create(
            order=order,
            medicine=medicine,
            quantity=quantity,
            price=price
        )
    
    order.total_price = total_price
    order.save()
    
    request.session['cart'] = {}
    
    return render(request, 'healthcare/order_confirmation.html', {'order': order})


# ===== HEALTH DASHBOARD =====
@login_required(login_url='login')
def health_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    
    appointments = Appointment.objects.filter(patient=patient)
    reports = MedicalReport.objects.filter(patient=patient)
    
    # Statistics
    appointments_count = appointments.count()
    reports_count = reports.count()
    prescriptions_count = Prescription.objects.filter(patient=patient).count()
    
    # Recent activity
    recent_appointments = appointments[:5]
    
    # Monthly appointments
    monthly_data = {}
    for apt in appointments:
        month = apt.appointment_date.strftime('%Y-%m')
        monthly_data[month] = monthly_data.get(month, 0) + 1
    
    # Report types distribution
    report_types = reports.values('report_type').annotate(count=Count('report_type'))
    
    context = {
        'patient': patient,
        'appointments_count': appointments_count,
        'reports_count': reports_count,
        'prescriptions_count': prescriptions_count,
        'recent_appointments': recent_appointments,
        'monthly_data': monthly_data,
        'report_types': report_types,
    }
    
    return render(request, 'healthcare/health_dashboard.html', context)
