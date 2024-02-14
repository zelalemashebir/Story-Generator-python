import random
import time

OPERATORS=["+","-","/","*"]
MIN_OPERAND= 3
MAX_operand= 12
Total_PROBLEMS=10


def generate_problem():
    left =random.randint(MIN_OPERAND,MAX_operand)
    right = random.randint(MIN_OPERAND,MAX_operand)
    operator=random.choice(OPERATORS)


    expr =str(left) + ""+  operator + "" + str(right)

    answer=eval(expr)

    return  expr,answer

wrong =0
input("press enter start")
print("--------------")

start_time =time.time()

for i in range(Total_PROBLEMS):
    expr,answer  = generate_problem()
    while True:
       guess=  input ("Problem #" + str(i + 1) + ":" + expr + "=")
       if guess == str(answer):  
           break
       wrong +=1

end_time =time.time()
total_time  = end_time -start_time    

print("---------------")   


print("nice work you finishe" ,total_time ,"seconds" )   
 