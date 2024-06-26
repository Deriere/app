# Generated by Django 4.2.11 on 2024-04-23 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название роли')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('password', models.CharField(max_length=150, verbose_name='Пароль')),
                ('email', models.CharField(max_length=200, unique=True)),
                ('phoneNumber', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_images')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicServices.roles', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователя',
                'db_table': 'User',
            },
        ),
    ]
