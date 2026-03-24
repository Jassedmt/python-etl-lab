
def extract_data(file_path):
    raw_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sales_info = line.strip().split(',')
            raw_data.append(sales_info)
    return raw_data

file_path = '05_sales_audit/data/ventas_raw.csv'

extracted_data = extract_data(file_path)
print(extracted_data)