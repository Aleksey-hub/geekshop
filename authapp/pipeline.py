import requests


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'github':
        return

    resp = requests.get('https://api.github.com/users/' + str(user))

    if resp.status_code != 200:
        return

    # data = resp.json()['response'][0]
    data = resp.json()
    if data['bio']:
        user.shopuserprofile.aboutMe = data['bio']

    user.save()
