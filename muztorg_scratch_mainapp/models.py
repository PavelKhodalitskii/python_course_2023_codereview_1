from django.db import models

# Create your models here.
class Product(models.Model):
    class ProductType(models.TextChoices):
        ElecticGuitar = 'EG', 'ElecticGuitar'
        AcousticGuitar = 'AG', 'AcousticGuitar'
        GuitarAmplifier = 'GA', 'GuitarAmplifier'
        AcousticSystem = 'AS', 'AcousticSystem'
        DigitalPianos = 'DP', 'DigitalPianos'
        Synthesizers = 'Sn', 'Synthesizers'
        Microfones = 'Mf', 'Microfones'
        RadioSystems = 'RS', 'RadioSystems'
    name = models.CharField(max_length=75, verbose_name="Имя товара")
    slug = models.SlugField(max_length=250)
    link = models.URLField(max_length=250)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    
class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="Детали", null=True)
    about = models.TextField()
    raiting = models.FloatField()


class ProductPhotos(models.Model):
    product_detail = models.ForeignKey(ProductDetails, on_delete=models.CASCADE, verbose_name="Фотографии", null=True)