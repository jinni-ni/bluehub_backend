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
    wantedAuthNo = models.TextField(blank=True) # 구인인증번호
    company = models.TextField() # 회사명
    busino = models.TextField(blank=True) # 사업자등록번호
    title = models.TextField() # 제목
    salTpNm = models.TextField(blank=True) # 임금형태
    sal = models.TextField(blank=True) #급여
    minSal = models.TextField(blank=True) # 최소임금
    maxSal = models.TextField(blank=True) # 최대임금
    region = models.TextField(blank=True) # 근무지역
    holidayTpNm = models.TextField(blank=True) # 근무형태
    minEdubg = models.TextField(blank=True) # 최소학력
    maxEdubg = models.TextField(blank=True) # 최대학력
    career = models.TextField(blank=True) # 경력
    regDt = models.DateField(blank=True, null=True) # 등록일자
    closeDt = models.DateField(blank=True, null=True) # 마감일자
    infoSvc = models.TextField(blank=True) # 정보제공처
    wantedInfoUrl = models.TextField(blank=True) # 워크넷 채용정보 URL
    zipCd = models.TextField(blank=True) # 근무지 우편번호
    strtnmCd = models.TextField(blank=True) # 근무지 도로명주소
    basicAddr = models.TextField(blank=True) # 근무지 기본주소
    detailAddr = models.TextField(blank=True) # 근무지 상세주소
    empTpCd = models.IntegerField(blank=True, null=True) # 고용형태코드
    jobsCd = models.IntegerField(blank=True, null=True) # 직종코드
    smodifyDtm = models.DateField(blank=True, null=True) # 최종수정일
    prefCd = models.TextField(blank=True) # 우대조건

    caption = models.TextField(max_length=500, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_ann_set')

    def __str__(self):
        return self.title

    def extract_tag_list(self):
        tag_name_list = re.findall(r"#[a-zA-Z\dㄱ-힣]+", self.caption)
        tag_list = []
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

    # TODO : get_absolute_url - post 후 detail로 redirect
    # def get_absolute_url(self):
    #     return reverse("recruit:announcement_detail", args=[self.pk])

    def is_like_user(self, user):
        return self.like_user_set.filter(pk=user.pk).exists()

    class Meta:
        ordering = ['-closeDt']

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
