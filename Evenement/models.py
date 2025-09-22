from django.db import models
from Person.models import Person
from django.utils.timezone import datetime
# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images/',blank=True)
    list_category=(
        ('M','Musique'),('S','Sport'),('C','Cinema')
    )
    category=models.CharField(max_length=255,choices=list_category)
    state=models.BooleanField(default=False)
    nb_participant=models.IntegerField(default=0)
    evt_date=models.DateField()
    creation_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    organizer=models.ForeignKey(
        Person,
        # on_delete=models.CASCADE
        on_delete=models.SET_NULL,
        null=True,
        related_name="Person"
    )
    participation=models.ManyToManyField(
        Person,
        related_name="participations" ,
        #through="participation_event"       
    )
    class Meta:
        constraints=[models.CheckConstraint(
            check=models.Q(evt_date__gte=datetime.now()),
            name="Please check the event date!")
        ]
        ordering=('title','evt_date')
class participation_event(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date=models.DateField(auto_now=True)
    class Meta:
        unique_together=('person','event')