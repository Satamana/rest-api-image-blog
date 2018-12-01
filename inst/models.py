import string as str
from random import choice
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

def gererate_id():
    n=10
    random = str.ascii_uppercase + str.ascii_lowercase + str.digits
    return ''.join(choise(random) for _ in range(n))


class Post(models.Model):
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=10, default=gererate_id)
    photo = models.FileField(upload_to='posts_photo')
    caption = models.CharField(max_length=100,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-date_created', ]

    def __str__(self):
        return self.slug

    def get_ablolute_url(self):
        return reverse('posts:view', kwargs= {'slug': self.slug})


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return '{} : {}'.format(self.follower.username, self.following.username)
