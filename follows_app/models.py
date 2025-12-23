from django.db import models
from users_app.models import UserProfile

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')  # prevents a user from following the same person twice

    def __str__(self):
        return f"{self.follower.user.username} follows {self.following.user.username}"