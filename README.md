# drf-Function-display
Django-Rest-Framework

---

**这个项目是展示如何使用Django-Rest-Framework框架**

---

### 在settings.py文件中设置restframework和添加app


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api'
]
```
---

### 设置模型

```python
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
```

**然后迁移数据库**

```python
python manage.py makemigrations
python manage.py migrate
```

---

### 设置路由

**主路由**

```python
from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/',include(('api.urls','api/'),namespace='api/')),
]
```

**app下的路由，该文件是新建的**

```python
from django.urls import re_path
from api import views

urlpatterns = [

    re_path(r'^index/$',views.Index.as_view(),name='index/'),

]
```

---

### 序列化与反序列化

**该文件是新建的，在app目录下**


```python
from rest_framework import serializers
from api import models
from rest_framework.validators import UniqueValidator

class MasterSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Master
        fields = '__all__'

    # 增加数据
    def create(self, validated_data):
        models.Master(**validated_data).save()
        return validated_data

    # 更新数据
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.schoolname = validated_data.get('schoolname',instance.schoolname)
        instance.city = validated_data.get('city',instance.city)
        instance.phone = validated_data.get('phone',instance.phone)
        instance.save()
        return instance

class GradeSerializers(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=64)
    designator = serializers.CharField(max_length=64)
    fount = serializers.DateTimeField()
    master_name = serializers.CharField(read_only=True,source='master.name')
    masterid = serializers.CharField(read_only=True,source='master.id')
    master = serializers.PrimaryKeyRelatedField(many=False,read_only=False,queryset=models.Master.objects.all())

    # 增加数据
    def create(self, validated_data):
        models.Grade(**validated_data).save()
        return validated_data

    # 更新数据
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.designator = validated_data.get('name',instance.name)
```

**参数说明**

|字段|字段构造方式|
| ------------ | ------------ |
|BooleanField|BooleanField()|
|NullBooleanField|NullBooleanField()|
|CharField|CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)|
|EmailField|EmailField(max_length=None, min_length=None, allow_blank=False)|
|RegexField|RegexField(regex, max_length=None, min_length=None, allow_blank=False)|
|SlugField|SlugField(maxlength=50, min_length=None, allow_blank=False) 正则字段，验证正则模式 [a-zA-Z0-9-]+|
|URLField|URLField(max_length=200, min_length=None, allow_blank=False)|
|UUIDField|UUIDField(format=‘hex_verbose’)|
|IPAddressField|IPAddressField(protocol=‘both’, unpack_ipv4=False, **options)|
|IntegerField|IntegerField(max_value=None, min_value=None)|
|FloatField|FloatField(max_value=None, min_value=None)|
|DecimalField|DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None)max_digits: 最多位数decimal_palces: 小数点位置|
|DateField|DateField(format=api_settings.DATE_FORMAT, input_formats=None)|
|TimeField|TimeField(format=api_settings.TIME_FORMAT, input_formats=None)|
|DurationField|DurationField()|
|ChoiceField|ChoiceField(choices)choices与Django的用法相同|
|MultipleChoiceField|MultipleChoiceField(choices)|
|FileField|FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)|
|ImageField|ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)|
|ListField|ListField(child=, min_length=None, max_length=None)|
|DictField|DictField(child=)|

---
