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
