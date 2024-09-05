import csv
from django.core.management.base import BaseCommand
from Types.models import TypesModel

class Command(BaseCommand):
    help = "Arquivo CSV para salvar varios tipos"

    def add_arguments(self, parser):
        parser.add_argument('href', type=str, help="Coloque aqui o local do arquivo CSV")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['href']

        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['name']
                    resume = row['resume']
                    self.stdout.write(self.style.WARNING(f'{name} foi cadastrado.'))

                    TypesModel.objects.create(name=name, resume=resume)
                
                self.stdout.write(self.style.SUCCESS("Cadastramos todos tipos"))
        
        except FileNotFoundError:
            return "Não foi passado nenhum arquivo"
        
        except  Exception as error:
            return f"Não foi Possivel realizar a importação: {error}"