import os
import json

# comfirm student result record if it exist
def compare_result_entry(u,l2):
    r=Results.objects.filter(student=u).values_list('result_details__level','result_details__semester','result_details__courses').distinct()
    l1=[]
    for r in r:
        for r in r:
            l1.append(int(r))
    if (l1==l2):
        return 1
    else:
        return 0


def compare_n_update_result(u,l2):
    r=Results.objects.filter(student=u).values_list('units','grades').distinct()
    l1=[]
    for r in r:
        for r in r:
            l1.append(int(r))
    if (l1==l2):
        return 1
    else:
        return 0


# def dev_prod():
#     if os.environ['dev_prod'] = 'local':
#         return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecfr_project.settings.development')
#     else:
#         return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecfr_project.settings.production')

def get_credentials():
    env_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.paht.join(env_file_dir, '.env.json'), 'r') as f:
        creds = json.loads(f.read())
    return creds


credentials = get_credentials()