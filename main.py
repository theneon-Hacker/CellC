import sys, re

with open(sys.argv[1]) as f:
    sc = f.read()

def lex(characters, token_table):
    pos = 0
    tokens_lst = []
    while pos < len(characters):
        match = None
        for token_expr in token_table:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens_lst.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens_lst


data = [
    (r'[ \t\n]', None),
    (r'\#.*', None),
    (r'add', 'ADD'),
    (r'new', 'NEW'),
    (r'del', 'DEL'),
    (r'=', 'EQ'),
    (r'~', 'NOTEQ'),
    (r'if', 'IF'),
    (r'next', 'NEXT'),
    (r'DATA', 'DATA'),
    (r'NOW', 'NOW'),
    (r'while', 'WHILE'),
    (r'\{', 'START'),
    (r'\}', 'END'),
    (r'echo', 'PRINT'),
    (r'\(', 'LBR'),
    (r'\)', 'RBR'),
    (r';', 'SEP'),
    (r'\>', 'MORE'),
    (r'\<', 'LESS'),
    (r'\$', 'INPUT'),
    (r'\'.*\'', 'STRING'),
    (r'[-]?[0-9]+', 'INT'),

]

toks = lex(sc, data)
# global ceils, index
ceils, index = [0] * 10, 0
def parse(toks):
    global ceils, index
    result = {}
    condition = []
    commands_to_loop = []
    to_print = [] 
    for j, i in enumerate(toks):
        if i[1] == 'MORE':
            result.update({j : result[j - 1] > parse([toks[j + 1]])[0]})
        elif i[1] == 'LESS':
            result.update({j : result[j - 1] < parse([toks[j + 1]])[0]})
        elif i[1] == 'EQ':
            result.update({j : result[j - 1] == parse([toks[j + 1]])[0]})
        elif i[1] == 'NOTEQ':
            result.update({j : result[j - 1] != parse([toks[j + 1]])[0]})
        elif i[1] == 'INPUT':
            result.update({j: int(input())})
        elif i[1] == 'INT':
            result.update({j: int(i[0])})
        elif i[1] == 'STRING':
            result.update({j: i[0][1:-1]})
        elif i[1] == 'NOW':
            result.update({j : ceils[index]})
        elif i[1] == 'DATA':
            result.update({j : ceils})
        elif i[1] == 'ADD':
            if j + 1 < len(toks):
                a = parse([toks[j + 1]]).get(0)
                if isinstance(a, int):
                    ceils[index] += a
                    parse(toks[j + 2:])
                    break
                else:
                    ceils[index] += 1
            else:
                ceils[index] += 1

        elif i[1] == 'NEXT':
            if j + 1 < len(toks):
                a = parse([toks[j + 1]]).get(0)
                if isinstance(a, int):
                    index += a
                    if index >= len(ceils):
                        index = len(ceils) - 1
                    elif index < 0: index = 0
                    parse(toks[j + 2:])
                    break
                else:
                    index += 1
                    if index >= len(ceils):
                        index = len(ceils) - 1
                    elif index < 0: index = 0
            else:
                index += 1
                if index >= len(ceils):
                        index = len(ceils) - 1
                elif index < 0: index = 0

        elif i[1] == 'NEW':
            ceils.append(0)
        elif i[1] == 'DEL':
            ceils.pop()
                
                
        elif i[1] == 'PRINT':
            if toks[j+1][1] == 'LBR':
                for n, i in enumerate(toks[j+2:]):
                    if i[1] == 'RBR':
                        break
                    else:
                        to_print.append(i)
                result.update({j: parse(to_print)[round(n / 2) - 1]}
                )
                print(result[j])
            else:
                result.update({j: parse([toks[j+1]])[0]})
                print(result[j])
        elif i[1] == 'WHILE':
            for z, x in enumerate(toks[j + 1:]):
                if x[1] == 'LBR': pass
                elif x[1] == 'RBR': break
                else:
                    condition.append(x)

            for g, y in enumerate(toks[z + j + 2:]):
                if y[0] == '{': pass
                elif y[0] == '}': break
                else:
                    commands_to_loop.append(y)

            while parse(condition)[round(z / 2) - 1]:
                parse(commands_to_loop)
            condition.clear()
            commands_to_loop.clear()
            parse(toks[z + j + 3 + g:])
            break
        elif i[1] == 'IF':
            for z, x in enumerate(toks[j + 1:]):
                if x[1] == 'LBR': pass
                elif x[1] == 'RBR': break
                else:
                    condition.append(x)

            for g, y in enumerate(toks[z + j + 2:]):
                if y[0] == '{': pass
                elif y[0] == '}': break
                else:
                    commands_to_loop.append(y)

            if parse(condition)[round(z / 2) - 1]:
                parse(commands_to_loop)
            condition.clear()
            commands_to_loop.clear()
            parse(toks[z + j + 3 + g:])
            break
    return result


parse(toks)
            
