from django.shortcuts import render, get_object_or_404
from  .models import ChaiVarity,Store
from .forms import ChaiVarityForm
# Create your views here.
def AllChai(request):
    chais= ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def View_Details(request,chai_id):
    chai = get_object_or_404(ChaiVarity,pk=chai_id)
    return  render(request,'chai/chai_detail.html',{'chai' : chai})

def ChaiStores(request):
    stores=None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varitey=form.cleaned_data['chai_varity']
            stores= Store.objects.filter(chai_varity=chai_varitey)
    else:
        form=ChaiVarityForm()
    return render(request,'chai/chai_store.html',{'stores':stores,'form':form})