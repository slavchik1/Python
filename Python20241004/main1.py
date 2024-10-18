def function(list):
    answer = 0
    for i in list:
        if i % 2 == 0:
            answer += 1
    return answer

print(function([1, 2, 3, 4, 5]))
