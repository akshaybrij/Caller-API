from rest_framework import serializers
from .models import User,Contact
import re
class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data): 
        pattern = re.compile("(0/91)?[7-9][0-9]{9}")
        if pattern.match(data['num']):     
            return data
        else:
            raise ValueError("Phone number is not valid")

class ContactSerializer(ProfileUserSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def validate(self, data):
        return super(ContactSerializer,self).validate(data)

class ContactPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('num','full_name')
