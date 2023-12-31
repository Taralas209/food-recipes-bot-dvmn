from django.db import models
import json


class User(models.Model):
    telegram_id = models.PositiveIntegerField(verbose_name='Телеграм ID')
    current_subscription_plan = models.ForeignKey('SubscriptionPlan', related_name='users',
                                                  verbose_name='Текущий план подписки', on_delete=models.SET_NULL,
                                                  null=True)

    def __str__(self):
        return str(self.telegram_id)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Recipes(models.Model):
    title = models.TextField(verbose_name='Название блюда')
    image = models.ImageField(verbose_name='Изображение блюда', upload_to='recipes')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    ingredients = models.ManyToManyField('Ingredients', verbose_name='Ингредиенты', related_name='Рецепты')
    category = models.ManyToManyField('Category', related_name='recipes', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ingredients(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class SubscriptionPlan(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='subscription_plans',
        verbose_name='Пользователь'
    )
    plan_choice = models.CharField(max_length=100, verbose_name='Выбор Плана', null=True, default=None)
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    daily_plans = models.TextField(verbose_name='Планы на каждый день')

    class Meta:
        verbose_name = 'План подписки'
        verbose_name_plural = 'Планы подписки'

    def __str__(self):
        user = str(self.user.telegram_id) if self.user else 'No User'
        return f"{user} - {str(self.start_date)} - {str(self.end_date)}"

    def set_daily_plans(self, daily_plans_dict):
        self.daily_plans = json.dumps(daily_plans_dict)

    def get_daily_plans(self):
        return json.loads(self.daily_plans)
