import pandas as pd
import random

# Predefined Names
names = ["John Doe", "Alice Brown", "Robert Smith", "Emma Johnson", "Michael Lee", 
         "Sophia Davis", "Daniel White", "Olivia Martin", "James Taylor", "Isabella Wilson"]

# Blood Types, Tissue Types, and Organs
blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
tissue_types = ["HLA-A1", "HLA-B7", "HLA-Cw4", "HLA-A2", "HLA-B8", "HLA-Cw6"]
organ_types = ["Kidney", "Liver", "Heart", "Lung", "Pancreas"]

# Generate Data for 500 Patients
data = []
for i in range(500):
    name = random.choice(names) + f" {i+1}"  # Avoid duplicate names
    role = random.choice(["Donor", "Recipient"])
    blood_type = random.choice(blood_types)
    tissue_type = random.choice(tissue_types)
    organ_type = random.choice(organ_types)
    
    # Random Latitude & Longitude
    latitude = round(random.uniform(-90, 90), 4)
    longitude = round(random.uniform(-180, 180), 4)

    data.append([name, role, blood_type, tissue_type, organ_type, latitude, longitude])

# Create DataFrame
df = pd.DataFrame(data, columns=["Name", "Role", "Blood Type", "Tissue Type", "Organ Type", "Latitude", "Longitude"])

# Save to Excel
excel_file = "simple_organ_donation_data.xlsx"
df.to_excel(excel_file, index=False)

print(f"✅ Excel file '{excel_file}' created successfully!")
