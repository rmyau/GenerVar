import random as rand
from sympy import Rational
def task13(var):
    if var%2==1:
        taskList = ["Случайная величина X распределена нормально с математическим ожиданием, равным ",
                    ". Вероятность попадания X в интервал (",
                    ") равна ",
                    ". Чему равна вероятность попадания X в интервал (",
                    ")? Записать для случайной величины X формулу плотности вероятности f(x)."]
        listP=[0.9973, 0.8944]
        xsigm = [2,3]
        a=rand.randint(2,5)
        sigm=rand.randint(2,10)
        isP = rand.randint(0,1)

        b=xsigm[isP]*sigm+a
        alf = 2*a-b
        b2=b+rand.randint(15,25)
        alf2 = b2-rand.randint(5,10)

        s=taskList[0]+str(a)+taskList[1]+str(alf)+";"+str(b)+taskList[2]
        s+=str(listP[isP])+taskList[3]+str(alf2)+";"+str(b2)+taskList[4]
        print(s)
        
        
        ans = "P("+str(alf2)+"<x<"+str(b2)+") = \u03A6("+str(round((b2-a)/sigm,2))
        ans+=")-\u03A6("+str(round((alf2-a)/sigm,2))+")"
        ans+="\nf(x)=1/("+str(sigm)+"sqrt(2\u03C0))*e^((-x-"+str(a)+")^2/"+str(2*sigm*sigm)+")"
        ans+="\n(a="+str(a)+", \u03C3="+str(sigm)+")"
        print(ans)
    else:
        taskList = ["Число вагонов, прибывающих в течение суток на грузовой пункт станции, является случайной величиной, распределенной по нормальному закону с параметрами: a=",                   
                    ",\u03C3=",
                    ". Определить вероятность прибытия на грузовой пункт от ",
                    " до ",
                    " вагонов в сутки."]
        sigm=rand.randint(5,15)
        a=rand.randint(15,40)
        b=rand.randint(10,5*sigm+a)
        alf=rand.randint(-10,b-5)
        s=taskList[0]+str(a)+taskList[1]+str(sigm)+taskList[2]
        s+=str(alf)+taskList[3]+str(b)+taskList[4]
        print(s)

        ans="P("+str(alf)+"<x<"+str(b)+") = \u03A6("+str(round((b-a)/sigm,2))
        ans+=")-\u03A6("+str(round((alf-a)/sigm,2))+")"
        print(ans)
        
for i in range(1):
    task13(1)
    task13(0)


        
