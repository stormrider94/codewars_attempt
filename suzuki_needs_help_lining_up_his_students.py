def lineup_students(st):
    students = sorted(st.split(),key=lambda name: -len(name))
    length_groups = {}
    final_students_sorted = []
    for student in students:
        if len(student) in length_groups:
            length_groups[len(student)].append(student)
        else:
            length_groups[len(student)] = []
            length_groups[len(student)].append(student)
    print(length_groups)
    for name_length in length_groups:
        final_students_sorted.extend(sorted(length_groups[name_length],reverse=True))
    return final_students_sorted