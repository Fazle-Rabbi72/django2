
from django.shortcuts import redirect
from django.contrib import messages
from . import forms
from . import models
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class DetailsCarView(DetailView):
    model = models.Car
    template_name='car_details.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Retrieve the car object
        comment_form = forms.CommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = self.object  # Assign the car to the comment
            new_comment.save()
            messages.success(self.request,"Comment Has Been Added Successfully!")
            # Redirect to the same page to avoid re-posting the comment
            return redirect('car_details', pk=self.object.pk)
        else:
            return self.get(request, *args, **kwargs)  

    def get_context_data(self,**kwargs) :
        context=super().get_context_data(**kwargs)
        car=self.object
        comments=car.comments.all()
        comment_form=forms.CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form        
        return context
