from rest_framework import serializers
from .models import Produce


class ProduceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produce
        fields = "__all__"
        read_only_fields = ["farmer", "date_added", "updated_at"]
        
    def validate(self, data):
        request = self.context.get('request')
        market  = data.get("market")
        
        if request.user.role not in ["ADMIN", "FARMER"]:
            serializers.ValidationError("You cannot add a Product")
            
        return data    
        
    # def validate(self, data):
    #      request = self.context['request']
    #      market = data.get('market')

    #      if request.user.role == "FARMER":
    #       if market not in request.user.allowed_markets.all():
    #         raise serializers.ValidationError(
    #             "You are not allowed to post in this market."
    #         )

    #      return data  