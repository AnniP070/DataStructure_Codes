def print_array(arr):
    # Check if the input is a 2D array
    if isinstance(arr[0], list):
        for row in arr:
            print(" ".join(map(str, row)))
    else:
        # Handle 1D array
        print(" ".join(map(str, arr)))
    print()

def find_average(arr, subs, students):
    avg_marks = [0] * subs
    count = [0] * subs
    for entry in arr:
        sub = entry[1]
        mark = entry[2]
        avg_marks[sub] += mark
        count[sub] += 1
    for i in range(subs):
        if count[i] != 0:
            avg_marks[i] //= count[i]
    return avg_marks

def highest_average(arr, subs, students):
    avg_marks = find_average(arr, subs, students)
    max_marks = 0
    sub_no = -1
    for i in range(len(avg_marks)):
        if avg_marks[i] > max_marks:
            max_marks = avg_marks[i]
            sub_no = i
    return max_marks, sub_no

def convert_to_compact(nums):
    efficient_arr = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] != 0:
                efficient_arr.append([i, j, nums[i][j]])
    return efficient_arr

def highest_mark_students(nums):
    highest_mark = []
    subjects = max([entry[1] for entry in nums]) + 1
    students = len(nums)
    for i in range(subjects):
        max_marks = 0
        index = -1
        for j in range(students):
            if nums[j][1] == i:
                if nums[j][2] > max_marks:
                    max_marks = nums[j][2]
                    index = nums[j][0]
        highest_mark.append([index + 1, max_marks] if index != -1 else [0, 0])
    return highest_mark

def main():
    nums = [
        [0, 0, 10, 0],
        [21, 0, 17, 0],
        [0, 12, 0, 0],
        [0, 0, 7, 0],
        [0, 0, 25, 3],
        [12, 0, 0, 1],
        [0, 0, 56, 0]
    ]
    students = len(nums)
    subjects = len(nums[0])
    efficient_arr = convert_to_compact(nums)
    print("Efficient Array:")
    print_array(efficient_arr)
    print("Avg marks:")
    avg_marks = find_average(efficient_arr, subjects, students)
    print_array(avg_marks)
    highest = highest_average(efficient_arr, subjects, students)
    print(f"Maximum average: {highest[0]} Subject: {highest[1]}")
    print("Student Index and Highest Marks per subject:")
    highest_mark = highest_mark_students(efficient_arr)
    print_array(highest_mark)

if __name__ == "__main__":
    main()
