from django.shortcuts import render, redirect
from .models import Profile


def profiles(request):
    prof = Profile.objects.all()
    context = {
        'profiles': prof
    }
    return render(request, 'users/index.html', context)

def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact="")  # __exact - точное совпадение
    other_skill = prof.skill_set.filter(description="")

    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skill': other_skill
    }
    return render(request, 'users/profile.html', context)
