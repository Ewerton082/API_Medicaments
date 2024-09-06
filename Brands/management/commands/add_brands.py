from django.core.management import BaseCommand
from Brands.models import BrandsModel
import csv


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('href', help="Passe aqui o arquivo CSV")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["href"]

        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    brand = row['brand_name']
                    BrandsModel.objects.create(brand_name=brand)
                    self.stdout.write(self.style.NOTICE(f"{brand} Cadastrado com sucesso"))

                self.stdout.write(self.style.SUCCESS("Importação concluida."))

        except FileNotFoundError:
            return self.stdout.write(self.style.ERROR("Não foi passado nenhum arquivo"))

        except Exception as error:
            return self.stdout.write(self.style.ERROR(error))
