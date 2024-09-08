from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='product_images/', default="media/product_images/제목_없는_아트워크_82.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='product_like')

    def __str__(self):
        return self.title
