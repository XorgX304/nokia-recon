##### # Xss Reflected And open redirect in `platform.innovation.nokia.com`

#### Steps To Reproduce(xss) :
* visit this <a href='https://platform.innovation.nokia.com/login.php?return_to=/index.php'>link</a>
* add this payload in return_to parameter "><script>alert('@Knassar702')</script>

#### impact :
###### With the help of xss a hacker or attacker can perform social engineering on users by redirecting them from real website to fake one. hacker can steal their cookies and download a malware on their system, and there are many more attacking scenarios a skilled attacker can perform with xss.
#### Recommendations for fix:
 * Content based escaping on the users input
 
#### Steps To Reproduce(openredirect) :
* open this <a href='https://platform.innovation.nokia.com/login.php?return_to=/index.php'>link</a>
* add your website in return_to parameter
* click in exit icon
