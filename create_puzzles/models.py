from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
User =get_user_model()

class MathPuzzle(models.Model):
    name = models.TextField(max_length=20,default="")
    title =models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='authored_puzzles')
    row = models.SmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)])
    cols = models.SmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)])
    DIFFICULTY_CHOICES =[
        ('easy','easy'),
        ('medium','medium'),
        ('hard','hard')
    ]
    difficulty = models.CharField(max_length=15,choices=DIFFICULTY_CHOICES,default='easy')
    grid = models.JSONField(blank=True,null=True,default=list)
    solution = models.JSONField(blank=True,null=True,default=dict)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null= True,blank = True,related_name="created_puzzles" )
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='updated_puzzless')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class meta:
        db_table ='math_puzzless'
        ordering =['-id']
        
        def __str__(self):
            return self.title