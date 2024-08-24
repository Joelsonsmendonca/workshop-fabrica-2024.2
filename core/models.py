from django.db import models

class GitHubUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class GitHubUserDetails(models.Model):
    login = models.CharField(max_length=100, unique=True)
    user_id = models.IntegerField(unique=True)
    node_id = models.CharField(max_length=100)
    avatar_url = models.URLField()
    gravatar_id = models.CharField(max_length=100, blank=True)
    url = models.URLField()
    html_url = models.URLField()
    followers_url = models.URLField()
    following_url = models.URLField()
    gists_url = models.URLField()
    starred_url = models.URLField()
    subscriptions_url = models.URLField()
    organizations_url = models.URLField()
    repos_url = models.URLField()
    events_url = models.URLField()
    received_events_url = models.URLField()
    user_type = models.CharField(max_length=50)
    site_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.login