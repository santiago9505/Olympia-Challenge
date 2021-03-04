from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Producto(models.Model):
    Name=models.CharField(max_length=50)

    price=models.CharField(max_length=10)

    description=models.TextField()

    stok=models.CharField(max_length=10)

    img_url=models.ImageField(upload_to='./productos/images',)

    product_choices=[
        ('Moda','Productos de Moda'),
        ('Limpieza', 'Productos de Limpieza'),
        ('Manufactura','Productos de Manufactura')
    ]
    tag_use=models.CharField(choices=product_choices, max_length=50)
    
    

    def __str__(self):
        return self.Name


class Comentario(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, related_name='coment', on_delete=models.CASCADE)
    texto=models.CharField(max_length=300)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
