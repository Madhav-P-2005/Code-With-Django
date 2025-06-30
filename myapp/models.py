from django.db import models

# Create your models here.

'''

⭐) Defining the Model :-  The model defines the structure of your database table. In this case, the Item model has a single field name, which is a CharField with a maximum length of 200 characters.


⭐) When you create or modify models, you must run the following commands to create the corresponding database table :- 

   python manage.py makemigrations :-  Generates a migration file based on your model.
   python manage.py migrate   :-  Applies those changes to the actual database.


'''
class Song(models.Model):

    title = models.CharField(max_length=200)

    artist = models.CharField(max_length=200)


    def __str__(self):

        # return f"{self.title} - {self.artist}"        # Output :-  Song 1 - Artist 1

        return self.title      
    
    '''

    Output :- 

    {
        "title": "Lambi Judai",
        "artist": "Krishnakumar Kunnath"
    }
    
    '''



'''

⭐) Integrating SQLite3 with Django ORM and Creating a Model

'''


class ToDo(models.Model):

    task = models.CharField(max_length=200)

    def __str__(self):
        return self.task