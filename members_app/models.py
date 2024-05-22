from django.db import models

class UserInput(models.Model):
    input_text = models.CharField(max_length=255)
