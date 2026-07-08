from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Voice Consultation
    path('consultation/', views.voice_consultation, name='voice_consultation'),
    path('api/ask-ai/', views.ask_ai, name='ask_ai'),
    
    # Medical Reports
    path('reports/', views.medical_reports, name='medical_reports'),
    path('reports/download/<int:report_id>/', views.download_report, name='download_report'),
    
    # Appointments
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    
    # Prescriptions
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('prescriptions/delete/<int:prescription_id>/', views.delete_prescription, name='delete_prescription'),
    path('prescriptions/download/<int:prescription_id>/', views.download_prescription, name='download_prescription'),
    
    # Pharmacy & Orders
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('api/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
    # Health Dashboard
    path('health-dashboard/', views.health_dashboard, name='health_dashboard'),
]
