from shop.models import Category, Product, Customer, Order, OrderDetail




from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Display data from all tables"

    def handle(self, *args, **kwargs):
        # Категории
        self.stdout.write("Категорії:")
        for category in Category.objects.all():
            self.stdout.write(f"{category.id}. {category.name}")
        self.stdout.write("")  # Пустая строка

        # Продукты
        self.stdout.write("Продукти:")
        for product in Product.objects.select_related('category').all():
            self.stdout.write(
                f"{product.id}. {product.name} - {product.price} грн (Категорія: {product.category.name})"
            )
        self.stdout.write("")

        # Клиенты
        self.stdout.write("Клієнти:")
        for customer in Customer.objects.all():
            self.stdout.write(
                f"{customer.id}. {customer.first_name} {customer.last_name} - {customer.phone} - {customer.email}"
            )
        self.stdout.write("")

        # Заказы
        self.stdout.write("Замовлення:")
        for order in Order.objects.select_related('customer').all():
            self.stdout.write(
                f"Замовлення {order.id} від {order.order_date} для {order.customer.first_name} {order.customer.last_name}"
            )
        self.stdout.write("")
