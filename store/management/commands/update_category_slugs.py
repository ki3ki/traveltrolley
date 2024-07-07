# store/management/commands/update_category_slugs.py

from django.core.management.base import BaseCommand
from store.models import Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Update slugs for categories'

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        slugs = set()

        for category in categories:
            original_slug = slugify(category.name)
            slug = original_slug

            # Ensure unique slug
            counter = 1
            while slug in slugs:
                slug = f"{original_slug}-{counter}"
                counter += 1

            # Update category slug
            category.slug = slug
            category.save()

            slugs.add(slug)

        self.stdout.write(self.style.SUCCESS('Successfully updated category slugs'))
