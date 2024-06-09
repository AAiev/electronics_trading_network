from django.db import models


NULLABLE = {'blank': True, 'null': True}


class TradingLink(models.Model):
    """ Модель торгового звена """

    TYPE_CHOICES = [
        ('FA', 'Завод'),
        ('RN', 'Розничная сеть'),
        ('IE', 'Индивидуальный предприниматель')
    ]

    name = models.CharField(max_length=150, verbose_name='название')
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='тип звена сети')
    level = models.SmallIntegerField(verbose_name='уровень в иерархии поставок')

    email = models.EmailField(max_length=100, verbose_name='email', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=20, verbose_name='номер дома', **NULLABLE)

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    arrear = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                 verbose_name='задолженность перед поставщиком', **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.type} {self.name}'

    class Meta:
        verbose_name = 'торговое звено'
        verbose_name_plural = 'торговые звенья'


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=200, verbose_name='название')
    model = models.CharField(max_length=200, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    trading_link = models.ForeignKey('TradingLink', on_delete=models.CASCADE, verbose_name='торговое звено')

    def __str__(self) -> str:
        return f'{self.name}. {self.model}. ({self.trading_link})'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
