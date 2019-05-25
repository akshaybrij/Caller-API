from django.shortcuts import render
from rest_framework.views import APIView
from .models import User,Contact
from .serializers import ProfileUserSerializer,ContactSerializer,ContactPUTSerializer
from rest_framework.response import Response
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
import re
from django.db.models import Q
from django.shortcuts import redirect
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class ContactView(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Contact.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactPUTSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class UserRegisterView(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUserSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class SearchView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Contact.objects.all()
    permission_classes=(IsAuthenticated,)
    serializer_class = ContactSerializer

    def get(self,request):
        search = self.request.query_params.get('search',None)
        pattern = re.compile("[A-Z]?[a-z]")
        if search is None:
            con = Contact.objects.all()
            ser = ContactSerializer(con,many=True)
            return Response(ser.data)
        if pattern.match(search):
            return self.search_by_name(search)
        else:
            return self.search_by_num(search)
    def search_by_name(self,search):
        res = Contact.objects.filter(full_name__startswith=search)
        unres = Contact.objects.filter(~Q(full_name__startswith=search))
        seres = ContactSerializer(res,many=True)
        unseres = ContactSerializer(unres,many=True)
        response_data = seres.data + unseres.data
        return Response(response_data,status=status.HTTP_200_OK)

    def search_by_num(self,search):
        _num_with_name = Contact.objects.filter(num=search,full_name__isnull=False)
        _num = Contact.objects.filter(num=search,full_name__isnull=True)
        if _num_with_name:
            res = ContactSerializer(_num_with_name,many=True)
            return Response(res.data,status=status.HTTP_200_OK)
        elif _num:
            res = ContactSerializer(_num)
            return Response(res.data,status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_404_NOT_FOUND)

        
class CreateContactsView(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes=(IsAuthenticated,)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


