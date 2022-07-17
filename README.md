README
## How to run this project on your localactivate  machine
- ✍️✍️✍️✍️✍️✍️✍️✍️✍️✍️
How to setup the project on your local machine.

1. Create a virtual environment on your machine.

2. Fork and clone the repository to the virtual environment.

3. In the project main directory locate 
ecfr_project->settings.py
Edit the database setting for your own MYSQL server 

4. Open your terminal to the project root directory and enter:
python manage.py runserver

Copy and paste the url given

5. Open another terminal and run
python manage.py migrate

python manage.py createsuperuser

Enter username and password skip email with "enter key"

7. You can now login with your username and password.

🤠🤠🤠🤠🤠

[30/12/2021 3:30 PM] Sylvanus Jerome: ❗❗❗❗❗❗
Do this before step 4 to install modules

Install python pip in your virtual environment

And run


pip install -r requirements.txt

❗❗❗❗


# cd documents/python_scripts/ecfr_project
# cd ../../users/sylvanus jerome/documents/python_scripts/ecfr_project
heroku git:remote -a herokudjangoapp
heroku apps -a appName --tail
heroku login -i
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


git config --global user.name ""
git config --global user.email ""
git config -l
git config --global credential.helper cache
git config --global --unset credential.helper
# python manage.py inspectdb

# u,created = User.objects.get_or_create(username=v, password=v)



#for setting up .gitignore while deleting already tracked files
#git config --global core.excludesfile ~/.gitignore_global
#git rm -r --cached .
#git add .
#git commit -m ".gitignore is now working"

#for checking track files
#git ls-tree -r master --name-only
#git ls-tree --full-tree --name-only -r HEAD
#git log --pretty=format: --name-only --diff-filter=A | sort - | sed '/^$/d'




@login_required
@allowed_users(allowed_roles=['exam_n_record','hod'])
@verify_email
def upload_result(request):
    context = {}
    if request.method == "POST":
        form = UploadResultForm(request.POST, request.FILES)
        print(request.FILES.get('excel_file'))
        if form.is_valid():
            file = request.FILES.get('excel_file')
            level = request.POST['level']
            semester = request.POST['semester']
            courses = request.POST['courses']
            section = request.POST['section']
            # check if it is hod
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            check_lec = inf.check_if_hod(group,level,semester,courses,section)
            if check_lec:
                # print('hoddddddddd')
                messages.success(request, 'This result already exist. Please visit the admin for any update')
                return redirect('results:declare_result')
            else:
                # print('not hoddddddddd')
                wb = load_workbook(file, data_only=True)
                # print(wb.sheetnames)
                sheet = wb['Sheet1']
                df = pd.DataFrame(sheet.values)
                df.columns = df.iloc[0]
                df = df.iloc[1:,[1,8,9,10]]
                resultFile = form.save()
                # print(df)
                for row in range(len(df.index)):
                    col=0
                    result=[]
                    for v in df.iloc[row]:
                        # print("col "+str(col))
                        if col == 0:
                            mat=v
                            user = User.objects.values('id').filter(username=v)
                            st = Student.objects.values('id').filter(mat_no=v)       
                            # new entry to find out out entry in the database
                            new_entry =[int(resultFile.level),int(resultFile.semester),int(resultFile.courses.id)]
                            # new_entry =[int(level),int(semester),int(courses)]
                            for user in user:
                                user = user['id']
                                print(user)
                            # compared_output = inf.compare_result_entry(user,new_entry)
                            # # if empty
                            if not user:
                                userr = User.objects.create_user(username=v, password=v)
                                user = userr.id
                                group = Group.objects.get(name='students')
                                userr.groups.add(group)
            
                                st = Student.objects.create(student=userr, mat_no=v, student_level=resultFile.level)
                                st_id=st.id
                            
                            compared_output = inf.compare_result_entry(user,new_entry)                        
                        else:
                            result.append(v)
                        col+=1
                    print(result)
                    if compared_output==0:
                        resultInserted = Results.objects.create(
                                result_details=resultFile,
                                mat_no=mat, courses=resultFile.courses,
                                units=result[0],grades=result[1],remarks=result[2],
                                semester=resultFile.semester
                                )
                        resultInserted = resultInserted.id
                        print("resultInserted "+str(resultInserted))
                    else:
                        print('olllddd entry')
                        l2 = []
                        l2.append(result[0])
                        l2.append(result[1])
                        print(l2)
                        entry_diff = inf.compare_n_update_result(user,l2)
                        if entry_diff==0:
                            resultUpdated = Results.objects.filter(
                                mat_no=mat,
                                courses=resultFile.courses
                                ).update(
                                units=result[0],grades=result[1]
                                )
                return redirect('results:declare_result')

        else:
            print(form.errors)
            # messages.success(request, 'Account was created for ' + username)
            return redirect('results:declare_result')
    else:
        form = UploadResultForm()
        context['main_page_title'] = 'Declare Students Result'
        context['panel_name'] = 'Results'
        context['panel_title'] = 'Declare Result'
        context['form'] = form
    return render(request, "results/declareresult_form.html", context)




<div class="row">
    <div class="col-sm-5">
        <div class="dataTables_info" id="example_info" role="status" aria-live="polite">Showing 1 to 1 of 1
            entries</div>
    </div>
    <div class="col-sm-7">
        <div class="dataTables_paginate paging_simple_numbers" id="example_paginate">
            <ul class="pagination">
                <li class="paginate_button previous disabled" id="example_previous"><a href="#" aria-controls="example"
                        data-dt-idx="0" tabindex="0">Previous</a></li>
                <li class="paginate_button active"><a href="#" aria-controls="example" data-dt-idx="1" tabindex="0">1</a></li>
                <li class="paginate_button next disabled" id="example_next"><a href="#" aria-controls="example"
                        data-dt-idx="2" tabindex="0">Next</a></li>
            </ul>
        </div>
    </div>
</div>




