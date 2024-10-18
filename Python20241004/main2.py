def function(string):
    answer = 0
    for i in string:
        if i in ['а', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']:
            answer += 1
    return answer

print(function("AMOGUS"))
