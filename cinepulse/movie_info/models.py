from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'),
                                                          ('F', 'Female'),
                                                          ('O', 'Others')])
    date_of_birth = models.DateField()

    def movie_count(self):
        return self.movie_set.count()

class Actor(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'),
                                                      ('F', 'Female'),
                                                      ('O', 'Others')])
    date_of_birth = models.DateField()
    def movie_count(self):
        return self.movie_set.count()

class Movie(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    runtime = models.IntegerField()
    certificate = models.CharField(max_length=3, choices=[('A', 'Adults Only'),
                                                          ('UA', 'Unrestricted with parental guidance'),
                                                          ('U', 'Unrestricted'),
                                                          ('S', 'Specialized audiences')])
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor)