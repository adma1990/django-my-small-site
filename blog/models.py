from django.db import models

# Create your models here.

class Mag(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Название')
    slug = models.SlugField(max_length=100, unique=True)
    discription = models.TextField(blank = True, verbose_name = 'Описание')
    image = models.ImageField(upload_to='images', verbose_name = 'Изображение')
    image1 = models.ImageField(upload_to='images', blank = True, verbose_name = 'Изображение №1')
    image2 = models.ImageField(upload_to='images', blank = True, verbose_name = 'Изображение №2')
    image3 = models.ImageField(upload_to='images', blank = True, verbose_name = 'Изображение №3')
    image4 = models.ImageField(upload_to='images', blank = True, verbose_name = 'Изображение №4')
    image5 = models.ImageField(upload_to='images', blank = True, verbose_name = 'Изображение №5')
    price = models.IntegerField(verbose_name = 'Цена')

    class Meta():
        verbose_name = "Каталог"

    def __str__(self):
        return self.name

#class Review(models.Model):
    #name = models.CharField(max_length=20, verbose_name = 'Имя')
    #message = models.TextField(verbose_name = 'Сообщение')


    #class Meta():
        #verbose_name = "Отзывы"

class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name='Имя')
    text = models.TextField(verbose_name='Комментарий')



    def __str__(self):
        return self.title

#class Images(models.Model):
    #mags = models.ForeignKey('Mag', on_delete=models.CASCADE)
    #images = models.ImageField(upload_to='images')

class CaruselImage(models.Model):
    caruselImagesOne = models.ImageField(upload_to='images', verbose_name = 'Изображение для карусели №1')
    caruselImagesTwo = models.ImageField(upload_to='images', verbose_name = 'Изображение для карусели №2')
    caruselImageThree = models.ImageField(upload_to='images', verbose_name = 'Изображение для карусели №3')

    class Meta():
        verbose_name = 'Изображения для карусели'
