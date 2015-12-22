from django.shortcuts import render,redirect, get_object_or_404

def detail_view(request,pk,obj_class):
  obj_name = obj_class.__name__.lower()
  obj = get_object_or_404(obj_class,pk=pk)
  
  return render(request, '%ss/detail.html' % obj_name, {"obj_name": obj})