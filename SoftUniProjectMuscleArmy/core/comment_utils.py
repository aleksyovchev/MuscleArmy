def apply_likes_count(comment):
    comment.likes_count = comment.commentlike_set.count()
    return comment


#seen in Workshop 2 (2:10:58)
def apply_user_liked_comment(comment):
    comment.is_liked_by_user = comment.likes_count > 0
    return comment


