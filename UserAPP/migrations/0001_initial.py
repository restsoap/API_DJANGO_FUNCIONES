# Generated by Django 4.1 on 2022-08-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=50)),
                ('Usersurname', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
