"""
Moduł odpowiedzialny za generowanie raportów na podstawie wyników badań.
"""
from mediscan.reference_values import ADULT_REFERENCE_VALUES
from mediscan.bloodwork_calculator import categorize_bmi, calculate_anemia_severity, calculate_nlr

def generate_basic_report(bloodwork_results, patient_info):
    """
    Generuje podstawowy raport z wyników badań krwi.
    
    Args:
        bloodwork_results (dict): Słownik z wynikami badań
        patient_info (dict): Informacje o pacjencie (wiek, płeć, waga, wzrost)
        
    Returns:
        dict: Raport zawierający analizę wyników
    """
    report = {
        "patient": patient_info,
        "analysis": [],
        "summary": "",
        "recommendations": []
    }
    
    # Analiza podstawowych parametrów
    for param, value in bloodwork_results.items():
        if param in ADULT_REFERENCE_VALUES:
            ref = ADULT_REFERENCE_VALUES[param]
            
            # Dostosowanie referencji dla kobiet dla niektórych parametrów
            if patient_info["sex"] == "F" and param + "_F" in ADULT_REFERENCE_VALUES:
                ref = ADULT_REFERENCE_VALUES[param + "_F"]
            
            status = "normal"
            if value < ref["min"]:
                status = "low"
            elif value > ref["max"]:
                status = "high"
            
            report["analysis"].append({
                "parameter": param,
                "value": value,
                "unit": ref["unit"],
                "reference_min": ref["min"],
                "reference_max": ref["max"],
                "status": status
            })
    
    # Dodanie BMI jeśli dostępne dane
    if "weight" in patient_info and "height" in patient_info:
        from mediscan.bloodwork_calculator import calculate_bmi
        bmi = calculate_bmi(patient_info["weight"], patient_info["height"])
        bmi_category = categorize_bmi(bmi)
        
        report["analysis"].append({
            "parameter": "BMI",
            "value": round(bmi, 2),
            "unit": "kg/m²",
            "reference_min": 18.5,
            "reference_max": 25.0,
            "status": "normal" if 18.5 <= bmi < 25.0 else ("low" if bmi < 18.5 else "high"),
            "category": bmi_category
        })
    
    # Ocena niedokrwistości jeśli dostępny poziom hemoglobiny
    if "HGB" in bloodwork_results:
        hemoglobin = bloodwork_results["HGB"]
        anemia_severity = calculate_anemia_severity(hemoglobin, patient_info["sex"])
        
        if anemia_severity != "brak":
            report["analysis"].append({
                "parameter": "Niedokrwistość",
                "value": anemia_severity,
                "unit": "",
                "reference": "brak",
                "status": "abnormal"
            })
    
    # Obliczenie wskaźnika NLR jeśli dostępne neutrofile i limfocyty
    if "NEUT" in bloodwork_results and "LYMPH" in bloodwork_results:
        neut = bloodwork_results["NEUT"]
        lymph = bloodwork_results["LYMPH"]
        
        try:
            nlr = calculate_nlr(neut, lymph)
            status = "high" if nlr > 3.0 else "normal"
            
            report["analysis"].append({
                "parameter": "NLR",
                "value": round(nlr, 2),
                "unit": "",
                "reference_min": 1.0,
                "reference_max": 3.0,
                "status": status
            })
            
            if nlr > 3.0:
                report["recommendations"].append("Podwyższony stosunek neutrofili do limfocytów (NLR) może wskazywać na stan zapalny. Zalecana konsultacja lekarska.")
        except ZeroDivisionError:
            # Pomijamy NLR jeśli liczba limfocytów wynosi 0
            pass
    
    # Generowanie podsumowania
    abnormal_count = sum(1 for item in report["analysis"] if item["status"] != "normal")
    
    if abnormal_count == 0:
        report["summary"] = "Wszystkie parametry w normie."
    else:
        report["summary"] = f"Wykryto {abnormal_count} nieprawidłowych parametrów."
    
    return report
            
