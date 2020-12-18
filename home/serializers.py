from rest_framework import serializers

from personalaccount.models import RequestChange


class RequestAPI(serializers.ModelSerializer):
    """Список заявок"""
    request_currency = serializers.SlugRelatedField(slug_field='base_currency', read_only=True)
    request_sistemchange = serializers.SlugRelatedField(slug_field='base_sistemchange', read_only=True)
    criteri = serializers.SlugRelatedField(slug_field='base_criteri', read_only=True)

    class Meta:
        model = RequestChange
        fields = '__all__'
