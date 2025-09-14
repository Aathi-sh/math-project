from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

class Item(models.Model):
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,null=True,blank=True,default='Admin')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    row = models.SmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)],
                                   help_text="Enter a number between 1 and 20")
    column = models.SmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)],
                                        help_text="Enter a number between 1 and 20")
    grid = models.JSONField(default=list)  # Store the grid as a list of lists
    solution = models.JSONField(default=dict)  # Store the solution as a dictionary
    
    # Automatically set when the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically set every time the object is saved
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.IntegerField(null=True,blank=True)
    updated_by = models.IntegerField(null=True,blank=True)
    active = models.BooleanField(default=True)

    def _str_(self):
        return self.title