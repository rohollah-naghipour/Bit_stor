from django.db import models

from users.models import User


class Package(models.Model):
    title = models.CharField(('title'), max_length=50)
    sku = models.CharField(('stock keeping unit'), max_length=20, db_index=True)
    description = models.TextField(('description'), blank=True)
    avatar = models.ImageField(('avatar'), blank=True, upload_to='packages/')
    is_enable = models.BooleanField(('is enable'), default=True)
    price = models.PositiveIntegerField(('price'))
    duration = models.DurationField(('duration'), blank=True, null=True)
    # gateways = models.ManyToManyField('payments.Gateway')
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(('updated time'), auto_now=True)

    class Meta:
        db_table = 'packages'
        verbose_name = ('Package')
        verbose_name_plural = ('Packages')

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey('users.User', related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='%(class)s', on_delete=models.CASCADE)
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    expire_time = models.DateTimeField(('expire time'), blank=True, null=True)

    class Meta:
        db_table = 'subscriptions'
        verbose_name = ('Subscription')
        verbose_name_plural = ('Subscriptions')



