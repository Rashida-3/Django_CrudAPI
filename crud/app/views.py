from rest_framework.response import Response
from .models import Student
from .serializers import studentserilizer
from rest_framework.views import APIView


# Create your views here.

class StudentAPI(APIView):
    def post(self, request):
        serilizer=studentserilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.errors)
        print(serilizer)

        return Response({'msg': 'created success'})
    

    def get(self,request, pk=None):
        id=pk
        if id:
            stu=Student.objects.get(id=id)
            serializer=studentserilizer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=studentserilizer(stu, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    def put(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=studentserilizer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response('updated')    

    def delete(self, request, pk):
        id=pk
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response("msg: deleted")

        




