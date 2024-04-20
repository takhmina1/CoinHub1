from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать только свои собственные объекты.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Администратор может выполнять любые действия, остальные - только чтение.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class CustomPermission(permissions.BasePermission):
    """
    Пример кастомного правила доступа.
    """
    def has_permission(self, request, view):
        return True

class IsOwnerOfBankAccount(permissions.BasePermission):
    """
    Пользователь может управлять только своими банковскими счетами.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.customer == request.user

class CanProcessApplication(permissions.BasePermission):
    """
    Пользователь может обрабатывать заявки только в определенных случаях.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("process_application")

class CanViewSensitiveData(permissions.BasePermission):
    """
    Пользователь может видеть чувствительные данные только при наличии специального разрешения.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("view_sensitive_data")

class IsEmployee(permissions.BasePermission):
    """
    Пользователь является сотрудником.
    """
    def has_permission(self, request, view):
        return request.user.is_employee

class IsManager(permissions.BasePermission):
    """
    Пользователь является менеджером.
    """
    def has_permission(self, request, view):
        return request.user.is_manager

class IsAdmin(permissions.BasePermission):
    """
    Пользователь является администратором.
    """
    def has_permission(self, request, view):
        return request.user.is_admin

class CanAccessResource(permissions.BasePermission):
    """
    Пользователь имеет доступ к ресурсу на основе его роли.
    """
    def has_permission(self, request, view):
        return request.user.role.can_access_resource(view.resource)

class HasSpecialPermission(permissions.BasePermission):
    """
    Пользователь имеет специальное разрешение.
    """
    def has_permission(self, request, view):
        return request.user.has_special_permission()

class IsSuperAdmin(permissions.BasePermission):
    """
    Пользователь является суперадминистратором.
    """
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsPremiumUser(permissions.BasePermission):
    """
    Пользователь является премиум-пользователем.
    """
    def has_permission(self, request, view):
        return request.user.is_premium

class CanEditOwnProfile(permissions.BasePermission):
    """
    Пользователь может редактировать свой профиль.
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class CanViewDocument(permissions.BasePermission):
    """
    Пользователь может просматривать документы.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("view_document")

class CanEditDocument(permissions.BasePermission):
    """
    Пользователь может редактировать документы.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("edit_document")

class CanDeleteDocument(permissions.BasePermission):
    """
    Пользователь может удалять документы.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("delete_document")

class CanApproveApplication(permissions.BasePermission):
    """
    Пользователь может утверждать заявки.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("approve_application")

class CanRejectApplication(permissions.BasePermission):
    """
    Пользователь может отклонять заявки.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("reject_application")

class CanViewDashboard(permissions.BasePermission):
    """
    Пользователь может просматривать панель управления.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("view_dashboard")

class CanEditSettings(permissions.BasePermission):
    """
    Пользователь может редактировать настройки.
    """
    def has_permission(self, request, view):
        return request.user.has_permission("edit_settings")















































































































# from rest_framework import permissions

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Пользователь может редактировать только свои собственные объекты.
#     """
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user

# class IsAdminOrReadOnly(permissions.BasePermission):
#     """
#     Администратор может выполнять любые действия, остальные - только чтение.
#     """
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff

# class CustomPermission(permissions.BasePermission):
#     """
#     Пример кастомного правила доступа.
#     """
#     def has_permission(self, request, view):
#         return True

# class IsOwnerOfBankAccount(permissions.BasePermission):
#     """
#     Пользователь может управлять только своими банковскими счетами.
#     """
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.customer == request.user

# class CanProcessApplication(permissions.BasePermission):
#     """
#     Пользователь может обрабатывать заявки только в определенных случаях.
#     """
#     def has_permission(self, request, view):
#         return request.user.has_permission("process_application")

# class CanViewSensitiveData(permissions.BasePermission):
#     """
#     Пользователь может видеть чувствительные данные только при наличии специального разрешения.
#     """
#     def has_permission(self, request, view):
#         return request.user.has_permission("view_sensitive_data")

# class IsEmployee(permissions.BasePermission):
#     """
#     Пользователь является сотрудником.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_employee

# class IsManager(permissions.BasePermission):
#     """
#     Пользователь является менеджером.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_manager

# class IsAdmin(permissions.BasePermission):
#     """
#     Пользователь является администратором.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_admin

# class CanAccessResource(permissions.BasePermission):
#     """
#     Пользователь имеет доступ к ресурсу на основе его роли.
#     """
#     def has_permission(self, request, view):
#         return request.user.role.can_access_resource(view.resource)

# class HasSpecialPermission(permissions.BasePermission):
#     """
#     Пользователь имеет специальное разрешение.
#     """
#     def has_permission(self, request, view):
#         return request.user.has_special_permission()

# class IsSuperAdmin(permissions.BasePermission):
#     """
#     Пользователь является суперадминистратором.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_superuser

# class IsPremiumUser(permissions.BasePermission):
#     """
#     Пользователь является премиум-пользователем.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_premium

# class CanEditOwnProfile(permissions.BasePermission):
#     """
#     Пользователь может редактировать свой профиль.
#     """
#     def has_object_permission(self, request, view, obj):
#         return obj == request.user
