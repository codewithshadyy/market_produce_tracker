from rest_framework import serializers
from .models import Produce


class ProduceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produce
        fields = "__all__"
        read_only_fields = ["farmer", "date_added", "updated_at"]
        
    def validate(self, data):
        request = self.context.get('request')
        
        if request.user.role not in ["ADMIN", "FArMER"]:
            serializers.ValidationError("You cannot add a Product")
            
        return data      