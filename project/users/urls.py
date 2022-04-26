from django.urls import path
from .views import *

urlpatterns = [
    path('login_user/', login_user, name='login-user'),
    path('logout_user/', logout_user, name='logout-user'),
    path('register/student', register_user, name='register-student'),
    path('register/club_rep', register_clubrep_user, name='register-club-user'),
    path('register/back_office', register_backoffice_user , name='register-backoffice-user'),
    
    path('clubs', get_clubRep_accounts , name='club-accounts'),
    path('students', get_student_accounts , name='student-accounts'),
    path('clubs/update', update_clubRep_accounts , name='club-update'),
    path('clubs/delete', delete_clubRep_accounts , name='club-delete'),
    path('students/update', update_student_accounts , name='student-update'),
    path('students/delete', delete_student_accounts , name='student-delete')
]
