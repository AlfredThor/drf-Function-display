from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from api import serializers
from api import models

@method_decorator(csrf_exempt,name='dispatch')
class Index(APIView):

    def get(self,request,*args,**kwargs):

        obj = models.Master.objects.all()
        serializer = serializers.MasterSerializers(obj,many=True)
        status = {'status':'success','code':200,'message':serializer.data}
        return Response(status)

    def post(self, request, *args, **kwargs):

        message = request.data
        serializer = serializers.MasterSerializers(data=message)
        success = serializer.is_valid(raise_exception=True)
        if success:
            info = serializer.save()
            data = info['name'] + '添加成功！'
            result = {'status': 'success', 'code': 200, 'message': data}
            return Response(result)
        else:
            result = {'status': 'fail', 'code': 400, 'message': serializer.errors}
            return Response(result)

    def put(self, request, *args, **kwargs):

        data = request.data
        master = models.Master.objects.filter(id=data['id']).first()
        master_obj = serializers.MasterSerializers(instance=master, data=data, partial=True)
        if master_obj.is_valid():
            master_obj.save()
            return Response(master_obj.data)
        else:
            return Response(master_obj.errors)

    def delete(self, request, *args, **kwargs):
        data = request.data
        obj = models.Master.objects.filter(id=data['id']).first()
        if obj is not None:
            obj.delete()
            return Response({'success': '删除成功！'})
        else:
            return Response({'fail': '数据不存在！'})


@method_decorator(csrf_exempt,name='dispatch')
class Index1(APIView):
    # 查
    def get(self,request,*args,**kwargs):

        teacher_obj = models.Grade.objects.filter(master_id=2).first()
        # teacher_obj = models.Grade.objects.all()
        serializer = serializers.GradeSerializers(teacher_obj)
        data = {'code':200,'status':'success','message':serializer.data}

        return Response(data)
    # 增
    def post(self,request):

        message = request.data
        serializer = serializers.GradeSerializers(data=message)
        success = serializer.is_valid(raise_exception=True)
        if success:
            info = serializer.save()
            data = info['name']+'添加成功！'
            result = {'status':'success','code':200,'message':data}
            print('PASS')
            return Response(result)
        else:
            result = {'status':'fail','code':400,'message':serializer.errors}
            return Response(result)

    # 改
    def put(self,request):
        data = request.data
        grade = models.Grade.objects.filter(id=data['id']).first()
        grade_obj = serializers.GradeSerializers(instance=grade,data=data,partial=True)
        if grade_obj.is_valid():
            grade_obj.save()
            return Response(grade_obj.data)
        else:
            return Response(grade_obj.errors)

    # 删
    def delete(self,request):
        data = request.data
        grade = models.Grade.objects.filter(id=data['id']).first()
        if grade is not None:
            grade.delete()
            return Response({'success':'删除成功！'})
        else:
            return Response({'fail':'数据不存在！'})