from classes.models import Classroom
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    ClassListSerializer,
    ClassDetailSerializer,
    ClassCreateUpdateSerializer,
    RegisterSerializer,
    UserLoginSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsTeacher
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.my_data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class ClassListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter,]
    search_fields = ['subject', 'year', 'teacher']


class ClassDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'class_id'
    permission_classes = [AllowAny,]


class ClassCreateView(CreateAPIView):
    serializer_class = ClassCreateUpdateSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'class_id'
    permission_classes = [IsAuthenticated,IsTeacher]


class ClassDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'class_id'
    permission_classes = [IsAuthenticated,IsAdminUser]
