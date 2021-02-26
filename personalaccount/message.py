from django.core.cache import cache


# Успешно сохранили
def message_success():
    index = {
        'message': 'Данные успешно сохранены',
        'message_type': 'Success'
    }
    cache.set('info_message', index, 30)


# Успешно активирован аккаунт
def message_email_succes():
    index = {
        'message': 'Аккаунт успешно активирован',
        'message_type': 'Success'
    }
    cache.set('info_message', index, 30)







