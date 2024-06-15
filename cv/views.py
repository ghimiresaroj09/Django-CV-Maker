from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Profile
import pdfkit
from django.template import loader


def cv_create(request):
    if request.method == 'POST':
        # Retrieve form data
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')
        school = request.POST.get('school')
        school_gpa = request.POST.get('school_gpa')
        school_joined_year = request.POST.get('school_joined_year')
        school_left_year = request.POST.get('school_left_year')
        college = request.POST.get('college')
        college_gpa = request.POST.get('college_gpa')
        stream = request.POST.get('stream')
        college_joined_year = request.POST.get('college_joined_year')
        college_left_year = request.POST.get('college_left_year')
        university = request.POST.get('university')
        university_gpa = request.POST.get('university_gpa')
        university_faculty = request.POST.get('university_faculty')
        university_joined_year = request.POST.get('university_joined_year')
        university_left_year = request.POST.get('university_left_year')
        project = request.POST.get('project')
        project_description = request.POST.get('project_description')
        project_link = request.POST.get('project_link')

        # current_company = request.POST.get('current_company')
        # current_position = request.POST.get('current_position')
        # current_work_description = request.POST.get('current_work_description')
        # current_joined_date = request.POST.get('current_joined_date')
        # previous_company = request.POST.get('previous_company')
        # previous_position = request.POST.get('previous_position')
        # previous_work_description = request.POST.get('previous_work_description')
        # previous_joined_date = request.POST.get('previous_joined_date')
        # previous_left_date = request.POST.get('previous_left_date')     
        # project_two = request.POST.get('project_two')
        # project_two_description = request.POST.get('project_two_description')
        # project_three = request.POST.get('project_three')
        # project_three_description = request.POST.get('project_three_description')

        technical_skills = request.POST.get('technical_skills')
        nontechnical_skills = request.POST.get('nontechnical_skills')
        language = request.POST.get('language')
        reference_name = request.POST.get('reference_name')
        reference_position = request.POST.get('reference_position')
        reference_organization = request.POST.get('reference_organization')
        reference_email = request.POST.get('reference_email')
        reference_phone = request.POST.get('reference_phone')

        # Create and save the Profile instance
        profile = Profile.objects.create(
            full_name=full_name,
            address=address,
            email=email,
            phone=phone,
            summary=summary,
            school=school,
            school_gpa=float(school_gpa) if school_gpa else None,
            school_joined_year=school_joined_year,
            school_left_year=school_left_year,
            college=college,
            college_gpa=float(college_gpa) if college_gpa else None,
            stream=stream,
            college_joined_year=college_joined_year,
            college_left_year=college_left_year,
            university=university,
            university_gpa=float(university_gpa) if university_gpa else None,
            university_faculty=university_faculty,
            university_joined_year=university_joined_year,
            university_left_year=university_left_year,
            project=project,
            project_description=project_description,
            project_link=project_link,
            # current_company=current_company,
            # current_position=current_position,
            # current_work_description=current_work_description,
            # current_joined_date=current_joined_date,
            # previous_company=previous_company,
            # previous_position=previous_position,
            # previous_work_description=previous_work_description,
            # previous_joined_date=previous_joined_date,
            # previous_left_date=previous_left_date,
            # project_two=project_two,
            # project_two_description=project_two_description,
            # project_three=project_three,
            # project_three_description=project_three_description,
            technical_skills=technical_skills,
            nontechnical_skills=nontechnical_skills,
            language=language,
            reference_name=reference_name,
            reference_position=reference_position,
            reference_organization=reference_organization,
            reference_email=reference_email,
            reference_phone=reference_phone
        )

        profile.save()
        return redirect('cv_view', profile_id=profile.id)  # Redirect to a view page of submitted data

    return render(request, 'index.html')


def cv_download(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    template = loader.get_template('pdf.html')
    html = template.render({'profile': profile})
    
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")  
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
    }
    
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    
    return response

def cv_view(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'cv.html',{'profile': profile})


def list_view(request):
    profile= Profile.objects.all()
    return render(request, 'list.html', {'profile': profile})


def cv_update(request,profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        profile.address = request.POST.get('address')
        profile.full_name = request.POST.get('full_name')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        profile.summary = request.POST.get('summary')
        profile.school = request.POST.get('school')
        profile.school_gpa = request.POST.get('school_gpa')
        profile.school_joined_year = request.POST.get('school_joined_year')
        profile.school_left_year = request.POST.get('school_left_year')
        profile.college = request.POST.get('college')
        profile.college_gpa = request.POST.get('college_gpa')
        profile.stream = request.POST.get('stream')
        profile.college_joined_year = request.POST.get('college_joined_year')
        profile.college_left_year = request.POST.get('college_left_year')
        profile.university = request.POST.get('university')
        profile.university_gpa = request.POST.get('university_gpa')
        profile.university_faculty = request.POST.get('university_faculty')
        profile.university_joined_year = request.POST.get('university_joined_year')
        profile.university_left_year = request.POST.get('university_left_year')
        profile.project = request.POST.get('project')
        profile.project_description = request.POST.get('project_description')
        profile.project_link = request.POST.get('project_link')
        profile.technical_skills = request.POST.get('technical_skills')
        profile.nontechnical_skills = request.POST.get('nontechnical_skills')
        profile.language = request.POST.get('language')
        profile.reference_name = request.POST.get('reference_name')
        profile.reference_position = request.POST.get('reference_position')
        profile.reference_organization = request.POST.get('reference_organization')
        profile.reference_email = request.POST.get('reference_email')
        profile.reference_phone = request.POST.get('reference_phone')
        profile.save()
        return redirect('cv_view', profile_id=profile.id)
    return render(request,'updatecv.html',{'profile':profile})

def cv_delete(request, profile_id):
    profile= get_object_or_404(Profile,id=profile_id)
    if request.method=="POST":
        profile.delete()
        return redirect('list_view')  
    return render(request,'delete.html',{'profile':profile})