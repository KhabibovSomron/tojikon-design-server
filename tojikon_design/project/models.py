from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField("Название категорий", max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категорий"
        verbose_name_plural = "Категорий"


class Project(models.Model):
    title = models.CharField("Название проекта", max_length=255)
    description = models.TextField("Описание проекта")
    created_date = models.DateField("Дата добавление проекта в бд", auto_now_add=True)
    finish_date = models.DateField("Дата окончания проекта")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"


class Image(models.Model):
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE)
    image = models.ImageField("Изображение проекта", upload_to="images/projects/", default="none")

    def __str__(self):
        return self.project
    
    class Meta:
        verbose_name = "Изображений проекта"
        verbose_name_plural = "Изображений проекта"


class Video(models.Model):
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE)
    link = models.CharField("Ссылка на видео из Youtube", max_length=500, default="")
    
    def __str__(self):
        return self.project
    
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"