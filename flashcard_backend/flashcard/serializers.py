from rest_framework import serializers
from .models import Flashcard


class FlashcardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flashcard
        fields = ['id', 'collection', 'front_text', 'back_text']
