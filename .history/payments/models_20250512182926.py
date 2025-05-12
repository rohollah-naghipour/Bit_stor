from django.db import models


class Gateway(models.Model):
    title = models.CharField(('title'), max_length=50)
    description = models.TextField(('description'), blank=True)
    avatar = models.ImageField(('avatar'), blank=True, upload_to='gateways/')
    is_enable = models.BooleanField(('is enable'), default=True)
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(('updated time'), auto_now=True)

    class Meta:
        db_table = 'gateways'
        verbose_name = ('Gateway')
        verbose_name_plural = ('Gateways')


class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID, ('Void')),
        (STATUS_PAID, ('Paid')),
        (STATUS_ERROR, ('Error')),
        (STATUS_CANCELED, ('User Canceled')),
        (STATUS_REFUNDED, ('Refunded')),
    )

    STATUS_TRANSLATIONS = {
        STATUS_VOID: ('Payment could not be processed'),
        STATUS_PAID: ('Payment successful'),
        STATUS_ERROR: ('Payment has encountered an error. Our technical team will check the problem shortly'),
        STATUS_CANCELED: ('Payment canceled by user.'),
        STATUS_REFUNDED: ('This payment has been refunded'),
    }

    user = models.ForeignKey('users.User', verbose_name=('user'), related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions.Package', verbose_name=('package'), related_name='%(class)s', on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway, verbose_name=('gateway'), related_name='%(class)s', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(('price'), default=0)
    status = models.PositiveSmallIntegerField(('status'), choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid = models.CharField(('device uuid'), max_length=40, blank=True)
    token = models.CharField(max_length = 250)
    phone_number = models.BigIntegerField(('phone number'), db_index=True)
    consumed_code = models.PositiveIntegerField(('consumed reference code'), null=True, db_index=True)
    created_time = models.DateTimeField(('creation time'), auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(('modification time'), auto_now=True)

    class Meta:
        db_table = 'payments'
        verbose_name = ('Payment')
        verbose_name_plural = ('Payments')
