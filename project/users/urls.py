from django.urls import path
from .views import *

urlpatterns = [
    path('login_user/', login_user, name='login-user'),
    path('logout_user/', logout_user, name='logout-user'),
    path('register/student', register_user, name='register-student'),
    path('register/club_rep', register_clubrep_user, name='register-club-user'),
    path('register/back_office', register_backoffice_user , name='register-backoffice-user'),
    
    path('clubrep/accounts', get_clubRep_accounts , name='clubrep-accounts'),
    path('students/accounts', get_student_accounts , name='student-accounts'),
    path('clubrep/accounts/<int:pk>/update', update_clubRep_accounts , name='clubrep-update'),
    path('clubrep/accounts/<int:pk>/delete', delete_clubRep_accounts , name='clubrep-delete'),
    path('student/account/<int:pk>/update', update_student_accounts , name='student-update'),
    path('student/account/<int:pk>/delete', delete_student_accounts , name='student-delete'),

    path('register/clubs', register_club , name='register-club'),
    path('clubs/', get_clubs , name='clubs'),
    path('clubs/<int:pk>/update', update_club , name='club-update'),
    path('clubs/<int:pk>/delete', delete_club , name='club-delete'),
]
