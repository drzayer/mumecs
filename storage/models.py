#from django.db import models
from mongoengine import *
import datetime

# Create your models here.

#class Tag(EmbeddedDocument):
#    name = StringField(max_lengt=50, required=True)
#    values = ListField(StringField(max_length=200))

class Tag(Document):
    name = StringField(max_lengt=50, required=True)
    values = ListField(StringField(max_length=200))
    
class Storage(Document):
    name = StringField(max_lengt=100, required=True, unique=True)
    slug = SlugField(max_length=100)
    date = DateTimeField(default=datetime.datetime.now)
    date_modified = DateTimeField(default=datetime.datetime.now)
    #tags = ListField(Tag)
    tags = ListField(ReferenceField(Tag, reverse_delete_rule=mongoengine.PULL))
    
    meta = {
        'allow_inheritance': True,
        'shard_key': ('date',),
        'ordering': ['-date_modified'],
        'indexes': ['tags']
    }

class Object(Storage):
    file = FileField()

class Collection(Storage):
    objects = ListField(ReferenceField(Object, reverse_delete_rule=mongoengine.PULL))
