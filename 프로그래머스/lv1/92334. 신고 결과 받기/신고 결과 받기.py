def solution(id_list, report, k):
    answer = []
    bad_people = []
    stoped_people = []
    good_people = []
    report = set(report)
    report = list(report)
    for i in range(len(report)):
        tmp = report[i].split()
        bad_people.append(tmp[1])
    
    for i in range(len(id_list)):
        if bad_people.count(id_list[i])>=k:
            stoped_people.append(id_list[i])

    for i in range(len(report)):
        tmp = report[i].split()
        if stoped_people.count(tmp[1]) == 1:
            good_people.append(tmp[0])

    for i in range(len(id_list)):
        answer.append(good_people.count(id_list[i]))

    return answer