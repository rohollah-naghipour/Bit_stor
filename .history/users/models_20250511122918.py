import random
from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager, send_mail

class UserManager(BaseUserManager):
    def create_user(self, username, email, phone_number=None,
                    password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')

        email = self.normalize_email(email) if email else None
        user = self.model(username=username,email=email,phone_number=phone_number,**extra_fields)
        #user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email=None, phone_number=None,
                         password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, phone_number, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=32, unique=True,
                                help_text=(
                                    'Required. 30 characters or fewer starting with a letter. Letters, digits and underscore only.'),
                                validators=[
                                    validators.RegexValidator(r'^[a-zA-Z][a-zA-Z0-9_\.]+$',
                                                              ('Enter a valid username starting with a-z. '
                                                                'This value may contain only letters, numbers '
                                                                'and underscore characters.'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': ("A user with that username already exists."),
                                }
                                )
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    email = models.EmailField(('email address'), unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_staff = models.BooleanField(('staff status'), default=False,
                                   help_text=('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(('active'), default=True,
                                    help_text=('Designates whether this user should be treated as active. '
                                                'Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    last_seen = models.DateTimeField(('last seen date'), null=True)

    objects = UserManager()

  
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = 'users'
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_loggedin_user(self):
        return self.phone_number is not None or self.email is not None

    def save(self, *args, **kwargs):
        if self.email is not None and self.email.strip() == '':
            self.email = None
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(('nick_name'), max_length=150, blank=True)
    avatar = models.ImageField(('avatar'), blank=True)
    birthday = models.DateField(('birthday'), null=True, blank=True)
    gender = models.BooleanField(('gender'), null=False,blank=False)
    province = models.ForeignKey(verbose_name=('province'), to='Province', null=True, on_delete=models.SET_NULL)
                                      

    class Meta:
        db_table = 'user_profiles'
        verbose_name = ('profile')
        verbose_name_plural = ('profiles')

    @property
    def get_first_name(self):
        return self.user.first_name

    @property
    def get_last_name(self):
        return self.user.last_name

    def get_nickname(self):
        return self.nick_name if self.nick_name else self.user.username


class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = (
        (WEB, 'web'),
        (IOS, 'ios'),
        (ANDROID, 'android'),
    )

    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(('Device UUID'), null=True)
    # notify_token = models.CharField(
    #     _('Notification Token'), max_length=200, blank=True,
    #     validators=[validators.RegexValidator(r'([a-z]|[A-z]|[0-9])\w+',
    #                                           _('Notify token is not valid'), 'invalid')]
    # )
    last_login = models.DateTimeField(('last login date'), null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=WEB)
    device_os = models.CharField(('device os'), max_length=20, blank=True)
    device_model = models.CharField(('device model'), max_length=50, blank=True)
    app_version = models.CharField(('app version'), max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_devices'
        verbose_name = ('device')
        verbose_name_plural = ('devices')
        unique_together = ('user', 'device_uuid')


class Province(models.Model):
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
