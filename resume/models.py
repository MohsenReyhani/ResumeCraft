from django.db import models
from django.contrib.auth import get_user_model

class Resume(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)  # E.g., "Founder at resumecraft"
    birth_date = models.DateField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)  # LinkedIn profile
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # Address if needed
    address = models.CharField(max_length=300, blank=True)
    # Summary Section
    summary = models.TextField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    modified_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever saved

    def __str__(self):
        return self.full_name

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, related_name='work_experiences', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)  # E.g., "Founder at resumecraft"
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # E.g., "Tehran, Iran"
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Leave blank for "current"
    description = models.TextField()  # Details about the role and responsibilities
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    modified_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever saved

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)  # E.g., "Django"
    proficiency = models.IntegerField()  # Rating out of 100 (or adjust scale)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    modified_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever saved

    def __str__(self):
        return self.skill_name

class SkillCategory(models.Model):
    resume = models.ForeignKey(Resume, related_name='skill_categories', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)  # E.g., "Soft Skills", "Teamwork & Collaboration"
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    modified_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever saved

    def __str__(self):
        return self.category_name

class SubSkill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='sub_skills', on_delete=models.CASCADE)
    sub_skill_name = models.CharField(max_length=200)  # E.g., "Problem Solving", "Critical Thinking"
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    modified_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever saved

    def __str__(self):
        return self.sub_skill_name

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='educations', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=200)  # E.g., "University Name"
    degree = models.CharField(max_length=100)  # E.g., "B.Sc. in Computer Science"
    graduation_date = models.DateField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    modified_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever saved

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"