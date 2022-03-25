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
        }
    return None


@register.simple_tag(takes_context=True)
def page_name(context):
    pages = {
        'Home'
    }

