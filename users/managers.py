from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name='Admin',
            last_name='Admin',
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user
