import csv

from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    help = 'Загрузка данных (сведений о телефонах) из cvs в БД'
    
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # скрипт загрузки данных из cvs в БД 
            new_phone = Phone(**phone)
            new_phone.save()
        
        self.stdout.write(self.style.SUCCESS(f'Из cvs в БД успешно загружены данные о {len(phones)} телефонах'))
