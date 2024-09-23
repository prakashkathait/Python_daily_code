
def count_substring(string, sub_string):
    cnt = 0
    s=len(sub_string)
    for i in range(len(string)):
        x=string[i:i+s]
        if x==sub_string:
            cnt += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)