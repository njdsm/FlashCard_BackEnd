from django.shortcuts import render
from .models import Flashcard
from .serializers import FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class FlashcardList(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass


class FlashcardDetail(APIView):
    def get_flashcard(self, request, pk):
        pass

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
