import os
import requests

# Datos de las asignaturas
asignaturas = [
    ("APRENDIZAJE_PROFUNDO", "31080010", "Aprendizaje Profundo"),
    ("FUNDAMENTOS_PROCESAMIENTO_LINGÜISTICO", "31080027", "Fundamentos del Procesamiento Lingüístico"),
    ("MINERIA_DATOS", "31101061", "Minería de Datos"),
    ("SISTEMAS_ADAPTATIVOS_EDUCACION", "31101095", "Sistemas Adaptativos en Educación"),
    ("METODOS_SIMBOLICOS", "3110117-", "Métodos Simbólicos"),
    ("METODOS_PROBABILISTAS", "31101199", "Métodos Probabilistas"),
    ("COMPUTACION_EVOLUTIVA", "31101220", "Computación Evolutiva"),
    ("VISION_ARTIFICIAL", "31101235", "Visión Artificial"),
    ("DESCUBRIMIENTO_INFORMACION_TEXTOS", "31101254", "Descubrimiento de Información en Textos"),
    ("APLICACIONES_IA_DESARROLLO_HUMANO_SOSTENIBLE", "31101273", "Aplicaciones de la IA para el Desarrollo Humano y Sostenible"),
    ("WEB_SEMANTICA_ENLAZADO_DATOS", "31108018", "Web Semántica y Enlazado de Datos"),
    ("METODOS_APRENDIZAJE_AUTOMATICO", "31108037", "Métodos de Aprendizaje Automático"),
    ("TFM_INVESTIGACION_IA", "31108022", "Trabajo de Fin de Máster en Investigación en Inteligencia Artificial"),
    ("METODOLOGIA_INVESTIGACION_SI", "31108041", "Metodología de Investigación en Sistemas Inteligentes")
]

# Carpeta raíz
root_folder = "UNED_Master_AI_GH"
os.makedirs(root_folder, exist_ok=True)

# URL base para descargar los PDFs
base_pdf_url = "https://www.uned.es/universidad/pdf/GuiasAsignaturasMaster/PDFGuiaPublica"

# Función para crear .gitkeep
def crear_gitkeep(folder):
    gitkeep_path = os.path.join(folder, ".gitkeep")
    with open(gitkeep_path, "w") as f:
        f.write("")

# Generar estructura y recursos
for nombre_carpeta, codigo_pdf, nombre_completo in asignaturas:
    asignatura_folder = os.path.join(root_folder, nombre_carpeta)
    os.makedirs(asignatura_folder, exist_ok=True)

    # Subcarpetas estándar
    subcarpetas = ["data", "docs", "notebooks", "src"]
    for sub in subcarpetas:
        sub_folder = os.path.join(asignatura_folder, sub)
        os.makedirs(sub_folder, exist_ok=True)
        crear_gitkeep(sub_folder)  # .gitkeep para carpetas vacías

    # Descargar guía y guardarla en docs/
    pdf_url = f"{base_pdf_url}?codigoAsignatura={codigo_pdf}&curso=2025&codigoTitulacion=310801&language=es"
    pdf_path = os.path.join(asignatura_folder, "docs", f"{nombre_completo.replace(' ', '_')}.pdf")
    try:
        print(f"Descargando guía: {nombre_completo}")
        response = requests.get(pdf_url)
        response.raise_for_status()
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print(f"Guía guardada en: {pdf_path}")
    except Exception as e:
        print(f"No se pudo descargar la guía para {nombre_completo}: {e}")

    # Crear README.md personalizado
    readme_path = os.path.join(asignatura_folder, "README.md")
    readme_content = (
f"# {nombre_completo}\n\n"
"[![GitHub](https://img.shields.io/badge/GitHub-fmmarco29-blue?style=flat-square&logo=github)](https://github.com/fmmarco29/UNED_AI_lab)\n"
"[![License](https://img.shields.io/github/license/fmmarco29/UNED_AI_lab?style=flat-square)](../LICENSE)\n\n"
"## Información de la Asignatura\n\n"
f"- Nombre: {nombre_completo}\n"
"- Créditos: 6 ECTS\n"
"- Descripción: Por completar con la descripción específica de la asignatura\n\n"
"## Estructura\n\n"
"```\n"
f"{nombre_carpeta}/\n"
"├── src/           # Código fuente\n"
"├── notebooks/     # Jupyter notebooks\n"
"├── data/          # Datasets y datos\n"
"├── docs/          # Documentación\n"
"└── README.md      # Este archivo\n"
"```\n\n"
"## Contenido\n\n"
"### Notebooks\n"
"- [ ] Introducción y conceptos básicos\n"
"- [ ] Implementaciones prácticas\n"
"- [ ] Ejercicios y ejemplos\n"
"- [ ] Proyecto final\n\n"
"### Código\n"
"- [ ] Algoritmos implementados desde cero\n"
"- [ ] Utilidades y funciones auxiliares\n"
"- [ ] Scripts de entrenamiento\n"
"- [ ] Evaluación de modelos\n\n"
"### Datos\n"
"- [ ] Datasets de ejemplo\n"
"- [ ] Datos preprocesados\n"
"- [ ] Resultados experimentales\n\n"
"## Objetivos de Aprendizaje\n\n"
"- [ ] Comprender los fundamentos teóricos\n"
"- [ ] Implementar algoritmos clave\n"
"- [ ] Aplicar técnicas a problemas reales\n"
"- [ ] Evaluar y comparar resultados\n\n"
"## Recursos Adicionales\n\n"
"- Papers de referencia: En carpeta docs/\n"
"- Enlaces útiles: Ver sección de recursos\n"
"- Videos explicativos: Lista de reproducción\n\n"
"## Autor\n\n"
"Fernando Martínez Marco - [@fmmarco29](https://github.com/fmmarco29)\n\n"
"---\n\n"
"[⬅️ Volver al repositorio principal](../)\n"
)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

print("\nEstructura completa creada con README.md y guías docentes listas.")
