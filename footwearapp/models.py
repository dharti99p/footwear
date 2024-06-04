from django.db import models

# Create your models here.


class Register(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)


class MenuForm(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class SubMenu(models.Model):
    menu_form = models.ForeignKey(MenuForm, related_name='sub_menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class BadgeMenu(models.Model):
    id = models.AutoField(primary_key=True)
    badge = models.CharField(max_length=300)
