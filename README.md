# django_apache_issue

1. Create a virtual envirnment
2. Install all the dependancy using requirement.txt file
3. copy the config file to /etc/apache/site-available and change the location according in the file.
4. restart apache service (sudo service apache2 restart)

Now the site should be able to get the error(/var/log/apache2/error.log)
