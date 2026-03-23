import csv

def extract_data(file_path):

    raw_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            pyroll_info = line.strip().split(';')
            raw_data.append(pyroll_info)
        return raw_data
    
file_path = "04_HR_Payroll/data/empleados_raw.txt"

extracted_data = extract_data(file_path)

def trasnformation_data(extracted_data):
    raw_data = []
    
    for row in extracted_data:
        id_employee = row[0]
        employee = row[1].title().strip()
        department = row[2]
        gross_salary = row[3]

        try:
            gross_salary = float(gross_salary)
            gross_salary = round(gross_salary, 2)
            net_salary = (gross_salary * 0.81) / 12
            net_salary = round(net_salary, 2)
            clean_data = [id_employee, employee, department, gross_salary, net_salary]
            raw_data.append(clean_data)
        except ValueError:
            gross_salary = 0.0
            employee = f"REVISAR {employee}"

            net_salary = 0.0

            clean_data = [id_employee, employee, department, gross_salary, net_salary]
            raw_data.append(clean_data)

    return raw_data

transformed_data = trasnformation_data(extracted_data)

def load_data(clean_data, output_path):
    header= ['ID','Empleado','Departamento', 'Salario_bruto', 'Neto_mensual']

    with open(output_path, 'w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(clean_data)

output_payroll = "04_HR_Payroll/output/nominas_finales.csv"

load_data(transformed_data, output_payroll)