from audioop import add
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authapp.models import (
    Attendance,
    Contact,
    MembershipPlan,
    Trainer,
    Enrollment,
    GALLERY,
)
from django.contrib.auth.decorators import login_required

# Create your views here.


def Home(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "ABOUT.html")

def service_view(request):
    return render(request, "SERVICE.html")


def gallery_view(request):
    posts = GALLERY.objects.all()
    context = {"posts": posts}
    return render(request, "GALLERY.html", context)


@login_required(login_url="/login")
def attendance(request):
    selecttrainer = Trainer.objects.all()
    context = {"selecttrainer": selecttrainer}
    if request.method == "POST":
        phonenumber = request.POST.get("phonenumber")
        Login = request.POST.get("logintime")
        Logout = request.POST.get("logout")
        SelectWorkout = request.POST.get("workout")
        TrainedBy = request.POST.get("trainer")
        query = Attendance(
            phonenumber=phonenumber,
            Login=Login,
            Logout=Logout,
            SelectWorkout=SelectWorkout,
            TrainedBy=TrainedBy,
        )
        query.save()
        messages.warning(request, "Attendance Applied Success!")
        return redirect("/attendance")
    return render(request, "attendance.html", context)


def about_us(request):
    return render(request, "about.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("usernumber")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if len(username) != 10:
            messages.info(request, "Phone number must be 10 digits!")
            return redirect("/signup")

        if pass1 != pass2:
            messages.info(request, "Password is not matching!")
            return redirect("/signup")

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Phone Number is taken!")
                return redirect("/signup")
        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is taken!")
                return redirect("/signup")
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "User is created Please Login!")
        return redirect("/login")

    return render(request, "signup.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("usernumber")
        password = request.POST.get("pass1")  # Corrected variable name

        myuser = authenticate(
            username=username, password=password
        )  # Corrected parameter name

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login successful!")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")  # Corrected typo
            return redirect("/login")

    return render(request, "handlelogin.html")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logout success!")
    return redirect("/login")


@login_required(login_url="/login")
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("num")
        desc = request.POST.get("desc")

        # Check if a contact request with the same email exists
        if Contact.objects.filter(email=email).exists():
            messages.info(
                request,
                "Your request has already been received. We will get back to you soon.",
            )
        else:
            # Create a new contact object and save it to the database
            myquery = Contact(
                name=name, email=email, phonenumber=number, description=desc
            )
            myquery.save()
            messages.info(
                request, "Thanks for contacting us, we will get back to you soon"
            )

        return redirect("/contact")

    return render(request, "contact.html")


@login_required(login_url="/login")
def enroll(request):
    membership = MembershipPlan.objects.all()
    selecttrainer = Trainer.objects.all()
    context = {"membership": membership, "selecttrainer": selecttrainer}
    if request.method == "POST":
        full_name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        phonenumber = request.POST.get("phonenumber")
        dob = request.POST.get("dob")
        member = request.POST.get("member")
        trainer = request.POST.get("trainer")
        reference = request.POST.get("reference")
        address = request.POST.get("address")
        query = Enrollment(
            full_name=full_name,
            email=email,
            gender=gender,
            phonenumber=phonenumber,
            dob=dob,
            select_membership_plan=member,
            select_trainer=trainer,
            reference=reference,
            address=address,
        )
        query.save()
        messages.success(request, "Thanks for enrollment!")
        return redirect("/join")
    return render(request, "enroll.html", context)


@login_required(login_url="/login")
def profile(request):
    user_phone = request.user
    posts = Enrollment.objects.filter(phonenumber=user_phone)
    attendance = Attendance.objects.filter(phonenumber=user_phone)
    context = {"posts": posts, "attendance": attendance}
    return render(request, "profile.html", context)
