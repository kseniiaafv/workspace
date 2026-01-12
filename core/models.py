from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField("Название сайта", max_length=120, default="KANISDOG")

    hero_text = models.TextField("Текст (Hero)", blank=True)
    hero_image = models.ImageField("Картинка (Hero)", upload_to="hero/", blank=True, null=True)

    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"