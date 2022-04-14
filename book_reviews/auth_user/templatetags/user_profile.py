from django import template

from book_reviews.auth_user.models import Profile

register = template.Library()


@register.simple_tag(takes_context=True)
def user_profile(context):
    request = context['request']

    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.id)
        return {
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'id': profile.user_id,
            'picture': profile.picture,
        }
    return None


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
