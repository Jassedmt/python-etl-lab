import os
import csv

def extract_data(full_route, origin_name):
    raw_data = []
    with open(full_route, 'r', encoding='utf-8') as file:
        for line in file:
            info = line.strip().split(',')
            
            # 💡 TRUCO: Añadimos el origen al final de la lista 
            info.append(origin_name) 
            
            raw_data.append(info)
    return raw_data

data_path = "06_logistics_audit/data/"
all_extracted_data = []

if not os.path.exists(data_path):
    print(f"Error: La carpeta {data_path} no existe.")
else:
    files = os.listdir(data_path)

    for file_name in files:
        if file_name.endswith('.csv'):
            # Crear ruta completa
            full_route = os.path.join(data_path, file_name)
            
            # Extraer el nombre del origen (ej: "warehouse_madrid" de "warehouse_madrid.csv")
            origin = file_name.replace(".csv", "")
            
            # LLAMAR A LA FUNCIÓN (Dentro del bucle para que lo haga con CADA archivo)
            data_from_file = extract_data(full_route, origin)
            
            # Acumular los datos
            all_extracted_data.extend(data_from_file)
            print(f"✅ Procesado: {file_name}")

print("-" * 30)
print(f"📦 Total de filas extraídas: {len(all_extracted_data)}")


def validate_row(row):
    zones = ["Norte", "Sur", "Este", "Oeste"]

    if not row[0]:
        return False, "ID vacío"
    
    try:
        weight = float(row[1])
        if weight <= 0:
            return False, "Peso menor o igual a 0 (cero)"
    except ValueError:
        return False, "Peso no es un número"
    
    try:
        zone = row[2]
        if zone not in zones: # <--- Usamos 'not in' para buscar en la lista
            return False, f"Zona '{zone}' no permitida"
    except IndexError:
        return False, "Falta la columna de Zona"
    
    try:
        cost = float(row[3])
        if cost < 0:
            return False, "Precio negativo"
    except ValueError:
        return False, "el Precio no es un número"
    
    return True, "OK"


# 1. Creamos las dos listas vacías para separar los datos
clean_data = []
error_report = []

# 2. Recorremos todos los datos que extrajimos antes
for row in all_extracted_data:
    # Llamamos a tu función para CADA fila
    is_valid, message = validate_row(row)
    
    if is_valid:
        # Si es True, la guardamos en limpios
        clean_data.append(row)
    else:
        # Si es False, creamos una copia de la fila y le pegamos el motivo del error
        row_with_error = row.copy()
        row_with_error.append(message)
        error_report.append(row_with_error)

# 3. Ahora sí, imprimimos un resumen para ver qué ha pasado
print(f"✅ Registros limpios: {len(clean_data)}")
print(f"⚠️ Registros con errores: {len(error_report)}")

# Si quieres ver los errores específicos:
print("\n--- DETALLE DE ERRORES ---")
for err in error_report:
    print(err)


def load_data(data, output_path, header): # Añadimos 'header' como parámetro
    # Nos aseguramos de que la carpeta de salida exista
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# --- LLAMADAS CORREGIDAS ---

# 1. Cabecera para limpios (incluye el Origen)
header_clean = ["ID_Envío", "Peso(kg)", "Zona", "Costo", "Origen_Archivo"]
load_data(clean_data, "06_logistics_audit/output/envios_limpios.csv", header_clean)

# 2. Cabecera para errores (incluye Origen y Motivo)
header_errors = ["ID_Envío", "Peso(kg)", "Zona", "Costo", "Origen_Archivo", "Motivo_Error"]
load_data(error_report, "06_logistics_audit/output/reporte_errores.csv", header_errors)