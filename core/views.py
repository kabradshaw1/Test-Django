from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)

class UserView(viewset.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()