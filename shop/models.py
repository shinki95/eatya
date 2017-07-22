from django.db import models


class Shop(models.Model):
    RATING_POINTS = (
        (5, '아주 좋아요'),
        (4, '좋아요'),
        (3, '보통이에요'),
        (2, '별로에요'),
        (1, '최악!'),
    )

    name = models.CharField(max_length=20, blank=True)
    menu = models.CharField(max_length=20, blank=True)
    price = models.IntegerField(verbose_name="가격", blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_POINTS)  
    photo = models.ImageField(upload_to="shop", blank=True)


    