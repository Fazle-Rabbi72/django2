from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(Category) #akta post multiple categorir moddhe thakte pare abar akta categorier moddhe mlutiple post thekte pare
    author=models.ForeignKey(Author ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title