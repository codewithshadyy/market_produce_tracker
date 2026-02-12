from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    
    """""
      Custom permission: Only ADMIN role can create/update/delete.
    Authenticated CLIENT can only read
    """
    def has_permission(self, request, view):
        
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        
        else:
            return request.user.is_authenticated and request.user.role == "ADMIN"
        
        
        
    