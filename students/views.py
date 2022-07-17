from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from hod.models import Hod
# from results.models import Results
# from results.forms import CheckResultForm

from subjects.models import Subject
# from helpers import inner_functions as inf
from helpers.decorators import verify_email, unauthenticated_user, allowed_users, admin_only
from hod.forms import UpdateUserForm


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['cls'] = Hod.objects.count()
        # context['results'] = Results.objects.count()
        context['students'] = Student.objects.count()
        context['subjects'] = Subject.objects.count()
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student Creation'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Create Student'
        return context

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    field_list = [
        'Student Name', 'Mat. No', 'Class', 'Level', 'Date of birth'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Students'
        context['panel_name']   =   'Students'
        context['panel_title']  =   'View Students Info'
        context['field_list']   =   self.field_list
        return context

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name_suffix = '_form'
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Update Student Info'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Update Student info'
        return context

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name_suffix = '_delete'
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student Delete Confirmation'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Delete Student'
        return context


@allowed_users(allowed_roles=['students','hod'])
@login_required
def student_edit(request):
    student = get_object_or_404(User, pk=request.user.id)
    st_details = get_object_or_404(Student, student=request.user.id)
    form = UpdateUserForm(instance=student)
    sec_form = StudentForm(instance=st_details)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=student)
        sec_form = StudentForm(request.POST, instance=st_details)
        if form.is_valid() and sec_form.is_valid():
            user = form.save()
            user_details = sec_form.save()

            username = request.user         
            messages.success(request, 'Account was updated for ' + str(username))
            return redirect('students:dashboard')
    context = {'form':form,
        'sec_form':sec_form,
        'main_page_title':'Update Student',
        'panel_name':'Students',
        'panel_title':'Update Student'
        }
    return render(request, "hod/hod_form.html", context)




