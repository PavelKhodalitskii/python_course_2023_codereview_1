from django.db import models
from django.urls import reverse

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
        BestDeals = 'Bd', 'BestDeals'
        NoCategory = 'NC', 'NoCategory'
    name = models.CharField(max_length=75, verbose_name="Имя товара")
    slug = models.SlugField(max_length=250)
    link = models.URLField(max_length=250)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото", blank=True)
    category = models.CharField(max_length=2, choices=ProductType.choices, default=ProductType.NoCategory)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug':self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="Детали", related_name="details",null=True)
    about = models.TextField()
    raiting = models.FloatField()


class ProductPhotos(models.Model):
    product_detail = models.OneToOneField(ProductDetails, on_delete=models.CASCADE, verbose_name="Фотографии", related_name="detail_photos", null=True)

class Photo(models.Model):
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото", blank=True)
    product_photos = models.ForeignKey(ProductPhotos, on_delete=models.CASCADE, verbose_name="Фото", related_name="photos", null=True)