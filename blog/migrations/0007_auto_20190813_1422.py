# Generated by Django 2.2.3 on 2019-08-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190813_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='mag',
            name='image1',
            field=models.ImageField(default=' ', upload_to='images', verbose_name='Изображение №1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mag',
            name='image2',
            field=models.ImageField(default=' ', upload_to='images', verbose_name='Изображение №2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mag',
            name='image3',
            field=models.ImageField(default=' ', upload_to='images', verbose_name='Изображение №3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mag',
            name='image4',
            field=models.ImageField(default=' ', upload_to='images', verbose_name='Изображение №4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mag',
            name='image5',
            field=models.ImageField(default=' ', upload_to='images', verbose_name='Изображение №5'),
            preserve_default=False,
        ),
    ]