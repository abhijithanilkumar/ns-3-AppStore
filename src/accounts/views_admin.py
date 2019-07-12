from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

User = get_user_model()


def moderate_users(request):
    users = User.objects.filter(groups__name='Moderation')
    if request.method == 'POST':
        print("POST")
    
    context = {
        'users': users
    }
    return render(request, 'admin/users.html', context);


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