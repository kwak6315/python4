#정올 language_coder  함수2-자가진단2

def date(arr):
    #월
    month = list(range(1,13))   #월

    #일
    day = list(range(1,32))    #일
    #월과 일이 맞는지 확인
    if arr[0] in month and arr[1] in day :
        if arr[0]  == 2 and (arr[1] == 30 or arr[1] == 31):
            print("BAD!")
        elif (arr[0] == 4 or arr[0] == 6 or arr[0]== 9 or arr[0] == 11) and (arr[1] == 31):
            print("BAD!")
        else:
            print("OK!")

    else:
        print("BAD!")







user = list(map(int, input("날짜를 입력해주세요:  ").split())) # user =  [2,30]print(user)

date(user)