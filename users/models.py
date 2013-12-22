from mongoengine import *

from mongoengine.django.auth import User
# Create your models here.

class UserAccount(User):
    SEX_GENDER = (('M', 'Male'), ('F', 'Female'))
    sex = CharField(max_length=1, choices=SEX_GENDER, required=True)
    birth_date = DateTimeField(required=True)
    region = StringField(max_length=200, required=True)
    token = StringField(max_length=100)

    #USERNAME_FIELD = u'email'
    #def __init__(self):
    #    super(User, self).__init__()
