from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
# Import default User serializer
from .serializers import UserSerializer


# Create your views here.
class AllUsersView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SingleUser(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        # Filter queryset by looping through CustomUser objects and return one that matches
        current_user = self.kwargs['id']
        return User.objects.filter(id=current_user)


