from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

from helpers import inner_functions as inf
from helpers.decorators import unauthenticated_user, allowed_users, admin_only
from .models import Hod,HodCourses
from .forms import HodForm, HodCoursesForm, CreateUserForm, UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# @login_required(login_url='admin_panels:login')
@allowed_users(allowed_roles=['exam_n_record'])
@admin_only
def hod_create(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='hod')
            user.groups.add(group)
            lec = Hod.objects.create(hod=user)
                            
            messages.success(request, 'Account was created for ' + username)
            return redirect('hod:hod_list')
    context = {'form':form,
        'main_page_title':'Hod Creation',
        'panel_name':'Hod',
        'panel_title':'Create Hod'
        }
    return render(request, "hod/hod_form.html", context)


@allowed_users(allowed_roles=['exam_n_record','hod','hod'])
@login_required
def hod_edit(request):
    hod = get_object_or_404(User, pk=request.user.id)
    lec_details = get_object_or_404(Hod, hod=request.user.id)
    form = UpdateUserForm(instance=hod)
    sec_form = HodForm(instance=lec_details)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=hod)
        sec_form = HodForm(request.POST, instance=lec_details)
        if form.is_valid() and sec_form.is_valid():
            user = form.save()
            user_details = sec_form.save()

            username = request.user         
            messages.success(request, 'Account was updated for ' + str(username))
            return redirect('ecfr_admin:dashboard')
    context = {'form':form,
        'sec_form':sec_form,
        'main_page_title':'Update Hod',
        'panel_name':'Hod',
        'panel_title':'Update Hod'
        }
    return render(request, "hod/hod_form.html", context)


@allowed_users(allowed_roles=['exam_n_record','hod','hod'])
def hod_list(request):
    context={}
    field_list = [
        'Hod Name', 'Mat No','Gender','Date of birth'
    ]
    # lec = Hod.objects.all().order_by('mat_no').distinct()
    lec = Hod.objects.filter(hod_reg__lte=timezone.now()).order_by('mat_no')
    lec = inf.pagenate(request,lec,1000)
        
    context['main_page_title'] = 'Manage Hod'
    context['panel_name']   =   'Hod'
    context['panel_title']  =   'View Hod Info'
    context['field_list']   =   field_list
    context['object_list']   =   lec
    # print(lec)
    return render(request, 'hod/hod_list.html', context)


@login_required
@allowed_users(allowed_roles=['exam_n_record','hod','hod'])
def hod_detail(request, pk):
    hod = get_object_or_404(Hod, pk=pk)
    if request.method == "POST":
        form = HodForm(request.POST, instance=hod)
        if form.is_valid():
            state = form.save()
    else:
        form = HodForm(instance=hod)
    context = {'form':form,
        'main_page_title':'Hod Creation',
        'panel_name':'Hod',
        'panel_title':'Update Hod',
        'hod': hod
        }
    return render(request, 'hod/hod_form.html', context)


# @allowed_users(allowed_roles=['exam_n_record'])
# def hod_courses(request):
#     form = HodCoursesForm()
#     if request.method == 'POST':
#         form = HodCoursesForm(request.POST)
#         if form.is_valid():
#             user = form.save()
                            
#             messages.success(request, 'Course Attached')
#             return redirect('hod:hod_courses_list',pk=user.hod.id)
#     context = {'form':form,
#         'main_page_title':'Hod Creation',
#         'panel_name':'Hod',
#         'panel_title':'Create Hod'
#         }
#     return render(request, "hod/hod_form.html", context)


@allowed_users(allowed_roles=['exam_n_record','hod','hod'])
def hod(request):
    context={}
    field_list = [
        'Hod Name'
    ]
    hod_courses = Hod.objects.filter(hod_reg__lte=timezone.now()).order_by('mat_no')
    hod_courses = inf.pagenate(request,hod_courses,1000)
    
    context['main_page_title'] = 'Manage Hod Courses'
    context['panel_name']   =   'Hod'
    context['panel_title']  =   'View Hod Courses'
    context['field_list']   =   field_list
    context['hod']   =   hod_courses
    return render(request, 'hod/hod_list.html', context)


# @allowed_users(allowed_roles=['exam_n_record','hod','hod'])
# def hod_courses_list(request, pk):
#     context={}
#     field_list = [
#         'Courses'
#     ]
#     courses = HodCourses.objects.filter(
#         hod_reg__lte=timezone.now(),
#         hod=pk).values('id','courses__subject_name','courses__subject_code')
#     courses = inf.pagenate(request,courses,1000)
#     # print(courses)
#     context['main_page_title'] = 'Manage Hod Courses'
#     context['panel_name']   =   'Hod'
#     context['panel_title']  =   'View Hod Courses'
#     context['field_list']   =   field_list
#     context['courses']   =   courses
#     return render(request, 'hod/hod_list.html', context)


# def delete_course(request, pk):
#     course = get_object_or_404(HodCourses, pk=pk)
#     course.delete()
#     # print(course.hod.id)
#     return redirect('hod:hod_courses_list', pk=course.hod.id)

# Create your views here.
