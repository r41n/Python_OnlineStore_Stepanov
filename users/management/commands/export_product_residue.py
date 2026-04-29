import json
from django.core.management.base import BaseCommand
from users.models import Inventory


class Command(BaseCommand):
    help = 'Экспорт остатков товаров в JSON'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            default='inventory_export.json',
            help='Имя выходного файла'
        )

    def handle(self, *args, **kwargs):
        output_file = kwargs['output']

        data = []

        inventories = Inventory.objects.select_related('product').all()

        for inv in inventories:
            data.append({
                "product_id": inv.product.id,
                "product_name": inv.product.name,
                "quantity": inv.quantity,
            })

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.stdout.write(
            self.style.SUCCESS(f"Экспорт завершён: {output_file}")
        )
