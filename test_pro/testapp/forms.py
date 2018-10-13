from django import forms

class TestcaseRegisteration(forms.Form):
    testid=forms.IntegerField()
    testname=forms.CharField(max_length=100)
    testcategory=forms.CharField(max_length=30)