from .client import StackexchangeClient, StackexchangeClientMock
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

SE_CLIENT_CLS = StackexchangeClientMock