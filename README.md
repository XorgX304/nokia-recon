# nokia-recon
Help for get some vulns in nokia :)

Don't Forget use ```dirsearch``` tool on this domains ..!

```
$ python3 dirsearch.py -u DOMAIN -e * -t 50
```
### Good Luck

```bash
am(){ #runs amass passively and saves to json
amass enum --passive -d $1 -json $1.json
jq .name $1.json | sed "s/\"//g"| httprobe -c 60 | tee -a $1-domains.txt
}
```
