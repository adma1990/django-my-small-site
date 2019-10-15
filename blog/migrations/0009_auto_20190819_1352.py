# Generated by Django 2.2.3 on 2019-08-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190813_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaruselImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caruselImagesOne', models.ImageField(upload_to='images', verbose_name='Изображение для карусели №1')),
                ('caruselImagesTwo', models.ImageField(upload_to='images', verbose_name='Изображение для карусели №2')),
                ('caruselImageThree', models.ImageField(upload_to='images', verbose_name='Изображение для карусели №3')),
            ],
            options={
                'verbose_name': 'Изображения для карусели',
            },
        ),
        migrations.AlterModelOptions(
            name='mag',
            options={'verbose_name': 'Каталог'},
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
