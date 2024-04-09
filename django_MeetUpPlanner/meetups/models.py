from django.db import models

class Organizer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__ (self):
        return f'{self.name} {self.address}'

class MeetUp(models.Model):
    title = models.CharField(max_length=200)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, through='Registration',  blank=True, null=True)


    def __str__(self):
        return f'{self.title}'

class Registration(models.Model):
    meetup = models.ForeignKey(MeetUp, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
