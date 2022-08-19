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
git push heroku master
heroku run python manage.py migrate
ghp_wq8VlPM66ziP7L8xQn5u6nvhuKhcwL3DBp
ghp_5W3dIwKHMpMyQM6zJZfx5iKCcQpv9L0MOR

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




hY

