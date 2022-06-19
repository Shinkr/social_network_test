from django.shortcuts import render, redirect
from .models import Profile, shout
from .forms import ShoutForm

# Create your views here.
def dashboard(request):

    form = ShoutForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            shout_a = form.save(commit=False)
            shout_a.user = request.user
            shout_a.save()
            return redirect("shout:dashboard")

    followed_shouts = shout.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
    return render(request, "dashboard.html", {"form": form, "shout": followed_shouts})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

def profile(request, pk):

    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "profile.html", {"profile": profile})