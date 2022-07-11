def throughput_per_second(log, start, end):
    cnt = 0
    for i in log:
        if i[0] < end and i[1] >= start:
            cnt += 1
    return cnt

def solution(lines):
    answer = 0
    log = []
    for i in lines:
        date, time, t = i.split()
        h, m, s = time.split(":")
        
        s_end_time = (float(h) * 3600 + float(m) * 60 + float(s)) * 1000
        s_start_time = s_end_time - float(t[:-1]) * 1000 + 1
        log.append((s_start_time, s_end_time))

    for i in log:
        answer = max(answer, throughput_per_second(log, i[0], i[0] + 1000), throughput_per_second(log, i[1], i[1] + 1000))

    return answer