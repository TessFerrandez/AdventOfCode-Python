from pyparsing import alphanums, alphas, nums, delimitedList, oneOf, Combine, Group, OneOrMore, Optional, Suppress, White, Word


def parse_ssn(input_string: str):
    """
    ssn     ::= nums+ '-' nums+ '-' nums+
    nums    ::= '0'..'9'
    """
    dash = '-'
    ssn_parser = Combine(Word(nums, exact=3) + dash + Word(nums, exact=2) + dash + Word(nums, exact=4))

    for match, start, stop in ssn_parser.scanString(input_string):
        print(match, start, stop)


def parse_key_value(input_string: str):
    key = Word(alphanums)('key')
    equals = Suppress('=')
    value = Word(alphanums)('value')

    kv_expression = key + equals + value

    for match in kv_expression.scanString(input_string):
        result = match[0]
        print(f'{result.key} is {result.value}')


def parse_url():
    """
    url ::= scheme '://' [userinfo] host [port] [path] [query] [fragment]
    scheme ::= http | https | ftp | file
    userinfo ::= url_chars+ ':' url_chars+ '@'
    host ::= alphanums | host (. + alphanums)
    port ::= ':' nums
    path ::= url_chars+
    query ::= '?' + query_pairs
    query_pairs ::= query_pairs | (query_pairs '&' query_pair)
    query_pair = url_chars+ '=' url_chars+
    fragment = '#' + url_chars
    url_chars = alphanums + '-_.~%+'
    """
    url_chars = alphanums + '-_.~%+'
    fragment = Combine((Suppress('#') + Word(url_chars)))('fragment')
    scheme = oneOf('http https ftp file')('sheme')
    host = Combine(delimitedList(Word(url_chars), '.'))('host')
    port = Suppress(':') + Word(nums)('port')
    user_info = (Word(url_chars)('username') + Suppress(':') + Word(url_chars)('password') + Suppress('@'))
    query_pair = Group(Word(url_chars) + Suppress('=') + Word(url_chars))
    query = Group(Suppress('?') + delimitedList(query_pair, '&'))('query')
    path = Combine(Suppress('/') + OneOrMore(~query + Word(url_chars + '/')))('path')

    url_parser = (scheme + Suppress('://') + Optional(user_info) + host + Optional(port) + Optional(path) + Optional(query) + Optional(fragment))

    test_urls = [
        'http://www.notarealsite.com',
        'http://www.notarealsite.com/',
        'http://www.notarealsite.com:1234/',
        'http://bob:%243cr3t@www.notarealsite.com:1234/',
        'http://www.notarealsite.com/presidents',
        'http://www.notarealsite.com/presidents/byterm?term=26&name=Roosevelt',
        'http://www.notarealsite.com/presidents/26',
        'http://www.notarealsite.com/us/indiana/gary/population',
        'ftp://ftp.info.com/downloads',
        'http://www.notarealsite.com#moose',
        'http://bob:s3cr3t@www.notarealsite.com:8080/presidents/byterm?term=26&name=Roosevelt#bio',
    ]

    for test_url in test_urls:
        print("URL:", test_url)
        tokens = url_parser.parseString(test_url)
        print(tokens, '\n')
        print("Scheme:", tokens.scheme)
        print("User name:", tokens.username)
        print("Password:", tokens.password)
        print("Host:", tokens.host)
        print("Port:", tokens.port)
        print("Path:", tokens.path)
        print("Query:")
        for key, value in tokens.query:
            print("\t{} ==> {}".format(key, value))
        print('Fragment:', tokens.fragment)
        print('-' * 60, '\n')


def uppercase_it(tokens):
    return [t.upper() for t in tokens]


def taking_action():
    prefix = 'A Fistful of' + White()
    fist_contents = Word(alphas)
    fist_contents.setParseAction(uppercase_it)
    title_parser = Combine(prefix + fist_contents)

    for title in ('A Fistful of Dollars', 'A Fistful of Spaghetti', 'A Fistful of Doughnuts'):
        print(title_parser.parseString(title))


def main():
    '''
    input_string = """
      xxx 225-92-8416 yyy
      103-33-3929 zzz 028-91-0122
    """
    parse_ssn(input_string)

    print('-' * 20)

    input_string = """
    city=Atlanta
    state=Georgia
    population=5522942
    """
    parse_key_value(input_string)

    print('-' * 20)

    parse_url()

    print('-' * 20)

    taking_action()
    '''


if __name__ == "__main__":
    main()
