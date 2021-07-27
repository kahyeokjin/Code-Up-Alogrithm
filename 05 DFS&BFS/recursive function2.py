def recursive(i):
    if i == 100:
        return
    print(i,"번째",i+1,"번째 재귀 함수를 호출합니다.")
    recursive(i+1)
    print(i,"번째 재귀 함수를 종료합니다.")

recursive(1)
    
