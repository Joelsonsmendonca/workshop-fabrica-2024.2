import requests
from django.shortcuts import render
from .models import GitHubUser, GitHubUserDetails

def github_user(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if username:
            url = f'https://api.github.com/users/{username}'
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                # Salvar os dados no modelo GitHubUser
                user, created = GitHubUser.objects.update_or_create(
                    username=username,
                    defaults={
                        'name': data.get('name'),
                        'bio': data.get('bio'),
                        'location': data.get('location'),
                        'followers': data.get('followers'),
                        'following': data.get('following'),
                    }
                )
                
                # Salvar os dados no modelo GitHubUserDetails
                details, created = GitHubUserDetails.objects.update_or_create(
                    login=data.get('login'),
                    defaults={
                        'user_id': data.get('id'),
                        'node_id': data.get('node_id'),
                        'avatar_url': data.get('avatar_url'),
                        'gravatar_id': data.get('gravatar_id'),
                        'url': data.get('url'),
                        'html_url': data.get('html_url'),
                        'followers_url': data.get('followers_url'),
                        'following_url': data.get('following_url'),
                        'gists_url': data.get('gists_url'),
                        'starred_url': data.get('starred_url'),
                        'subscriptions_url': data.get('subscriptions_url'),
                        'organizations_url': data.get('organizations_url'),
                        'repos_url': data.get('repos_url'),
                        'events_url': data.get('events_url'),
                        'received_events_url': data.get('received_events_url'),
                        'user_type': data.get('type'),
                        'site_admin': data.get('site_admin'),
                    }
                )
                
                return render(request, 'github_user.html', {'data': data})
            else:
                return render(request, 'github_user.html', {'error': 'User not found'})
        return render(request, 'github_user.html')