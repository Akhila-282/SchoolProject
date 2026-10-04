from django import forms

class admission(forms.Form):
    id=forms.IntegerField()
    stu_name=forms.CharField()
    stu_father=forms.CharField()
    joindate=forms.CharField()
    stu_class=forms.CharField()
    fees=forms.IntegerField()