from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,username,full_name,num,password,**options):
        if not full_name or not username:
            raise ValueError("You missed a parameter username or full name.")
        if not num:
            import pdb;pdb.set_trace()
            raise ValueError("You missed a parameter number");

        self.full_name = full_name
        self.num = num
        self.username= username
        user = self.model(username=self.username,full_name=self.full_name,num=self.num,**options)
        user.set_password(password)
        user.save(using=self._db)
        return user
