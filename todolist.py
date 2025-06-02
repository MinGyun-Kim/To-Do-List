import os

todolist_file = []
def main_menu():
    print("         Welcome to To Do List")
    print(" " * 8, "-"*20)
    print("""         |    1. 등록하기   |
         |    2. 삭제하기   |
         |    3. 수정하기   |
         |    4. 목록보기   |
         |    5. 끝내기     |""")
    print(" " * 8, "-" * 20)
    select = input("원하는 메뉴를 입력해 주세요 :")
    return select

def registration():
    workname = ""
    while workname != "5.txt":
        workname = input("할 일을 쓰세요 : ") + ".txt"    #할 일을 사용자에게 입력을 받고 그뒤에 .txt를 붙여서 텍스트 파일로 변환한다.
        f = open(workname, "w")                           # workname을 쓰기버전으로 열어준다
        f.close()                                         #쓰기가 완료가 되면 닫아준다.
        todolist_file.append(workname)                    #todolist_file의 리스트에 workname의 파일을 리스트 형식으로 추가 시켜준다.
        
    todolist_file.remove("5.txt")
    
    # 추가시킨 리스트의 항목을 확인하는 코드이다.
    for j in range(len(todolist_file)):     
                print(f"{j+1}번 {todolist_file[j]}")
    return todolist_file    
    
def remv():
    for i in range(len(todolist_file)):                #todolist_file의 인덱스 만큼 반복을 한다.
        print(f"{i + 1}번 {todolist_file[i]}")         #인덱스에 +1 번이라고 하고 todolist_file[i번인덱스]를 출력해준다.
    delete = int(input("삭제할 번호를 입력하세요 : "))  # 사용자에게 삭제할 번호를 받는다.

    if 1 <= delete <= len(todolist_file):               # delete가 1과 todolist_file의 인덱스 길이안에 있는 유효한 수 인지 확인한다. 
        del todolist_file[delete - 1]                   # 사용자가 지정한 번호의 파일을 삭제하기 위해서 delete에서 -1을 해준 값을 삭제한다
                                                            # 그 이유는 인덱스 번호는 0부터 시작하기 때문에 사용자가 작성한 번호와 -1만큼 차이가 나기 때문이다.
        print("삭제되었습니다.")
    else:
        print("잘못된 번호입니다.")                      # 만약 유효하지 않는 번호를 누르면 잘못된 번호라고 출력해준다.
               
        # 삭제시킨 리스트의 항목을 확인하는 코드이다.
    for j in range(len(todolist_file)):
        print(f"{j+1}번 {todolist_file[j]}")
    return todolist_file
                        
def retouch():
    # 각 항목을 보여주고 수정할 번호를 입력받는 코드이다.
    for i in range(len(todolist_file)):
        print(f"{i + 1}번 {todolist_file[i]}")
    modify = int(input("수정할 번호를 입력하세요 : "))
        #위에 삭제 시키는것과 같이 modify의 항목이 유효한지 확인한다.
    if 1 <= modify <= len(todolist_file):
        del todolist_file[modify - 1]
        #그리고 modifyname으로 수정할 내용을 받고 insert를 이용해서 사용자가 수정할 번호를 입력한 곧에 추가를 해준다.
    modifyname = input("수정할 내용을 작성하세요 : ") + ".txt"
    f = open(modifyname, "w")
    f.close
    todolist_file.insert(modify - 1, modifyname)
        
        # 수정 시킨 리스트의 항목을 확인하는 코드이다.
    for j in range(len(todolist_file)):
        print(f"{j+1}번 {todolist_file[j]}")
        # To Do List를 종료하는 조건이다.
    return todolist_file
def read():
    for j in range(len(todolist_file)):     
                print(f"{j+1}번 {todolist_file[j]}")

while True:
   
    work = main_menu()
    
    if work == "1":
        registration()
        os.system('cls')                    
    elif work == "2":
        remv()
        os.system('cls')                
    elif work == "3":
       retouch()
       os.system('cls')
    elif work == "4":
        read()
    elif work == "5":
        print("To Do List를 종료합니다.")
        break
        # 만약 위의 항목이 아닌 다른 번호를 입력했을경우 번호 입력을 다시 받는다.
    else:
        print("번호를 다시 확인해주세요.")
    
