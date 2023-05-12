
from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import Bootstrapmodelform



class UserAddForm(Bootstrapmodelform):
    name=forms.CharField(min_length=3,label="用户名")
    class Meta:
        model=models.UserInfo
        fields=["name","password","account","age","create_time","gender"]



class MobileAdd(Bootstrapmodelform):
    mobile=forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')]
    )
    class Meta:
        model=models.Mobile
        fields="__all__"
    def clean_mobile(self):
        txt_mobile=self.cleaned_data['mobile']
        exist=models.Mobile.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exist:
            raise ValidationError("手机号已经存在")
        return txt_mobile
# Create your views here.
