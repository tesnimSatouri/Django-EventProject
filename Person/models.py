from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.
def VerifLength(value):
    if len(str(value))!=8:
        raise ValidationError("Your CIN must have 8 integers")
    return value
def verif_email(value):
    if(str(value).endswith("@esprit.tn")==False):
        raise ValidationError("Your email {v} must ends with @esprit.tn",
                              params={'v':value})
    return value
class Person(AbstractUser):
    # cin=models.IntegerField(primary_key=True,validators=[MinLengthValidator(8),MaxLengthValidator(8)])
    cin=models.IntegerField(primary_key=True,validators=[VerifLength])
    email=models.EmailField(unique=True, validators=[verif_email] )
    def __str__(self):
        return f"L'email est: {self.email} et le uusername est {self.username}"
    # return self.email + self.username

#l str kima toString() f Java tkhai l objet y3awd y3tik string