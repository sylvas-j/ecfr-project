# from xhtml2pdf import pisa
# from django.template.loader import get_template
from django.http import HttpResponse
# from io import BytesIO
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
# from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.db.models import Q
# from django.http import JsonResponse
from django.urls import reverse_lazy

from helpers.decorators import verify_email, unauthenticated_user, allowed_users, admin_only
from hod.models import Hod
from subjects.models import Subject, SubjectRegistered
from students.models import Student

@unauthenticated_user
def index(request):
    # template_name = "index.html"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("\nUser Name = ",username)
        print("Password = ",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'students':
                return redirect('students:dashboard')
            else:
                return redirect('ecfr_admin:dashboard')
            # return redirect('ecfr_admin:dashboard')
        else:
            context = {'message':'Invalid User Name and Password'}
            return render(request, 'index.html', context)
    return render(request, 'index.html', {'name': 'ecfr,hodoffice,student', 'pass': 'Ecfr@123'})


def verify_email_view(request):
    mat=request.GET['mat']
    user_type=request.GET['user_type']
    mat=mat.replace('|','/')
    if user_type=='students':
        u = Student.objects.filter(mat_no=mat).update(active=1)
    else:
        u = Hod.objects.filter(mat_no=mat).update(active=1)
    return HttpResponse('Email verified!')
        

def logoutUser(request):
    logout(request)
    return redirect('home')


# from django.contrib.auth.decorators import login_required

# @unauthenticated_user
class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    # @login_required
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['cls'] = Hod.objects.count()
        # context['results'] = Results.objects.count()
        context['students'] = Student.objects.count()
        context['subjects'] = Subject.objects.count()
        context['approved'] = SubjectRegistered.objects.filter(status='Approved').count()
        context['pending'] = SubjectRegistered.objects.filter(status='Pending').count()
        return context
    
class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('ecfr_admin:dashboard')
    template_name = 'password_change_form.html'

    
    def get_context_data(self, **kwargs):
        context = super(PasswordChangeView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Admin Change Password'
        context['panel_title'] = 'Admin Change Password'
        return context



def search_table(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        action = request.GET.get('action')
        print(query)
        print(action)
        if query is not None:
            if action == 'Courses':
                lookups= Q(subject_name__icontains=query)
                queries = Subject.objects.filter(lookups).order_by('subject_name')
                field_list = ['Subject Name', 'Subject Code', 'Creation Date', 'Last Updated'
                            ]
                context={'object_list':queries,
                        'field_list':field_list
                        }
                return render(request, 'subjects/subject_list_table.html', context)
            elif action == 'Students Mat No':
                lookups= Q(mat_no__icontains=query)
                queries = Student.objects.filter(lookups).order_by('mat_no')
                field_list = ['Student Name', 'Mat. No', 'Class', 'Level', 'Date of birth']
                context={'object_list':queries,
                        'field_list':field_list
                        }
                return render(request, 'students/student_list_table.html', context)
            elif action == 'Hod ID':
                lookups= Q(mat_no__icontains=query)
                queries = Hod.objects.filter(lookups).order_by('mat_no')
                field_list = ['Hod Name', 'Mat No','Gender','Date of birth']
                context={'object_list':queries,
                        'field_list':field_list
                        }
                return render(request, 'hod/hod_list_table.html', context)
            elif action == 'Result Files':
                lookups= Q(mat_no__icontains=query)
                # queries = UploadResu?lt.objects.filter(lookups).order_by('section')
                queries=list(UploadResult.objects
                .filter(section__icontains=query).values('section','level','semester','courses__subject_name','courses__subject_code','excel_file')
                .order_by('-section'))
            
                field_list = ['Section','Level','Semester','Courses']
                context={'object_list':queries,
                        'field_list':field_list
                        }
                return render(request, 'results/result_files_table.html', context) 
            else:
                pass
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))












