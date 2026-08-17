import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            add_phone = Phone(
                id=int(phone['id']),
                name=phone['name'],
                price=float(phone['price'].replace(',', '.')),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'].lower() in ['true', '1', 'yes', 'True'],
                slug=slugify(phone['name'])
            )
            add_phone.save()

