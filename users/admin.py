from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# кастомизация админки, для приложения users.
class CustomUserAdmin(UserAdmin):
    # формы.
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    #
    list_display_links = ('username',)
    # верхняя панель кнопок
    save_on_top = True
    # поля для просмотра(нередактируемые).
    readonly_fields = ('id','date_joined', 'last_login', 'is_superuser')
    # отображение полей на странице
    list_display = ('id', 'username', 'email')
    # фильтр
    list_filter = ('date_joined', 'is_staff', 'is_active')
    # структура карточки пользователя
    fieldsets = (
        ('Основные настройки', {'fields': ('id', 'balance', 'username', 'email', 'password', 'first_name', 'last_name', 'middle_name',('date_joined', 'last_login'), 'bio')}),
        ('Разрешения', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    # структура карточки создания нового пользователя
    add_fieldsets = (
        ('Новый пользователь', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'bio', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    # поиск по..
    search_fields = ('username',)
    # сортировка по..
    ordering = ('-id',)


admin.site.register(CustomUser, CustomUserAdmin)
# Названиия и заголовки админки
admin.site.site_title = 'ADMIN PANEL'
admin.site.site_header = 'ADMIN MyWallet'
