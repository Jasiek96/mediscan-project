"""
Moduł zawierający referencyjne wartości dla parametrów krwi.
"""

# Referencyjne wartości dla dorosłych
ADULT_REFERENCE_VALUES = {
    # Morfologia
    "RBC": {"min": 4.5, "max": 5.5, "unit": "x10^12/L"},  # Erytrocyty
    "WBC": {"min": 4.0, "max": 10.0, "unit": "x10^9/L"},  # Leukocyty
    "HGB": {"min": 13.5, "max": 17.5, "unit": "g/dL"},    # Hemoglobina (mężczyźni)
    "HGB_F": {"min": 12.0, "max": 16.0, "unit": "g/dL"},  # Hemoglobina (kobiety)
    "HCT": {"min": 40.0, "max": 50.0, "unit": "%"},       # Hematokryt (mężczyźni)
    "HCT_F": {"min": 36.0, "max": 46.0, "unit": "%"},     # Hematokryt (kobiety)
    "PLT": {"min": 150, "max": 400, "unit": "x10^9/L"},   # Płytki krwi
    
    # Wzór odsetkowy leukocytów
    "NEUT": {"min": 40.0, "max": 80.0, "unit": "%"},      # Neutrofile
    "LYMPH": {"min": 20.0, "max": 40.0, "unit": "%"},     # Limfocyty
    "MONO": {"min": 2.0, "max": 10.0, "unit": "%"},       # Monocyty
    "EOS": {"min": 1.0, "max": 6.0, "unit": "%"},         # Eozynofile
    "BASO": {"min": 0.0, "max": 2.0, "unit": "%"},        # Bazofile
    
    # Parametry biochemiczne
    "GLUC": {"min": 70, "max": 99, "unit": "mg/dL"},      # Glukoza (na czczo)
    "UREA": {"min": 7.0, "max": 20.0, "unit": "mg/dL"},   # Mocznik
    "CREAT": {"min": 0.6, "max": 1.2, "unit": "mg/dL"},   # Kreatynina
    "T_PROT": {"min": 6.0, "max": 8.0, "unit": "g/dL"},   # Białko całkowite
    "ALB": {"min": 3.5, "max": 5.0, "unit": "g/dL"},      # Albumina
    "T_BIL": {"min": 0.3, "max": 1.2, "unit": "mg/dL"},   # Bilirubina całkowita
    "AST": {"min": 10, "max": 40, "unit": "U/L"},         # Aminotransferaza asparaginianowa
    "ALT": {"min": 7, "max": 56, "unit": "U/L"},          # Aminotransferaza alaninowa
}

# Referencyjne wartości BMI według WHO
BMI_CATEGORIES = {
    "wygłodzenie": {"min": 0, "max": 16.0},
    "wychudzenie": {"min": 16.0, "max": 17.0},
    "niedowaga": {"min": 17.0, "max": 18.5},
    "waga prawidłowa": {"min": 18.5, "max": 25.0},
    "nadwaga": {"min": 25.0, "max": 30.0},
    "otyłość I stopnia": {"min": 30.0, "max": 35.0},
    "otyłość II stopnia": {"min": 35.0, "max": 40.0},
    "otyłość III stopnia": {"min": 40.0, "max": float('inf')},
}

# Wartości referencyjne dla dzieci są inne i zależą od wieku