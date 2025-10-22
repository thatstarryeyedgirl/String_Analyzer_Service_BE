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
    
    
class NaturalLanguageFilterView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '').lower()
        filters = {}

        if "palindrome" in query:
            filters['is_palindrome'] = True
        if "single word" in query:
            filters['word_count'] = 1
        if "longer than" in query:
            num = ''.join([c for c in query.split("longer than")[1] if c.isdigit()])
            if num: filters['min_length'] = int(num)
        if "shorter than" in query:
            num = ''.join([c for c in query.split("shorter than")[1] if c.isdigit()])
            if num: filters['max_length'] = int(num)
        if "letter" in query:
            filters['contains_character'] = query.split("letter")[-1].strip()[0]

        strings = AnalyzeString.objects.all()
        if 'is_palindrome' in filters:
            strings = strings.filter(is_palindrome=True)
        if 'word_count' in filters:
            strings = strings.filter(word_count=filters['word_count'])
        if 'min_length' in filters:
            strings = strings.filter(length__gte=filters['min_length'])
        if 'max_length' in filters:
            strings = strings.filter(length__lte=filters['max_length'])
        if 'contains_character' in filters:
            strings = strings.filter(value__icontains=filters['contains_character'])

        serializer = AnalyzeStringSerializer(strings, many=True)
        return Response(serializer.data)
    
    
class DeleteStringView(generics.DestroyAPIView):
    queryset = AnalyzeString.objects.all()
    serializer_class = AnalyzeStringSerializer
    lookup_field = 'value'
    
    