#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文，我们使用了TextField
    body = models.TextField()
    #文章的创建时间
    created_time = models.DateTimeField()
    #文章最后一次修改的时间
    modified_time = models.DateTimeField()
    #文章摘要，指定CharField的blank=True参数值后就可以允许空值
    excerpt = models.CharField(max_length=200,blank=True)
    #一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey
    category = models.ForeignKey(Category)
    #一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField
    tags = models.ManyToManyField(Tag,blank=True)
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title

    #自定义get_absolute_url方法
    #记得从django.urls中导入reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    class Meta:
        ordering = ['-created_time']