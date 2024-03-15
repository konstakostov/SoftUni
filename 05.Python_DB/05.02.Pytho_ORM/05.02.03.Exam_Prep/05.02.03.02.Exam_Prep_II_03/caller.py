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
    profiles = None

    if search_string is not None:
        profiles = Profile.objects.annotate(
            total_orders=Count('order')
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
            f"orders: {profile.total_orders}"
        )

    return '\n'.join(result)


def get_loyal_profiles():
    loyal_profiles = Profile.objects.annotate(
            total_orders=Count('order')
        ).filter(
            total_orders__gt=2,
        ).order_by(
            '-total_orders'
        )

    if not loyal_profiles:
        return ""

    result = []

    for profile in loyal_profiles:
        result.append(
            f"Profile: {profile.full_name}, "
            f"orders: {profile.total_orders}"
        )

    return '\n'.join(result)


def get_last_sold_products():
    last_order = Order.objects.all().order_by(
        '-creation_date'
    ).first()

    if not last_order:
        return ""

    last_order_products = last_order.products.order_by(
        'name'
    ).values_list(
        'name',
        flat=True,
    )

    return f"Last sold products: {', '.join(last_order_products)}"


def get_top_products():
    top_products = Product.objects.annotate(
        total_orders=Count('order'),
    ).filter(
        total_orders__gt=0,
    ).order_by(
        '-total_orders',
        'name',
    )[:5]

    if not top_products:
        return ""

    product_list = []

    for product in top_products:
        product_list.append(
            f"{product.name}, "
            f"sold {product.total_orders} times"
        )

    return f"Top products:\n" + '\n'.join(product_list)


def apply_discounts():
    num_of_updated_orders = Order.objects.annotate(
        total_products=Count('products')
    ).filter(
        total_products__gt=2,
        is_completed=False,
    ).update(
        total_price=F('total_price') * 0.90
    )

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():
    oldest_order = Order.objects.prefetch_related(
        'products'
    ).filter(
        is_completed=False,
    ).order_by(
        'creation_date',
    ).first()

    if not oldest_order:
        return ""

    for product in oldest_order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    oldest_order.is_completed = True

    oldest_order.save()

    return "Order has been completed!"
