from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa kategorii")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Dostępny'),
        ('repair', 'W naprawie'),
        ('written_off', 'Spisany'),
    ]

    inventory_number = models.CharField(max_length=50, unique=True, verbose_name="Numer inwentarzowy")
    name = models.CharField(max_length=200, verbose_name="Nazwa sprzętu")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Status")
    added_date = models.DateField(auto_now_add=True, verbose_name="Data dodania")

    def __str__(self):
        return f"{self.inventory_number} - {self.name}"

    class Meta:
        verbose_name = "Sprzęt"
        verbose_name_plural = "Sprzęt"