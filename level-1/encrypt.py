def solution(x):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    for char in x:
        if char in abc:
            encrypted_message += abc[::-1][abc.index(char)]
        else:
            encrypted_message += char

    return encrypted_message


print(solution('Hello!'))
