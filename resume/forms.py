from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Resume
from django import forms
from django.forms import inlineformset_factory
from .models import Resume, WorkExperience, SkillCategory, SubSkill

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['full_name', 'title', 'birth_date', 'contact_email', 'contact_phone', 'linkedin_url', 'profile_image', 'summary']
        labels = {
            'full_name': 'نام کامل',
            'title': 'عنوان شغلی',
            'birth_date': 'تاریخ تولد',
            'contact_email': 'ایمیل تماس',
            'contact_phone': 'شماره تماس',
            'linkedin_url': 'لینک پروفایل LinkedIn',
            'profile_image': 'تصویر پروفایل',
            'summary': 'خلاصه حرفه‌ای',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'نام کامل خود را وارد کنید', 
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'عنوان شغلی خود را وارد کنید', 
                'class': 'form-control'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date', 
                'placeholder': 'تاریخ تولد خود را وارد کنید', 
                'class': 'form-control'
            }),
            'contact_email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل خود را وارد کنید', 
                'class': 'form-control'
            }),
            'contact_phone': forms.TextInput(attrs={
                'placeholder': 'شماره تماس خود را وارد کنید', 
                'class': 'form-control'
            }),
            'linkedin_url': forms.URLInput(attrs={
                'placeholder': 'لینک پروفایل LinkedIn خود را وارد کنید', 
                'class': 'form-control'
            }),
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'id_profile_image',   # Custom ID for easy JS targeting
                'class': 'form-control',    # Bootstrap class for styling
                'data-button-text': 'آپلود عکس',   # Custom data attribute for JS
                'data-placeholder-text': 'هیچ عکسی انتخاب نشده است.'  # Custom data attribute for JS
            }),
            'summary': forms.Textarea(attrs={
                'placeholder': 'خلاصه‌ای از حرفه خود را وارد کنید', 
                'class': 'form-control', 
                'rows': 5
            }),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company_name', 'location', 'start_date', 'end_date', 'description']
        labels = {
            'job_title': 'عنوان شغلی',
            'company_name': 'نام شرکت',
            'location': 'موقعیت جغرافیایی',
            'start_date': 'تاریخ شروع',
            'end_date': 'تاریخ پایان',
            'description': 'توضیحات',
        }
        widgets = {
            'job_title': forms.TextInput(attrs={
                'placeholder': 'عنوان شغلی خود را وارد کنید', 
                'class': 'form-control'
            }),
            'company_name': forms.TextInput(attrs={
                'placeholder': 'نام شرکت خود را وارد کنید', 
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'موقعیت جغرافیایی شرکت را وارد کنید', 
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date', 
                'placeholder': 'تاریخ شروع کار خود را وارد کنید', 
                'class': 'form-control'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date', 
                'placeholder': 'تاریخ پایان کار خود را وارد کنید (در صورت وجود)', 
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'توضیحات مربوط به شغل را وارد کنید', 
                'class': 'form-control', 
                'rows': 3
            }),
        }
        
# Define the formset for WorkExperience linked to a Resume
WorkExperienceFormSet = inlineformset_factory(
    Resume, WorkExperience,
    form=WorkExperienceForm,
    extra=1,  # Number of extra forms to show
    can_delete=True  # Allow deletion of individual items
)

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['category_name']
        labels = {
            'category_name': 'نام دسته‌بندی مهارت',  # Persian label for category_name
        }
        widgets = {
            'category_name': forms.TextInput(attrs={
                'placeholder': 'نام دسته‌بندی مهارت را وارد کنید',  # Persian placeholder
                'class': 'form-control'  # Add Bootstrap form-control class
            }),
        }

# Define the formset for SkillCategory linked to a Resume
SkillCategoryFormSet = inlineformset_factory(
    Resume, SkillCategory,
    form=SkillCategoryForm,
    extra=1,  # Number of extra forms to show
    can_delete=True  # Allow deletion of individual items
)

class SubSkillForm(forms.ModelForm):
    class Meta:
        model = SubSkill
        fields = ['sub_skill_name']
        labels = {
            'sub_skill_name': 'نام مهارت فرعی',  # Persian label for sub_skill_name
        }
        widgets = {
            'sub_skill_name': forms.TextInput(attrs={
                'placeholder': 'نام مهارت فرعی را وارد کنید',  # Persian placeholder
                'class': 'form-control'  # Add Bootstrap form-control class
            }),
        }

# SubSkill Formset
SubSkillFormSet = inlineformset_factory(
    SkillCategory, SubSkill,
    fields=('sub_skill_name',),
    extra=1,  # Allows one empty form for adding new sub-skills
    can_delete=True  # Allow users to delete existing sub-skills
)