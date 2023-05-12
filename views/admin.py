from django.shortcuts import render,redirect
from app01 import models
from app01.utils.bootstrap import Bootstrapmodelform
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.encrypt import md5


class Adminmodelform(Bootstrapmodelform):
    confirm_password=forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model=models.Admin
        fields=["user_name","password","confirm_password"]
        widgets={
            "password":forms.PasswordInput(render_value=True)
        }
    def clean_password(self):
        pwd=self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd=self.cleaned_data.get("password")
        confirm=md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm
class AdminEditForm(Bootstrapmodelform):
    class Meta:
        model=models.Admin
        fields=["user_name"]
class AdminResetForm(Bootstrapmodelform):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )
    class Meta:
        model=models.Admin
        fields=["password","confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }
    def clean_password(self):
        pwd=self.cleaned_data.get("password")
        md5_pwd=md5(pwd)

        exists=models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError('密码与先前重复')
        return md5_pwd

    def clean_confirm_password(self):
        pwd=self.cleaned_data.get("password")
        confirm=md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm


def admin(request):

    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["mobile__contains"] = search_data

    datalist=models.Admin.objects.all()
    context={"datalist":datalist,"search_data":search_data}
    return render(request,'admin_list.html',context)
def add(request):
    title='新建管理员'
    '''添加管理员'''
    if request.method=="GET":
        form=Adminmodelform()
        return render(request,"change.html",{"title":title,"form":form})

    form=Adminmodelform(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request,"change.html",{"form":form,"title":title})
def edit(request,nid):
    title="编辑管理员"
    row_object=models.Admin.objects.filter(id=nid).first()
    if not row_object:
        msg={"msg":"编号不存在"}
        return render(request,"error.html",msg)
    if request.method=="GET":
        form = AdminEditForm(instance=row_object)
        return render(request,"change.html",{"form":form,"title":title})
    form=AdminEditForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request,"change.html",{"form":form,"title":title})
def reset(request,nid):
    row_object = models.Admin.objects.filter(id=nid).first()

    if not row_object:
        msg = {"msg": "编号不存在"}
        return render(request, "error.html", msg)
    title = "重置密码-{}".format(row_object.user_name)

    if request.method == "GET":
        form=AdminResetForm()
        return render(request,"change.html",{"form":form,"title":title})

    form = AdminResetForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")

    return render(request, "change.html", {"form": form, "title": title})

