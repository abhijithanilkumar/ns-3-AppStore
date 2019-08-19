from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.http import HttpResponseRedirect

User = get_user_model()


@login_required
def moderate_users(request):
    users = User.objects.filter(groups__name='Moderation')
    if request.method == 'POST':
        user_pk = request.POST['pk']
        user_group = request.POST['group']
        user_obj = User.objects.get(pk=user_pk)
        if user_group != 'Moderation':
            # Remove user from Moderation Group
            g = Group.objects.get(name='Moderation')
            g.user_set.remove(user_obj)
            profile = Profile.objects.get(user=user_obj)
            profile.moderated = True
            profile.save()
            g = Group.objects.get(name=user_group)
            g.user_set.add(user_obj)
        return HttpResponseRedirect('/users')
    
    context = {
        'users': users
    }
    return render(request, 'admin/users.html', context);


@login_required
def delete_user(request):
    if request.method == 'POST':
        if 'delete' in request.POST and 'pk' in request.POST:
            pk = request.POST['pk']
            try:
                user = User.objects.get(pk=pk)
            except Exception:
                return
            user.delete()
        return HttpResponseRedirect('/users')