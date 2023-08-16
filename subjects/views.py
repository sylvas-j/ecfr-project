from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectRegistered
from .forms import SubjectForm, SubjectRegisteredForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

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
        'Subject Name', 'Subject Code','Subject Unit', 'Level','Semester', 'Creation Date', 'Last Updated'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Register Subjects'
        context['panel_name']   =   'Subjects'
        context['panel_title']  =   'View Subjects Info'
        context['field_list']   =   self.field_list
        return context

class SubjectList():
    def subject_list(request):
        if request.method == 'GET':
            level = request.GET['level']
            section = request.GET['section']
            semester = request.GET['semester']
            print('kkkkkkkk', level)
            context={}
            field_list = [
                'Subject','Unit', 'Status',
            ]
            course_status=Subject.objects.filter(subject_level=level, subject_semester=semester)
            context['field_list'] = field_list
            context['object_list'] = course_status
            return render(request, 'subjects/subject_list_form.html', context)

    def subject_student_list(request, pk):
        if request.method == 'GET':
            print('kkkkkkkk')
            context={}
            field_list = [
                'Subject','Unit', 'Status',
            ]
            # course_status = get_object_or_404(SubjectRegistered, pk=pk)
            course_status=SubjectRegistered.objects.filter(student=pk)
            context['main_page_title'] = 'Course Registration Confirmation'
            context['panel_name'] = 'Course Registration'
            context['panel_title'] = 'Approve/Reject Courses'
            context['field_list'] = field_list
            context['object_list'] = course_status
            return render(request, 'subjects/subjectregistered_section.html', context)




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
    

class SubjectReg():
    def subject_reg_status(request):
        context={}
        
        context['reg_button'] = 'reg_button'
        context['main_page_title'] = 'Course Registration Confirmation'
        context['panel_name'] = 'Course Registration'
        context['panel_title'] = 'Courses Registered'
        return render(request, 'subjects/subjectregistered_list.html', context)


    def subject_reg_status_checker(request):
        if request.method == 'GET':
            level = request.GET['level']
            section = request.GET['section']
            semester = request.GET['semester']

            context={}
            field_list = [
                'Subject','Unit', 'Status',
            ]
            course_status=SubjectRegistered.objects.filter(student=request.user, subject__subject_level=level, subject__subject_semester=semester)
            context['field_list'] = field_list
            context['object_list'] = course_status
            return render(request, 'subjects/subjectregistered_section_list.html', context)


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
        if request.GET['data']:
            data = request.GET['data']
            # print(type(data))
            data = data.strip('][').replace('"','').split(',')
            #print(data)
            for x in data:
                # print(x)
                course = get_object_or_404(Subject, pk=x)
                print(course.id)
                new_entry =[int(request.user.id),int(course.id),]
                # check if course is already registered
                compared_output = inf.compare_course_entry(request.user.id,course.id,new_entry)                        
                if compared_output==0:
                    # print('okiiiiiiii')
                    course_reg=SubjectRegistered.objects.create(student=request.user,subject=course)

        #return redirect('subjects:subject_list_form.html')        
        # messages.success(request, 'Courses registered')
    else:
        print('someting')
    return render(request, 'subjects/subject_list_form.html', {'course':course})
# {{ request.build_absolute_uri | safe }}

def subject_status_update(request):
    if request.method == "GET":
        if request.GET['course']:
            data = request.GET['course']
            print(data)
            feedback = {}
            data = data.strip('][').replace('"','').split('-')
            if data[0] == 'approve':
                course_status=SubjectRegistered.objects.filter(subject=data[1]).update(status='Approved')
                feedback['data'] = 'Approved'
            else:
                course_status=SubjectRegistered.objects.filter(subject=data[1]).update(status='Rejected')
                feedback['data'] = 'Rejected'
            
            return JsonResponse(feedback)
    else:
        print('someting')
        return render(request, 'subjects/subjectregistered_list.html')
# {{ request.build_absolute_uri | safe }}
    #     return JsonResponse(data)
    # subjects = None
    # data['result'] = 'you made a request with empty data'
    # return HttpResponse(json.dumps(data), content_type="application/json")
