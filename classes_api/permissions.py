from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    message = "You are not the teacher of this class. Go away! You're naughty..."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.teacher == request.user:
            return True
        return False