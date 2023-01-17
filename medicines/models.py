from django.db import models

from laboratories.models import Laboratory

class Medicine(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False, default=1)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, related_name='medicines')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
