from django.http import HttpResponse
from django.shortcuts import render
import time
import requests


import requests
url="https://ide.geeksforgeeks.org/main.php"
url2="https://ide.geeksforgeeks.org/submissionResult.php"

def home(request):
    return render(request,'home.html')
def code_page(request):
    """language:
    C
    Java
    Cpp
    Csharp
    Perl
    Php
    Python
    Python3
    Scala
    """
    lang=str(request.POST['language'])
    code1=request.POST['codetext']
    inp1=request.POST['codeinp']
    code="""{}""".format(code1)
    print(code)
    print(lang)
    """code=
    class main{
    public static void main(String args[])
    {
        System.out.print("Manoj");
        for(int i=0;i<10;i++)
        {
            System.out.println(i);
        }
    }
    }
    """
    inp=inp1
    print(inp)
    data={
    'lang':lang,
    'code':code,
    'input':inp,
    'save':False
    }

    r=requests.post(url,data=data)

    r=r.json()
    print(r)
    if(r['status']=='ERROR'):
        op=r['message']
    else:
        data2={
            'sid':r['sid'],
            'requestType':'fetchResults'
        }
        while(True):
            r2=requests.post(url2,data=data2)
            r2=r2.json()
            print(r2)
            if('cmpError' in r2.keys()):
                op=r2['cmpError']
                break
            if('rntError' in r2.keys()):
                op=r2['rntError']
                break

            if(r2['status']=='SUCCESS'):
                print("\n",r2['status'])
                op=r2['output']
                break
        print(op)
    return render(request,'home.html',{"op":op})