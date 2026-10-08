from django.core.cache import cache
from django.conf import settings


# ── Plans Cache ────────────────────────────────────────────────

def get_cached_plans():
    return cache.get('plans_all')


def set_cached_plans(data):
    cache.set('plans_all', data, timeout=settings.CACHE_TTL['plans'])


def evict_plans_cache():
    cache.delete('plans_all')


# ── Permissions Cache ──────────────────────────────────────────

def get_cached_permissions(user_id: int):
    return cache.get(f'permissions_{user_id}')


def set_cached_permissions(user_id: int, data):
    cache.set(f'permissions_{user_id}', data, timeout=settings.CACHE_TTL['permissions'])


def evict_permissions_cache(user_id: int):
    cache.delete(f'permissions_{user_id}')


# ── Subscription Cache ─────────────────────────────────────────

def get_cached_subscription(sub_id: int):
    return cache.get(f'subscription_{sub_id}')


def set_cached_subscription(sub_id: int, data):
    cache.set(f'subscription_{sub_id}', data, timeout=settings.CACHE_TTL['subscription'])


def evict_subscription_cache(sub_id: int):
    cache.delete(f'subscription_{sub_id}')
