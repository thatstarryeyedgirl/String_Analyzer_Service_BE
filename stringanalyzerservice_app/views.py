from .models import AnalyzeString
from .serializers import AnalyzeStringSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from hashlib import sha256


# Create your views here.
class CreateStringView(APIView):
    def post(self, request):
        value = request.data.get('value')
        if not value:
            return Response({"error": '"value" field is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(value, str):
            return Response({"error": '"value" must be a string'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        hash_value = sha256(value.encode()).hexdigest() # says convert the value/string to bytes(as hashing only works on bytes), generate a unique hash for it and convert it to a readable hexadec. string
        if AnalyzeString.objects.filter(sha256_hash=hash_value).exists():
            return Response({"error": "String already exists"}, status=status.HTTP_409_CONFLICT)
        obj = AnalyzeString(value=value)
        obj.save()
        return Response(AnalyzeStringSerializer(obj).data, status=status.HTTP_201_CREATED)
    

class RetrieveStringView(generics.RetrieveAPIView):
    serializer_class = AnalyzeStringSerializer
    queryset = AnalyzeString.objects.all()
    lookup_field = 'value'
    
    
class ListStringView(APIView):
    def get(self, request):
        word = AnalyzeString.objects.all()
        try:
            if 'is_palindrome' in request.GET:
                word= word.filter(is_palindrome=request.GET['is_palindrome'].lower() == 'true')
            if 'min_length' in request.GET:
                word = word.filter(length__gte=int(request.GET['min_length']))
            if 'max_length' in request.GET:
                word = word.filter(length__lte=int(request.GET['max_length']))
            if 'word_count' in request.GET:
                word = word.filter(word_count=int(request.GET['word_count']))
            if 'contains_character' in request.GET:
                word = word.filter(value__icontains=request.GET['contains_character'])
        except ValueError:
            return Response({"error": "Invalid query parameters"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": AnalyzeStringSerializer(word, many=True).data, "count": word.count(), "filters_applied": request.GET})
    
    
class DeleteStringView(generics.DestroyAPIView):
    queryset = AnalyzeString.objects.all()
    serializer_class = AnalyzeStringSerializer
    lookup_field = 'value'
    
    