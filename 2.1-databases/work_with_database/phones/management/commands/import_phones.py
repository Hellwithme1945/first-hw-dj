import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Импортирует телефоны из CSV в базу данных'

    def handle(self, *args, **kwargs):
        with open('phones.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                Phone.objects.create(
                    name=row['name'],
                    image=row['image'],
                    price=row['price'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'] == 'True'
                )
        self.stdout.write(self.style.SUCCESS('Телефоны успешно импортированы!'))
