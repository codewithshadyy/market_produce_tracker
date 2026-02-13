

from rest_framework.permissions  import BasePermission


class IsFarmerOrAdmin(BasePermission):
      
      def has_permission(self, request, view):
            return(
                request.user.is_authenticated and
                request.user.role in ["ADMIN", "FARMER"]
            )
            
class IsOwnerOrAdmin(BasePermission):
    
        def has_object_permission(self, request, view, obj):
           return(
                request.user.role == "ADMIN" or
                obj.farmer == request.user
           )