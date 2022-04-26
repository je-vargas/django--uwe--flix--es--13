def get_user_groups(request):
    group = request.user.groups.values_list('name',flat = True) # QuerySet Object
    return list(group) 
    