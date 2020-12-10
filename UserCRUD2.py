info = [] #dict 선언
mem = [] #list 선언

def printMem(dic):
    print(dic['num'],dic['name'],dic['phone'])
    
while(True):
    inputa = input("회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)")
    
    if(inputa=='c'):
            insert = input("회원번호,이름,전화:")
            mem = insert.split(',')
            num,name,phone = mem
            info.append({'num':int(num),'name':name,'phone':phone})
                        
    elif(inputa=='r'):
        for m in info:
            print(m)
    
    elif(inputa=='u'):
        newPhone = int(input("새 전화번호:"))
        for m in info:
            if(num==m['num']):
                m['phone'] = newPhone
                break
                        
    elif(inputa=='d'):
        delNum = input("삭제할 회원번호:")
        for m in info:
            if(delNum==m['num']):
                info.remove(m)
                break
    
    elif(inputa=='s'):
        searchNum = int(input("검색할 회원번호:"))
        for m in info:
            if(searchNum==m['num']):
                num = searchNum
                print(m)
                break
                        
    elif(inputa=='x'):
        break
        
print('프로그램종료...')
