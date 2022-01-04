from django.contrib.auth.forms import UserCreationForm
from .models import GamePublisher


class CreateUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = GamePublisher
        fields = ('username', 'email', 'favorite_thing', 'country', 'password1', 'password2')    