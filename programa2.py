import os
import random
import pandas as pd

# Configuración inicial
carpeta_salida = "Trabajo_Final"
archivo_consolidado = "ReporteConsolidado.xlsx"

# Listado de asignatura según el pensum de ingeniería industrial
asignaturas = [
    # Primer semestre
    {"nombre": "Álgebra y Trigonometría", "semestre": 1, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Cálculo Diferencial", "semestre": 1, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Geometría Vectorial y Analítica", "semestre": 1, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Vivamos la Universidad", "semestre": 1, "creditos": 1, "max_estudiantes_por_grupo": 40},
    {"nombre": "Inglés I", "semestre": 1, "creditos": 1, "max_estudiantes_por_grupo": 40},
    {"nombre": "Lectoescritura", "semestre": 1, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Introducción a la Ingeniería Industrial", "semestre": 1, "creditos": 1, "max_estudiantes_por_grupo": 40},
    # Segundo semestre
    {"nombre": "Gestión de las Organizaciones", "semestre": 2, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Habilidades Gerenciales", "semestre": 2, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Álgebra Lineal", "semestre": 2, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Cálculo Integral", "semestre": 2, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Descubriendo la Física", "semestre": 2, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Inglés II", "semestre": 2, "creditos": 1, "max_estudiantes_por_grupo": 40},
    # Tercer semestre
    {"nombre": "Gestión Contable", "semestre": 3, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Física Mecánica", "semestre": 3, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Inglés III", "semestre": 3, "creditos": 1, "max_estudiantes_por_grupo": 40},
    {"nombre": "Algoritmia y Programación", "semestre": 3, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Probabilidad e Inferencia Estadística", "semestre": 3, "creditos": 3, "max_estudiantes_por_grupo": 40},
    {"nombre": "Teoría General de Sistemas", "semestre": 3, "creditos": 3, "max_estudiantes_por_grupo": 40},
    # Cuarto semestre
    {"nombre": "Ingeniería Económica", "semestre": 4, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Electiva en Física", "semestre": 4, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Inglés IV", "semestre": 4, "creditos": 1, "max_estudiantes_por_grupo": 35},
    {"nombre": "Diseño de Experimentos y Análisis de Regresión", "semestre": 4, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Optimización", "semestre": 4, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Gestión de Métodos y Tiempos", "semestre": 4, "creditos": 4, "max_estudiantes_por_grupo": 35},
    # Quinto semestre
    {"nombre": "Gestión Financiera", "semestre": 5, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Laboratorio Integrado de Física", "semestre": 5, "creditos": 1, "max_estudiantes_por_grupo": 35},
    {"nombre": "Inglés V", "semestre": 5, "creditos": 1, "max_estudiantes_por_grupo": 35},
    {"nombre": "Formación Ciudadana y Constitucional", "semestre": 5, "creditos": 1, "max_estudiantes_por_grupo": 35},
    {"nombre": "Dinámica de Sistemas", "semestre": 5, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Muestreo y Series de Tiempo", "semestre": 5, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Procesos Estocásticos y Análisis de Decisión", "semestre": 5, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Gestión por Procesos", "semestre": 5, "creditos": 3, "max_estudiantes_por_grupo": 35},
    # Sexto semestre
    {"nombre": "Gestión Tecnológica", "semestre": 6, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Legislación", "semestre": 6, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Electiva en Humanidades I", "semestre": 6, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Inglés VI", "semestre": 6, "creditos": 1, "max_estudiantes_por_grupo": 35},
    {"nombre": "Simulación Discreta", "semestre": 6, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Formulación de Proyectos de Investigación", "semestre": 6, "creditos": 3, "max_estudiantes_por_grupo": 35},
    {"nombre": "Normalización y Control de la Calidad", "semestre": 6, "creditos": 3, "max_estudiantes_por_grupo": 35},
    # Séptimo semestre
    {"nombre": "Formulación y Evaluación de Proyectos de Inversión", "semestre": 7, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Emprendimiento", "semestre": 7, "creditos": 2, "max_estudiantes_por_grupo": 25},
    {"nombre": "Electiva en Humanidades II", "semestre": 7, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Énfasis Profesional I", "semestre": 7, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Electiva Complementaria I", "semestre": 7, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Diseño de Sistemas Productivos", "semestre": 7, "creditos": 3, "max_estudiantes_por_grupo": 25},
    # Octavo semestre
    {"nombre": "Gestión de Proyectos", "semestre": 8, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Electiva en Humanidades III", "semestre": 8, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Énfasis Profesional II", "semestre": 8, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Electiva Complementaria II", "semestre": 8, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Administración de la Producción y del Servicio", "semestre": 8, "creditos": 3, "max_estudiantes_por_grupo": 25},
    # Noveno semestre
    {"nombre": "Electiva en Humanidades IV", "semestre": 9, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Énfasis Profesional III", "semestre": 9, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Electiva Complementaria III", "semestre": 9, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Gestión de la Cadena de Abastecimiento", "semestre": 9, "creditos": 3, "max_estudiantes_por_grupo": 25},
    {"nombre": "Ingeniería del Mejoramiento Continuo", "semestre": 9, "creditos": 3, "max_estudiantes_por_grupo": 25},
    # Décimo semestre
    {"nombre": "Práctica Profesional", "semestre": 10, "creditos": 12, "max_estudiantes_por_grupo": 10},
]

# Asegurar creación de las carpetas
def crear_estructura_carpetas(carpeta_base, asignaturas):
    for asignatura in asignaturas:
        carpeta_asignatura = os.path.join(carpeta_base, f"Semestre_{asignatura['semestre']}", asignatura["nombre"].replace(" ", "_"))
        if not os.path.exists(carpeta_asignatura):
            os.makedirs(carpeta_asignatura)

# Leer datos de estudiantes desde un archivo CSV y generar IDs
def cargar_datos_estudiantes(archivo_csv):
    if not os.path.exists(archivo_csv):
        raise FileNotFoundError(f"El archivo {archivo_csv} no existe.")
    estudiantes = pd.read_csv(archivo_csv, names=["Nombre"], header=0)
    estudiantes["ID"] = range(1, len(estudiantes) + 1)
    return estudiantes

# Dividir estudiantes en grupos
def asignar_grupos(estudiantes, asignatura):
    max_estudiantes_por_grupo = asignatura["max_estudiantes_por_grupo"]
    grupos = [estudiantes[i:i + max_estudiantes_por_grupo] for i in range(0, len(estudiantes), max_estudiantes_por_grupo)]
    return grupos

# Generar notas para estudiantes (se debe de tener el 70% aprobados)
def generar_notas(grupos, tasa_aprobacion=0.7):
    resultados = []
    total_estudiantes = sum(len(grupo) for grupo in grupos)
    estudiantes_aprobados = int(total_estudiantes * tasa_aprobacion)
    estudiantes_reprobados = total_estudiantes - estudiantes_aprobados

    notas = [round(random.uniform(3.0, 5.0), 2) for _ in range(estudiantes_aprobados)] + \
            [round(random.uniform(2.0, 2.9), 2) for _ in range(estudiantes_reprobados)]
    random.shuffle(notas)

    indice_notas = 0
    for id_grupo, grupo in enumerate(grupos, start=1):
        for _, estudiante in grupo.iterrows():
            resultados.append({
                "ID estudiante": estudiante["ID"],
                "Grupo": id_grupo,
                "Nota": notas[indice_notas]
            })
            indice_notas += 1
    return pd.DataFrame(resultados)

# Generar código único para asignatura (se toma solo las primeras 3 letras del nombre,semestre y número de creditos para cumplir con 6 caracteres)
def generar_codigo_asignatura(asignatura, indice):
    codigo_nombre = asignatura["nombre"][:3].upper()
    codigo_asignatura = f"{codigo_nombre}{asignatura['semestre']}{asignatura['creditos']}"
    return codigo_asignatura[:6]

# Guardar archivos en archivo de excel y de CSV
def guardar_archivos(asignatura, grupos, notas, carpeta_base):
    carpeta_asignatura = os.path.join(carpeta_base, f"Semestre_{asignatura['semestre']}", asignatura["nombre"].replace(" ", "_"))
    for id_grupo, grupo in enumerate(grupos, start=1):
        nombre_archivo = f"{generar_codigo_asignatura(asignatura, id_grupo)}-{asignatura['nombre'].replace(' ', '').capitalize()}-{len(grupo)}-{id_grupo}"
        grupo_con_notas = pd.merge(grupo, notas[notas["Grupo"] == id_grupo], left_on="ID", right_on="ID estudiante")
        if "ID estudiante" in grupo_con_notas.columns and "ID" in grupo_con_notas.columns:
            grupo_con_notas = grupo_con_notas.drop(columns=["ID estudiante"])

        # Agregar columnas
        
        grupo_con_notas["semestre"] = asignatura["semestre"]
        grupo_con_notas["Código Asignatura"] = generar_codigo_asignatura(asignatura, id_grupo)
        grupo_con_notas["Nombre Asignatura"] = asignatura["nombre"]
        

        # Cambiar el orden de las columnas 
        columnas_ordenadas = [
            "Código Asignatura",
            "Nombre Asignatura",
            "semestre",
            "ID",
            "Nombre",
            "Grupo",
            "Nota"
        ]
        grupo_con_notas = grupo_con_notas[columnas_ordenadas]

        # Guardar en Excel
        grupo_con_notas.to_excel(os.path.join(carpeta_asignatura, f"{nombre_archivo}.xlsx"), index=False)

        # Guardar en CSV
        grupo_con_notas.to_csv(os.path.join(carpeta_asignatura, f"{nombre_archivo}.csv"), index=False)

# Consolidar información para reporte final ( este reporte contiene información de las asignaturas y notas promedio)
def consolidar_reporte(asignaturas, estudiantes):
    datos_consolidados = []
    for indice, asignatura in enumerate(asignaturas, start=1):
        codigo_asignatura = generar_codigo_asignatura(asignatura, indice)
        grupos = asignar_grupos(estudiantes, asignatura)
        notas = generar_notas(grupos)
        
        for id_grupo, grupo in enumerate(grupos, start=1):
            datos_consolidados.append({
                "Código Asignatura (CA)": codigo_asignatura,
                "Asignatura": asignatura["nombre"],
                "Semestre": asignatura["semestre"],
                "Créditos": asignatura["creditos"],
                "Número Total de Estudiantes (NTE)": len(grupo),
                "Código del Curso (CC)": f"{codigo_asignatura}-G{id_grupo}",
                "Nota Promedio": round(notas[notas["Grupo"] == id_grupo]["Nota"].mean(), 2)
            })
    return pd.DataFrame(datos_consolidados)

# Guardar reporte consolidado (cada fila es un grupo con cada asignatura)
def guardar_reporte_consolidado(dataframe, archivo_salida):
    dataframe.to_excel(archivo_salida, index=False)

# Flujo principal
def main(archivo_csv):
    # Crear carpetas solo una vez
    crear_estructura_carpetas(carpeta_salida, asignaturas)

    # Leer datos de estudiantes
    estudiantes = cargar_datos_estudiantes(archivo_csv)

    # Consolidar datos para reporte final
    datos_consolidados = consolidar_reporte(asignaturas, estudiantes)

    # Guardar reporte consolidado
    guardar_reporte_consolidado(datos_consolidados, archivo_consolidado)

    # Generar archivos individuales para cada asignatura
    for asignatura in asignaturas:
        grupos = asignar_grupos(estudiantes, asignatura)
        notas = generar_notas(grupos)
        guardar_archivos(asignatura, grupos, notas, carpeta_salida)
   
if __name__ == "__main__":
    archivo_csv = "data.csv"  
    main(archivo_csv)
