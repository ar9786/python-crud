from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
  #  path('student-list/', views.student_list),
  #  path('stuinfo/<int:pk>', views.student_detail),
  # path('student-create/', views.student_create),  
    path('employee-list/', views.Employee.as_view()),
    path('employee/<int:pk>', views.EmployeeUpdated.as_view()),
    path('course-details/',views.CourseList.as_view(),name='course_details'),
    path('course-details-list/',views.CourseDetailsList.as_view(),name='course_details_list'),
    path('course-details-condt/',views.getData,name='course_details_condt'),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh-token/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verify-token/',TokenVerifyView.as_view(),name='token_verify'),
    path('check-celery/',views.checkCelery,name='checkCelery')
]
