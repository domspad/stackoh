# stackoh
viz the SO data!

All the data!


## running heroku stuff

```
source stackohenv/bin/activate

heroku create

heroku ps:scale web=1 --app stackoh

sudo gem install foreman  (to try locally running)

git push heroku master

heroku apps --all

heroku logs --app stackoh

heroku addons:open papertrail --app stackoh

heroku open --app stackoh

heroku local --app stackoh

foreman start
```