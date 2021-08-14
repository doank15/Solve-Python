if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores=student_marks[query_name] # trả về value của key query_name
    x = sum(query_scores)/3 #dùng hàm sum để tính tổng các scores trong quẻry_scores
    print("{:.2f}".format(x)) #format 2 chữ số thập phân 

    