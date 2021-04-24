import re
from django.urls import reverse
from django.conf import settings
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Announcement(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # 제목
    company = models.CharField(max_length=100)  # 회사명
    basicAddr = models.TextField(blank=True)  # 근무지 기본주소
    sal = models.IntegerField()  # 급여
    regDt = models.DateField(blank=True, null=True)  # 등록일자
    closeDt = models.DateField(blank=True, null=True)  # 마감일자
    region = models.CharField(max_length=100, blank=True)  # 근무지역
    explain = models.TextField(blank=True)  # 설명
    caption = models.TextField(max_length=500, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    favs = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='favs')

    wantedAuthNo = models.TextField(blank=True) # 구인인증번호
    busino = models.TextField(blank=True) # 사업자등록번호
    salTpNm = models.TextField(blank=True) # 임금형태
    minSal = models.IntegerField(blank=True, null=True) # 최소임금
    maxSal = models.IntegerField(blank=True, null=True) # 최대임금
    holidayTpNm = models.TextField(blank=True) # 근무형태
    minEdubg = models.TextField(blank=True) # 최소학력
    maxEdubg = models.TextField(blank=True) # 최대학력
    career = models.TextField(blank=True) # 경력
    infoSvc = models.TextField(blank=True) # 정보제공처
    wantedInfoUrl = models.TextField(blank=True) # 워크넷 채용정보 URL
    zipCd = models.TextField(blank=True) # 근무지 우편번호
    strtnmCd = models.TextField(blank=True) # 근무지 도로명주소
    detailAddr = models.TextField(blank=True) # 근무지 상세주소
    empTpCd = models.IntegerField(blank=True, null=True) # 고용형태코드
    jobsCd = models.IntegerField(blank=True, null=True) # 직종코드
    smodifyDtm = models.DateField(blank=True, null=True) # 최종수정일
    prefCd = models.TextField(blank=True) # 우대조건

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-closeDt']

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
