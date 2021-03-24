from rest_framework import serializers

from personalaccount.models import RequestChange


class ALLPSSerializers(serializers.Serializer):
    """Сериализация показываемых ПС"""

    id = serializers.IntegerField()
    name = serializers.CharField()
    valute = serializers.CharField()
    curse = serializers.DecimalField(max_digits=16, decimal_places=4)
    reserve = serializers.DecimalField(max_digits=20, decimal_places=8)
    min_limit = serializers.DecimalField(max_digits=16, decimal_places=8)
    max_limit = serializers.DecimalField(max_digits=16, decimal_places=8)


class DepositRequestCreateSerializers(serializers.Serializer):
    """Создание заявки на Пополнение(Проверка переданных данных)"""

    order_pay = serializers.IntegerField()
    order_amount = serializers.DecimalField(max_digits=16, decimal_places=8)
    order_criterion = serializers.IntegerField()


class WidthRequestCreateSerializers(serializers.Serializer):
    """Создание заявки на Вывод(Проверка переданных данных)"""

    order_pay = serializers.IntegerField()
    order_amount = serializers.DecimalField(max_digits=16, decimal_places=8)
    order_criterion = serializers.IntegerField()
    order_rekvisites = serializers.CharField()


class AllRequestCreateModelSerializers(serializers.ModelSerializer):
    """Создание заявки на пополнение и вывод(Конечная валидация заявки)"""

    class Meta:
        model = RequestChange
        exclude = ['date_change_request', 'date_end_change', ]

    def create(self, validated_data):
        return RequestChange.objects.create(**validated_data)


class DepositRequestUpdateSerializers(serializers.Serializer):
    """Изменения статуса заявки"""

    order_number = serializers.CharField()






