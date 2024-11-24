from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView
from django.db.models.deletion import ProtectedError

from .models import Resume, WorkExperience, SkillCategory, JsonResume
from .forms import ResumeForm, WorkExperienceFormSet, SkillCategoryFormSet, JsonResumeForm
from dashboard import notification
from dashboard.views import BaseListView

# Decorators for caching and login requirement
decorators = [never_cache, login_required]

@method_decorator(decorators, name='dispatch')
class ResumeView(FormView):
    """
    View for creating and editing a resume.
    Uses GET to show the form and POST to handle form submission.
    """

    def get(self, request, resume_id=None):
        is_edit = True if resume_id else False
        resume = get_object_or_404(Resume, id=resume_id, created_by=request.user) if resume_id else None

        form = ResumeForm(instance=resume)
        work_experience_formset = WorkExperienceFormSet(instance=resume)
        skill_category_formset = SkillCategoryFormSet(instance=resume)

        context = {
            'is_edit': is_edit,
            'form': form,
            'work_experience_formset': work_experience_formset,
            'skill_category_formset': skill_category_formset,
            'segment': 'resume',
        }

        if is_edit:
            context['resume_id'] = resume_id

        return render(request, 'resume/new_resume.html', context)

    def post(self, request, resume_id=None):
        isSuccess = False
        is_edit = True if resume_id else False
        resume = get_object_or_404(Resume, id=resume_id, created_by=request.user) if is_edit else None

        form = ResumeForm(request.POST, request.FILES, instance=resume)
        work_experience_formset = WorkExperienceFormSet(request.POST, instance=resume)
        skill_category_formset = SkillCategoryFormSet(request.POST, instance=resume)

        if form.is_valid() and work_experience_formset.is_valid() and skill_category_formset.is_valid():
            resume = form.save(commit=False)
            resume.created_by = request.user
            resume.save()

            work_experience_formset.instance = resume
            skill_category_formset.instance = resume
            work_experience_formset.save()
            skill_category_formset.save()

            notification.create_edit_was_success(request, is_edit, "Resume")
            isSuccess = True
        else:
            notification.unkown_prosses_form(request, form.errors)

        if isSuccess:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                if 'btn-show-resume-print' in request.POST:
                    # Redirect to the resume print preview page
                    return redirect('print_resume', resume_id=resume.id)
                else:
                    # Default success redirect
                    return redirect("resume")
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': notification.clean_errors(form.errors)})
            else:
                return redirect("create_resume")
                

@method_decorator(decorators, name='dispatch')
class ResumeViewV02(FormView):
    """
    View for creating and editing a resume.
    Uses GET to show the form and POST to handle form submission.
    """

    def get(self, request, resume_id=None):
        is_edit = True if resume_id else False
        resume = get_object_or_404(JsonResume, id=resume_id, created_by=request.user) if resume_id else None

        form = JsonResumeForm(instance=resume)
        context = {
            'is_edit': is_edit,
            'form': form,
            'segment': 'resume',
        }

        if is_edit:
            context['resume_id'] = resume_id

        return render(request, 'resume/new_json_resume.html', context)

    def post(self, request, resume_id=None):
        isSuccess = False
        is_edit = True if resume_id else False
        resume = get_object_or_404(JsonResume, id=resume_id, created_by=request.user) if is_edit else None

        form = JsonResumeForm(request.POST, request.FILES, instance=resume)

        if form.is_valid():
            resume = form.save(commit=False)
            resume.created_by = request.user
            resume.save()

            notification.create_edit_was_success(request, is_edit, "Resume")
            isSuccess = True
        else:
            notification.unkown_prosses_form(request, form.errors)

        if isSuccess:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                if 'btn-show-resume-print' in request.POST:
                    # Redirect to the resume print preview page
                    return redirect('print_resume', resume_id=resume.id)
                else:
                    # Default success redirect
                    return redirect("resume")
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': notification.clean_errors(form.errors)})
            else:
                return redirect("create_resume")


class ResumeListView(BaseListView):
    model = Resume
    template_name = 'resume/resume_page.html'
    segment = 'resume'
    search_fields = ['title']


# for print reumse page
@never_cache
@login_required(login_url="/app/accounts/login/")
def print_resume(request, resume_id=None):

    # Get the resume object
    resume = get_object_or_404(JsonResume, id=resume_id)
    
    context = {
        "resume": resume,
        "segment": "print",
    }

    return render(request, "resume/resume_json_print.html", context)



# Removing a resume via AJAX
@never_cache
@login_required(login_url="/app/accounts/login/")
def remove_resume(request):
    """
    AJAX view for removing a resume.
    """
    try:
        if request.method == 'POST':
            resume_id = request.POST.get('item_id')
            resume = get_object_or_404(JsonResume, id=resume_id, created_by=request.user)
            resume.delete()

            notification.remove_was_success(request)

            return JsonResponse({'success': True})

        return JsonResponse({'success': False})

    except ProtectedError:
        return JsonResponse({'success': False, "error": "There are dependencies linked to this resume. Please remove them first."})


# Fetch all resumes without pagination
@never_cache
@login_required(login_url="/app/accounts/login/")
def resume_all_list(request):
    """
    View to return all resumes created by the logged-in user in a dictionary format via JSON.
    """
    data_list = JsonResume.objects.filter(created_by=request.user).order_by('-created_at')

    items = {}
    for resume in data_list:
        items[str(resume.id)] = resume.full_name

    return JsonResponse(items)
