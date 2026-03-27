import os

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

