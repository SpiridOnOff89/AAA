import json
import keyword


class AttrMakerMixin:
    def __init__(self, mapping: dict):
        for attr in mapping:
            if attr != 'price':
                setattr(self,
                        attr + '_' if keyword.iskeyword(attr) else attr,
                        mapping[attr])
        if 'location' in self.__dict__:
            self.location = AttrMakerMixin(self.location)


class ColorizeMixin:

    repr_color_code = 33

    def __repr__(self):
        message = f'{self.title} | {self.price} ₽'
        return f"\033[1;{self.repr_color_code};40m {message}  \n"


class Advert(AttrMakerMixin, ColorizeMixin):
    def __init__(self, advert: dict):
        self._advert = advert
        super().__init__(self._advert)
        super().__init__

        self._price = int(self._advert['price']) if 'price' in self._advert else 0
        if self._price < 0:
            raise ValueError('must be >= 0')
        if 'class' in self.__dict__:
            self.class_ = self.__dict__['class']

    @property
    def price(self):
        return self._price


if __name__ == '__main__':
    iphone_str = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    corgi_dict = json.loads(corgi_str)
    iphone_dict = json.loads(iphone_str)
    corgi = Advert(corgi_dict)
    iphone = Advert(iphone_dict)
    # Advert({'title': 'дырявый носок', 'price': -3})
    print(iphone.price)
    print(iphone.location.address)
    print(corgi.class_)
    print(corgi)
