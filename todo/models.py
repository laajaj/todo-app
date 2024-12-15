
from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Priority(models.Model):
    level = models.CharField(max_length=50)  # Par exemple, "Haute", "Moyenne", "Basse"
    
    def __str__(self):
        return self.level


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Relation un-à-plusieurs
    projects = models.ManyToManyField(Project, related_name='tasks', null=True, blank=True)  # Relation plusieurs-à-plusieurs
    priority = models.OneToOneField(Priority, on_delete=models.SET_NULL, null=True, blank=True)  # Relation un-à-un

    def __str__(self):
        return self.title