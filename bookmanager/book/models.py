from django.db import models

# Create your models here.
"""
1. 我们的模型类 需要继承自 models.Model
2. 没有指定主键时, 迁移创建数据表的时候会自动为我们添加一个主键 -- id
3. 字段
    字段名 = models.类型(选项)
    字段名

"""


class BookInfo(models.Model):
    # 会自动创建一个 id 字段
    name = models.CharField(max_length=50)

    def __str__(self):
        result = f'{self.id}\t {self.name}'
        return result

class PeopleInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.BooleanField()
    # 设置外键约束外键约束
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)