# Generated by Django 3.2.4 on 2021-06-08 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('storage', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ingredients',
            },
        ),
        migrations.CreateModel(
            name='MainCategoryIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'main_categories_ingredients',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.maincategoryingredient')),
            ],
            options={
                'db_table': 'sub_categories_ingredients',
            },
        ),
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'db_table': 'ingredients_recipes',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.subcategoryingredient'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ManyToManyField(through='ingredient.IngredientRecipe', to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ManyToManyField(to='user.User'),
        ),
    ]
