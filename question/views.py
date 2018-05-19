# import MySQLdb
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.shortcuts import redirect

from .models import MyUser
from .forms import LoginForm
from .forms import RegisterForm
from .models import Question
from .models import Entry
from .answer import AskQuestion


def login(request):
    #  1.判断必填项用户名和密码是否为空，如果为空，提示"用户名和密码为必填项”
    #  2.判断用户名和密码是否正确，如果错位，提示"用户名或密码"的错误信息
    #  3.登录成功后，进入主页(index.html)
    if request.method == 'POST':
        myUser = request.POST.get('username')
        passwd = request.POST.get('password')
        print("用户名："+myUser+" 密码："+passwd)
        try:
            passwd_db = MyUser.objects.get(username=myUser).password
        except:
            messages.add_message(request,messages.WARNING,'找不到用户')
            return render(request,'user/login.html',{'login_info_list':"请使用正确的账号密码登录"})
        if passwd_db == passwd:
            request.session['is_login'] = 'True'
            request.session['username'] = myUser
            print(request.session['username'])
            request.session.set_expiry(600)
            return redirect('/question/index/')
        else:
            messages.add_message(request,messages.WARNING,'密码错误')
            return render(request,'user/login.html',{'login_info_list':"请使用正确的账号密码登录"})
    if request.method == 'GET':
        form = LoginForm()
        return render(request,"user/login.html",locals())

def register(request):
    if request.method == "POST":
        register = RegisterForm(request.POST)
        if register.is_valid():
            #获取表单信息
            user = register.cleaned_data['username']
            #try:
            filterResult = MyUser.objects.filter(username = user)
            if len(filterResult)>0:
                return render(request,'user/register.html',{"errors":"用户名已存在"})
            else:
                password1 = register.cleaned_data['password1']
                password2 = register.cleaned_data['password2']
                email = register.cleaned_data['email']
                sex = register.cleaned_data['sex']
                grade = register.cleaned_data['grade']
                errors = []
                if (password2 != password1):
                    errors.append("两次输入的密码不一致!")
                    return render(request,'user/register.html',{'errors':errors})
                    #return HttpResponse('两次输入的密码不一致!,请重新输入密码')
                password = password2
                #将表单写入数据库
                myUser = MyUser()
                myUser.username = user
                myUser.password = password
                myUser.email = email
                myUser.sex = sex
                myUser.gender = grade
                myUser.save()
                #返回注册成功页面
                return redirect("/question/index/")
    else:
        register = RegisterForm()
        return render(request,'user/register.html',locals())

def index(request):
    if request.session.get('is_login'):
        print(request.session.get('username'))
        return render(request, 'question/index.html', {})
    else:
        return redirect('/question/login/')

def default(request):
    questions = Question.objects.all()
    return render_to_response('question/default.html',locals())

def question(request):
    questions = Question.objects.all()
    return render_to_response('question/question.html',locals())

def type(request):
    questions = Question.objects.all()
    return render_to_response('question/type.html',locals())

def ask_question(request):
    if request.session.get('is_login'):
        if request.session.get('quest_id'):
            if request.method == "POST":
                askQuestion = AskQuestion(request.POST)
                userAnswer = request.POST.get('user_answer')
                print(userAnswer)
                myUser = request.session.get('username')
                questId = request.session.get('quest_id')
                askQuestion.user_answer=userAnswer
                filterResult = Entry.objects.filter(username=myUser).filter(question=questId)
                number = filterResult.__len__()
                print(number)
                value = number+1
                request.session['version'] = value
                User = MyUser.objects.get(username=myUser)
                Quest = Question.objects.get(id = questId)
                create = Entry.objects.create(
                    question=Quest,
                    username=User,
                    version=value,
                    user_answer=userAnswer,
                )
                print(type(create),create)
                return redirect('/question/show-answer/')
            else:
                questId = request.session.get('quest_id')
                print(questId)
                Quest=Question.objects.get(id=questId)
                return render(request,'question/ask-question.html',locals())
        else:
            return redirect('/question/default/')
    else:
        return redirect('/question/login/')

def get_quest(request,question):
    request.session['quest_id'] = question
    Quest = Question.objects.get(id=question)
    return render(request,'question/each-quest.html',locals())

def type_quests(request,qType):
    Quests = Question.objects.filter(question_type=qType)
    return render(request,'question/question-type.html',locals())

def show_answer(request):
    if request.session.get('is_login'):
        if request.session.get('quest_id'):
            if request.session.get('version'):
                uname = request.session.get('username')
                questid = request.session.get('quest_id')
                Quest = Question.objects.get(id=questid)
                myUser = MyUser.objects.get(username=uname)
                vers = request.session.get('version')
                Answer = Entry.objects.filter(question=questid).filter(username=uname).get(version=vers)
                return render(request,'question/answer.html',locals())
            else:
                return redirect('/question/ask-question/')
        else:
            return redirect('/question/default')
    else:
        return redirect('/question/login/')

def search_result(request):
    pass

def search(request):
    if 'search' in request.GET and request.GET['search']:
        q = request.GET.get['search']
        quests = Question.objects.filter(quesion_type=q)
        return render(request,'question/search-result.html',locals())
    else:
        message = '查找结果为空'
        return HttpResponse(message)

