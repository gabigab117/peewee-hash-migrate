from datetime import datetime
from email_validator import validate_email, EmailNotValidError

from peewee import *
from argon2 import PasswordHasher
from settings import db

class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    
    class Meta:
        database = db
    
    def save(self, *args, **kwargs):
        try:
            validate_email(self.email)
        except EmailNotValidError as e:
            print(f"Error validating email: {e}")
            return False
        return super().save(*args, **kwargs)

    def _set_password(self, password):
        ph = PasswordHasher()
        hash = ph.hash(password)
        self.password = hash
    
    @classmethod
    def create_user(cls, name, email, password):
        user = cls(name=name, email=email)
        user._set_password(password)
        user.save()
        return user
    
    def login(self, password):
        ph = PasswordHasher()
        try:
            ph.verify(self.password, password)
            return True
        except Exception:
            return False
        

class Message(Model):
    title = CharField()
    message = CharField()
    created_at = DateTimeField(default=datetime.now)
    user = ForeignKeyField(User, backref="messages")
    # test = CharField(null=True)

    class Meta:
        database = db