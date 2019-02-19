from api.models import Event
from .serializers import EventSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView


class EventDetailView(APIView):
    def get(self, request, pk):
        event = Event.objects.get(Q(user__id=pk) &
                                  Q(eventRound=1)
                                  )
        data = EventSerializer(event).data
        return Response(data)


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
