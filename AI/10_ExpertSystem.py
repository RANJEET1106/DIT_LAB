# Dictionary mapping symptoms to diseases
symptom_to_disease = {
    "fever": "flu",
    "cough": "flu",
    "headache": "migraine",
    "nausea": "migraine",
    "chest pain": "heart attack",
    "shortness of breath": "heart attack",
    "rash": "allergy",
    "sneezing": "allergy"
}

print("Welcome to the Medical Expert System!")
print("Please answer the following questions with 'yes' or 'no'.")

patient_symptoms = []

# Ask user for symptoms
for symptom in symptom_to_disease:
    answer = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
    if answer == "yes":
        patient_symptoms.append(symptom)

# Analyze symptoms and diagnose
if not patient_symptoms:
    print("No symptoms detected. Please consult a healthcare professional.")
else:
    possible_diseases = set()
    for symptom in patient_symptoms:
        disease = symptom_to_disease[symptom]
        if disease:
            possible_diseases.add(disease)

    if not possible_diseases:
        print("No known conditions match the symptoms.")
    else:
        print("Based on the symptoms you provided, possible conditions are:")
        for disease in possible_diseases:
            print(f"- {disease}")
        print("Please consult a doctor for a proper diagnosis.")
