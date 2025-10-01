import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('base', 'Base Card'),
        ('man_of_the_match', 'Man of the Match'),
        ('club_legend', 'Club Legend'),
        ('rising_star', 'Rising Star'),
        ('100_club', '100 Club'),
        ('limited_edition', 'Limited Edition'),
        ('signature_style', 'Signature Style'),
        ('hat_trick_hero', 'Hat-Trick Hero'),
        ('captain', 'Captain'),
        ('trophy_card', 'Trophy Card'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)      
    price = models.FloatField()               
    description = models.TextField()             
    thumbnail = models.URLField(max_length=500)                
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='base')
    is_featured = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

