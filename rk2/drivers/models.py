from django.db import models


class Autopark(models.Model):
    name = models.CharField(max_length=256, verbose_name="Autopark name")

    def __str__(self):
        return self.name


class Driver (models.Model):
    name = models.CharField(max_length=256, verbose_name="Driver name")
    salary = models.PositiveIntegerField(verbose_name="Driver's salary")
    autopark = models.ForeignKey(
        Autopark,
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None,
        related_name="drivers"
    )

    def __str__(self):
        return self.name