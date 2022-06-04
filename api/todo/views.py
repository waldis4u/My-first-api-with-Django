from rest_framework import viewsets
from .models import todo
from .serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer
