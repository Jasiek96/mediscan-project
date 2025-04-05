import pytest
from mediscan.report_generator import generate_basic_report

def test_generate_basic_report_normal():
    """Test generowania raportu dla normalnych wartości."""
    bloodwork_results = {
        "RBC": 5.0,
        "WBC": 7.0,
        "HGB": 15.0,
        "PLT": 250
    }
    
    patient_info = {
        "id": "P12345",
        "name": "Jan Kowalski",
        "age": 35,
        "sex": "M",
        "weight": 75,
        "height": 180
    }
    
    report = generate_basic_report(bloodwork_results, patient_info)
    
    assert report["patient"] == patient_info
    assert len(report["analysis"]) == 5  # 4 parametry krwi + BMI
    assert report["summary"] == "Wszystkie parametry w normie."
    assert len(report["recommendations"]) == 0

def test_generate_basic_report_abnormal():
    """Test generowania raportu dla nieprawidłowych wartości."""
    bloodwork_results = {
        "RBC": 3.0,  # Poniżej normy
        "WBC": 12.0,  # Powyżej normy
        "HGB": 15.0,  # W normie
        "PLT": 250  # W normie
    }
    
    patient_info = {
        "id": "P12345",
        "name": "Jan Kowalski",
        "age": 35,
        "sex": "M",
        "weight": 75,
        "height": 180
    }
    
    report = generate_basic_report(bloodwork_results, patient_info)
    
    assert report["patient"] == patient_info
    assert len(report["analysis"]) == 5  # 4 parametry krwi + BMI
    assert "Wykryto 2 nieprawidłowych parametrów" in report["summary"]

    # Sprawdzenie statusów
    statuses = {item["parameter"]: item["status"] for item in report["analysis"]}
    assert statuses["RBC"] == "low"
    assert statuses["WBC"] == "high"
    assert statuses["HGB"] == "normal"
    assert statuses["PLT"] == "normal"
    assert statuses["BMI"] == "normal"