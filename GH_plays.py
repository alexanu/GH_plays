
# To interact with the GitHub API you can either 
# 1) authenticate to access protected functionality 
github3.login(username, password)

# 2) or you can interact with it anonymously.

from github3 import GitHub
gh = GitHub()




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



from github3 import login
gh = login(username, password)
gists = [g for g in gh.iter_gists()] # Listing gists

# ----------------------------------------------------------------------------------------------------------------------------
from github3 import login, GitHub

sigma = 'sigmavirus24'
github3 = 'github3.py'
todopy = 'Todo.txt-python'
kr = 'kennethreitz'
requests = 'requests'

g = login(user, password)

if g.is_subscribed(sigma, todopy):
    g.unsubscribe(sigma, todopy)

for follower in g.iter_followers():
    print("{0} is following me.".format(follower.login))

for followee in g.iter_following():
    print("I am following {0}.".format(followee.login))

if g.is_following(sigma):
    g.unfollow(sigma)

# ----------------------------------------------------------------------------------------------------------------------------


for short_repository in github.repositories_by('python-hyper'):
    ...
    
uritemplate = github.repository('python-hyper', 'uritemplate') # uritemplate is a name of a package
contributors_without_forks = (set(uritemplate.contributors()) -
                              set(fork.owner for fork in uritemplate.forks()))
print(f'The following contributors deleted their forks of {uritemplate!r}')
for contributor in sorted(contributors_without_forks, key=lambda c: c.login):
    print(f'  * {contributor.login}')
    
    

class github3.repos.repo.Repository(json, session)

fork # Whether or not this repository is a fork of another.
forks_url # The URL to retrieve this repository’s list of forks.
