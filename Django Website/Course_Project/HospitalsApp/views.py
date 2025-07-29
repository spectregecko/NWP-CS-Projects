from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import authenticated_user, allowed_user
from .forms import NewHospitalForm, SendEmailForm
from .models import Hospital
from django.db.models import Q
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
import re
import smtplib
from email.message import EmailMessage

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request, 'home.html')

@login_required(login_url='login')
@allowed_user(allowed_groups=['Admins'])
def add_new_hospital(request):
    if request.method == 'POST':
        form = NewHospitalForm(request.POST)
        if form.is_valid():
            modified = form.save(commit=False)

            # Zip code reformatting.
            if re.match(r'^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]-\d[ABCEGHJ-NPRSTV-Z]\d$', modified.zip_code, re.IGNORECASE): # e.g. t8V-4c4 -> T8V4C4
                modified.zip_code = modified.zip_code[:3].upper() + modified.zip_code[4:].upper()
            elif re.match(r'^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] \d[ABCEGHJ-NPRSTV-Z]\d$', modified.zip_code, re.IGNORECASE): # e.g. T8V 4c4 -> T8V4C4
                modified.zip_code = modified.zip_code[:3].upper() + modified.zip_code[4:].upper()
            elif re.match(r'^[0-9]{5}(?:-[0-9]{4})$', modified.zip_code): # e.g. 12345-6789 -> 123456789
                modified.zip_code = modified.zip_code[:5] + modified.zip_code[6:]
            elif re.match(r'^[0-9]{5}(?: [0-9]{4})$', modified.zip_code): # e.g. 12345 6789 -> 123456789
                modified.zip_code = modified.zip_code[:5] + modified.zip_code[6:]

            # Type reformatting.
            modified.type = modified.type[0].upper() + modified.type[1:].lower() # e.g. prIVaTe -> Private
            
            modified.save()
            form.save_m2m()
            messages.success(request, ('A new hospital was added successfully!'))
            return redirect('homepage')
        else:
            messages.error(request, ('Failed to add a new hospital! One of more of the fields have issues.'))
            return render(request, 'add.html', {'form' : form})
    form = NewHospitalForm()
    return render(request, 'add.html', {'form' : form})

@login_required(login_url='login')
def list_hospitals(request, pk=None):
    hospital_list = Hospital.objects.all().order_by('name')
    if pk is not None:
        hospital_list = Hospital.objects.filter(pk=pk)
        messages.success(request, (f'Viewing {pk}'))
    return render(request, 'list.html', {'hospital_list' : hospital_list})

@login_required(login_url='login')
def search_hospital(request):
    if request.method == 'POST':
        response = request.POST['response'].strip()
        searchFilter = request.POST['searchFilter']

        if searchFilter == 'name':
            hospital_list = Hospital.objects.filter(name__contains=response).order_by('name')
            if hospital_list.count() == 0:
                messages.error(request, ('There are no hospitals associated with that name!'))
                return render(request, 'search.html')
            messages.success(request, ('Search was successful!'))
            return render(request, 'list.html', {'hospital_list' : hospital_list})
        
        elif searchFilter == 'zipcode':
            if ' ' in response or '-' in response:
                temp = ''
                for i in range(len(response)):
                    if response[i] != ' ' and response[i] != '-':
                        temp += response[i]
                response = temp
            hospital_list = Hospital.objects.filter(zip_code__contains=response).order_by('name')
            if hospital_list.count() == 0:
                messages.error(request, ('There are no hospitals associated with that zip code!'))
                return render(request, 'search.html')
            messages.success(request, ('Search was successful!'))
            return render(request, 'list.html', {'hospital_list' : hospital_list})
        
        elif searchFilter == 'phone':
            temp = ''
            for i in range(len(response)):
                if response[i] != '(' and response[i] != ')' and response[i] != ' ' and response[i] != '-':
                    temp += response[i]
            temp3 = temp
            if len(temp) > 3:
                temp = temp[:3] + '-' + temp[3:]
            temp2 = temp
            if len(temp) > 7:
                temp = temp[:7] + '-' + temp[7:]
            hospital_list = Hospital.objects.filter(Q(phone__contains=temp) | Q(phone__contains=temp2) | Q(phone__contains=temp3)).order_by('name')
            if hospital_list.count() == 0:
                messages.error(request, ('There are no hospitals associated with that phone number!'))
                return render(request, 'search.html')
            messages.success(request, ('Search was successful!'))
            return render(request, 'list.html', {'hospital_list' : hospital_list})
        
        elif searchFilter == 'type':
            hospital_list = Hospital.objects.filter(type__startswith=response).order_by('name')
            if hospital_list.count() == 0:
                messages.error(request, ('There are no hospitals with that type!'))
                return render(request, 'search.html')
            messages.success(request, ('Search was successful!'))
            return render(request, 'list.html', {'hospital_list' : hospital_list})
        
        elif searchFilter == 'email':
            hospital_list = Hospital.objects.filter(email__startswith=response).order_by('name')
            if hospital_list.count() == 0:
                messages.error(request, ('There are no hospitals associated with that email!'))
                return render(request, 'search.html')
            messages.success(request, ('Search was successful!'))
            return render(request, 'list.html', {'hospital_list' : hospital_list})
        
    return render(request, 'search.html')

@login_required(login_url='login')
@allowed_user(allowed_groups=['Admins'])
def update_hospital(request, pk=None): # Need to implement
    if request.method == 'POST':
        pk = request.POST['pk']
        if 'update' in request.POST:
            name = request.POST['name']
            zip_code = request.POST['zip_code']
            phone = request.POST['phone']
            myType = request.POST['type']
            email = request.POST['email']

            # Zip code reformatting.
            if re.match(r'^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]-\d[ABCEGHJ-NPRSTV-Z]\d$', zip_code, re.IGNORECASE): # e.g. t8V-4c4 -> T8V4C4
                zip_code = zip_code[:3].upper() + zip_code[4:].upper()
            elif re.match(r'^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] \d[ABCEGHJ-NPRSTV-Z]\d$', zip_code, re.IGNORECASE): # e.g. T8V 4c4 -> T8V4C4
                zip_code = zip_code[:3].upper() + zip_code[4:].upper()
            elif re.match(r'^[0-9]{5}(?:-[0-9]{4})$', zip_code): # e.g. 12345-6789 -> 123456789
                zip_code = zip_code[:5] + zip_code[6:]
            elif re.match(r'^[0-9]{5}(?: [0-9]{4})$', zip_code): # e.g. 12345 6789 -> 123456789
                zip_code = zip_code[:5] + zip_code[6:]

            # Type reformatting.
            myType = myType[0].upper() + myType[1:].lower() # e.g. prIVaTe -> Private

            hospital_entry = Hospital.objects.filter(name=pk).update(name=name, zip_code=zip_code, phone=phone, type=myType, email=email)
            messages.success(request, ('Successfully updated the chosen Hospital!'))
            return redirect('homepage')
        elif 'cancel' in request.POST:
            messages.error(request, (f'{pk} was not changed!'))
            return redirect('homepage')

    if pk is None:
        return redirect('homepage')
    hospital_entry = Hospital.objects.get(name=pk)
    return render(request, 'update.html', {'hospital' : hospital_entry})

@login_required(login_url='login')
@allowed_user(allowed_groups=['Admins'])
def delete_hospital(request, pk=None):
    if request.method == 'POST':
        if 'yes' in request.POST:
            Hospital.objects.filter(pk=pk).update(visible=False)
            messages.success(request, (f'{pk} was successfully deleted!'))
            return redirect('homepage')
        elif 'no' in request.POST:
            messages.error(request, (f'{pk} was not deleted!'))
            return redirect('homepage')
    if pk is None:
        return redirect('homepage')
    return render(request, 'delete.html', {'pk' : pk})

@authenticated_user
def registration_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            if (first_name and not first_name.isalpha()) or (last_name and not last_name.isalpha()):
                messages.error(request, ('Please enter a valid alphabetic name!'))
                return render(request, 'registration.html', {'form' : form})
            else:
                newuser = form.save()
                user = form.cleaned_data.get('username')
                group = Group.objects.get(name='Users')
                newuser.groups.add(group)
                messages.success(request, f'A new user account was created for {user}')
                return redirect('login')
        else:
            messages.error(request, ('Form has invalid fields!'))
            return render(request, 'registration.html', {'form' : form})
    form = CreateUserForm()
    return render(request, 'registration.html', {'form' : form})

@authenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Incorrect username or password')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def email(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            contents = form.save(commit=False)

            EMAIL_ADDRESS = request.POST['emailAddress']
            EMAIL_PASSWORD = contents.password

            message = EmailMessage()
            message['To'] = contents.receiver
            message['Subject'] = contents.subject
            message.set_content(contents.message)
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(message)
                messages.success(request, ('Email was sent!'))
            except Exception:
                messages.error(request, ('Email could not be sent! Make sure you are using the correct email password.'))
            return redirect('homepage')
        else:
            messages.error(request, ('Email could not be sent! Make sure you are using a valid email for the recipient.'))
            return render(request, 'email.html', {'form' : form})
    form = SendEmailForm()
    return render(request, 'email.html', {'form' : form})