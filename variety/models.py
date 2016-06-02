from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Variety(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    latin = models.CharField(max_length=250, blank=True, null=True)
    category = TreeForeignKey('Category')
    is_stock = models.BooleanField(default=True)

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name_plural = "varieties"


@python_2_unicode_compatible
class Category(MPTTModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250, unique=True)
    url = models.SlugField(max_length=250)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    level = models.PositiveIntegerField(default=0)
    lft = models.PositiveIntegerField(default=0)
    rght = models.PositiveIntegerField(default=0)
    tree_id = models.PositiveIntegerField(default=0)

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"

    class MPTTMeta:
        order_insertion_by = ['title']

@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    
    country = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    adrdess = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.PositiveSmallIntegerField(blank=True, null=True)
    
    def __str__ (self):
        return self.name+" "+self.first_name
    
    class Meta:
        verbose_name_plural = "profile"

@python_2_unicode_compatible
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='one')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.user+" "+self.friend
    
    class Meta:
        verbose_name_plural = "follow"

@python_2_unicode_compatible
class Group(models.Model):
    title = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    adress = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__ (self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"

@python_2_unicode_compatible
class User_group(models.Model):
    #Passer par un belong
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    rank = models.IntegerField()
    
    def __str__ (self):
        return self.user+" "+self.group

    class Meta:
        verbose_name_plural = "user_group"

@python_2_unicode_compatible
class Desire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    qtt = models.IntegerField()
    message = models.CharField(max_length=5000, unique=True)
    
    def __str__ (self):
        return self.user+" "+self.variety
    
    class Meta:
        verbose_name_plural = "desire"

@python_2_unicode_compatible
class Catalog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    qtt = models.IntegerField()
    shares_qtt = models.IntegerField()
    
    def __str__ (self):
        return self.user+" "+self.variety
    
    class Meta:
        verbose_name_plural = "catalog"

@python_2_unicode_compatible
class Desire_group(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    qtt = models.IntegerField()
    message = models.CharField(max_length=5000)
    
    def __str__ (self):
        return self.group+" "+self.variety
    
    class Meta:
        verbose_name_plural = "request_group"

@python_2_unicode_compatible
class Catalog_group(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    qtt = models.IntegerField()
    shares_qtt = models.IntegerField()
    
    def __str__ (self):
        return self.group+" "+self.variety
    
    class Meta:
        verbose_name_plural = "catalog_group"