def extract_data(file_path):
    raw_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            financial_info = line.strip().split(',')
            raw_data.append(financial_info)

    return raw_data

route = "03_financial_consolidation/data/pagos_raw.txt"
extract_data = extract_data(route)

print(f"Datos extraídos correctamente: {len(extract_data)}")


def data_transformation(finantial_raw):

    clean_data = []

    for row in finantial_raw:
        id = row[0]
        client = row[1].strip().title()
        original_amount = row[2]
        original_amount = float(original_amount)
        badge = row[3]
    
        cleaned_data = [id, client, original_amount, badge]
        clean_data.append(cleaned_data)

    return clean_data

print(data_transformation(extract_data))