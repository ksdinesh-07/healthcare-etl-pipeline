import pandas as pd
import random
from datetime import datetime, timedelta
import os

print("=" * 50)
print("Healthcare Data Generation Script")
print("=" * 50)

# Create dimension tables data
patients_data = [
    {"patient_id": "P5001", "patient_name": "John Doe", "age": 65, "gender": "Male", "blood_type": "A+", "address": "123 Main St", "city": "New York", "state": "NY", "zip_code": "10001", "insurance_provider": "UnitedHealth", "phone_number": "555-0101"},
    {"patient_id": "P5002", "patient_name": "Jane Smith", "age": 34, "gender": "Female", "blood_type": "O-", "address": "456 Oak Ave", "city": "Los Angeles", "state": "CA", "zip_code": "90001", "insurance_provider": "BlueCross", "phone_number": "555-0102"},
    {"patient_id": "P5003", "patient_name": "Robert Johnson", "age": 72, "gender": "Male", "blood_type": "B+", "address": "789 Pine Rd", "city": "Chicago", "state": "IL", "zip_code": "60601", "insurance_provider": "Cigna", "phone_number": "555-0103"},
    {"patient_id": "P5004", "patient_name": "Mary Williams", "age": 28, "gender": "Female", "blood_type": "AB+", "address": "321 Elm St", "city": "Houston", "state": "TX", "zip_code": "77001", "insurance_provider": "Aetna", "phone_number": "555-0104"},
    {"patient_id": "P5005", "patient_name": "David Brown", "age": 45, "gender": "Male", "blood_type": "O+", "address": "654 Maple Dr", "city": "Phoenix", "state": "AZ", "zip_code": "85001", "insurance_provider": "Medicare", "phone_number": "555-0105"},
]

doctors_data = [
    {"doctor_id": "D201", "doctor_name": "Dr. Sarah Johnson", "specialization": "Cardiologist", "department_id": "cardiology", "years_experience": 12, "email": "sarah.johnson@hospital.com", "phone": "555-0201"},
    {"doctor_id": "D202", "doctor_name": "Dr. Michael Chen", "specialization": "ER Physician", "department_id": "emergency", "years_experience": 8, "email": "michael.chen@hospital.com", "phone": "555-0202"},
    {"doctor_id": "D203", "doctor_name": "Dr. Emily Rodriguez", "specialization": "Orthopedic Surgeon", "department_id": "orthopedics", "years_experience": 15, "email": "emily.rodriguez@hospital.com", "phone": "555-0203"},
    {"doctor_id": "D204", "doctor_name": "Dr. James Wilson", "specialization": "Neurologist", "department_id": "neurology", "years_experience": 10, "email": "james.wilson@hospital.com", "phone": "555-0204"},
]

departments_data = [
    {"department_id": "cardiology", "department_name": "Cardiology", "floor": 3, "building": "Main Building", "head_doctor_id": "D201", "capacity": 50},
    {"department_id": "emergency", "department_name": "Emergency", "floor": 1, "building": "Main Building", "head_doctor_id": "D202", "capacity": 80},
    {"department_id": "orthopedics", "department_name": "Orthopedics", "floor": 2, "building": "East Wing", "head_doctor_id": "D203", "capacity": 40},
    {"department_id": "neurology", "department_name": "Neurology", "floor": 4, "building": "Main Building", "head_doctor_id": "D204", "capacity": 35},
]

diagnoses_data = [
    {"diagnosis_code": "I10", "diagnosis_name": "Essential Hypertension", "category": "Cardiovascular", "severity": "Moderate", "average_treatment_cost": 2500, "typical_stay_days": 3},
    {"diagnosis_code": "I25", "diagnosis_name": "Chronic Ischemic Heart Disease", "category": "Cardiovascular", "severity": "High", "average_treatment_cost": 3200, "typical_stay_days": 4},
    {"diagnosis_code": "J15", "diagnosis_name": "Bacterial Pneumonia", "category": "Respiratory", "severity": "Moderate", "average_treatment_cost": 1800, "typical_stay_days": 1},
    {"diagnosis_code": "M16", "diagnosis_name": "Osteoarthritis of Hip", "category": "Musculoskeletal", "severity": "High", "average_treatment_cost": 5000, "typical_stay_days": 5},
    {"diagnosis_code": "G40", "diagnosis_name": "Epilepsy", "category": "Neurological", "severity": "Moderate", "average_treatment_cost": 2800, "typical_stay_days": 2},
    {"diagnosis_code": "E11", "diagnosis_name": "Type 2 Diabetes", "category": "Endocrine", "severity": "High", "average_treatment_cost": 3500, "typical_stay_days": 3},
]

print("\n📊 Creating dimension tables...")

# Save dimension tables
pd.DataFrame(patients_data).to_csv("data/dim/patients.csv", index=False)
pd.DataFrame(doctors_data).to_csv("data/dim/doctors.csv", index=False)
pd.DataFrame(departments_data).to_csv("data/dim/departments.csv", index=False)
pd.DataFrame(diagnoses_data).to_csv("data/dim/diagnoses.csv", index=False)

print("✅ Dimension tables created successfully!")
print(f"   - patients.csv: {len(patients_data)} records")
print(f"   - doctors.csv: {len(doctors_data)} records")
print(f"   - departments.csv: {len(departments_data)} records")
print(f"   - diagnoses.csv: {len(diagnoses_data)} records")

# Generate daily visits
print("\n📅 Generating daily visit records...")
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 30)

current_date = start_date
total_visits = 0

while current_date <= end_date:
    visits = []
    num_visits = random.randint(50, 150)
    
    for i in range(num_visits):
        patient = random.choice(patients_data)
        doctor = random.choice(doctors_data)
        diagnosis = random.choice(diagnoses_data)
        
        base_cost = diagnosis["average_treatment_cost"]
        actual_cost = base_cost + random.randint(-int(base_cost*0.2), int(base_cost*0.2))
        
        base_stay = diagnosis["typical_stay_days"]
        actual_stay = max(1, base_stay + random.randint(-1, 2))
        
        visit = {
            "visit_id": f"V{current_date.strftime('%Y%m%d')}{i:04d}",
            "patient_id": patient["patient_id"],
            "doctor_id": doctor["doctor_id"],
            "department_id": doctor["department_id"],
            "visit_date": current_date.strftime("%Y-%m-%d"),
            "diagnosis_code": diagnosis["diagnosis_code"],
            "treatment_cost": actual_cost,
            "length_of_stay_days": actual_stay,
            "readmission_flag": "True" if random.random() < 0.08 else "False",
            "discharge_status": random.choice(["Improved", "Stable", "Treated", "Referred", "Critical"]),
            "insurance_approved": "True" if random.random() < 0.95 else "False"
        }
        visits.append(visit)
    
    visits_df = pd.DataFrame(visits)
    filename = f"data/daily-visits/visits_{current_date.strftime('%Y%m%d')}.csv"
    visits_df.to_csv(filename, index=False)
    
    print(f"   ✅ visits_{current_date.strftime('%Y%m%d')}.csv: {len(visits)} records")
    total_visits += len(visits)
    
    current_date += timedelta(days=1)

print("\n" + "=" * 50)
print(f"🎉 DATA GENERATION COMPLETE!")
print("=" * 50)
print(f"📁 Dimension Tables: 4 files in data/dim/")
print(f"📁 Daily Visit Files: 30 files in data/daily-visits/")
print(f"📊 Total Visit Records: {total_visits}")
print("=" * 50)
