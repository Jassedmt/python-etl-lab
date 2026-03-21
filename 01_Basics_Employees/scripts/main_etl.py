import csv

def extract_data(file_path):
    """Fase E: Extraer datos de un archivo de texto."""
    raw_data = []
    
    # Abrimos el archivo en modo lectura ('r')
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Cada línea es un empleado. La dividimos por la coma.
            employee_info = line.strip().split(',')
            raw_data.append(employee_info)
            
    return raw_data

# --- PRUEBA DE EXTRACCIÓN ---
# Usamos la ruta relativa hacia la carpeta data
ruta = "01_Basics_Employees/data/empleados_raw.txt"
datos_extraidos = extract_data(ruta)

print(f"📦 Datos extraídos correctamente: {len(datos_extraidos)} registros encontrados.")
print(datos_extraidos[0]) # Debería imprimir la lista del primer empleado

print("-" * 30) #--------------------------------------------------

# Transformación de datos
def transform_data(raw_data):
    clean_data = []
    for row in raw_data:
        name = row[0].strip().title()
        email = row[1].strip().lower()
        salary = row[2].replace("€", "").strip().replace(".", "").replace(",", ".")
        salary = float(salary)
        net_salary = salary * 0.85

        employee_clean = [name, email, net_salary]
        clean_data.append(employee_clean)

    return clean_data

print(transform_data(datos_extraidos))

print("-" * 30) #--------------------------------------------------

def load_data(clean_data, output_path):
    """Fase L: Guardar los datos limpios en un archivo CSV."""
    # Definimos los nombres de las columnas (la cabecera)
    header = ['Nombre', 'Email', 'Salario Neto']
    
    # Abrimos el archivo en modo 'w' (Write / Escritura)
    # 'newline=""' evita que Windows añada líneas en blanco extra
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # 1. Escribimos la fila de títulos
        writer.writerow(header)
        
        # 2. Escribimos todas las listas de empleados de golpe
        writer.writerows(clean_data)

# --- EJECUCIÓN FINAL ---

# 1. Extraemos
ruta_entrada = "01_Basics_Employees/data/empleados_raw.txt"
datos_sucios = extract_data(ruta_entrada)

# 2. Transformamos (¡Aquí guardamos el resultado en una variable!)
datos_limpios = transform_data(datos_sucios) 

# 3. Cargamos
ruta_salida = "01_Basics_Employees/output/empleados_final.csv"
load_data(datos_limpios, ruta_salida)

print(f"🚀 Proceso completado. Archivo guardado en: {ruta_salida}")