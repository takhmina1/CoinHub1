from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserAdditionalInfo

class UserAdditionalInfoInline(admin.StackedInline):
    model = UserAdditionalInfo
    can_delete = False
    verbose_name_plural = 'Дополнительная информация о пользователе'

class CustomUserAdmin(UserAdmin):
    model = User
    inlines = (UserAdditionalInfoInline,)
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)































































# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['email', 'username', 'email_confirmed']  # Отображение только email, username и email_confirmed

#     fieldsets = (
#         (None, {'fields': ('email', 'username', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )

#     search_fields = ('email', 'username')
#     ordering = ('email',)

#     filter_horizontal = ()
#     list_filter = ()

# admin.site.register(CustomUser, CustomUserAdmin)
























# # from django.contrib import admin
# # from django.contrib.auth.admin import UserAdmin
# # from .models import CustomUser

# # class CustomUserAdmin(UserAdmin):
# #     model = CustomUser
# #     list_display = ['email', 'username', 'is_staff', 'is_active']
# #     fieldsets = (
# #         (None, {'fields': ('email', 'username', 'password')}),
# #         ('Permissions', {'fields': ('is_staff', 'is_active')}),
# #     )
# #     add_fieldsets = (
# #         (None, {
# #             'classes': ('wide',),
# #             'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
# #         ),
# #     )
# #     search_fields = ('email', 'username')
# #     ordering = ('email',)

# #     # Избавляемся от ссылок на поля, которые не принадлежат модели CustomUser
# #     filter_horizontal = ()
# #     list_filter = ()

# # admin.site.register(CustomUser, CustomUserAdmin)
