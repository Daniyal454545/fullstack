from django.db import models


class Person(models.Model):
    name = models.CharField('имя', max_length=100) #имя
    last_name = models.CharField('фамилия', max_length=100) #фамилия
    age = models.CharField('возраст', max_length=100) #возраст
    height = models.CharField('выстота', max_length=10, blank=True) #выстота
    weight = models.CharField('вес', max_length=100, blank=True) #вес
    blood_type = models.CharField('группа крови', max_length=10, blank=True) #группа крови
    allergy = models.CharField('аллергия на что либо', max_length=100, blank=True) #аллергия на что либо
    symptoms = models.CharField('симптомы', max_length=500, blank=True) #симптомы
    disability = models.CharField('инвалидность', max_length=100, blank=True) #инвалидность
    injury = models.CharField('травма', max_length=100, blank=True)
    illness = models.CharField('болезнь', max_length=100) #болезнь
    person_images = models.ImageField('фотография', upload_to='person_image/', blank=True)


    def __str__(self):
        return f'{self.name} - {self.last_name}'