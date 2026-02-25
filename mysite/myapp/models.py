from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6 ,decimal_places=2)
    pub_date=models.DateField()
    description=models.TextField()
    cover_image=models.ImageField(upload_to='book-covers/', null=True,blank=True)

    def __str__(self):
       return f"{self.title}-{self.author}"

