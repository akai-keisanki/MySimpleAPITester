from secondary import *


def main() -> None:

    op : str

    r : requests.models.Response

    while True:

        op = input('OP: ')

        if op in ['q', 'quit', 'exit']: break

        elif op in ['n', 'new', 't', 'test']:
            show_req(req(input('-> Method  : '), input('-> URL     : '), input('-> Params  : '), input('-> JSON    : ')))

    return

if __name__ == '__main__': main()
