from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Difficulty(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Easy, Medium, Hard
    value = models.PositiveSmallIntegerField(unique=True)  # 1, 2, 3

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True, default='Admin')
    
    # Store numeric value in DB, join to Difficulty
    difficulty = models.ForeignKey(
        Difficulty, 
        on_delete=models.CASCADE, 
        related_name='items',
        to_field='value',  # join on numeric value
    )
    
    row = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        help_text="Enter a number between 1 and 20"
    )
    column = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        help_text="Enter a number between 1 and 20"
    )
    grid = models.JSONField(default=list)  # Store the grid as a list of lists
    solution = models.JSONField(default=dict)  # Store the solution as a dictionary
    choices = models.JSONField(default=list)  # Store the choices as a list

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def difficulty_name(self):
        # Returns the text for API, not stored in DB
        return self.difficulty.name if self.difficulty else None
    
class puzzleLevel(models.Model):
        difficulty = models.ForeignKey(
        Difficulty, 
        on_delete=models.CASCADE, 
        related_name='puzzle_levels',
        to_field='value',  # join on numeric value
        )
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        created_by = models.IntegerField(null=True, blank=True)
        updated_by = models.IntegerField(null=True, blank=True)

        def __str__(self):
             return f"Level - {self.difficulty.name}"

        