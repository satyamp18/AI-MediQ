from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say')
    ], blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Appointment(models.Model):
    CONSULTATION_CHOICES = [
        ('IN_PERSON', 'In-Person'),
        ('VIDEO', 'Video Call'),
        ('PHONE', 'Phone Call'),
    ]
    
    DEPARTMENT_CHOICES = [
        ('GENERAL', 'General Physician'),
        ('CARDIO', 'Cardiologist'),
        ('DERMA', 'Dermatologist'),
        ('DENTAL', 'Dentist'),
        ('PSYCH', 'Psychiatrist'),
        ('ORTHO', 'Orthopedic'),
        ('PEDIA', 'Pediatrician'),
        ('GYNECO', 'Gynecologist'),
        ('ENT', 'ENT Specialist'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    doctor_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_CHOICES)
    symptoms = models.TextField()
    is_emergency = models.BooleanField(default=False)
    is_followup = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ], default='CONFIRMED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.doctor_name} - {self.appointment_date}"

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']


class MedicalReport(models.Model):
    REPORT_TYPES = [
        ('BLOOD_TEST', 'Blood Test'),
        ('XRAY', 'X-Ray'),
        ('MRI', 'MRI'),
        ('CT_SCAN', 'CT Scan'),
        ('ULTRASOUND', 'Ultrasound'),
        ('PRESCRIPTION', 'Prescription'),
        ('OTHER', 'Other'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_reports')
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='medical_reports/')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    report_date = models.DateField()
    notes = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.name}"

    class Meta:
        ordering = ['-uploaded_at']


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    symptoms = models.TextField()
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.user.username}"

    class Meta:
        ordering = ['-created_at']


class ConsultationHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultation_history')
    question = models.TextField()
    ai_response = models.TextField()
    mode = models.CharField(max_length=50, default='General Health')
    language = models.CharField(max_length=10, default='en')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation - {self.patient.user.username}"

    class Meta:
        ordering = ['-created_at']


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='medicines/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Order(models.Model):
    ORDER_STATUS = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='orders')
    medicines = models.ManyToManyField(Medicine, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.patient.user.username}"

    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"
