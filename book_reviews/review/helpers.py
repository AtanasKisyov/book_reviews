from book_reviews.auth_user.models import Profile


def is_review_owner(user, obj):
    result = False
    if user.is_authenticated:
        profile = Profile.objects.get(pk=user.id)
        result = obj.reviewed_by == profile
    return result


def is_comment_owner(user, obj):
    result = False
    if user.is_authenticated:
        profile = Profile.objects.get(pk=user.id)
        result = obj.commented_by == profile
    return result
