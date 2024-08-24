import requests
from django.shortcuts import render

def github_user(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if username:
            url = f'https://api.github.com/users/{username}'
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                return render(request, 'github_user.html', {'data': data})
            else:
                return render(request, 'github_user.html', {'error': 'User not found'})
        return render(request, 'github_user.html')