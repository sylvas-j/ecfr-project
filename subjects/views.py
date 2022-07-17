from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectRegistered
from .forms import SubjectForm, SubjectRegisteredForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
import json
from helpers import inner_functions as inf


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Creation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Add Subject'
        return context


class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    field_list = [
        'Subject Name', 'Subject Code', 'Creation Date', 'Last Updated'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Subjects'
        context['panel_name']   =   'Subjects'
        context['panel_title']  =   'View Subjects Info'
        context['field_list']   =   self.field_list
        return context

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name_suffix = '_form'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:subject_list')

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name_suffix = '_delete'
    success_url = reverse_lazy('subjects:subject_list')

    
    def get_context_data(self, **kwargs):
        context = super(SubjectDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Delete Confirmation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Delete Subject'
        return context
    
class SubjectRegisteredCreateView(LoginRequiredMixin, CreateView):
    model = SubjectRegistered
    form_class = SubjectRegisteredForm
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(SubjectRegisteredCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'SubjectCombination Creation'
        context['panel_name'] = 'SubjectConbinations'
        context['panel_title'] = 'Create SubjectConbination'
        return context

class SubjectRegisteredListView(LoginRequiredMixin, ListView):
    model = SubjectRegistered
    field_list = [
        'Subject', 'Status',
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Check Courses Registered'
        context['panel_name']   =   'Courses Registered'
        context['panel_title']  =   'View Courses Registered Info'
        context['field_list']   =   self.field_list
        return context

class SubjectRegisteredUpdateView(LoginRequiredMixin, UpdateView):
    model = SubjectRegistered
    template_name_suffix = '_form'
    form_class = SubjectRegisteredForm
    success_url = reverse_lazy('subjects:subject_registered_list')

class SubjectRegisteredDeleteView(LoginRequiredMixin, DeleteView):
    model = SubjectRegistered
    template_name_suffix = "_delete"
    success_url = reverse_lazy('subjects:subject_registered_list')

    def get_context_data(self, **kwargs):
        context = super(SubjectRegisteredDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'SubjectCombination Delete Confirmation'
        context['panel_name'] = 'SubjectCombinations'
        context['panel_title'] = 'Delete SubjectCombination'
        return context


# Received data fron ajax api to register courses
def subject_reg(request):
    if request.method != "POST":
        data = request.GET['data']
        # print(type(data))
        data = data.strip('][').replace('"','').split(',')
        for x in data:
            # print(x)
            course = get_object_or_404(Subject, pk=x)
            print(course.id)
            new_entry =[int(request.user.id),int(course.id),]
            # check if course is already registered
            compared_output = inf.compare_course_entry(request.user.id,course.id,new_entry)                        
            if compared_output==0:
                print('okiiiiiiii')
                course_reg=SubjectRegistered.objects.create(student=request.user,subject=course)

            messages.success(request, 'Courses registered')
    else:
        print('someting')
    return render(request, 'subjects/subject_list_form.html', {'course':course})
# {{ request.build_absolute_uri | safe }}

def subject_status(request):
    if request.method != "POST":
        data = request.GET['data']
        # print(type(data))
        data = data.strip('][').replace('"','').split(',')
        for x in data:
            # print(x)
            course = get_object_or_404(Subject, pk=x)
            print(course.id)
            new_entry =[int(request.user.id),int(course.id),]
            # check if course is already registered
            compared_output = inf.compare_course_entry(request.user.id,course.id,new_entry)                        
            if compared_output==0:
                print('okiiiiiiii')
                course_reg=SubjectRegistered.objects.create(student=request.user,subject=course)

            messages.success(request, 'Courses registered')
    else:
        print('someting')
    return render(request, 'subjects/subject_list_form.html', {'course':course})
# {{ request.build_absolute_uri | safe }}
