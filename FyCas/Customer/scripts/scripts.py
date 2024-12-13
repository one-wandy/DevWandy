import csv
from Customer.models import Customer  # Ajusta según el nombre de tu modelo y app
from datetime import datetime

def run():
    # Abre el archivo CSV y realiza la importación
    with open('Customer/scripts/customer_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            try:
                # Convierte el valor de 'day_created' si es necesario
                day_created = datetime.strptime(row['day_created'], '%Y-%m-%d')  # Ajusta el formato si es necesario
                
                # Crea el objeto Customer
                Customer.objects.create(
                    name=row['name'],
                    last_name=row['last_name'],
                    number=row['number'],
                    address=row['address'],
                    amount_purpose=row['amount_purpose'],
                    work_information=row['work_information'],
                    references_peopple=row['references_peopple'],
                    dni=row['dni'],

                        
                    amount=0,

                    name_r1=row['name_r1'],
                    number_r1=row['number_r1'],
                    name_r2=row['name_r2'],
                    number_r2=row['number_r2'],
                    lat=row['lat'],
                    lon=row['lon'],
                    calle_numero=row['calle_numero'],
                    cargo=row['cargo'],
                    ciudad=row['ciudad'],
                    direccion=row['direccion'],
                    empresa_trabaja=row['empresa_trabaja'],
                    estado_civil=row['estado_civil'],
                    moneda=row['moneda'],
                    municipio=row['municipio'],
                    nacimiento=row['nacimiento'],
                    ocupacion=row['ocupacion'],
                    phone=row['phone'],
                    provincia=row['provincia'],
                    salario_m=row['salario_m'],
                    sexo=row['sexo'],
                    day_created=day_created  # Usamos la fecha convertida
                )
            except Exception as e:
                print(f"Error al importar la fila {row}: {e}")
                continue  # Ignorar y continuar con la siguiente fila

    print("Datos importados correctamente.")