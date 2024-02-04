from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    required_categories = [
        "Appetizers",
        "Main Course",
        "Desserts",
    ]

    for category in required_categories:
        if category.lower() not in value.lower():
            raise ValidationError(f'The menu must include each of the categories '
                                  f'"Appetizers", "Main Course", "Desserts".')





