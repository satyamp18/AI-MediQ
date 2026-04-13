#!/usr/bin/env python
"""
Script to add sample medicines to the pharmacy
Run: python manage.py shell < add_medicines.py
"""

from healthcare.models import Medicine

# Sample medicines data
medicines_data = [
    {
        'name': 'Paracetamol 500mg',
        'dosage': '500mg Tablet',
        'price': 25.00,
        'description': 'Used for pain relief and fever reduction. Take 1-2 tablets every 4-6 hours.',
        'in_stock': True
    },
    {
        'name': 'Ibuprofen 200mg',
        'dosage': '200mg Tablet',
        'price': 35.00,
        'description': 'Anti-inflammatory medicine for pain and inflammation. Take with food.',
        'in_stock': True
    },
    {
        'name': 'Aspirin 75mg',
        'dosage': '75mg Tablet',
        'price': 15.00,
        'description': 'Blood thinner and pain reliever. Commonly used for heart health.',
        'in_stock': True
    },
    {
        'name': 'Cough Syrup',
        'dosage': '100ml Bottle',
        'price': 120.00,
        'description': 'Effective cough suppressant. Take 5ml twice daily.',
        'in_stock': True
    },
    {
        'name': 'Vitamin C 500mg',
        'dosage': '500mg Tablet',
        'price': 45.00,
        'description': 'Boosts immunity and antioxidant support. Take 1 tablet daily.',
        'in_stock': True
    },
    {
        'name': 'Vitamin D3 1000IU',
        'dosage': '1000IU Tablet',
        'price': 55.00,
        'description': 'Supports bone health and calcium absorption. Take 1 tablet daily.',
        'in_stock': True
    },
    {
        'name': 'Multivitamin',
        'dosage': 'Daily Tablet',
        'price': 150.00,
        'description': 'Complete nutritional support with essential vitamins and minerals.',
        'in_stock': True
    },
    {
        'name': 'Antacid Gel',
        'dosage': '200ml Bottle',
        'price': 85.00,
        'description': 'Relieves acidity and stomach upset. Take 2-3 spoons after meals.',
        'in_stock': True
    },
    {
        'name': 'Cough Drops',
        'dosage': 'Pack of 20',
        'price': 40.00,
        'description': 'Menthol-based throat lozenges for quick relief. Suck 1 drop every 2 hours.',
        'in_stock': True
    },
    {
        'name': 'Antibacterial Cream',
        'dosage': '30g Tube',
        'price': 65.00,
        'description': 'For minor cuts and wounds. Apply thin layer 2-3 times daily.',
        'in_stock': True
    },
    {
        'name': 'Cold & Flu Tablet',
        'dosage': 'Pack of 10',
        'price': 95.00,
        'description': 'Combination medicine for cold and flu symptoms. Take 1 tablet every 6 hours.',
        'in_stock': True
    },
    {
        'name': 'Calcium Supplement',
        'dosage': '600mg Tablet',
        'price': 130.00,
        'description': 'For strong bones and teeth. Take 1 tablet daily with food.',
        'in_stock': True
    },
    {
        'name': 'Iron Supplement',
        'dosage': '65mg Tablet',
        'price': 110.00,
        'description': 'Treats iron deficiency anemia. Take 1 tablet once daily.',
        'in_stock': True
    },
    {
        'name': 'Digestive Enzyme',
        'dosage': 'Pack of 30 Tablets',
        'price': 180.00,
        'description': 'Aids digestion and nutrient absorption. Take 1-2 tablets with meals.',
        'in_stock': True
    },
    {
        'name': 'Zinc Supplement',
        'dosage': '25mg Tablet',
        'price': 75.00,
        'description': 'Boosts immunity and wound healing. Take 1 tablet daily.',
        'in_stock': True
    },
]

# Add medicines to database
added_count = 0
for medicine_data in medicines_data:
    medicine, created = Medicine.objects.get_or_create(
        name=medicine_data['name'],
        defaults={
            'dosage': medicine_data['dosage'],
            'price': medicine_data['price'],
            'description': medicine_data['description'],
            'in_stock': medicine_data['in_stock']
        }
    )
    if created:
        added_count += 1
        print(f"✓ Added: {medicine.name}")
    else:
        print(f"→ Already exists: {medicine.name}")

print(f"\n✓ Total medicines added: {added_count}")
print(f"✓ Total medicines in pharmacy: {Medicine.objects.count()}")
