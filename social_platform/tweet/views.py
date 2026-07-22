from django.shortcuts import render
from .models import Tweet,Profile
from .forms import TweetForms,RegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .utils import send_email_to_client
from django.contrib.auth.forms import PasswordResetForm
#
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForms(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms()
    return render(request,'tweet_form.html',{'form' : form})

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST' :
        form = TweetForms(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForms(instance=tweet)
        return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_del(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'del_confirm.html', {'tweet':tweet})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():

            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.set_password(form.cleaned_data["password1"])
            user.save()

            Profile.objects.create(
                user=user,
                profile_pic=form.cleaned_data.get("profile_pic")
            )

            login(request, user)
            return redirect("tweet_list")

    else:
        form = RegistrationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )
@login_required
def profile(request):
    tweets = Tweet.objects.filter(user=request.user).order_by("-created_at")

    context = {
        "tweets": tweets,
        "total_tweets": tweets.count(),
    }

    return render(request, "registration/profile.html", context)

def sent_email(request):
    send_email_to_client(
        subject="Password Reset",
        message=f'{request.user.username} .you can reset your password!',
        recipient_email=request.user.email,
    )
    return redirect("tweet_list")

def logged_out(request):
    logout(request)
    return render(request, "registration/logged_out.html")