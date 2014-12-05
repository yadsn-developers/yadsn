"""
Auth models.
"""


class Auth(object):
    """
    Auth model.
    """

#
# def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if not user or not user.is_active:
#             raise forms.ValidationError("Invalid login credentials")
#         return self.cleaned_data
#
#     def login(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         return user
