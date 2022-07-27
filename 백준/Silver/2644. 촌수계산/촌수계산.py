from collections import deque, defaultdict


def relation_people(people, start_person, relation_graph):
    q = deque()
    q.append(start_person)
    chon_list = [-1] * (people + 1)
    chon_list[start_person] = 0

    while q:
        cur_person = q.popleft()

        for person in relation_graph[cur_person]:
            if chon_list[person] == -1:
                chon_list[person] = chon_list[cur_person] + 1
                q.append(person)
    
    return chon_list

people = int(input())
start_person, target_person = map(int, input().split())
relations = int(input())
relation_graph = defaultdict(list)
for _ in range(relations):
    parent, child = map(int, input().split())
    relation_graph[parent].append(child)
    relation_graph[child].append(parent) 

answer = relation_people(people, start_person, relation_graph)
print(answer[target_person])