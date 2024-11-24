from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path("",views.index),
   # **********************************admin************************************
   path("admin_login",views.admin_login),
   path("admin_login_data",views.admin_login_data),
   path("admin_login_success",views.admin_login_success),
   path("admin_logout",views.admin_logout),
   path("post_event",views.post_event),
   path("post_event_data",views.post_event_data),
   path("view_event",views.view_event),
   path("event_delete/<int:id>",views.event_delete),
   path("full_view_event/<int:id>",views.full_view_event),
   path("student_register/<int:id>",views.student_register),
   path("admin_view_feedback",views.admin_view_feedback),
   # **********************************user**********************************
   path("user_register",views.user_register),
   path("login_check",views.login_check),
   path("user_login_success",views.user_login_success),
   path("user_logout",views.user_logout),
   path("feeback_menu",views.feeback_menu),
   path("feeback_data/<int:id>",views.feeback_data),
   path("rating_data",views.rating_data),

]