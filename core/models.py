from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField("Название сайта", max_length=120, default="KANISDOG")

    hero_text = models.TextField("Текст (Hero)", blank=True)
    hero_image = models.ImageField("Картинка (Hero)", upload_to="hero/", blank=True, null=True)

    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"


class Specialist(models.Model):
    photo = models.ImageField(upload_to='specialists/', verbose_name="Фотография")
    name = models.CharField(max_length=100, verbose_name="Имя")
    role = models.CharField(max_length=100, verbose_name="Должность")
    experience = models.CharField(max_length=50, verbose_name="Опыт работы")
    breed = models.CharField(max_length=100, verbose_name="Порода собаки", help_text="Если специалист работает с собакой")

    order = models.PositiveIntegerField(default=0, verbose_name="Порядок вывода")
    is_active = models.BooleanField(default=True, verbose_name="Показывать на сайте")

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        ordering = ['order']

    def __str__(self):
        return self.name


class Dog(models.Model):
    photo = models.ImageField(upload_to='dogs/', verbose_name="Фотография")
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.CharField(max_length=100, verbose_name="Порода")
    age = models.CharField(max_length=50, verbose_name="Возраст")
    character = models.CharField(max_length=255, verbose_name="Характер")
    likes = models.CharField(max_length=255, verbose_name="Что любит")

    # Связь с моделью Специалиста (если вы назвали её Specialist)
    specialist = models.ForeignKey(
        'Specialist',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Специалист (хозяин)",
        related_name='dogs'
    )

    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Показывать")

    class Meta:
        verbose_name = "Собака-терапевт"
        verbose_name_plural = "Собаки-терапевты"
        ordering = ['order']

    def __str__(self):
        return self.name


class Review(models.Model):
    CATEGORY_CHOICES = [
        ('parent', 'Отзывы родителей'),
        ('adult', 'Отзывы взрослых'),
        ('result', 'Результаты'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Имя")
    age_info = models.CharField(max_length=100, blank=True, verbose_name="Возраст (ребенка/клиента)", help_text="Например: 7 лет")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveIntegerField(default=5, verbose_name="Оценка (1-5)")

    is_active = models.BooleanField(default=True, verbose_name="Показывать")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв / Результат"
        verbose_name_plural = "Отзывы и Результаты"

    def __str__(self):
        return f"{self.name} - {self.get_category_display()}"

    # Хелпер для вывода звезд в шаблоне (возвращает диапазон)
    def star_range(self):
        return range(self.rating)