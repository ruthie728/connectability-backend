from django.db import models
from users_app.models import UserProfile
from posts_app.models import Post, Comment

class Notification(models.Model):
    NOTIF_TYPES = [
        ('follow', 'Follow'),
        ('like', 'Like'),
        ('comment', 'Comment'),
    ]

    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_notifications')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notifications')
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sender.user.username} -> {self.receiver.user.username} ({self.notif_type})"