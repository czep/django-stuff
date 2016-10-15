from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Stuff

class StuffForm(ModelForm):
    class Meta:
        model = Stuff
        fields = ['junk', 'things', 'somenum']

def stuff_list(request, template_name='stuff/stuff_list.html'):
    stuff = Stuff.objects.all()
    data = {}
    data['object_list'] = stuff
    return render(request, template_name, data)

@login_required
def stuff_create(request, template_name='stuff/stuff_form.html'):
    form = StuffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('stuff_list')
    return render(request, template_name, {'form':form})

@login_required
def stuff_update(request, pk, template_name='stuff/stuff_form.html'):
    stuff = get_object_or_404(Stuff, pk=pk)
    form = StuffForm(request.POST or None, instance=stuff)
    if form.is_valid():
        form.save()
        return redirect('stuff_list')
    return render(request, template_name, {'form':form})

@login_required
def stuff_delete(request, pk, template_name='stuff/stuff_confirm_delete.html'):
    stuff = get_object_or_404(Stuff, pk=pk)    
    if request.method=='POST':
        stuff.delete()
        return redirect('stuff_list')
    return render(request, template_name, {'object':stuff})
