from django.shortcuts import render,redirect
from app01 import models
from app01.utils.form import UserAddForm


def user_list(request):
    datalist=models.UserInfo.objects.all()
    return render(request,"user_list.html",{"datalist":datalist})


def user_add2(request):
    if request.method=="GET":
        form=UserAddForm()
        return  render(request,'user_add2.html',{"form":form})
    form=UserAddForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request,'user_add2.html',{"form":form})


def user_edit(request,nid):
    row_object=models.UserInfo.objects.filter(id=nid).first()
    if request.method=="GET":
        form=UserAddForm(instance=row_object)
        return render(request,'user_edit.html',{"form":form})
    form=UserAddForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request,'user_add2.html',{'form':form})

def user_delete(request):
    id=request.GET.get('id')
    models.UserInfo.objects.filter(id=id).delete()
    return redirect("/user/list/")