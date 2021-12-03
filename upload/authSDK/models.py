from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


class UserManager(BaseUserManager):
    use_in_migrations = True


class User(AbstractBaseUser):
    """User class model used for authentication"""

    username = models.CharField(max_length=255, unique=True, blank=True)
    jwt_secret = models.UUIDField(default=uuid.uuid4)

    class Meta:
        managed = False
        db_table = "users_user"

    USERNAME_FIELD = "username"

    def jwt_get_secret_key(self):
        return self.jwt_secret
