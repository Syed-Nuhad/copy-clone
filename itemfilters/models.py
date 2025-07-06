from django.db import models
from django.conf import settings

class Filter(models.Model):
    """
    Stores user-defined filters for auto-buy/autocop functionality.
    """
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('games', 'Games'),
        ('clothing', 'Clothing'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords")
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    autocop_enabled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} ({self.keywords})"
