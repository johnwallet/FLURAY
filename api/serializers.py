from rest_framework import serializers

from personalaccount.models import RequestChange
from users.models import CustomUser


class RequestPSStatusSerializers(serializers.Serializer):
    """Получение списка для заявок на пополнение, с информацией о ПС (Название, Активность, Резерв, Минимальный лимит, Максимальный лимит)"""

    code = serializers.CharField()
    name = serializers.CharField()
    valute = serializers.CharField()
    curse = serializers.DecimalField(max_digits=10, decimal_places=4)
    reserve = serializers.DecimalField(max_digits=16, decimal_places=8)
    min_limit = serializers.DecimalField(max_digits=16, decimal_places=8)
    max_limit = serializers.DecimalField(max_digits=16, decimal_places=8)


class DepositRequestCreateSerializers(serializers.Serializer):
    """Создание заявки на пополнение"""

    code = serializers.CharField()





