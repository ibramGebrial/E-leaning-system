from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, MessageForm

from .models import Profile, Message

# Create your views here.


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username or password is incorrect')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def registerUser(request):
    page = 'logout'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('home')
        else:
            messages.warning(
                request, 'An error has occurred during registration!')
    context = {'page': page, 'form': form}
    return render(request, 'users/register.html', context)


def profiles(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/profiles.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    course = profile.course_set.all()
    context = {'profile': profile, 'course': course}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messagerecipient = profile.recipients.all()
    unreadCount = messagerecipient.filter(is_read=False).count()
    context = {'messagerecipient': messagerecipient,
               'unreadCount': unreadCount}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def message(request, pk):
    profile = request.user.profile
    messagee = profile.recipients.get(id=pk)
    if messagee.is_read == False:
        messagee.is_read = True
        messagee.save()
    context = {'messagee': messagee}
    return render(request, 'users/message.html', context)


def sendMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            messagee = form.save(commit=False)
            messagee.sender = sender
            messagee.recipient = recipient

            if sender:
                messagee.name = sender.name
                messagee.email = sender.email
            messagee.save()

            messages.success(
                request, 'Your message was sent successfully sent')
            return redirect('profiles', pk=recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message_form.html', context)
