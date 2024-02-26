from rest_framework import serializers
from shop.models import Item
from shop.services import buy


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


    def get_url(self, instance):
        response = buy(
            name=instance.name,
            price=instance.price
        )
        return response['url']