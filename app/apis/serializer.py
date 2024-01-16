from rest_framework import serializers
import uuid
from app.cv_generator import Cv_Generator


class CvSerializer (serializers.Serializer) : 
    full_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    about_me = serializers.CharField()
    projects = serializers.ListField()
    cv_type = serializers.ChoiceField(choices=(('light','light'),('dark','dark')))

    def projects_validate(self, value):

        if len(value) > 4 :
            raise serializers.ValidationError({'message',"much projects you enter"})
        
        return value
    

    def save(self, **kwargs):
        saved_path = f'media/{uuid.uuid4()}.pdf'
        data = self.validated_data

        personl = {    
            "name" : data['full_name'] ,
            "phone" : data['phone'],
            "address" : data['address'],
            "email" : data['email']
        }

        cv = Cv_Generator(
            personl_info = personl,
            projects = data['projects'],
            about_me = data['about_me']
        )

        if data['cv_type'] == 'light' : 
            cv.light_cv_mode().save(saved_path)
        
        elif data['cv_type'] == 'dark' : 
            cv.dark_cv_mode().save(saved_path)
            

        return {'cv' : saved_path}