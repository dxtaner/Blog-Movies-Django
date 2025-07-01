from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=25, label="kullanıcı adı")
    password = forms.CharField(
        max_length=20, label="parola", widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=20, label="parola doğrula", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler Eşleşmiyor..")

        values = {
            "username": username,
            "password": password,
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="kullanıcı adı")
    password = forms.CharField(label="parola", widget=forms.PasswordInput)
