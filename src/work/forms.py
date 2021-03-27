from django import forms
from .models import Work


class WorkForm(forms.ModelForm):
    project = forms.CharField(label='Project', widget=forms.TextInput(attrs={"placeholder": "Select the project"}))
    # email = forms.EmailField()
    hours = forms.DecimalField(label='Number of hours worked', initial=8,
                               widget=forms.TextInput(attrs={"placeholder": "Select number of hours worked"}))
    work_descriptions = forms.CharField(label='Work description',
                                        widget=forms.Textarea(
                                            attrs={
                                                "class": "new-class-name two",
                                                "id": "my-id-for-textarea",
                                                "placeholder": "Please fill the description of your work",
                                                "rows": 4,
                                                "cols": 50,
                                            }
                                        ))
    date = forms.DateField(label='Date')

    class Meta:
        model = Work
        fields = [
            'project',
            'hours',
            'work_descriptions',
            'date',
        ]

    # def clean_project(self, *args, **kwargs):
    #     project = self.cleaned_data.get('project')
    #     if "CFE" not in project:
    #         raise forms.ValidationError("This is not a valid project")
    #     if "ABC" not in project:
    #         raise forms.ValidationError("This is not a valid project")
    #
    #     else:
    #         return project
    #
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("eurial.com.ro"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email


class RawWorkForm(forms.Form):
    project = forms.CharField(label='Project', widget=forms.TextInput(attrs={"placeholder": "Select the project"}))
    hours = forms.DecimalField(label='Number of hours worked', initial=8,
                               widget=forms.TextInput(attrs={"placeholder": "Select number of hours worked"}))
    work_descriptions = forms.CharField(label='Work description',
                                        widget=forms.Textarea(
                                            attrs={
                                                "class": "new-class-name two",
                                                "id": "my-id-for-textarea",
                                                "placeholder": "Please fill the description of your work",
                                                "rows": 4,
                                                "cols": 50,
                                            }
                                        ))
    date = forms.DateField(label='Date')
