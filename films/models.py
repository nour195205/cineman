from django import forms
from django.db import models
from django.utils import timezone

class Film_list(models.Model):
    id = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.FloatField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    description = models.TextField()
    category = models.CharField(max_length=100 , choices=[('Action','Action'),('Adventure','Adventure'),('Comedy','Comedy'),("Drama","Drama"),("Horror","Horror"),("Sci-Fi","Sci-Fi"),("Romance","Romance"),("Thriller","Thriller"),("Fantasy","Fantasy"),("Documentary","Documentary"),("Animation","Animation"),("Crime","Crime"),("Historical","Historical"),("Musical","Musical"),("Mystery","Mystery"),("War","War"),("Sports","Sports")])
    image = models.ImageField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Parties(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField(default=timezone.now)
    seats = models.IntegerField(default=50)
    film = models.ForeignKey(Film_list, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PartyForm(forms.ModelForm):
    film = forms.ModelChoiceField(queryset=Film_list.objects.all(), empty_label="اختر فيلم", required=True)

    class Meta:
        model = Parties
        fields = ['id','name', 'date_time', 'seats', 'film']
