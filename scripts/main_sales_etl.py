import csv


# Extraer datos

def extract_data(file_path):

    raw_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sales_info = line.strip().split(';')
            raw_data.append(sales_info)
    
    return raw_data

route = "data/ventas_raw.txt"
extracted_data = extract_data(route)

print(f"📦 Datos extraídos correctamente: {len(extracted_data)} registros encontrados.")
print(extracted_data[0]) 

print("-" * 30)

#Transformación de datos

def sanitize_sales(sales_raw):
    sales_cleaned = []

    for sales in sales_raw:
        product_name = sales[0].strip().title()
        amount_product = sales[1]
        product_price = sales[2]
        clean_price = product_price.replace("€", "").replace("EUR", "").replace("eur", "").replace(",", ".").strip()
        clean_price = float(clean_price)
        amount_product = int(amount_product)
    
        operation_row = clean_price * amount_product
        
        products_cleaned = [product_name, amount_product, clean_price, operation_row]
        sales_cleaned.append(products_cleaned)

    return sales_cleaned

print (f"{sanitize_sales(extracted_data)}")


print("-" * 30) #--------------------------------------------------

#Envío de archivos sanitizados

def load_data(clean_data, output_path):
    header = ['Producto', 'Cantidad', 'Precio Unitario', "Precio Total"]

    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(clean_data)

entry_route = "data/ventas_raw.txt"
unclean_sales = extract_data(entry_route)

cleaned_sales = sanitize_sales(unclean_sales)

output_route = "output/ventas_final.csv"
load_data(cleaned_sales, output_route)

print(f"🚀 Proceso completado. Archivo guardado en: {output_route}")