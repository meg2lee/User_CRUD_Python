#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list = {} #dict 선언
mem = [] #list 선언
while(True):
    inputa = input("회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)")
    
    if(inputa=='c'):
            insert = input("회원번호,이름,전화:")
            mem = insert.split(',')
            num,name,phone = mem
            list = {'num':num,'name':name,'phone':phone}
                        
    elif(inputa=='r'):
        for k,v in list.items():
            print(k,v)
    
    elif(inputa=='u'):
        newPhone = int(input("새 전화번호:"))
        for m in list.items():
            if(m[0]==num):
                m[2] = newPhone
                break
                        
    elif(inputa=='d'):
        delNum = input("삭제할 회원번호:")
        for m in list.items():
            if(delNum==m.num):
                list.remove(m)
                break
    
    elif(inputa=='s'):
        searchNum = int(input("검색할 회원번호:"))
        for m in list.items():
            if(searchNum==m.num):
                num = searchNum
                print(m)
                break
                        
    elif(inputa=='x'):
        break
        
print('프로그램종료...')

