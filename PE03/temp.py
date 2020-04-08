


def calc(word):
    if len(word) == 1:
        return word[0]
    word = sorted(word, key = lambda x:len(x))
    print(word)
    for x, val in enumerate(word[0]):
        if val != word[1][x]:
            return word[0][:x]
    return word[0]




def longest_prefix(words):
    if len(words) <= 2:
        prefix = calc(words)
        return prefix
    val1 = longest_prefix(words[:len(words)//2])
    val2 = longest_prefix(words[len(words)//2:])
    return calc([val1, val2])
    




#def  binary_tree(key, tree):
#    if key > tree[0]:
#        return binary_tree(key, tree[3]())
#    elif key < tree[0]:
#        return binary_tree(key, tree[2]())
#    else:
#        return tree[1]



#def process(commands):
#    dic = {"|": lambda x, y: x|y, "&": lambda x, y: x&y, "x": lambda x, y: cart(x,y), "-": lambda x, y: x-y}
#    while len(commands) != 1:
#        s1 = commands[0]
#        s2 = commands[2]
#        print(s1,s2,commands)
#        val = dic[commands[1]](s1,s2)
#        commands = commands[3:]
#        commands.insert(0, val)
#    return commands[0]
#def cart(s1,s2):
#    a = [(x,y) for x in s1 for y in s2]
#    o = set({})
#    for x in a:
#        o.add(x)
#    return o


#
#def morgan(expr):
#
#    def negate(expr):
#        out = []
#        expr = list(expr)
#        skip = False
#        for x, val in enumerate(expr):
#            if not skip:
#                if type(val) == tuple:
#                    out.append(negate(val))
#                    skip = False #duvidoso! colocar no fim?
#                elif val == '¬':
#                    out.append(expr[x+1])
#                    skip = True
#                elif val == '∨':
#                    out.append('∧')
#                elif val == '∧':
#                    out.append('∨')
#                else:
#                    out.append(('¬', val))
#                
#        for x in range(len(out)):
#            if type(out[x]) == tuple and len(out[x]) == 1:
#                out[x] = out[x][0]
#        return tuple(out)
#
#    def simplify(expr):
#        out = []
#        skip = False
#        for x, val in enumerate(expr):
#            if not skip:
#                if type(val) == tuple:
#                    out.append(simplify(val))
#                    skip = False
#                elif val == '¬' and type(expr[x+1]) == tuple:
#                    out.append(negate(expr[x+1]))
#                    skip = True
#                else:
#                    out.append(val)
#        out = tuple(out)
#        if len(out) == 1:
#            out = out[0]
#        if len(out) == 1:
#            out = out[0]
#        return out
#    return simplify(expr)