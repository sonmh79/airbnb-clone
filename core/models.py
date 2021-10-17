from django.db import models
from . import managers

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # 새로 모델 생성 시 기록
    updated = models.DateTimeField(auto_now=True)  # 모델 저장 시 기록
    objects = managers.CustomModelManager()

    class Meta:
        # 데이터 베이스에 등록 X
        abstract = True
