hi nokia security team .. While testing the Register page I’ve found Rate limit vuln

Steps To Reproduce:
* go to Register page (<a href='https://qa-direct-online.networks.nokia.com/'>link</a>)
* enter your account informations username , email . etc.. 
* click on continue
* get the request using burp suite
* enter the email of victim in email parameter

You Can use my <a href='https://github.com/knassar702/nokia-recon/blob/master/exploits/nokia_emails.py'>script</a>
# Impact

E-mail bombs hack may create Denial of service (DoS) conditions against your e-mail software and even your network and Internet connection by taking up a large amount of bandwidth and, sometimes, requiring large amounts of storage space
