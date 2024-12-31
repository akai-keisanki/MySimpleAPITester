from terciary import *

def req(met : str, url : str, pr : str = '{}', js : str = '{}') -> requests.models.Response:

    try:
        json = eval(js)
        params = eval(pr)
    except:
        print('Error while evaluating data')
        return

    if met not in req_mets.keys():
        print('Error while trying to get request method.')
        return

    try:
        return req_mets[met](url, params = params, json = json)
    except:
        print('Error while requesting')
        return

def show_req(r : requests.models.Response) -> None:

    if r == None:
        print('Request error')
        return

    tmp : str = ' - '
    tmp += 'Informational' if 100 <= r.status_code < 200 else 'Successfull' if 200 <= r.status_code < 300 else 'Redirection' if 300 <= r.status_code < 400 else 'Client error' if 400 <= r.status_code < 500 else 'Server error' if 500 <= r.status_code < 600 else 'Unknown'
    try: tmp += ' - ' + stt_cods[r.status_code]
    except: pass
    finally:
        print(f'<- status  : {r.status_code}{tmp}')
        print(f'<- text    : \n----------------\n{r.text}\n----------------')
