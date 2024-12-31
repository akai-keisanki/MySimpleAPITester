import requests

req_mets : dict[callable] = {
        'GET' : requests.get,
        'POST' : requests.post,
        'DELETE' : requests.delete,
    }

stt_cods : dict[callable] = {
        100 : 'Continue',
        101 : 'Switching Protocols',
        102 : 'Processing',
        103 : 'Early Hints',

        200 : 'OK',
        201 : 'Created',
        102 : 'Accepted',
        203 : 'Non-Authoritative Information',
        204 : 'No Content',
        205 : 'Reset Content',
        206 : 'Partial Content',
        207 : 'Multi-Status',
        208 : 'Already Reported',
        226 : 'IM Used',

        300 : 'Multiple Choices',
        301 : 'Moved Permanently',
        302 : 'Found',
        303 : 'See Other',
        304 : 'Not Modified',
        305 : 'Use Proxy',
        306 : 'unused',
        307 : 'Temporary Redirect',
        308 : 'Permanent Redirect',

        400 : 'Bad Request',
        401 : 'Unauthorized',
        402 : 'Payment Required',
        403 : 'Forbidden',
        404 : 'Not Found',
        405 : 'Method Not Allowed',
        406 : 'Not Acceptable',
        407 : 'Proxy Authentication Required',
        408 : 'Request Timeout',
        409 : 'Conflict',
        410 : 'Gone',
        411 : 'Length Required',
        412 : 'Precondition Failed',
        413 : 'Content Too Large',
        414 : 'URI Too Long',
        415 : 'Unsupported Media Type',
        416 : 'Range Not Satisfiable',
        417 : 'Expectation Failed',
        418 : 'I\'m a teapot',
        421 : 'Misdirected Request',
        422 : 'Unprocessable Content',
        423 : 'Locked',
        424 : 'Failed Dependency',
        425 : 'Too Early',
        426 : 'Upgrade Required',
        428 : 'Precondition Required',
        429 : 'Too Many Requests',
        431 : 'Request Header Fields Too Large',
        451 : 'Unavailable Fro Legal Reasons',

        500 : 'Internal Server Error',
        501 : 'Not Implemented',
        502 : 'Bad Gateway',
        503 : 'Service Unavailable',
        504 : 'Gateway Timeout',
        505 : 'HTTP Version Not Supported',
        506 : 'Variant Also Negotiates',
        507 : 'Insufficient Storage',
        508 : 'Loop Detected',
        510 : 'Not Extended',
        511 : 'Network Authentication Required'
    }


def req(met : str, url : str, pr : str = '{}', js : str = '{}') -> requests.models.Response:

    return req_mets[met](url, params = eval(pr), json = eval(js))

def show_req(r : requests.models.Response) -> None:

    tmp : str = ' - '
    tmp += 'Informational' if 100 <= r.status_code < 200 else 'Successfull' if 200 <= r.status_code < 300 else 'Redirection' if 300 <= r.status_code < 400 else 'Client error' if 400 <= r.status_code < 500 else 'Server error' if 500 <= r.status_code < 600 else 'Unknown'
    try: tmp += ' - ' + stt_cods[r.status_code]
    except: pass
    finally:
        print(f'<- status  : {r.status_code}{tmp}')
        print(f'<- text    : \n----------------\n{r.text}\n----------------')
