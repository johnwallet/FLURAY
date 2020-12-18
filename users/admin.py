from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, CustomUserId


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
    readonly_fields = ('id', 'date_joined', 'last_login', 'is_superuser')
    # отображение полей на странице
    list_display = ('id', 'username', 'email')
    # фильтр
    list_filter = ('userid', 'date_joined', 'is_staff', 'is_active')
    # структура карточки пользователя
    fieldsets = (
        ('Основные настройки', {'fields': ('avatar', 'id', 'username', 'balance', 'email', 'password', 'kompan_name', 'first_name', 'last_name', 'middle_name', ('date_joined', 'last_login'))}),
        ('Реквизиты для пополнения', {'fields': ('requsites_sberbank_rub', 'requsites_psb_rub', 'requsites_tinkoff_rub', 'requsites_gazprombank_rub',
                                  'requsites_alfabank_rub', 'requsites_russtandart_rub', 'requsites_vtb_rub', 'requsites_rosselhoz_rub', 'requsites_raifaizen_rub',
                                  'requsites_roketbank_rub', 'requsites_otkritie_rub', 'requsites_pochtabank_rub', 'requsites_rnkb_rub', 'requsites_rosbank_rub',
                                  'requsites_mtsbank_rub', 'requsites_qiwi_rub', 'requsites_qiwi_usd', 'requsites_payeer_rub', 'requsites_payeer_usd', 'requsites_payeer_eur',
                                  'requsites_webmoney_rub', 'requsites_webmoney_usd', 'requsites_webmoney_eur', 'requsites_pm_btc', 'requsites_pm_usd', 'requsites_pm_eur',
                                  'requsites_skrill_rub', 'requsites_skrill_usd', 'requsites_paypal_rub', 'requsites_paypal_usd', 'requsites_paypal_eur', 'requsites_umoney_rub',
                                  'requsites_btc', 'requsites_xrp', 'requsites_ltc', 'requsites_bch', 'requsites_xmr', 'requsites_eth', 'requsites_etc', 'requsites_dash')}),
        ('Реквизиты для вывода', {'fields': ('requsites_width_sberbank_rub', 'requsites_width_psb_rub', 'requsites_width_tinkoff_rub', 'requsites_width_gazprombank_rub',
                                    'requsites_width_alfabank_rub', 'requsites_width_russtandart_rub', 'requsites_width_vtb_rub', 'requsites_width_rosselhoz_rub',
                                    'requsites_width_raifaizen_rub', 'requsites_width_roketbank_rub', 'requsites_width_otkritie_rub', 'requsites_width_pochtabank_rub', 'requsites_width_rnkb_rub',
                                    'requsites_width_rosbank_rub', 'requsites_width_mtsbank_rub', 'requsites_width_qiwi_rub', 'requsites_width_qiwi_usd', 'requsites_width_payeer_rub',
                                    'requsites_width_payeer_usd', 'requsites_width_payeer_eur', 'requsites_width_webmoney_rub', 'requsites_width_webmoney_usd', 'requsites_width_webmoney_eur', 'requsites_width_pm_btc',
                                    'requsites_width_pm_usd', 'requsites_width_pm_eur', 'requsites_width_skrill_rub', 'requsites_width_skrill_usd', 'requsites_width_paypal_rub', 'requsites_width_paypal_usd',
                                    'requsites_width_paypal_eur', 'requsites_width_umoney_rub', 'requsites_width_btc', 'requsites_width_xrp', 'requsites_width_ltc', 'requsites_width_bch', 'requsites_width_xmr', 'requsites_width_eth', 'requsites_width_etc', 'requsites_width_dash')}),
        ('Разрешения', {'fields': ('userid', 'is_staff', 'is_active', 'is_superuser')}),
    )
    # структура карточки создания нового пользователя
    add_fieldsets = (
        ('Новый пользователь', {
            'classes': ('wide',),
            'fields': ('userid', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    # поиск по..
    search_fields = ('username',)
    # сортировка по..
    ordering = ('-id',)


class CustomUserIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'custuserid')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserId, CustomUserIdAdmin)


# Названиия и заголовки админки
admin.site.site_title = 'ADMIN PANEL'
admin.site.site_header = 'ADMIN MyWallet'
