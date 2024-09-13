from django.urls import path
from .views import ResumeView, ResumeListView, remove_resume, resume_all_list, print_resume
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Index - List of resumes
    path('', ResumeListView.as_view(), name="resume"),
    # API endpoint for fetching all resumes (without pagination)
    path('v1/api/', resume_all_list, name="resume_all"),
    # Create a new resume
    path('create/', login_required(ResumeView.as_view()), name='create_resume'),
    # Edit an existing resume
    path('edit/<int:resume_id>/', login_required(ResumeView.as_view()), name='edit_resume'),
    path('print/<int:resume_id>/', print_resume, name='print_resume'),
    # Remove a resume (AJAX)
    path('remove/', remove_resume, name='remove_resume'),
]
