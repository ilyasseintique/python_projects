# dic = [{"name":"ilyasse"}]
# print(dic[0]["name"])
# print(f'my name is {dic[0]["name"]}')
def arithmetic_arranger(problems,show_answers=False):
    first_line=''
    second_line=''
    dashes=''
    solution=''
    gap='    '
    if len(problems)>5:
        return 'error'
    for item in problems:
        first,op,second=item.split(' ')
        if len(first)>4 or len(second)>4:
            return 'error'
        if op not in ('+','-'):
            return 'error'
        if not first.isdigit() or not second.isdigit():
            return 'error'
        first_line+=first.rjust(6)+gap
        second_line+=op+second.rjust(5)+gap
        dashes+="______"+gap
        solution+=str(eval(item)).rjust(6)+gap
    tot=[]
    tot.append(first_line)
    tot.append(second_line)
    tot.append(dashes)
    tot.append(solution)
    return '\n'.join(tot)
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

