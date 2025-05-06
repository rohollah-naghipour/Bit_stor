from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(('title'), max_length=50)
    description = models.TextField(('description'), blank=True)
    avatar = models.ImageField(('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(('is enable'), default=True)
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(('title'), max_length=50)
    description = models.TextField(('description'), blank=True)
    avatar = models.ImageField(('avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=('categories'), blank=True)
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = ('product')
        verbose_name_plural = ('products')

    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, ('audio')),
        (FILE_VIDEO, ('video')),
        (FILE_PDF, ('pdf'))
    )

    product = models.ForeignKey('Product', verbose_name=('product'), related_name='files', on_delete=models.CASCADE)
    title = models.CharField(('title'), max_length=50)
    file_type = models.PositiveSmallIntegerField(('file type'), choices=FILE_TYPES)
    file = models.FileField(('file'), upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(('is enable'), default=True)
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = ('file')
        verbose_name_plural = ('files')

    def __str__(self):
        return self.title
