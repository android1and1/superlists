Provisioning a new site
============================================

## Required package:

* Nginx
* Python 3
* Git
* Pip
* Virtualenv

eg,on Ubuntu:
	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## Nginx Virtual Host Config

* see nginx.template.conf.
* replace SITENAME with,eg,staging.my-domain.com

## Upstart job
* see gunicorn-updatart.template.conf
* replace SITENAME with,eg,staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
 |
 |----sites
	|
        |	
	|----SITENAME
        |	|
	|       |---database
        |	|---source(created by"django-admin.py startproject source")
        |	|---static
        |	|---virtualenv
        |	|
        |	|
	|----SITENAME(another)
		|
		|---database
        	|---source(created by"django-admin.py startproject source")
		|---static
		|---virtualenv
