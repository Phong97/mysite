# Generated by Django 2.0.3 on 2018-04-06 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180406_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(on_delete='SET NULL', to='myapp.Group'),
        ),
    ]