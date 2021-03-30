from django.db import models
import time
import os
from uuid import uuid4

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(upload_to=('here/{}'.format(time.strftime("%Y/%m/%d"))),blank=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'here/images/{}'.format(time.strftime("%Y/%m/%d")))

    def __str__(self):
        return self.post.title