from django.shortcuts import render
from django.shortcuts import get_object_or_404

from medicines.models import Medicine
from rest_framework import status

from medicines.serializer import MedicineSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def medicines(request):

    if request.method == 'GET':
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MedicineSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def medicines_details(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'GET':
        ...


    if request.method == 'DELETE':
        medicine.delete()
        

    if request.method == 'PUT':
        
        serializer = MedicineSerializer(data=request.data)

        if serializer.is_valid():
            medicine.name = request.data.get('name', medicine.name)
            medicine.price = request.data.get('price', medicine.price)

            medicine.save()


    serializer = MedicineSerializer(medicine)
    return Response(serializer.data)
            

# {"name": "Eduardo Cambio de nombre", "price": 201, "laboratory_id": 1}