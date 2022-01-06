from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name="main"),
    
    path('create_post', views.createPost, name="create_post"),
    path('update_post/<str:pk>', views.updatePost, name="update_post"),
    path('delete_post/<str:pk>', views.deletePost, name="delete_post"),
    path('post_table', views.postTable, name="post_table"),


    path('create_mentor', views.createMentor, name="create_mentor"),
    path('mentors_table', views.mentorsTable, name="mentors_table"),
    path('update_mentor/<str:pk>', views.updateMentor, name="update_mentor"),
    path('delete_mentor/<str:pk>', views.deleteMentor, name="delete_mentor"),


    path('create_students', views.create_students, name="create_students"),
    path('update_student/<str:pk>', views.updateStudent, name="update_student"),
    path('delete_student/<str:pk>', views.deleteStudent, name="delete_student"),
    path('students_table', views.students_table, name="students_table"),


    path('groups_table', views.groups_table, name="groups_table"),
    path('create_group', views.createGroup, name="create_group"),
    path('update_group/<str:pk>', views.updateGroup, name="update_group"),
    path('delete_group/<str:pk>', views.deleteGroup, name="delete_group"),


    path('register', views.register_user, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
]
