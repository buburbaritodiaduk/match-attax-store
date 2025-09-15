import uuid
from django.db import models

"""
class News(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    news_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
"""

class Product(models.Model):
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

    name = models.CharField(max_length=100)      
    price = models.FloatField()               
    description = models.TextField()             
    thumbnail = models.URLField()                
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='base')
    is_featured = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
