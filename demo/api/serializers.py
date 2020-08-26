from rest_framework import serializers
from api import models
from rest_framework.validators import UniqueValidator

class MasterSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Master
        fields = '__all__'

    # 增加数据
    def create(self, validated_data):
        models.Master(**validated_data).save()
        return validated_data

    # 更新数据
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.schoolname = validated_data.get('schoolname',instance.schoolname)
        instance.city = validated_data.get('city',instance.city)
        instance.phone = validated_data.get('phone',instance.phone)
        instance.save()
        return instance

class GradeSerializers(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=64)
    designator = serializers.CharField(max_length=64)
    fount = serializers.DateTimeField()
    master_name = serializers.CharField(read_only=True,source='master.name')
    masterid = serializers.CharField(read_only=True,source='master.id')
    master = serializers.PrimaryKeyRelatedField(many=False,read_only=False,queryset=models.Master.objects.all())

    # 增加数据
    def create(self, validated_data):
        models.Grade(**validated_data).save()
        return validated_data

    # 更新数据
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.designator = validated_data.get('name',instance.name)