# Generated by Django 3.0.6 on 2020-06-27 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200627_1149'),
        ('blog', '0003_auto_20200626_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customUser'),
        ),
    ]