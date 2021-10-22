from django.db import models


class Receipt(models.Model):
    image:models.ImageField = models.ImageField(upload_to='images',blank=False,null=True)
    name:models.CharField = models.CharField(max_length=50)
    description:models.TextField = models.TextField()
    created_at:models.DateTimeField = models.DateTimeField(auto_created=True,blank=False)
    is_moderated:models.BooleanField = models.BooleanField(default=False)

    def __str__(self):
        return self.name
