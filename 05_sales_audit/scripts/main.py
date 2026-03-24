import csv

def extract_data(file_path):
    raw_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sales_info = line.strip().split(',')
            raw_data.append(sales_info)
    return raw_data

file_path = '05_sales_audit/data/ventas_raw.csv'

extracted_data = extract_data(file_path)

def data_transformation(extracted_data):

    clean_data = []

    for row in extracted_data:
        id_prod = row[0]
        name_prod = row[1]
        total_income = row[2]
        units_prod = row[3]

        try:
            total_income = float(total_income)
            units_prod = int(units_prod)
            unit_price = total_income/units_prod
        except(ValueError, ZeroDivisionError):
            name_prod = f"REVISAR {name_prod}"
            total_income = 0.0
            unit_price = 0.0

        data_cleaned = [id_prod, name_prod, total_income, units_prod, unit_price]
        clean_data.append(data_cleaned)

    return clean_data

transformed_data = data_transformation(extracted_data)

def load_data(clean_data, output_path):

    header = ["ID", "Producto", "Ingreso", "Unidades", "Precio_Unitario"]

    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(clean_data)

output_path = "05_sales_audit/output/auditoria_precios.csv"

load_data(transformed_data, output_path)