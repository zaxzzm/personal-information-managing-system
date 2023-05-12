from django.shortcuts import render,redirect
from app01 import models


def depart_list(request):
    data_list=models.Department.objects.all()
    return render(request,'depart_list.html',{'datalist':data_list})


def depart_add(request):
    if request.method=="GET":
        return render(request,'depart_add.html')
    title=request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/list/")


def depart_delete(request):
    id=request.GET.get('id')
    models.Department.objects.filter(id=id).delete()
    return redirect("/depart/list/")


def depart_edit(request,nid):
    if request.method=="GET":
        object=models.Department.objects.filter(id=nid).first()
        return render(request,'depart_edit.html',{'object':object})
    title=request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")