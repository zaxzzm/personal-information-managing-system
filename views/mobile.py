from django.shortcuts import render,redirect
from app01 import models
from django.utils.safestring import mark_safe
from app01.utils.form import MobileAdd


def mobile_list(request):

    data_dict={}
    search_data=request.GET.get('q',"")

    page_size = 10
    page = int(request.GET.get('page', 1))
    start = (page - 1) * page_size
    end = page * page_size
    total_count=models.Mobile.objects.filter(**data_dict).count()
    total_page_count,div=divmod(total_count,page_size)
    if div:
        total_page_count+=1
    page_str_list=[]
    for i in range(1,total_page_count+1):
        ele='<li><a href="?page={}">{}</a></li>'.format(i,i)
        page_str_list.append(ele)
    page_string=mark_safe("".join(page_str_list))
    if search_data:
        data_dict["mobile__contains"]=search_data
    datalist=models.Mobile.objects.filter(**data_dict)[start:end]
    return render(request,'user_mobile.html',{"datalist":datalist,"search_data":search_data,"page_string":page_string})
def mobile_add(request):
    if request.method=="GET":
        form=MobileAdd()
        return  render(request,'mobile_add.html',{"form":form})
    form=MobileAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/mobile/list/")
    return render(request,'mobile_add.html',{"form":form})
def mobile_edit(request,nid):
    row_object=models.Mobile.objects.filter(id=nid).first()
    if request.method=="GET":
        form=MobileAdd(instance=row_object)
        return render(request,"mobile_edit.html",{"form":form})
    form = MobileAdd(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/mobile/list")
    return render(request,"mobile_edit.html",{"form":form})
def mobile_delete(request,nid):
    models.Mobile.objects.filter(id=nid).delete()
    return redirect("/mobile/list/")