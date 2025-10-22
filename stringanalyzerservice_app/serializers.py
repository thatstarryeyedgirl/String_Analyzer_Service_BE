from rest_framework import serializers
from .models import AnalyzeString


class AnalyzeStringSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()

    class Meta:
        model = AnalyzeString
        fields = [ 'value', 'properties', 'created_at']
        read_only_fields = ['sha256_hash', 'properties', 'created_at']

    def get_properties(self, obj): # is called when django is preparing the API response
        return obj.properties_dict()
    
    