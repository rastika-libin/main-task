from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Submit_Details
from django.contrib import messages
from datetime import date

@login_required
def view_submissions(request):
    if request.user.role == 'Admin':
        submissions = Submit_Details.objects.all()
    else:
        submissions = Submit_Details.objects.filter(user=request.user)
    return render(request, 'details.html', {'submissions': submissions})

@login_required
def fill_form_redirect(request):
    if request.user.role == 'Admin':
        return redirect('admin_form')
    else:
        return redirect('user_form')

@login_required
def user_form(request):
    if request.user.role != 'User':
        return redirect('homepage')

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not firstname or not lastname or not email or not message:
            return render(request, 'user-form.html', {'error': 'All fields are required.'})

        # Save to DB
        Submit_Details.objects.create(
            user=request.user,
            firstname=firstname,
            lastname=lastname,
            email=email,
            message=message,
            date=date.today()
        )

        # Send confirmation email
        send_mail(
            subject='Form Submitted Successfully',
            message=f"Dear {firstname},\n\nYour form has been submitted successfully.\n\nDetails:\nName: {firstname} {lastname}\nEmail: {email}\nMessage: {message}",
            recipient_list=[email],
            from_email="websmtp@technicrafts.com",
        )

        # Add Django message
        messages.success(request, 'Form submitted and confirmation email sent!')
        return redirect('user_form')

    return render(request, 'user-form.html')


@login_required
def admin_view(request):
    if request.user.role != 'Admin':
        return redirect('user_form')

    submissions = Submit_Details.objects.select_related('user').all()
    return render(request, 'admin-form.html', {'submissions': submissions})