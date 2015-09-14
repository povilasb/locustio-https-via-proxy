=====
About
=====

http://locust.io/ is an open source load testing tool. Unfortunately, it
does not support HTTPS testing via HTTP proxy server when HTTP tunnel is used.

The problem is with the low level component `urllib3` which is used by
locust to make HTTP/HTTPS requests.
When proxy server is used with HTTPS requests, `urllib3` makes `CONNECT`
requests but does not append `Proxy-Authorization` header.

This repository contains `locust` and `requests` sources imported from pip
together with a small fix.


How to use it?
==============

By the time this commit was made, it was not known to me how to properly start
locust. So a dirty hack was made.

You have to install locust with pip:

	$ pip install locustio

Edit `locustfile.py` to meet your needs.

Then you can run:

	$ ./start_locust -h https://mytarget.com/path.html
