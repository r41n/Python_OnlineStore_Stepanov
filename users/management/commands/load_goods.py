from django.core.management.base import BaseCommand
from users.models import Product, Inventory



class Command(BaseCommand):
    help = 'Загрузка товаров в базу данных'

    def handle(self, *args, **kwargs):
        goods = [
            {"name": "Ноутбук", "price": 57000, "quantity": 5},
            {"name": "Смартфон", "price": 30000, "quantity": 10},
        ]

        for item in goods:
            product, created = Product.objects.get_or_create(
                name=item["name"],
                defaults={"price": item["price"],
                          "description": "",
                          "image": "products/default.jpg",
                }
            )

            inventory, _ = Inventory.objects.get_or_create(product=product)
            inventory.quantity = item["quantity"]
            inventory.save()

            if created:
                self.stdout.write(self.style.SUCCESS(f"Создан товар: {product.name}"))
            else:
                self.stdout.write(f"Обновлён товар: {product.name}")

        self.stdout.write(self.style.SUCCESS("Загрузка завершена"))
