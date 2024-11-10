import re

gpa_10 = [5, 7, 8, 10, 9]
gpa_4 = map(lambda gpa: gpa/10*4, gpa_10)
print(list(gpa_4))

friends = ["An", "Khoa", "Linh", "Tuan"]
friends_upper = map(str.upper, friends)
print(list(friends_upper))


def count_characters(text):
  words = text.lower().split()
  all_chars = ''.join(words)
  chars = set(all_chars)

  char_counts = map(lambda char: (char, all_chars.count(char)), chars)

  return dict(char_counts)

text = "Khoa"
result = count_characters(text)
print(result)


def quet_the(ngay1, ngay2):
    set_ngay1 = set(ngay1)
    set_ngay2 = set(ngay2)
    
    ngay_2_1 = set_ngay2
    mot_trong_hai_ngay = set_ngay1.union(set_ngay2)
    chi_ngay1 = set_ngay1 - set_ngay2

    return ngay_2_1, mot_trong_hai_ngay, chi_ngay1

ngay1 = [101, 107, 359, 107]
ngay2 = [994, 928, 788, 780, 928, 101]

ket_qua = quet_the(ngay1, ngay2)
print("Ngày 2/1:", ket_qua[0])
print("Ngày 1/1 hoặc 2/1:", ket_qua[1])
print("Chỉ ngày 1/1:", ket_qua[2])

def sort_students(student_list):
    sorted_students = sorted(
        enumerate(student_list),
        key=lambda x: (-x[1]['math'], -x[1]['literature'], x[0])
    )
    return [student[1] for student in sorted_students]

students = [
    {'id': 984, 'math': 9.0, 'literature': 5.4},
    {'id': 12, 'math': 9.5, 'literature': 4.3},
    {'id': 324, 'math': 9.0, 'literature': 5.4}
]

sorted_students = sort_students(students)
print(sorted_students)

def find_class_president_votes(votes_dict):
    vote_count = {}

    for votes in votes_dict.values():
        for student in set(votes):
            vote_count[student] = vote_count.get(student, 0) + 1

    max_votes = max(vote_count.values(), default=0)

    top_students = [student for student, count in vote_count.items() if count == max_votes]

    return f"STT: {', '.join(map(str, top_students))} | Số phiếu: {max_votes}"

votes_dict = {
    1: [2, 3, 4],
    2: [2],
    5: [1, 1, 3]
}

print(find_class_president_votes(votes_dict))

def mail_regEx(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    if not re.match(pattern, email):
        return "Email không hợp lệ: phải kết thúc bằng '@gmail.com'"
    return "Email hợp lệ"

print(mail_regEx("example@gmail.com")) 
print(mail_regEx("example@yahoo.com"))
print(mail_regEx("example@gmail.co"))
print(mail_regEx("examplegmail.com"))