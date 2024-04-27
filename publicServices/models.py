from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название роли")

    class Meta:
        db_table = "Role"
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    role = models.ForeignKey(to=Roles, on_delete=models.CASCADE, verbose_name="Роль")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    password = models.CharField(max_length=150, verbose_name="Пароль")
    email = models.CharField(
        max_length=200,
        unique=True,
    )
    phoneNumber = models.CharField(max_length=150, verbose_name="Номер телефона")
    image = models.ImageField(upload_to="user_images", blank=True, null=True)

    class Meta:
        db_table = "User"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователя"

    def __str__(self):
        return f"{self.name}"
