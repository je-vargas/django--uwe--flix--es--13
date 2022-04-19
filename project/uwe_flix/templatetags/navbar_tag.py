from django import template
from django.contrib.auth.models import Group
from access import get_user_groups

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group):
    user_access = user.groups.values_list('name',flat = True)
    if group in user_access: return True 
    else: return False
