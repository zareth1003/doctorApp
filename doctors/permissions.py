from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
  def has_permission(self, request,view):   #Este metodo lo que retorna es un booleano
    return request.user.groups.filter(name="doctors").exists()  #existe el grupo doctirs, filtrar si existe por su nombre, y si existe 