from django.db import models

class Master(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    authid = models.CharField(max_length=18)
    schoolname = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    rename = models.CharField(max_length=64)
    register_time = models.DateTimeField()
    phone = models.CharField(max_length=256)

    class Meta:
        db_table = 'master'
        verbose_name = '老师'
        verbose_name_plural = verbose_name

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    designator = models.CharField(max_length=64)
    fount = models.DateTimeField()
    master = models.ForeignKey('Master',to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table = 'grade'
        verbose_name = '班级'
        verbose_name_plural = verbose_name