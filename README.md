# nokia-recon
Help for get some vulns in nokia :)

Don't Forget use ```dirsearch``` tool on this domains ..!

```
$ python3 dirsearch.py -u DOMAIN -e * -t 50
```
### Good Luck

```bash
recon(){
	sublist3r -d $1 -o domains.txt
	amass enum --passive -d $1 -o domains.txt
	assetfinder -subs-only $1 > domains.txt
	sort -u domains.txt -o domains.txt
	cat domains.txt | httprobe | tee -a live_domains.txt
}

```
