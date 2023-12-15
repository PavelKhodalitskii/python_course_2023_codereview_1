from django.test import TestCase
from django.template.defaultfilters import slugify
from requests import get

from .models import Product, ProductDetails, ProductPhotos, Photo
from .scratch import Scratch
# Create your tests here.

class TestParsing(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scratch = Scratch()

    def test_muztorg_response(self):
        print("Muztorg response test: ")
        response = get("https://www.muztorg.ru/")
        self.assertEqual(response.status_code, 200)
        print("PASSED")

    def test_cats_response(self):
        print("Categories response test: ")
        for cat in self.scratch.urls.values():
            response = get(cat + "1")
            self.assertEqual(response.status_code, 200)
        print("PASSED")

    def test_get_data_by_cat(self):
        print("Get data from category page test: ")
        for cat in self.scratch.urls.keys():
            self.scratch.get_data_by_cat(cat, 1, 1)
        print("PASSED")

class TestParsingViews(TestCase):
    cat_urls = [
        '/category/EG/',
        '/category/AG/',
        '/category/GA/',
        '/category/AS/',
        '/category/DP/',
        '/category/Sn/',
        '/category/Mf/',
        '/category/RS/',
    ]

    def test_mainpage_response(self):
        print("Main page response test: ")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        print("PASSED")

    def test_prodcut_detail_view_response(self):
        print("Detail view of product page response test: ")
        cat_index = Product.ProductType.values.index("EG")
        name = "Test_product"
        product = Product(name=name,
                        slug=slugify(name),
                        price=10000,
                        link="",
                        category=Product.ProductType.choices[cat_index][0])
        product.save()
        response = self.client.get(product.get_absolute_url())
        self.assertEqual(response.status_code, 200)
            
    # def test_categorys(self):
    #     for url in self.cat_urls:
    #         response = self.client.get(url + "1")
    #         self.assertEqual(response.status_code, 200)