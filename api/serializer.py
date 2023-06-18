from rest_framework import serializers
from .models import notes,shared
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = notes
        fields = '__all__'
        extra_kwargs = {'user_id': {'required': False}}

    def validate(self, data):
        if not data.get('notes_text') and not data.get('notes_file'):
            raise serializers.ValidationError({
                "notes_text": "Text note is required if video,audio is not provided.",
                "notes_file": "Video,audio is required if text is not provided.",
                "notes_text , notes_file": "you can also provide both text or video notes"
            })
        return data


class SharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = shared
        fields = '__all__'
