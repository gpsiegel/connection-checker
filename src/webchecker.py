import requests
import re

def filtered_site(str):
    repls = {'http://': '', 'https://': '', 'www.': ''}
    #ensures http://, https://, and www. are filtered out for user_result method
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str)      

def user_result(f_site):
    try:
        with requests.get('http://{}'.format(f_site), timeout=3) as res:
            lists = res.headers
            for k,v in lists.items():
                print(k,v)
    except TypeError:
        print("N/A")
        

def check_website(website):
    try:
        f_site = filtered_site(website)
        result = str(user_result(f_site))
        return result
    except Exception:
        print('An error has occurred with that input')