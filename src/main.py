from secondary import *


def main() -> None:

    op : str

    r : requests.models.Response

    while True:

        s = requests.Session()

        op = input('OP: ')

        if op in ['q', 'quit', 'exit']: break

        elif op in ['n', 'new', 't', 'test']:
            show_req(req(s, input('-> Method  : '), input('-> URL     : '), input('-> Params  : '), input('-> JSON    : ')))
        
        elif op in ['sp', 'section-parameters', 'section-params']:
            try: s.params = eval(input('-> Params  : '))
            except: print('Error while evaluating parameters')

    return

if __name__ == '__main__': main()
