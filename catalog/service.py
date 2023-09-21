from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cached_category():
    key = 'category'
    quryset = Category.objects.all()

    if settings.CACHE_ENABLED:
        category_list = cache.get(key)
        if category_list is None:
            category_list = quryset
            cache.set(key, category_list)
        return category_list
    return quryset

