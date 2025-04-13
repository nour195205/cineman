from django import forms
from .models import Parties

class TicketBookingForm(forms.Form):
    number_of_tickets = forms.IntegerField(min_value=1, max_value=50, label='عدد التذاكر')

    def __init__(self, *args, **kwargs):
        self.party = kwargs.pop('party', None)  # للحصول على الحفلة المرتبطة
        super().__init__(*args, **kwargs)

    def clean_number_of_tickets(self):
        tickets = self.cleaned_data.get('number_of_tickets')
        
        # تحقق من وجود party والتأكد أنه مش فارغ
        if self.party is None:
            raise forms.ValidationError("Party is not available.")
        
        if tickets > self.party.seats:
            raise forms.ValidationError(f"Only {self.party.seats} seats available.")
        
        return tickets

