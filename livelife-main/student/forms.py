from django import forms

class RescueRequestForm(forms.Form):
  category = forms.ChoiceField(choices=[('', 'Select Category'), ('disabled', 'Disabled'), ('wounded', 'Wounded'), ('orphan', 'Orphan')], required=True)
  location = forms.CharField(required=True)
  details = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=True)

  def __str__(self):
    return self.cleaned_data.get('category') + ' - ' + self.cleaned_data.get('location')

