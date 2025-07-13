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
    


'''

⭐) Creating Relationships Between Models :-  1) Connecting models using Django ORM    2) Creating views to handle data interactions involving related models

'''

class Category(models.Model):
    name = models.CharField(max_length=100)


    def ___str__(self):
        return self.name
    
'''

Note :-  on_delete=models.CASCADE argument in the ForeignKey field. This argument specifies what happens when the linked category is deleted. In this case, it's set to CASCADE, which means that if a category is deleted, all tasks linked to that category will also be deleted.

'''

class To_Do(models.Model):
    task = models.CharField(max_length=200)

    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    def __str__(self):
        return self.task
    


'''

⭐) Validating Data with Django :- Adding custom validation rules to your Django models

'''

from django.core.exceptions import ValidationError


def validate_task(value):
    if len(value) < 3:
        raise ValidationError('Task must be at least 3 characters long')

class To_Do_2(models.Model):
    task = models.CharField(max_length=200 , validators=[validate_task])

    def __str__(self):
        return self.task
    


'''

⭐) Understanding Data Retrieval in Django ORM :- 

'''

class To_Do_3(models.Model):

    # Used in this topic too :- Retrieving a Single Record by ID  and also using in Updating Records by ID 
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    # title = models.CharField(max_length=255, default='Untitled')
    # description = models.TextField(default=False)
    # completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    



'''

⭐)  The preload() view is used to insert some default data into your database, only if it doesn’t already exist.

'''

class To_Do_preload_Example(models.Model):
    task_preload = models.CharField(max_length=200)
    completed_preload = models.BooleanField(default=False)
    category_preload = models.CharField(max_length=100, default='Default Value! ')
    tag_preload = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.task_preload
    


'''

⭐) Updating Records by ID :-

'''

class To_Do_Update(models.Model):

    task_update = models.CharField(max_length=200)

    completed_update  = models.BooleanField(default=False)


    def __str__(self):
        return self.task_update
    


class To_Do_Patch(models.Model):

    course = models.CharField(max_length=200)

    description = models.TextField(max_length=200)

    course_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.course
    


'''

⭐) Deleting Records by ID :-   Using To_Do_3 Model .

'''

class To_Do_3(models.Model):

    # Used in this topic too :- Retrieving a Single Record by ID  and also using in Updating Records by ID 
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    # title = models.CharField(max_length=255, default='Untitled')
    # description = models.TextField(default=False)
    # completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task