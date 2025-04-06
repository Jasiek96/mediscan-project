def calculate_bmi(weight_kg, height_cm):
    """
    Oblicza BMI (Body Mass Index) na podstawie wagi i wzrostu.
    Args:
    weight_kg (float): Waga w kilogramach
    height_cm (float): Wzrost w centymetrach
    Returns:
    float: Wartość BMI
    Raises:
    ValueError: Jeśli waga lub wzrost są niedodatnie    
    """
    # Sprawdzenie, czy wartości są dodatnie
    if weight_kg <= 0:
        raise ValueError("Waga musi być dodatnia")
    if height_cm <= 0:
        raise ValueError("Wzrost musi być dodatni")

    height_m = height_cm / 100 # konwersja cm na m
    return weight_kg / (height_m * height_m)

def calculate_nlr(neutrophils, lymphocytes):
    """
    Oblicza stosunek neutrofili do limfocytów (NLR).
    Podwyższony NLR może wskazywać na stan zapalny.
    
    Args:
        neutrophils (float): Liczba neutrofili (10^9/L)
        lymphocytes (float): Liczba limfocytów (10^9/L)
        
    Raises:
        ValueError: Jeśli wartości są ujemne
        ZeroDivisionError: Jeśli lymphocytes wynosi 0
    Returns:
        float: Wartość NLR
    """
    # Sprawdzenie, czy wartości są dodatnie
    if neutrophils < 0:
        raise ValueError("Liczba neutrofili nie może być ujemna")
    if lymphocytes < 0:
        raise ValueError("Liczba limfocytów nie może być ujemna")
    return neutrophils / lymphocytes

def categorize_bmi(bmi):
    """
    Kategoryzuje BMI zgodnie ze standardami WHO.
    
    Args:
        bmi (float): Wartość BMI
        
    Returns:
        str: Kategoria BMI
    """
    if bmi < 16.0:
        return "wygłodzenie"
    elif bmi < 17.0:
        return "wychudzenie"
    elif bmi < 18.5:
        return "niedowaga"
    elif bmi < 25.0:
        return "waga prawidłowa"
    elif bmi < 30.0:
        return "nadwaga"
    elif bmi < 35.0:
        return "otyłość I stopnia"
    elif bmi < 40.0:
        return "otyłość II stopnia"
    else:
        return "otyłość III stopnia"

def calculate_anemia_severity(hemoglobin, sex):
    """
    Określa stopień niedokrwistości na podstawie poziomu hemoglobiny.
    
    Args:
        hemoglobin (float): Poziom hemoglobiny (g/dL)
        sex (str): Płeć pacjenta ('M' lub 'F')
        
    Returns:
        str: Stopień niedokrwistości lub 'brak'
    """
    if sex == 'M':
        if hemoglobin >= 13.5:
            return "brak"
        elif hemoglobin >= 11.0:
            return "łagodna"
        elif hemoglobin >= 8.0:
            return "umiarkowana"
        else:
            return "ciężka"
    elif sex == 'F':
        if hemoglobin >= 11.0:  # BŁĄD: powinno być 12.0   hemoglobin >= 10.0:
            return "brak"
        elif hemoglobin >= 8.0:
            return "łagodna"
        elif hemoglobin >= 6.1:
            return "umiarkowana"
        else:
            return "ciężka"
    else:
        # POPRAWIONE: Dodano rzucanie wyjątku dla nieprawidłowej płci
        raise ValueError(f"Nieprawidłowa płeć: {sex}. Dozwolone wartości to 'M' lub 'F'.")