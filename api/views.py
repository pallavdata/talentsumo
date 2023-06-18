from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from .serializer import NoteSerializer,SharedSerializer,RegistrationSerializer
from rest_framework import status
from .models import shared, notes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

# Create your views here.

def Intro(request):
    return render(request,"intro.html")

class Reg_view(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            tokenuser = serializer.save()
            token = request.data.get("resttoken", False)
            jwttoken = RefreshToken.for_user(tokenuser)
            tokendata = jwttoken.access_token
            return Response({"name": f"{tokenuser.username}", "refresh": str(tokendata)}, status=status.HTTP_200_OK)
        returndata = serializer.data
        returndata.pop('password',None)
        return Response({"errors": serializer.errors,"data":returndata}, status=status.HTTP_400_BAD_REQUEST)


class Notes(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser) 

    def get(self,request):
        try:
            note = notes.objects.filter(user_id=request.user.id)
            serializer = NoteSerializer(note,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'message':'no data'},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        print(request.user.id)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Shared(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            data = shared.objects.filter(user_id = request.user.id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        newdata = SharedSerializer(data, many=True)
        return Response(newdata.data,status=status.HTTP_200_OK)

    def post(self,request):
        id=request.data.get("noteid")
        username = request.data.get("username")
        if username == request.user.username:
            return Response({"error":"can't share notes youself"},status=status.HTTP_404_NOT_FOUND)
        if not id and not userid:
            return Response({"error":"noteid and username required"},status=status.HTTP_404_NOT_FOUND)
        try:
            note = notes.objects.get(id=id,user_id=request.user)
        except:
            return Response({"error":"note not belongs to the user"},status=status.HTTP_404_NOT_FOUND)
        try:
            user_instance = User.objects.get(username=username)
        except:
            return Response({"error":"no user"},status=status.HTTP_404_NOT_FOUND)
        savedata = shared(user_id=user_instance,note_id=note,created_by=request.user)
        savedata.save()
        return Response({"added":"added"},status=status.HTTP_200_OK)


## if we want to use url to send id then we use


# class Sharedurl(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self,request,id):
#         userid = request.data.get("userid")
#         if not id and not userid:
#             return Response({"error":"id and userid required"},status=status.HTTP_404_NOT_FOUND)
#         try:
#             note = notes.objects.get(id=id,user_id=request.user)
#         except:
#             return Response({"error":"note not belongs to the user"},status=status.HTTP_404_NOT_FOUND)
#         try:
#             user_instance = User.objects.get(user=userid)
#         except:
#             return Response({"error":"no user"},status=status.HTTP_404_NOT_FOUND)
#         savedata = Shared(user_id=user_instance,note_id=note,created_by=request.user)
#         savedata.save()
#         return Response({"added":"added"},status=status.HTTP_200_OK)
        
