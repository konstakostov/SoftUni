day = int(input())              # Working Days

doctors = 7                     # Available Doctors
treated_patients = 0            # Treated Patients
untreated_patients = 0          # Untreated Patients

# Logic
for days_passed in range(1, day + 1):
    patients = int(input())     # Number of Patients Each Day

    if days_passed % 3 == 0:    # Determining Available Doctors
        if untreated_patients > treated_patients:
            doctors += 1
        else:
            doctors += 0

    if patients <= doctors:     # Treated Patients
        treated_patients += patients

    else:                       # Untreated Patients
        treated_patients += doctors
        untreated_patients += (patients - doctors)

# Printed Results
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
