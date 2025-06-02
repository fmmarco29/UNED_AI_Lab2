import requests
from bs4 import BeautifulSoup

# Lista de asignaturas con su código y nombre
asignaturas = [
    ('31080010', 'APRENDIZAJE PROFUNDO'),
    ('31080027', 'FUNDAMENTOS DEL PROCESAMIENTO LINGÜÍSTICO'),
    ('31101061', 'MINERÍA DE DATOS'),
    ('31101095', 'SISTEMAS ADAPTATIVOS EN EDUCACIÓN'),
    ('3110117-', 'MÉTODOS SIMBÓLICOS'),
    ('31101199', 'MÉTODOS PROBABILISTAS'),
    ('31101220', 'COMPUTACIÓN EVOLUTIVA'),
    ('31101235', 'VISIÓN ARTIFICIAL'),
    ('31101254', 'DESCUBRIMIENTO DE INFORMACIÓN EN TEXTOS'),
    ('31101273', 'APLICACIONES DE LA INTELIGENCIA ARTIFICIAL PARA EL DESARROLLO HUMANO Y SOSTENIBLE'),
    ('31108018', 'WEB SEMÁNTICA Y ENLAZADO DE DATOS'),
    ('31108037', 'MÉTODOS DE APRENDIZAJE AUTOMÁTICO'),
    ('31108022', 'TRABAJO DE FIN DE MÁSTER EN INVESTIGACIÓN EN INTELIGENCIA ARTIFICIAL'),
    ('31108041', 'METODOLOGÍA DE INVESTIGACIÓN EN SISTEMAS INTELIGENTES')
]

# Código de la titulación
cod_titulacion = '310801'

# Función para obtener los contenidos de una asignatura
def obtener_contenidos(cod_asignatura, nombre_asignatura):
    url = f'https://www.uned.es/universidad/inicio/estudios/masteres/master-universitario-en-investigacion-en-inteligencia-artificial/asignaturas.html?codAsignatura={cod_asignatura}&codTitulacion={cod_titulacion}&idContenido=1'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar el encabezado de "CONTENIDOS"
        encabezados = soup.find_all(['h2', 'h3', 'h4'])
        for encabezado in encabezados:
            if 'CONTENIDOS' in encabezado.get_text().upper():
                # Obtener el siguiente elemento que contiene los contenidos
                contenido = ''
                siguiente = encabezado.find_next_sibling()
                while siguiente and siguiente.name not in ['h2', 'h3', 'h4']:
                    contenido += siguiente.get_text(strip=True) + '\n'
                    siguiente = siguiente.find_next_sibling()
                return contenido.strip()
        return 'Contenidos no encontrados.'
    except requests.RequestException as e:
        return f'Error al acceder a la página: {e}'

# Iterar sobre las asignaturas y mostrar sus contenidos
for cod_asignatura, nombre_asignatura in asignaturas:
    print(f'\n📘 {nombre_asignatura} ({cod_asignatura})')
    contenidos = obtener_contenidos(cod_asignatura, nombre_asignatura)
    print(contenidos)
