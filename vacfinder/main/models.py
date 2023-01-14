from django.db import models

# Create your models here.
class Graphics(models.Model):
    title = models.CharField("Название графика", max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "График"
        verbose_name_plural = "Графики"