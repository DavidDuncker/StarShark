from datetime import timezone, datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SiteUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.account_created = datetime.now()
        user.set_password(password)
        user.save()
        return user


class SiteUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=True)
    password = models.CharField(_('password'), max_length=128)
    birthdate = models.DateField(verbose_name="Birth Date", null=True)
    email = models.CharField(max_length=40, unique=False, null=True)
    name = models.CharField(max_length=50, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
    objects = SiteUserManager()
    reactions = {}
    reaction_types = ['like', 'dislike', 'happy', 'sad', 'mad', 'dismiss']
    for reaction_type in reaction_types:
        #reactions[reaction_type] = models.ManyToManyField()
        pass

    profile_pic = ""
    multimedia = ""


class Submission(models.Model):
    author = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True)
    parents = models.ManyToManyField('self')

    class LegalStatus(models.TextChoices):
        ALL_GOOD = 'AG', ("No legal issues with this post")
        DMCA = 'DM', ("Copyright issues")
        ILLEGAL_SPEECH = 'IS', ("Illegal speech")

    legal_status = models.CharField(max_length=2, choices=LegalStatus.choices, default=LegalStatus.ALL_GOOD)
    expanded_legal_status = models.CharField(max_length=50)


class Emoji(Submission):
    class Types(models.TextChoices):
        LIKE = 'L', ('Like')
        DISLIKE = 'D', ("Dislike")
        HAPPY = 'H', ("Happy")
        SAD = 'S', ("Sad")
        MAD = "M", ("Mad")
        DISMISS = "X", ("Dismiss as inappropriate")

    type = models.CharField(max_length=1, choices=Types.choices)

    @classmethod
    def create(cls, inputted_type):
        emoji = cls(type = inputted_type)
        return emoji


class Text(Submission):
    full_text = models.CharField(max_length=10000, null=True)
    length = models.IntegerField(null=False)

    class Types(models.TextChoices):
        SHORT = 'S', ('Short text, <100 characters')
        MEDIUM = 'M', ("Medium text, >100 & <600 characters")
        LONG = 'L', ("Long text, >600 characters")

    type = models.CharField(max_length=1, choices=Types.choices)

    @classmethod
    def create(cls, input_text):
        text = input_text
        length = len(input_text)
        if length < 100:
            type = 'S'
        elif length >=100 & length <=600:
            type = "M"
        else:
            type = "L"
        txt = cls(text, length, type)
        return txt


class Media(Submission):
    url = models.CharField(max_length=150)
