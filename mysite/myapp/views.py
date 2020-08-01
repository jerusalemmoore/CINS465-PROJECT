from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from . import models
from . import forms
# import json
# Create your views here.
#TEMPLATE HOME PAGE
@login_required(login_url='/login/')
def homeView(request):
    if request.user.is_authenticated:#if user is logged in
        if request.method =='POST':
            postForm = forms.PostForm(request.POST,request.FILES)#form can be submitted
            if postForm.is_valid():
                postModel = models.PostModel(#create a post model with the following
                    user = request.user,
                    content = postForm.cleaned_data["content"],
                    image = postForm.cleaned_data["image"]
                    )
                postModel.save()#save the postModel
        postForm = forms.PostForm()#refresh the form
        # li = models.PostModel.objects.filter(user=request.user)#list of user's post
        li = models.PostModel.objects.all()
        friend, created = models.Friend.objects.get_or_create(currentUser=request.user)
        friends = friend.users.all()
    else:
        redirect('/login/')
    context = {
    "friends": friends,
    "userPosts":li,
    "hello_mesg":"CINS465 Hello World",
    "title": "Hello World",
    "userInfoForm": postForm,
    }
    return render(request, "index.html", context=context)

def postDelete(request, id):
    post = get_object_or_404(models.PostModel, id=id)
    if request.method == 'POST':
        post.delete()
    return redirect('/home/')

def changeFriendsUserView(request, operation, id):
    li = models.PostModel.objects.filter(user=id)#list of posts from guest user
    guestUser = models.User.objects.filter(id=id)[0]
    friend, created = models.Friend.objects.get_or_create(currentUser=request.user)
    friends = friend.users.all()
    context = {
    "userPosts":li,
    "guestUser":guestUser,
    "friends": friends
    }
    newFriend = User.objects.get(id=id)
    if operation == 'add':
        models.Friend.make_friend(request.user, newFriend)
    elif operation == 'remove':
        models.Friend.lose_friend(request.user, newFriend)
    return render(request,"userPage.html", context=context)


def changeFriends(request,operation,id):
    newFriend = User.objects.get(id=id)
    if operation == 'add':
        models.Friend.make_friend(request.user, newFriend)
    elif operation == 'remove':
        models.Friend.lose_friend(request.user, newFriend)
    return redirect('/home/')
#LOGIN PAGE
# def loginView(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#     return render(request,'login.html')

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        # form = AuthenticationForm(request.POST)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home/')
        else:
            messages.error(request, 'Invalid username/password, click the Sign Up button to create an account')
            return redirect('/login/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

#LOGOUT PAGE
def logoutView(request):
    logout(request)
    return redirect('/login/')

#SIGNUP PAGE
def signupView(request):
    # include a login form
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, "signup.html",{'form':form})

def exploreView(request):
    if request.user.is_authenticated:
        li = models.PostModel.objects.all()
        context={
        "globalPosts":li,
        "explorePage":"Explore Page"
        }
        return render(request,"explore.html", context=context)
    else:
        redirect("/login/")

def userView(request, id):
    li = models.PostModel.objects.all()#list of posts from guest user
    guestUser = models.User.objects.filter(id=id)[0]
    friend, created = models.Friend.objects.get_or_create(currentUser=request.user)
    friends = friend.users.all()
    guestFriend, created = models.Friend.objects.get_or_create(currentUser=guestUser)
    guestFriends = guestFriend.users.all()
    context = {
    "userPosts":li,
    "guestFriends": guestFriends,
    "guestUser":guestUser,
    "friends": friends,
    }
    if request.user.id == id:
        return redirect("/home/")
    else:
        return render(request,"userPage.html", context=context)

def getUsers(request):
    userModels = models.UserInfoModel.objects.all()
    userList = {}
    userList["users"] = []
    for user in userModels:
        tempUser = {}
        tempUser["id"] = user.id
        tempUser["username"] = user.username
        tempUser["userpassword"] = user.userpassword
        tempUser["email"] = user.email
        userList["users"].append(tempUser)
    return JsonResponse(userList)
def friendsView(request):
    friend, created = models.Friend.objects.get_or_create(currentUser=request.user)
    friends = friend.users.all()
    context = {
    "friends":friends
    }
    return render(request, 'friends.html', context=context)

def guestFriendsView(request, id):
    guestUser = models.User.objects.get(id=id)
    friend, created = models.Friend.objects.get_or_create(currentUser=guestUser)
    friends = friend.users.all()
    context = {
    "friends":friends,
    "guestUser":guestUser,
    }
    return render(request,'guestFriends.html',context=context)

def chat(request):
    return render(request, 'chat.html')

def room(request, room_name):
    context = {
        'room_name':room_name,
    }
    return render(request, 'room.html', context=context)
def settingsView(request):
    if request.method =='POST':
        form = forms.EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/home/')
        else:
            messages.error(request, 'User already exists')
            return redirect('/settings/')
    else:
        form = forms.EditAccountForm(instance=request.user)
        context = {
        "form":form
        }
        return render(request, 'settings.html', context=context)
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/login/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changePassword.html', {
        'form': form
    })
