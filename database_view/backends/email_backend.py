from database_view.models import MyUser
from django.contrib.auth.backends import ModelBackend

#class EmailBackend(ModelBackend):
 #   def authenticate(self, request, email=None, password=None, **kwargs):
  #      UserModel = MyUser
   #     try:
    #        user = UserModel.objects.get(email=email)
     #       success = user.check_password(password)
      #      if success:
       #         return user
       # except UserModel.DoesNotExist:
        #    return None

  #  def get_user(self, user_id):
   #     try:
    #        return MyUser.objects.get(pk=user_id)
     #   except:
      #      return None