{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Member: #클래스 선언\n",
    "    def __init__(self, num, name, phone): #생성자 정의(객체초기화) self=this(현재객체의 참조)\n",
    "        self.num = num\n",
    "        self.name = name\n",
    "        self.phone = phone\n",
    "    def printMem(self): #개발자 정의, \n",
    "        print(self.num,self.name,self.phone)\n",
    "    def __str__(self): #자바의 toString(내장함수)\n",
    "        return f\"{self.num} {self.name} {self.phone}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11 홍범도 010-1234-5678\n",
      "11 Ward 010-1234-5678\n"
     ]
    }
   ],
   "source": [
    "m = Member(11,'홍범도','010-1234-5678')\n",
    "m.printMem() # m객체의 참조로 가서 해당 객체 출력\n",
    "m.name = 'Ward' #객체정보 추가 후,\n",
    "print(m) #객체의 정보를 문자열로 출력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)C\n",
      "회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)c\n",
      "회원번호,이름,전화:1,meg,426\n",
      "회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)r\n",
      "1 meg 426\n",
      "회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)u\n",
      "새 전화번호:57345\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'num' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-063194aef0b0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     16\u001b[0m         \u001b[0mnewPhone\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"새 전화번호:\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mm\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 18\u001b[1;33m             \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnum\u001b[0m\u001b[1;33m==\u001b[0m\u001b[0mm\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnum\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     19\u001b[0m                 \u001b[0mm\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mphone\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnewPhone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m                 \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'num' is not defined"
     ]
    }
   ],
   "source": [
    "list = []\n",
    "mem = []\n",
    "while(True):\n",
    "    inputa = input(\"회원정보 추가(c), 리스트보기(r), 수정(u), 삭제(d), 검색(s), 종료(x)\")\n",
    "    \n",
    "    if(inputa=='c'):\n",
    "            insert = input(\"회원번호,이름,전화:\")\n",
    "            mem = insert.split(',')\n",
    "            list.append(Member(int(mem[0]),mem[1],mem[2]))\n",
    "                        \n",
    "    elif(inputa=='r'):\n",
    "        for m in list:\n",
    "            print(m)\n",
    "    \n",
    "    elif(inputa=='u'):\n",
    "        newPhone = int(input(\"새 전화번호:\"))\n",
    "        for m in list:\n",
    "            if(num==m.num):\n",
    "                m.phone = newPhone\n",
    "                break\n",
    "                        \n",
    "    elif(inputa=='d'):\n",
    "        delNum = input(\"삭제할 회원번호:\")\n",
    "        for m in list:\n",
    "            if(delNum==m.num):\n",
    "                list.remove(m)\n",
    "                break\n",
    "    \n",
    "    elif(inputa=='s'):\n",
    "        searchNum = int(input(\"검색할 회원번호:\"))\n",
    "        for m in list:\n",
    "            if(searchNum==m.num):\n",
    "                num = searchNum\n",
    "                print(m)\n",
    "                break\n",
    "                        \n",
    "    elif(inputa=='x'):\n",
    "        break\n",
    "        \n",
    "print('프로그램종료...')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
