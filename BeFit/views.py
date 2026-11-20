from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from BeFit.serializers import UserSerializer,MemberShipSerializer
from rest_framework import authentication,permissions,serializers
from BeFit.models import MemberShipDb

# Create your views here.
class SignUpView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=210)
        else:
            return Response(serializer_instance.errors,status=400)

    def get(self,request):
        qs=User.objects.all()
        serializer_instance=UserSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def delete(self,request,pk):
        User.objects.filter(id=pk).delete()
        return Response({
            "Message" : "User Deleted Successfullt..!"
        })

class MemberShipListCreateView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        form_data = request.data
        serializer_instance = MemberShipSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save(member=request.user)

            return Response(data={
                "Message": "Membership Added Successfully.....!",
                "Membership Details": serializer_instance.data
            })

        else:
            return Response(data=serializer_instance.errors)

    def get(self,request):
        qs=MemberShipDb.objects.all()
        serializer_instance=MemberShipSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

class MemberShipRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        membersip_obj=get_object_or_404(MemberShipDb,id=pk)
        serializer_instance=MemberShipSerializer(membersip_obj)
        return Response (data=serializer_instance.data)

    def put(self,request,pk):
        membership_obj=get_object_or_404(MemberShipDb,id=pk)
        serializer_instance=MemberShipSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "Message" : "MemberShip Updated Successfully..!",
                "Updated_MemberShip" : serializer_instance.data
            })
        else:
            return Response (data=serializer_instance.errors)

    def delete(self,request,pk):
        membership_obj=get_object_or_404(MemberShipDb,id=pk)
        membership_obj.delete()
        return Response(data={
            "Message" : "MemberShip Deleted Successfully...!"
        })
