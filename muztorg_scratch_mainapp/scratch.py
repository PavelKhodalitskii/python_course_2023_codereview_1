from django.template.defaultfilters import slugify

from .models import Product, ProductDetails, ProductPhotos, Photo
from config.settings import MEDIA_ROOT

from requests import get, post
from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Scratch:
    __instance = None
    base="https://www.muztorg.ru"

    urls = {
        "EG": "https://www.muztorg.ru/category/elektrogitary?page=",
        "AG": "https://www.muztorg.ru/category/akusticheskie-gitary?page=",
        "GA": "https://www.muztorg.ru/category/usiliteli-dlya-gitar?page=",
        "AS": "https://www.muztorg.ru/category/akusticheskie-sistemy-2585?pagse=",
        "DP": "https://www.muztorg.ru/category/czifrovye-pianino?page=",
        "Sn": "https://www.muztorg.ru/category/sintezatory?page=",
        "Mf": "https://www.muztorg.ru/category/mikrofony?page=",
        "RS": "https://www.muztorg.ru/category/radiosistemy?page="
    }

    def __init__(self):
        self.__instance = self
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def get_photos(self, card_soup, product_detail, product):
        photos_divs = card_soup.find_all("div", class_="swiper-slide")
        product_photos = ProductPhotos(product_detail=product_detail)
        product_photos.save()
        for i in range(len(photos_divs)):
            try:
                photo_link = BeautifulSoup(f'{photos_divs[i].find("img")}', "lxml").img['data-src']
                image = get(photo_link)
                save_path = "media/photos/" + slugify(product_detail.product.name) + str(i) + ".jpg"
                image_path = "photos/" + slugify(product_detail.product.name) + str(i) + ".jpg"
                src = open(save_path, "wb")
                src.write(image.content)
                src.close()
                photo = Photo(photo=image_path)
                photo.product_photos_id = product_photos.id
                photo.save()

                if i == 0:
                    print("IMAGE PATH: ", image_path, "SAVE PATH: ", save_path)
                    # Product.objects.get(id=product_detail.product.id).update(photo=image_path)
                    product.image = image_path
                    # product.photo_str = image_path
                    product.save()
            except KeyError:
                break
            except TypeError:
                continue
        product_photos.save()
        product_detail.photos = product_photos
        product_detail.save()

    def get_product_details(self, link, product):
        card_response = get(link)
        card_soup = BeautifulSoup(card_response.text, "lxml")
        try:
            raiting = card_soup.find("div", class_="rating").find("span", class_="rating__value").text
        except:
            raise RuntimeError("Что-то пошло не так")
        # product_info_div = card_soup.find("div", class_="container").find("div", class_="product-info ")
        product_info_div = card_soup.find("div", class_="product-page")
        description = product_info_div.find("div", class_="_description").text
        # garanty = product_info_div.find(".product-info__i", first=True).find("div", first=True).text
        # print(garanty)

        product_details = ProductDetails(product=product,
                                        raiting=raiting,
                                        about=description)
        product_details.save()

        self.get_photos(card_soup, product_details, product)
        # try:
        #     self.get_photos(card_soup, product_details)
        # except:
        #     pass

    def get_data_by_cat(self, cat, page):
        #Получаем url категории, формируем url страницы и получаем суп
        url = self.urls[cat]
        page_url = url + str(page)
        response = get(page_url)
        soup = BeautifulSoup(response.text, "lxml")
        
        #Получаем все карточки товаров
        product_cards = soup.find_all('section', class_="product-thumbnail")

        for card in product_cards:
            #Если не можем получить цену - запарсили что-то не то
            try:
                price = BeautifulSoup(str(card), 'lxml').section['data-price']
            except:
                continue

            name_div = card.find("div", class_="title")
            link_append = BeautifulSoup(f"{name_div.find('a')}", 'lxml').a['href']
            name = name_div.find('a').text
            link = self.base + link_append
            
            try:
                #Пробуем получить продукт по имени
                product = Product.objects.get(name=name)
                print("НАШЕЛ ТОВАР: ", product.name)
                #Обновляем детали товара
                # self.get_product_details(link, product)
            except:
                #Если такого нет создаем
                cat_index = Product.ProductType.values.index(cat)
                print(cat_index)
                print(Product.ProductType.labels[cat_index])
                product = Product(name=name,
                            slug=slugify(name),
                            price=price,
                            link=link,
                            category=Product.ProductType.choices[cat_index][0])
                product.save()
                print("СОЗДАЛ ТОВАР: ", name, price, link, sep=" ")

                # Получаем детали товара
                try:
                    self.get_product_details(link, product)
                except(RuntimeError):
                    continue