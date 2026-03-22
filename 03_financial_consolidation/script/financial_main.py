import csv

def extract_data(file_path):
    raw_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            financial_info = line.strip().split(',')
            raw_data.append(financial_info)

    return raw_data

route = "03_financial_consolidation/data/pagos_raw.txt"
extracted_data = extract_data(route)


def data_transformation(finantial_raw):

    clean_data = []

    for row in finantial_raw:
        id = row[0]
        client = row[1].strip().title()
        original_amount = row[2]
        original_amount = float(original_amount)
        badge = row[3].upper()
    
        cleaned_data = [id, client, original_amount, badge]
        clean_data.append(cleaned_data)

    return clean_data

transformed_data = data_transformation(extracted_data)

def badge_to_eur(transformed_data):
    badges = []

    for badge in transformed_data:
        
        tariff = {"USD": 0.92, "GBP": 1.17, "EUR": 1.0}

        valuation = tariff[badge[3]]
        converted_amount = round(badge[2] * valuation, 2)

        final_row = [badge[0], badge[1], badge[2], badge[3], converted_amount]
        
        badges.append(final_row)
    return badges
    
badge_cleaned = badge_to_eur(transformed_data)


def load_data(clean_data, output_path):
    header = ["ID", "Cliente", "Monto_Original", "Divisa_Original", "Monto_EUR"]

    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(clean_data)

badge_cleaned = badge_to_eur(transformed_data)

output_route = "03_financial_consolidation/output/pagos_consolidados.csv"
load_data(badge_cleaned, output_route)