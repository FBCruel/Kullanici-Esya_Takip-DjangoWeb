from django.db import models

# Create your models here.
class Worker(models.Model):
    person = models.CharField(max_length=50, verbose_name="isim")
    superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.person

class Device(models.Model):
    person_id = models.ForeignKey(Worker, default=1, on_delete=models.CASCADE)
    stok = models.CharField(max_length=30, null=True, blank=True, verbose_name="Stok")
    device = models.CharField(max_length=30, null=True, blank=True, verbose_name="Cihaz")
    number = models.CharField(max_length=5, null=True, blank=True, verbose_name="Sayı")
    brand = models.CharField(max_length=50, null=True, blank=True, verbose_name="Marka")
    model = models.CharField(max_length=50, null=True, blank=True, verbose_name="Model")
    serial = models.CharField(max_length=50, null=True, blank=True, verbose_name="Seri No")
    status = models.CharField(max_length=50, null=True, blank=True, verbose_name="Durumu")
    exp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Açıklama")
    iz = models.CharField(max_length=100000000, null=True, blank=True, verbose_name="Eski Kullanıcı / Tarih")
    price = models.CharField(max_length=15, null=True, blank=True, verbose_name="Fiyat")
    take_date = models.CharField(max_length=50, null=True, blank=True, verbose_name="Alım Tarihi")
    zim_date = models.CharField(max_length=50, null=True, blank=True, verbose_name="Zimmet Tarihi")
    def __str__(self):
        return str(self.person_id)

class History(models.Model):
    who = models.CharField(max_length=50,null=True, blank=True, verbose_name="Kullanıcı Adı")
    whom = models.CharField(max_length=50, null=True, blank=True, verbose_name="Etkilenen Kişi")
    operation_type = models.CharField(max_length=30, null=True, blank=True, verbose_name="İşlem Türü")
    stok = models.CharField(max_length=30, null=True, blank=True, verbose_name="Stok")
    device = models.CharField(max_length=30, null=True, blank=True, verbose_name="Cihaz")
    operation_date = models.CharField(max_length=40,null=True, blank=True, verbose_name="Tarih")
    def __str__(self):
        return str(self.whom)


