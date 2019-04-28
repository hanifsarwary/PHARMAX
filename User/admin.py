from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserCreationForm,UserAdmin,UserChangeForm
from django import forms
from django.contrib.auth.hashers import make_password


# class customform(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ['username','password','email', 'dob',
#     'phone',
#     'salary',
#     'cnic',
#     'bid',
#     'address',
#     'desgination' ]
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         clearPassNoHash = self.cleaned_data['password']
#         self.password = make_password(clearPassNoHash, None, 'md5')
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class MyUserChangeForm(UserChangeForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'email', 'dob',
#                   'phone',
#                   'salary',
#                   'cnic',
#                   'bid',
#                   'address',
#                   'desgination']
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         clearPassNoHash = self.cleaned_data['password']
#         self.password = make_password(clearPassNoHash, None, 'md5')
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class MyUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password', 'email', 'dob',
#                    'phone',
#                    'salary',
#                    'cnic',
#                    'bid',
#                    'address',
#                    'desgination'),
#         }),
#     )
#     def save_form(self, request, form, change):
#         clearPassNoHash = form.cleaned_data['password']
#
#         password = make_password(clearPassNoHash, None, 'md5')
#         form.password = password
#         form.save(commit=True)

class cform(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        clearPassNoHash = self.cleaned_data['password']
        self.cleaned_data['password'] = make_password(clearPassNoHash, None, 'md5')
        return self.cleaned_data

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomAdmin(admin.ModelAdmin):
    form = cform

admin.site.register(CustomUser,CustomAdmin)
admin.site.register(Supplier)
