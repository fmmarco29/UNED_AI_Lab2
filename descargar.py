import os
import requests

# Diccionario con los nombres de las carpetas y los códigos de asignatura
asignaturas = {
    "01_Fundamentos_IA": "31101199",
    "02_Metodos_Aprendizaje_Automatico": "31101220",
    "03_Metodos_Probabilistas_IA": "31101235",
    "04_Metodos_Simbolicos_IA": "31101248",
    "05_Metodos_Bioinspirados_IA": "31101251",
    "06_Metodos_Hibridos_IA": "31101264",
    "07_Aprendizaje_Profundo": "31101061",
    "08_Procesamiento_Lenguaje_Natural": "31101170",
    "09_Vision_Artificial": "31101277",
    "10_Mineria_Datos": "31101280",
    "11_Descubrimiento_Informacion_Textos": "31101293",
    "12_Aplicaciones_IA_Desarrollo_Humano": "31108041",
    "13_IA_Ingenieria": "31108022",
    "14_Tecnicas_IA_Ingenieria": "31108038",
    "15_Complementos_Formacion_IA": "31101207",
    "16_Metodologia_Investigacion": "31101185",
    "17_TFM": "31108045"
}

# URL base para descargar los PDFs
base_pdf_url = "https://www.uned.es/universidad/pdf/GuiasAsignaturasMaster/PDFGuiaPublica"

# Carpeta raíz del proyecto (ajústalo si quieres)
root_folder = "UNED_Master_AI_Complete"

# Descargar cada guía y colocarla en la carpeta docs correspondiente
for asignatura, codigo in asignaturas.items():
    docs_path = os.path.join(root_folder, asignatura, "docs")
    pdf_name = f"{asignatura}.pdf"
    pdf_path = os.path.join(docs_path, pdf_name)

    pdf_url = f"{base_pdf_url}?codigoAsignatura={codigo}&curso=2025&codigoTitulacion=310801&language=es"
    print(f"Descargando guía para {asignatura} desde {pdf_url}")

    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print(f"Guía guardada en: {pdf_path}")
    except Exception as e:
        print(f"No se pudo descargar la guía para {asignatura}. Error: {e}")

print("\nDescarga de todas las guías completada.")
