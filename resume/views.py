from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView
from .models import Resume, WorkExperience, SkillCategory
from .forms import ResumeForm, WorkExperienceFormSet, SkillCategoryFormSet
from dashboard import notification
from django.db.models.deletion import ProtectedError

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
            return JsonResponse({'success': True}) if request.is_ajax() else redirect("resume_page")
        else:
            return JsonResponse({'error': notification.clean_errors(form.errors)}) if request.is_ajax() else redirect("new_resume")


@method_decorator(decorators, name='dispatch')
class ResumeListView(ListView):
    """
    View for listing resumes. Paginated list view.
    """
    model = Resume
    template_name = 'resume/resume_page.html'
    context_object_name = 'resumes'
    paginate_by = 10  # Pagination

    def get_queryset(self):
        return Resume.objects.filter(created_by=self.request.user).order_by('-created_at')


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
            resume = get_object_or_404(Resume, id=resume_id, created_by=request.user)
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
    data_list = Resume.objects.filter(created_by=request.user).order_by('-created_at')

    items = {}
    for resume in data_list:
        items[str(resume.id)] = resume.full_name

    return JsonResponse(items)
