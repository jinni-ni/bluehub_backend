from django.conf import settings
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Announcement(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wantedAuthNo = models.TextField(blank=True) # 구인인증번호
    company = models.TextField() # 회사명
    busino = models.TextField() # 사업자등록번호
    title = models.TextField() # 제목
    salTpNm = models.TextField() # 임금형태
    sal = models.TextField() #급여
    minSal = models.TextField() # 최소임금
    maxSal = models.TextField() # 최대임금
    region = models.TextField() # 근무지역
    holidayTpNm = models.TextField() # 근무형태
    minEdubg = models.TextField() # 최소학력
    maxEdubg = models.TextField() # 최대학력
    career = models.TextField() # 경력
    regDt = models.DateField() # 등록일자
    closeDt = models.DateField() # 마감일자
    infoSvc = models.TextField() # 정보제공처
    wantedInfoUrl = models.TextField() # 워크넷 채용정보 URL
    zipCd = models.TextField() # 근무지 우편번호
    strtnmCd = models.TextField() # 근무지 도로명주소
    basicAddr = models.TextField() # 근무지 기본주소
    detailAddr = models.TextField() # 근무지 상세주소
    empTpCd = models.IntegerField() # 고용형태코드
    jobsCd = models.IntegerField() # 직종코드
    smodifyDtm = models.DateField() # 최종수정일
    prefCd = models.TextField() # 우대조건

    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_ann_set')

