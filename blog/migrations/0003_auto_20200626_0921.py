# Generated by Django 3.0.6 on 2020-06-26 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200626_0921'),
        ('blog', '0002_auto_20200626_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customUser'),
        ),
    ]
