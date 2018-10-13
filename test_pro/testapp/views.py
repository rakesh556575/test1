from django.shortcuts import render,render_to_response
from django.http import HttpResponse,StreamingHttpResponse
from testapp.models import Testcases
from . import forms
import subprocess
import time
from django.template.loader import render_to_string
import os
def index(request):
    test_list = Testcases.objects.all()
    my_dict = {"test_list": test_list}
    msg="</h1>Welcome to test app</h1>"
    return render(request,"index.html",context=my_dict)

def  ms1(request):
    test_list=Testcases.objects.all()
    print(test_list)
    my_dict={"test_list":test_list}
    return render(request, "MS1.html", context=my_dict)


def  ms2(request):
    test_list=Testcases.objects.all()
    print(test_list)
    my_dict={"test_list":test_list}
    return render(request, "MS2.html", context=my_dict)

def  ms3(request):
    test_list=Testcases.objects.all()
    print(test_list)
    my_dict={"test_list":test_list}
    return render(request, "MS3.html", context=my_dict)



def  ms4(request):
    test_list=Testcases.objects.all()
    print(test_list)
    my_dict={"test_list":test_list}
    return render(request, "MS4.html", context=my_dict)


def testregisterview(request):
    if request.method=="GET":
        form=forms.TestcaseRegisteration()
        return render(request, "register.html", {"form": form})

    if request.method=="POST":
        form=forms.TestcaseRegisteration(request.POST)
        if form.is_valid():
            print("form validation is sucessfull ")
            print("Testid:{}".format(form.cleaned_data["testid"]))
        else:
            print("form is invalid")






from subprocess import Popen, PIPE
command="ping www.google.com".split(" ")
#commad="print {}".format(testid)
def run_command(command,testid):
#    process = subprocess.Popen(command, stdout=subprocess.PIPE)
#    while True:
#        output = process.stdout.readline()
#        if  not output :
#            break
#        if output:
#            yield "<div>%s</div>\n" % output
#            yield " " * 1024  # Encourage browser to render incrementally
#            time.sleep(1)
    yield "<html><body>\n"
    yield "<h1>Test case C{} Running</h1><br/>".format(testid)
    for x in range(0, int(testid)+10):

        yield '{} <br /> {}'.format(x, ' ' * 1024)
        time.sleep(1)


    yield "<h1>Test case C{} Execution done</h1><br/>".format(testid)
    yield "</body></html>\n"


def run(request):
    if request.method == 'GET':
        testid=request.GET.get('testid')
        command = "ping www.google.com".split(" ")
        resp = StreamingHttpResponse(run_command(command,testid))
    return resp


