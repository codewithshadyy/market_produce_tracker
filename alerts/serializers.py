from rest_framework import serializers
from .models import PriceAlert

class PriceAlertSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PriceAlert
        fields = [
            "id",
            "produce",
            "threshold_price",
            "alert_type",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]
    
    def validate(self, attrs):
        request = self.context['request']
        
        if request.user.role  ==  ["ADMIN", "FARMER"]:
             raise serializers.ValidationError(
                "Only Clints can create alerts."
            )
             
        if attrs["alert_type"] == "threshold" and not attrs.get("threshold_price"):
            raise serializers.ValidationError(
                "Threshold price is required for threshold alerts."
            )
        return attrs
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)         
    