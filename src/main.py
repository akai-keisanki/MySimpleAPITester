from secondary import *

def main() -> None:

    dotenv.load_dotenv()

    op : str
    r : requests.models.Response

    s : requests.Session = requests.Session()

    while True:

        op = input('OP: ')

        if op in ['q', 'quit', 'exit']: break

        elif op in ['n', 'new', 't', 'test', 'r', 'request', 'new-request', 'new-req', 'test-request', 'test-req']:
            show_req(req(s, input('-> Method  : '), input('-> URL     : '), input('-> Params  : '), input('-> JSON    : ')))
        
        elif op in ['sp', 'section-parameters', 'section-params', 's-params']:
            try: s.params = eval(input('-> Params  : '))
            except: print('Error while evaluating parameters')

        elif op in ['ssp', 'show-section-parameters', 'show-section-params', 'show-s-params']:
            print(f'-- sec.par.: {s.params}')

        elif op in ['de', 'dotenv', 'get-dotenv', 'dotenv-params', 'desp', '.env']:
            try: s.params[input('-> label   : ')] = os.environ.get(input('-> .env var: '))
            except: print('Error while getting parameters')

    return

if __name__ == '__main__': main()
