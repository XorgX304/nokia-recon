# Xmlrpc.php 

# Description :
##### Wordpress that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DDOS and Start Brute Force attack . The website https://wavelite-selector.networks.nokia.com has the xmlrpc.php file enabled
##### In order to determine whether the xmlrpc.php file is enabled or not, using the Repeater tab in Burp, send the request below.

```
$ curl -d @do.txt https://wavelite-selector.networks.nokia.com/xmlrpc.php
```
<img src='src/xmlrpc_first.png'>
