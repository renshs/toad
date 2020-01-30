phone_number = input()
correct = True
if phone_number.strartswith('8') or phone_number.startswith('+7'):
    while ' ' in phone_number:
        phone_number.split()
        phone_number = ''.join(phone_number)
        for i in range(len(phone_number)):
            if phone_number[i] == '(':
                closed = False
                for j in range(i + 1, len(phone_number)):
                    if phone_number[j] == '(':
                        correct = False
                    elif phone_number[j] == ')':
                        closed = True
                if not closed:
                    correct = False
        if correct:
            if phone_number[0] == '-' or phone_number[-1] == '-':
                correct = False
            for i in range(1, len(phone_number) - 1):
                if phone_number[i] == '-' and phone_number[i + 1]:
                    correct = False
answer = ''
if correct:
    for i in range(len(phone_number)):
        if i == 0 and phone_number[i] == 8:
            answer += '+7'
        if phone_number[i] in '1234567890':
            answer += phone_number[i]
print(answer)


