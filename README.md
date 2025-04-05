# MediScan

Proste narzędzie do analizy podstawowych wyników badań krwi używane w szpitalach w krajach rozwijających się.

## Opis

MediScan to biblioteka Python, która:
- Analizuje podstawowe parametry badań krwi
- Porównuje je z wartościami referencyjnymi
- Generuje prosty raport wskazujący odchylenia od normy
- Sugeruje możliwe interpretacje kliniczne

## Instalacja

```bash
pip install -r requirements.txt
```

## Przykład użycia

```python

from mediscan.report_generator import generate_basic_report

# Przykładowe wyniki badań
bloodwork_results = {
    "RBC": 5.0,
    "WBC": 7.0,
    "HGB": 15.0,
    "PLT": 250,
    "NEUT": 60.0,
    "LYMPH": 30.0
}

# Informacje o pacjencie
patient_info = {
    "id": "P12345",
    "name": "Jan Kowalski",
    "age": 35,
    "sex": "M",
    "weight": 75,
    "height": 180
}

# Generowanie raportu
report = generate_basic_report(bloodwork_results, patient_info)
print(report["summary"])

```
## Licencja
Ten projekt jest udostępniany na licencji MIT.