from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    url = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pretty_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]