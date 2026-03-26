def solution(answers):
    stud1 = [1,2,3,4,5] * 2000
    stud2 = [2,1,2,3,2,4,2,5] * 2000
    stud3 = [3,3,1,1,2,2,4,4,5,5] * 2000 
    students = [stud1,stud2,stud3]
    score = [0,0,0]
    
    for idx, answer in enumerate(answers):
        for i in range(3):
            userAnswer = students[i][idx]
            if userAnswer == answer:
                score[i] += 1
    
    answer = []
    for i in range(3):
        if max(score) == score[i]:
            answer.append(i+1)
    
    return answer