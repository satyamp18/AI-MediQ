from django.contrib import admin
from .models import Patient, Appointment, MedicalReport, Prescription, ConsultationHistory, Medicine, Order, OrderItem

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'age', 'gender', 'phone', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'phone')
    
    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Patient Name'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor_name', 'appointment_date', 'status', 'is_emergency')
    list_filter = ('status', 'department', 'appointment_date')
    search_fields = ('patient__user__username', 'doctor_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient',)
        }),
        ('Appointment Details', {
            'fields': ('department', 'doctor_name', 'appointment_date', 'appointment_time', 'consultation_type')
        }),
        ('Medical Information', {
            'fields': ('symptoms', 'is_emergency', 'is_followup')
        }),
        ('Status & Timestamps', {
            'fields': ('status', 'created_at', 'updated_at')
        }),
    )


@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'patient', 'report_type', 'report_date', 'uploaded_at')
    list_filter = ('report_type', 'report_date', 'uploaded_at')
    search_fields = ('patient__user__username', 'name')
    readonly_fields = ('uploaded_at',)


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'symptoms_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('patient__user__username', 'symptoms')
    readonly_fields = ('created_at',)
    
    def symptoms_preview(self, obj):
        return obj.symptoms[:50] + '...' if len(obj.symptoms) > 50 else obj.symptoms
    symptoms_preview.short_description = 'Symptoms'


@admin.register(ConsultationHistory)
class ConsultationHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'mode', 'language', 'created_at')
    list_filter = ('mode', 'language', 'created_at')
    search_fields = ('patient__user__username', 'question')
    readonly_fields = ('created_at',)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'price', 'in_stock')
    list_filter = ('in_stock', 'price')
    search_fields = ('name', 'dosage')
    
    fieldsets = (
        ('Medicine Information', {
            'fields': ('name', 'dosage', 'description')
        }),
        ('Pricing & Availability', {
            'fields': ('price', 'in_stock')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('patient__user__username',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('patient',)
        }),
        ('Order Status', {
            'fields': ('status', 'total_price')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'order', 'quantity', 'price')
    list_filter = ('order__status',)
    search_fields = ('medicine__name', 'order__id')
