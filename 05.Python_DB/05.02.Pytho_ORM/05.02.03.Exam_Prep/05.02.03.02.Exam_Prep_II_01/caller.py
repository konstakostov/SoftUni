import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create and run your queries within functions
def get_profiles(search_string=None):
    if search_string is None:
        return ""

    profiles = Profile.objects.annotate(
        orders_count=Count('order')
    ).filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    ).order_by(
        'full_name',
    )

    if not profiles:
        return ""

    result = []

    for profile in profiles:
        result.append(
            f"Profile: {profile.full_name}, "
            f"email: {profile.email}, "
            f"phone number: {profile.phone_number}, "
            f"orders: {profile.orders_count}"
        )

    return '\n'.join(result)


def get_loyal_profiles():
    profiles = Profile.objects.annotate(
            orders_count=Count('order')
        ).filter(
            orders_count__gt=2
        ).order_by(
            '-orders_count'
        )

    if not profiles:
        return ""

    result = []

    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, orders: {profile.orders_count}")

    return '\n'.join(result)


def get_last_sold_products():
    latest_order = Order.objects.order_by(
        '-creation_date'
    ).first()

    if not latest_order:
        return ""

    products = latest_order.products.order_by(
        'name',
    ).values_list(
        'name',
        flat=True
    )

    products_string = ', '.join(products)

    return f"Last sold products: {products_string}"


def get_top_products():
    top_products = Product.objects.annotate(
        orders_count=Count('order')
    ).filter(
        orders_count__gt=0,
    ).order_by(
        '-orders_count',
        'name',
    )[:5]

    if not top_products:
        return ""

    product_list = []

    for product in top_products:
        product_list.append(f"{product.name}, sold {product.orders_count} times")

    return f"Top products:\n" + '\n'.join(product_list)


def apply_discounts():
    updated_orders = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False,
    ).update(
        total_price=F('total_price') * 0.90
    )

    return f"Discount applied to {updated_orders} orders."


def complete_order():
    oldest_order = Order.objects.prefetch_related(
        'products'
    ).filter(
        is_completed=False,
    ).order_by(
        'creation_date',
    ).first()

    if oldest_order is None:
        return ""

    for product in oldest_order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    oldest_order.is_completed = True

    oldest_order.save()

    return "Order has been completed!"
