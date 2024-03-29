import uuid
from django.db import models 
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.validators import UnicodeUsernameValidator 
from django.contrib.auth.models import PermissionsMixin,AbstractUser,UserManager

class MyUserManager(UserManager): 
    def _create_user(self, username, email, password, **extra_fields): 
        """ 
        Create and save a user with the given username, email, and password. 
        """ 
        if not username: 
            raise ValueError('The given username must be set')

        if not extra_fields.get("phone_number"): 
            raise ValueError('The given phone number must be set')
         
        email = self.normalize_email(email) 
        username= self.model.normalize_username(username) 
        user= self.model(username=username,email=email,**extra_fields) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user 

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False) 
        extra_fields.setdefault('is_superuser', False) 
        return self._create_user(username, email, password, **extra_fields) 

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 

        if extra_fields.get('is_staff') is not True: 
            raise ValueError('Superuser must have is_staff=True.') 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True.') 
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser,PermissionsMixin):
    """ 
    An abstract base class implementing a fully featured User model with 
    admin-compliant permissions. 
    Username and password are required. Other fields are optional. 
    """ 
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username_validator = UnicodeUsernameValidator() 
    username = models.CharField( 
        _('username'), 
        max_length=150, 
        unique=True, 
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'), 
        validators=[username_validator], 
        error_messages={ 
            'unique': _("A user with that username already exists."), 
        }, 
    ) 
    first_name = models.CharField(_('first name'),max_length=150,blank=False)
    last_name = models.CharField(_('last name'),max_length=150,blank=False)
    email = models.EmailField(_('email address'),blank=True,null=True)
    phone_number= models.CharField(_('phone number'),max_length=13,blank=False,unique=True)
    is_staff = models.BooleanField( 
        _('staff status'), 
        default=False, 
        help_text=_('Designates whether the user can log into this admin site.'), 
    ) 
    is_active = models.BooleanField( 
        _('active'), 
        default=True, 
        help_text=_( 
            'Designates whether this user should be treated as active. ' 
            'Unselect this instead of deleting accounts.' 
        ), 
    )
    sasapay_vendor = models.BooleanField( 
        _('sasapay vendor'), 
        default=False, 
        help_text=_( 
            'Designates whether this user is a sasapay vendor. ' 
        ), 
    )  
    external_vendor = models.BooleanField( 
        _('external vendor'), 
        default=False, 
        help_text=_( 
            'Designates whether this user is a external vendor. ' 
        ), 
    )  
    customer = models.BooleanField( 
        _('customer'), 
        default=False, 
        help_text=_( 
            'Designates whether this user is a customer. ' 
        ), 
    ) 
    
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now) 
    objects = MyUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "%s %s" %(self.first_name,self.last_name)