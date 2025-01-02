from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


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
    
    def get_absolute_url(self):
        return reverse("edit_resume", args=[str(self.id)])


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
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"


def mother_resume():
    return {
        "personal_info": {
            "name": "Mohsen Reyhani",
            "role": "BackEnd Developer",
            "dob": "Feb 10, 1996",
            "contact": {
                "email": "MohsenReyhani@gmail.com",
                "linkedin": "linkedin.com/in/mreyhani/",
                "phone": "+98 939 6600 120"
            }
        },
        "summary": "Experienced Python developer with over 8 years of software engineering expertise, focusing on scalable backend development using Django and Python-based frameworks. Proficient in building high-performance systems with Django, Celery, Redis, PostgreSQL, and hands-on experience in cloud services (AWS). Adept at architecting robust solutions and optimizing systems for AI-driven platforms. Strong knowledge of front-end technologies including JavaScript, coupled with the ability to manage end-to-end development processes.",
        "career_objective": "Seeking a Python Developer role to leverage my skills in Django, drive innovative AI platforms, and contribute to technical roadmaps within dynamic, fast-growing teams.",
        "work_experience": [
            {
                "title": "Founder",
                "company": "EZFACTOR.IR",
                "location": "Tehran, Iran",
                "date": "April 2023 - Current",
                "description": "Developed and deployed scalable backend solutions with Django, working over 1500+ hours on core features."
            },
            {
                "title": "Backend Developer",
                "company": "JOBSEEK",
                "location": "Tehran, Iran",
                "date": "October 2021 - April 2022",
                "description": "Aggregated databases from 5 major job platforms in Iran into a unified, fast, and searchable system. Optimized the platform for high traffic and improved search speeds by 40%."
            },
            {
                "title": "Co-Founder & CTO",
                "company": "LUCAA",
                "location": "Tehran, Iran",
                "date": "May 2018 - October 2021",
                "description": "Automated 20+ small-scale tasks for social media marketing using Django. Led a technical team to implement marketing intelligence solutions for client growth."
            },
            {
                "title": "Android Developer",
                "company": "NIVO",
                "location": "Tehran, Iran",
                "date": "Dec 2017 - Oct 2018",
                "description": "Head of Android development for a personal financial management app with over 60,000 active users."
            }
        ],
        "skills": {
            "software_skills": {
                "Python (Backend)": 5,
                "Django": 5,
                "Flask/FastAPI": 4,
                "JavaScript (Frontend & Backend)": 4,
                "PostgreSQL, Redis (Databases)": 4,
                "Agile Methodologies": 5,
                "Figma (UI/UX Design)": 3,
                "WordPress - Elementor, PHP": 3,
                "Android (Java)": 2
            },
            "soft_skills": [
                "Problem Solving & Analytical Thinking",
                "Leadership in Software Development",
                "Effective Communication",
                "Innovative & Growth-Oriented Mindset",
                "Technical Documentation",
                "Medium Writing Proficiency"
            ],
            "teamwork_collaboration": [
                "Mentoring & Leading Teams",
                "Cross-Functional Collaboration",
                "Proactive Feedback Sharing",
                "Project & Task Ownership"
            ],
            "project_management": [
                "Agile Methodologies (Scrum, Kanban)",
                "End-to-End Project Execution",
                "Technical Roadmap Development",
                "Risk & Issue Management"
            ],
            "adaptability_growth": [
                "Rapid Adaptation to New Tools & Frameworks",
                "Continuous Learning & Upskilling",
                "Implementing Scalable and Efficient Processes"
            ],
            "customer_centric_skills": [
                "Customer-Focused Problem Solving",
                "Translating Requirements into Scalable Solutions",
                "User Experience Optimization"
            ]
        }
    }  


class JsonResume(models.Model):
    # Personal Information
    company_name = models.CharField(max_length=200, default='company')
    role_name = models.CharField(max_length=200, blank=True, null=True)
    ad_link = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    data = models.JSONField(default=mother_resume)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse("edit_resume", args=[str(self.id)])
