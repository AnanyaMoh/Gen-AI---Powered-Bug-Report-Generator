import os
import requests

def create_github_issue(report):
    token = os.getenv('GITHUB_TOKEN')
    repo = os.getenv('REPO_NAME')

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json'
    }

    data = {
        "title": "Bug Report - AI Generated",
        "body": report['markdown']
    }

    response = requests.post(
        f"https://api.github.com/repos/{repo}/issues",
        headers=headers,
        json=data
    )

    if response.status_code == 201:
        return response.json()['html_url']
    else:
        return f"Error: {response.status_code}"
