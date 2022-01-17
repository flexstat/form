from django.db import models

class FeedBackMain(models.Model):
    domain_name = models.CharField(max_length=255, verbose_name='Имя сайта клиента',  blank = True, null = True)
    description = models.TextField(verbose_name='Описание проблемы клиента',  blank = True, null = True)
    name = models.CharField(max_length=255, verbose_name='Имя клиента',  blank = True, null = True)
    email = models.CharField(max_length=255, verbose_name='Почтовый ящик для связи с клиентом',  blank = True, null = True)
    phone = models.CharField(max_length=255, verbose_name='Телефон для связи с клиентом',  blank = True, null = True)
    inform = models.TextField(verbose_name='Откуда клиент узнал о услугах',  blank = True, null = True)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Сообщения с главной формы сайта'
        verbose_name_plural='Сообщение с главной формы сайта'   