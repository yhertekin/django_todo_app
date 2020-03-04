from django.db import models
from django import forms
from django.forms import ModelForm
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'