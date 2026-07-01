from rest_framework.decorators import (
    api_view,
    permission_classes
)

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import (
    Response
)

from .models import Student

from .serializers import (
    RegisterSerializer,
    StudentSerializer
)


# REGISTER API
@api_view(["POST"])
def register(request):

    serializer = RegisterSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response({

            "message":

            "Registered"

        })

    return Response(
        serializer.errors
    )


# STUDENT API
@api_view(["GET"])
@permission_classes([
    IsAuthenticated
])

def students(request):

    data = Student.objects.all()

    serializer = StudentSerializer(

        data,

        many=True

    )

    return Response(

        serializer.data

    )