import pytest
from rest_framework.test import APIClient

from apps.main.models import CategoryFood, Food, FoodReviews, Promo, Tags


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def category_food():
    category = CategoryFood.objects.create(name="Burger", order=1, slug="burger")

    return category


@pytest.fixture
def tags_test():
    tags = Tags.objects.create(name="Burger")

    return tags


@pytest.fixture
def promo_test():
    promo = Promo.objects.create(name="Burger", discount_percent=12)

    return promo


# @pytest.fixture
# def restourant(user , category , address):
#     res = Restourant.objects.create(
#         name = "Food",
#         description = "food desc",
#         category=category,
#         address_id = address,
#         location_url = "https://yandex.uz/maps/org/244997649299/?ll=69.221894%2C41.293430&z=16",
#         orders_count=1,
#         working_hourse = " 09:00 - 20:00"


#     )
#     return res


@pytest.fixture
def food_test(restourant, category_food, promo_test, tags_test):
    food = Food.objects.create(
        name="KFC",
        description="kfc ovqat nomi",
        category=category_food,
        restourant=restourant,
        base_price="20000",
        is_promo_active=True,
        is_available=True,
        slug="burger",
    )

    food.promo.set([promo_test])
    food.tags.set([tags_test])
    return food


@pytest.fixture
def food_reviews(user, food_test):
    data = FoodReviews.objects.create(rating=3, comment="Hello reviews", user=user, food=food_test)

    return data
