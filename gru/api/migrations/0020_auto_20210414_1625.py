# Generated by Django 3.1.7 on 2021-04-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20210414_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferreduni',
            name='pref_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]