from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Test(models.Model):
    "Generated Model"
    r1 = models.ForeignKey(
        "home.CustomText", on_delete=models.CASCADE, related_name="test_r1",
    )
    r2 = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="test_r2",
    )
    r3 = models.ForeignKey(
        "home.HomePage", on_delete=models.CASCADE, related_name="test_r3",
    )
