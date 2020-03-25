# nokia-recon
Help for get some vulns in nokia :)

Don't Forget use ```dirsearch``` tool on this domains ..!

```
$ python3 dirsearch.py -u DOMAIN -e * -t 50
```
### Good Luck

```bash
recon(){
        mkdir $1
        cd $1
        sublist3r -d $1 -o domains.txt
        amass enum --passive -d $1 -o domains.txt
        assetfinder -subs-only $1 >> domains.txt
        sort -u domains.txt -o domains.txt
        mkdir out
        cat domains.txt | xargs -I % sh -c 'whatweb % -v --color=never --no-errors > out/%.txt'
        echo '[+] Done '
}



```
