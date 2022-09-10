from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from room.models import Room
from task.models import Task
from task.serializers import TaskSerializer


class UserTaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.user_tasks.all()


class RoomTaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_string = self.request.query_params['requestString']
        room_id = self.request.query_params['roomId']
        room = get_object_or_404(Room, request_string=request_string, id=room_id)
        return room.room_tasks.all()
