from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Contact, MembershipPlan, Trainer, Enrollment, Gallery, WorkoutLog
from django.core.mail import send_mail
from django.http import HttpResponse

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # if len(username)>10 or len(username)<10:
        #     messages.info(request,"Phone Number Must be 10 Digits")
        #     return redirect('/signup')

        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "User Name is Taken")
                return redirect('/signup')

        except Exception as identifier:      #However, it's important to note that using a broad except block like this (except Exception as identifier:) without handling specific exceptions can potentially hide errors and make debugging more difficult
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "User is Created Please Login")
        return redirect('/login')

    return render(request, "signup.html")

def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')

    return render(request, "handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('/login')


def Home(request):
    return render(request, "index.html")

def workouts(request):
    return render(request, "workouts.html")

def gallery(request):
    posts = Gallery.objects.all()
    context = {"posts": posts}
    return render(request, "gallery.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc = request.POST.get('desc')
        myquery = Contact(name=name, email=email, phonenumber=number, description=desc)
        myquery.save()
        messages.info(request, "Thanks for Contacting us, we will get back to you soon")
        return redirect('/contact')

    return render(request, "contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login")
        return redirect('/login')

    Membership = MembershipPlan.objects.all()
    SelectTrainer = Trainer.objects.all()
    context = {"Membership": Membership, "SelectTrainer": SelectTrainer}
    if request.method == "POST":
        Fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        Phonenumber = request.POST.get('Phonenumber')
        DOB = request.POST.get('DOB')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        reference = request.POST.get('reference')
        address = request.POST.get('address')
        query = Enrollment(Fullname=Fullname, Email=email, Gender=gender, Phonenumber=Phonenumber, DOB=DOB,
                           SelectMembershipPlan=member, SelectTrainer=trainer, Reference=reference, Address=address)
        query.save()
        messages.success(request, "Thanks For The Enrollment")
        return redirect('/enroll')

    return render(request, "enroll.html", context)

def workout(request):
        return HttpResponse("<center><h1>Please  Enroll</h1><center>")


def workoutlog(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login and Try Again")
        return redirect('/login')

    SelectTrainer = Trainer.objects.all()
    context = {"SelectTrainer": SelectTrainer}

    if request.method == "POST":
        Fullname = request.POST.get('Fullname')
        Login = request.POST.get('login')
        Logout = request.POST.get('logout')
        SelectWorkout = request.POST.get('workout')
        custom_workout = request.POST.get('customWorkout')  # Get custom workout data
        w1 = request.POST.get('w1')
        r1 = request.POST.get('r1')
        w2 = request.POST.get('w2')
        r2 = request.POST.get('r2')
        w3 = request.POST.get('w3')
        r3 = request.POST.get('r3')
        TrainedBy = request.POST.get('trainer')
        mail=request.POST.get('mail')

        # Use custom workout if provided, else use selected workout
        SelectWorkout = custom_workout if SelectWorkout == "Other" and custom_workout else SelectWorkout

        query = WorkoutLog(Fullname=Fullname, Login=Login, Logout=Logout, SelectWorkout=SelectWorkout,
                           w1=w1, r1=r1, w2=w2, r2=r2, w3=w3, r3=r3, TrainedBy=TrainedBy)
        query.save()
        messages.warning(request, "Workout Log Completed")


        # Construct mail with all details
        message = f'Your WorkoutLog has been created successfully :\n\n'
        message += f'Fullname: {Fullname}\n'
        message += f'Login: {Login}\n'
        message += f'Logout: {Logout}\n'
        message += f'SelectWorkout: {SelectWorkout}\n'
        message += f'Custom Workout: {custom_workout}\n'
        message += f'W1: {w1}, R1: {r1}\n'
        message += f'W2: {w2}, R2: {r2}\n'
        message += f'W3: {w3}, R3: {r3}\n'
        message += f'Trained By: {TrainedBy}\n'
        message += f'Kickstart your journey in PI Fitness..... Thank you!!'

        # Sending email to the registered user
        subject = 'Workout Log Created'
        from_email = 'sumanmadappa6@gmail.com.com'  # Update with your email address
        recipient_list = [request.user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect('/login')
    return render(request, "workoutlog.html", context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login")
        return redirect('/login')

    user_name = request.user
    posts = Enrollment.objects.filter(Fullname=user_name)
    workoutlog = WorkoutLog.objects.filter(Fullname=user_name)
    selected_workout = None

    if request.method == 'POST':
        selected_workout = request.POST.get('selectedWorkout', None)
        custom_workout = request.POST.get('customWorkout', None)  # Get custom workout data
        selected_workout = custom_workout if selected_workout == "Other" and custom_workout else selected_workout

    context = {"posts": posts, "workoutlog": workoutlog, "selected_workout": selected_workout}
    return render(request, "profile.html", context)

def delete_profile(request):
    if request.method == 'POST':
        # Retrieving the logged-in user
        user = request.user

        # Deletes the enrollment details associated with the user
        # Enrollment.objects.filter(Fullname=user).delete()

        # Deletes the workout logs associated with the user
        WorkoutLog.objects.filter(Fullname=user).delete()

        # Redirect to a home page
        messages.success(request, "Your Workout log has been deleted successfully.")
        return redirect('profile')















