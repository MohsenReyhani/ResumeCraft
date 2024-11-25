from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import ResumeView, ResumeListView, remove_resume, resume_all_list, print_resume, ResumeViewV02


urlpatterns = [
    # Index - List of resumes
    path('', ResumeListView.as_view(), name="resume"),
    # API endpoint for fetching all resumes (without pagination)
    path('v1/api/', resume_all_list, name="resume_all"),
    # Create a new resume
    path('create/', ResumeViewV02.as_view(), name='create_resume'),
    # Edit an existing resume
    path('edit/<int:resume_id>/', ResumeViewV02.as_view(), name='edit_resume'),
    path('print/<int:resume_id>/', print_resume, name='print_resume'),
    # Remove a resume (AJAX)
    path('remove/', remove_resume, name='remove_resume'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)