from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField("ФИО", max_length=255)
    specialization = models.CharField("Специализация", max_length=100)
    email = models.CharField("Электронная почта", max_length=100)
    about = models.CharField("О сотруднике", max_length=255)
    image = models.ImageField("Изображение", upload_to="images/employees/", default="none")

    def __str__(self) -> str:
        return f"{self.name} - {self.specialization}"
    

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"
