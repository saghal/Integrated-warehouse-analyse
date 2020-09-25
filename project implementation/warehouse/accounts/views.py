from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from .forms import SignUpForm
from django.urls import reverse, reverse_lazy



def newcontract(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('newcontract')
    else:
        form = SignUpForm()
    return render(request, 'accounts/newcontract.html', {'form': form})


def contracts(request):

    all_users = get_user_model().objects.all()

    context = {'allusers': all_users}

    return render(request, 'accounts/contracts.html', context)

class ContractListView(ListView):
    model = get_user_model()
    template_name = 'accounts/contracts.html'
    context_object_name = 'contracts'


class ContractUpdateView(UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'email']
    template_name = 'accounts/contract_detail.html'
    reverse_lazy('contracts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

