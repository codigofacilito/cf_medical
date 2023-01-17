from medicines.models import Medicine
from laboratories.models import Laboratory

from rest_framework import serializers

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = ['id', 'name']

"""
class MedicineSerializer(serializers.ModelSerializer):
    laboratory = LaboratorySerializer(many=False, read_only=True)

    class Meta:
        model = Medicine
        fields = ['id', 'name', 'laboratory']
        read_only_fields = ['id']
"""

class MedicineSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    laboratory_id = serializers.IntegerField()
    laboratory = LaboratorySerializer(many=False, read_only=True)

    def create(self, data):
        return Medicine.objects.create(
            name=data['name'],
            price=data['price'],
            laboratory_id=data['laboratory_id']
        )

# {"name": "Medicine 3", "price": 200, "laboratory_id": 1}