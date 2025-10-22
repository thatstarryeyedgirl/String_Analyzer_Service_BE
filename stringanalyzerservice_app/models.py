from django.db import models
from django.utils import timezone
import hashlib


# Create your models here.
class AnalyzeString(models.Model):
    length = models.IntegerField()
    is_palindrome = models.BooleanField()
    unique_characters = models.IntegerField()
    word_count = models.IntegerField()
    sha256_hash = models.CharField(max_length=100, unique=True)
    character_frequency_map = models.JSONField()
    value = models.TextField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        chars = set(self.value) # get all the values in the string
        val_lower = self.value.lower() # convert/change the string to lowercase for palindrome check
        self.sha256_hash = hashlib.sha256(self.value.encode()).hexdigest() # unique hash
        self.length = len(self.value) # count total characters
        self.is_palindrome = val_lower == val_lower[::-1] # checks if the string reads the same forwards and backwards
        self.unique_characters = len(chars) # counts distinct characters
        self.word_count = len(self.value.split()) # count words separated by spaces
        self.character_frequency_map = {c: self.value.count(c) for c in chars} # count how many times each character appears
        super().save(*args, **kwargs) # saves the object to the database

    def properties_dict(self):
        return {
            "length": self.length,
            "is_palindrome": self.is_palindrome,
            "unique_characters": self.unique_characters,
            "word_count": self.word_count,
            "sha256_hash": self.sha256_hash,
            "character_frequency_map": self.character_frequency_map
        }
        
        