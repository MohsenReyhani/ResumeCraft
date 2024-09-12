from django.contrib import admin
from .models import Resume, WorkExperience, Skill, SkillCategory, SubSkill, Education

# Inline Admin for WorkExperience
class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1  # Number of empty forms to display
    can_delete = True

# Inline Admin for Skill
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    can_delete = True

# Inline Admin for SkillCategory
class SkillCategoryInline(admin.TabularInline):
    model = SkillCategory
    extra = 1
    can_delete = True

# Inline Admin for SubSkill
class SubSkillInline(admin.TabularInline):
    model = SubSkill
    extra = 1
    can_delete = True

# Inline Admin for Education
class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    can_delete = True

# Main Admin for Resume
class ResumeAdmin(admin.ModelAdmin):
    ordering = ['-id']  # Order by latest first
    list_display = ('full_name', 'title', 'contact_email', 'contact_phone', 'created_at')  # Adjust the fields you want to display in the list view
    search_fields = ('full_name', 'contact_email', 'title')  # Searchable fields in the admin
    inlines = [WorkExperienceInline, SkillInline, SkillCategoryInline, EducationInline]  # Inlines for related models

admin.site.register(Resume, ResumeAdmin)
