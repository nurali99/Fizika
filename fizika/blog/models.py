from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
# Create your models here.
class Mexanika(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    rasm=models.ImageField(blank=True, upload_to='images/')
    time=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title 
class Molekulyar(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    rasm=models.ImageField(blank=True)
    time=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title
class Elektrostatika(models.Model):    #Elektrostatika bo'limi ucun model yasalgan faqat blog sate
    title=models.CharField(max_length=255)
    body=models.TextField()
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    rasm=models.ImageField(blank=True)
    time=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title
class Optika(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(blank=True)
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    rasm=models.ImageField(blank=True)
    time=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title
class AtomYadro(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    rasm=models.ImageField(blank=True)
    time=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title
class Muallif(models.Model):   #Mualliflarni kiritiladi
    I_F_SH=models.CharField(max_length=100)
    text=models.TextField()
    rasm=models.ImageField(blank=True)
    def __str__(self):
        return self.I_F_SH
class Kitob(models.Model):
    nomi=models.CharField(max_length=70)
    rasm=models.ImageField(blank=True)
    text=models.TextField(max_length=200)
    def __str__(self):
        return self.nomi
class KunYangiliklar(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    rasm=models.ImageField(blank=True)
    time=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title   
    # def get_absolute_url(self):
    #     return reverse('kunyangiliklar_detail', args=[str(self.id)])
