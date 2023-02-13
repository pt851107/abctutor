from django import forms

CAMP_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CAMP_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False,widget=forms.HiddenInput)