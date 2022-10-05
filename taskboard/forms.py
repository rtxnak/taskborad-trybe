from django import forms
from .models import Board, Task


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['title']


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['board_id',
                  'title',
                  'description',
                  'status']


class StatusTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['id',
                  'status']
