from rest_framework import permissions


class GlobalPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        model_perm_string = self. get_model_permission_string(
            method=request.method,
            view=view
        )

        if not model_perm_string:
            return False

        if request.method in ["GET", "OPTIONS", "HEAD"]:
            return request.user.has_perm(model_perm_string)

        if request.method == "POST":
            return request.user.has_perm(model_perm_string)

        if request.method in ["PATCH", "PUT"]:
            return request.user.has_perm(model_perm_string)

        if request.method == "DELETE":
            return request.user.has_perm(model_perm_string)

        return False

    def get_model_permission_string(self, method, view):
        try:
            app_name = view.queryset.model._meta.app_label
            model_name = view.queryset.model._meta.model_name
            action = self.get_method_string(method)
            return f"{app_name}.{action}_{model_name}"
        except AttributeError:
            return None

    def get_method_string(self, method):
        METHODLIST = {"GET": "view",
                      "POST": "add",
                      "PUT": "change",
                      "PATCH": "change",
                      "DELETE": "delete",
                      "OPTIONS": "view",
                      "HEAD": "view",
                      }
        return METHODLIST.get(method, '')
