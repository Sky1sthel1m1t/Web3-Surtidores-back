from rest_framework.permissions import BasePermission


class IsVendedor(BasePermission):
    message = 'No tienes permisos para hacer esto'

    def has_permission(self, request, view):
        token = request.auth
        role_id = token['role']
        return role_id == 4


class IsAdministradorSurtidor(BasePermission):
    message = 'No tienes permisos para hacer esto'

    def has_permission(self, request, view):
        token = request.auth
        role_id = token['role']
        return role_id == 1


class IsAdministradorAccesos(BasePermission):
    message = 'No tienes permisos para hacer esto'

    def has_permission(self, request, view):
        token = request.auth
        role_id = token['role']
        return role_id == 3


class IsAdministradorRefineria(BasePermission):
    message = 'No tienes permisos para hacer esto'

    def has_permission(self, request, view):
        token = request.auth
        role_id = token['role']
        return role_id == 2

class IsChofer(BasePermission):
    message = 'No tienes permisos para hacer esto'

    def has_permission(self, request, view):
        token = request.auth
        role_id = token['role']
        return role_id == 5