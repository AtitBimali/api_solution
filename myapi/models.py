
from django.db import models
#Importing validators:
from .validators import validate_file_size,validate_file_extension, validate_payment,validate_length

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=150,null=True)
    content = models.FileField(validators=[validate_file_size,validate_file_extension])
    uploader = models.CharField(max_length=100,null=True)
    length = models.PositiveBigIntegerField(null=True,validators=[validate_length])
    payment = models.FloatField(validators=[validate_payment],null=True)
    
    
    def __str__(self):
        return self.title