# Generated by Django 4.2.5 on 2023-09-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipes_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='category',
        ),
        migrations.AddField(
            model_name='recipes',
            name='category',
            field=models.ManyToManyField(null=True, related_name='recipes', to='recipes.category', verbose_name='Категория'),
        ),
    ]
