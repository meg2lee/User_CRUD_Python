#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Member: #클래스 선언
    def __init__(self, num, name, phone): #생성자 정의(객체초기화) self=this(현재객체의 참조)
        self.num = num
        self.name = name
        self.phone = phone
    def printMem(self): #개발자 정의, 
        print(self.num,self.name,self.phone)
    def __str__(self): #자바의 toString(내장함수)
        return f"{self.num} {self.name} {self.phone}"


# In[3]:


m = Member(11,'홍범도','010-1234-5678')
m.printMem() # m객체의 참조로 가서 해당 객체 출력
m.name = 'Ward' #객체정보 추가 후,
print(m) #객체의 정보를 문자열로 출력


# In[4]:


list = []
mem = []
while(True):
    inputa = input("회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)")
    
    if(inputa=='c'):
            insert = input("회원번호,이름,전화:")
            mem = insert.split(',')
            list.append(Member(int(mem[0]),mem[1],mem[2]))
                        
    elif(inputa=='r'):
        for m in list:
            print(m)
    
    elif(inputa=='u'):
        newPhone = int(input("새 전화번호:"))
        for m in list:
            if(num==m.num):
                m.phone = newPhone
                break
                        
    elif(inputa=='d'):
        delNum = int(input("삭제할 회원번호:"))
        for m in list:
            if(delNum==m.num):
                list.remove(m)
                break
    
    elif(inputa=='s'):
        searchNum = int(input("검색할 회원번호:"))
        for m in list:
            if(searchNum==m.num):
                num = searchNum
                print(m)
                break
                        
    elif(inputa=='x'):
        break
        
print('프로그램종료...')

