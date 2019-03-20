from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


# from django.contrib.auth.models import User
# class EmailAuth:
#     """Authentication of a user by exact match on the email and password"""
#     def authenticate(self, username=None, password=None):
#         """Get an instance of `User` based on the email and verify the pass"""
#         try:
#             user = User.objects.get(email=username)
#             if user.check_password(password):
#                 return user
#             return None
#         except User.DoesNotExist:
#             return None
#     def get_user(self, user_id):
#         """Used by the Django auth system to retrive a user instance"""
#         try:
#             user = User.objects.get(pk=user_id)
#             if user.is_active:
#                 return user
#             return None
#         except User.DoesNotExist:
#             return None
