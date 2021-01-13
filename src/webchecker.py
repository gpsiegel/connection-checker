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
            server = res.headers.get('server')
            mod = res.headers.get('Last-Modified')
            content = res.headers.get('Content-Type')

            if server is None:
                server = 'N/A'
            if mod is None:
                mod = 'N/A'
            if content is None:
                content = 'N/A'

            f_list = server, mod, content, f_site
            return "\n{}".format('\n'.join(f_list))
    except TypeError:
        print("N/A")
        

def check_website(website):
    try:
        f_site = filtered_site(website)
        result = str(user_result(f_site))
        return result
    except Exception:
        print('An error has occurred with that input')
