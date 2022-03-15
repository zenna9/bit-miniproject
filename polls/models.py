from django.db import models

class Store(models.Model):
    idx = models.IntegerField(default=0)
    area = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=200)
    addr2 = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    open_info = models.CharField(max_length=100)
    close_info = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    target1_code = models.CharField(max_length=100)
    target1_etc = models.CharField(max_length=100)
    target2_code = models.CharField(max_length=100)
    target2_etc = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_etc = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    img_name = models.CharField(max_length=100)
    sup_obj = models.CharField(max_length=100)
    sup_num = models.CharField(max_length=100)
    sup_item = models.CharField(max_length=100)
    store_type = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    eatin = models.CharField(max_length=100)
    takeout = models.CharField(max_length=100)
    delivery = models.CharField(max_length=100)
    img_src = models.CharField(max_length=200)
    url = models.CharField(max_length=8192)

class Gu(models.Model):
    num = models.IntegerField(default=0)
    gu = models.CharField(max_length=100)



