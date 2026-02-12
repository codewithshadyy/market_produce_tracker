from .models import Market
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Market
        fields = ['id', 'name', 'location', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
        
    def validate_name(self, value):
        if len(value)<3:
            serializers.ValidationError("Market name should be 3 or more characters") 
        return value
    def validate_location(self, value):
        if not value.strip():
            serializers.ValidationError("OOPs! location cannot be empty")        
        
        return value