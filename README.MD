**Live** - https://cv-test-app-monday.herokuapp.com/



To locally usage:
~~~
sudo docker build -t test .
~~~

~~~
sudo docker run test .
~~~


also grequests doing async requests as well
~~~
import grequests

urls = [
    'http://www.heroku.com',
    'http://tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://kennethreitz.com'
]

rs = (grequests.get(u) for u in urls)


~~~
