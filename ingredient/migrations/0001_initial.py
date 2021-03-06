# Generated by Django 3.2.4 on 2021-06-18 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('storage', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ingredients',
            },
        ),
        migrations.CreateModel(
            name='IngredientMainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ingredient_main_categories',
            },
        ),
        migrations.CreateModel(
            name='IngredientSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.ingredientmaincategory')),
            ],
            options={
                'db_table': 'ingredient_sub_categories',
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
                'db_table': 'ingredient_recipes',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredient.ingredientsubcategory'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ManyToManyField(through='ingredient.IngredientRecipe', to='recipe.Recipe'),
        ),
    ]
