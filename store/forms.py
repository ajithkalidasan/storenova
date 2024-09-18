from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.core import validators
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"
        )

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )
        
class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            
        )

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )
        
class ResetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ("newpassword1", "newpassword2")
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "New Password"}
        ),
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm New Password"}
        ),
    )
    



class ProfileForm(forms.ModelForm):
    phone = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
        required=False,
        validators=[validators.RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (e.g., +999999999).')]
    )
    
    email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True,
        help_text="Enter a valid email address."
    )
    
    address = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
        required=False
    )
    
    city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
        required=False
    )
    
   
    
    zipcode = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}),
        required=False,
        validators=[validators.RegexValidator(r'^\d{6}$', 'Enter a valid 6-digit zipcode.')]
    )
    
    country = forms.ChoiceField(
        label="",
        choices=[('', 'Select Country'), ('US', 'United States'), ('CA', 'Canada'), ('UK', 'United Kingdom'),('IND', 'India')], # Add more countries as needed
        widget=forms.Select(attrs={'class':'form-control'}),
        required=False
    )
    
    class Meta:
        model = Profile
        fields = ('phone', 'email', 'address', 'city', 'zipcode', 'country')


       
        
