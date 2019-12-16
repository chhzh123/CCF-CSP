n = int(input())

def parse_num(s):
    num = ""
    idx_char = 0
    for idx, char in enumerate(s):
        if char.isdigit():
            num += char
        else:
            idx_char = idx
            num = 1 if num == "" else int(num)
            return idx_char, num
    idx_char += 1
    num = 1 if num == "" else int(num)
    return idx_char, num

def parse_ele(s):
    if len(s) >= 2 and s[1].islower():
        idx, num = parse_num(s[2:])
        return 2+idx, s[:2], num
    else:
        idx, num = parse_num(s[1:])
        return 1+idx, s[0], num

def parse(terms):
    elements = {}
    terms = terms.split("+")
    for term in terms:
        # find coef
        idx_coef, coef = parse_num(term)
        # print(term,"idx:",idx_coef,coef)
        # find elements
        term = term[idx_coef:]
        inner_coef, inner_num = 1, 1
        stack = []
        while len(term) != 0:
            if term[0] == "(":
                stack.append("(")
                term = term[1:]
                ridx = len(term)
                for i in range(len(stack)):
                    ridx = term[:ridx].rfind(")")
                _, inner_num = parse_num(term[ridx+1:])
                inner_coef *= inner_num
                # print(inner_num,inner_coef)
                index, ele, num = parse_ele(term)
            elif term[0] == ")":
                stack.pop()
                term = term[1:]
                index, _ = parse_num(term)
                inner_coef //= inner_num
                term = term[index:]
                continue
            else:
                index, ele, num = parse_ele(term)
            # print(term,"idx",index,ele,num)
            elements[ele] = elements.get(ele,0) + num * coef * inner_coef
            term = term[index:]
    # print(elements)
    return elements

for i in range(n):
    left, right = input().split("=")
    dictl = parse(left)
    dictr = parse(right)
    if dictl == dictr:
        print("Y")
    else:
        print("N")