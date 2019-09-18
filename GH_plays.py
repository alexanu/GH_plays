


# --------------------------------------------------------------------------------
from github3 import login

gh = login('sigmavirus24', password='<password>')

sigmavirus24 = gh.me()
# <AuthenticatedUser [sigmavirus24:Ian Stapleton Cordasco]>

print(sigmavirus24.name) 
print(sigmavirus24.login)
print(sigmavirus24.followers_count)

for f in gh.followers():
    print(str(f))

kennethreitz = gh.user('kennethreitz')

print(kennethreitz.name)
print(kennethreitz.login)
print(kennethreitz.followers_count)

followers = [str(f) for f in gh.followers('kennethreitz')]
