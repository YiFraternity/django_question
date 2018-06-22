# import MySQLdb
import random

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
from . import calculation
from . import Dfile
from . import config

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
    if request.method == "POST":
        questions = Question.objects.all()
    else:
        questions = Question.objects.all()
    return render(request,'question/default.html',locals())

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
                if Quest.img_location:
                    img = Quest.img_location
                    return render(request,'question/ask-question-img.html',locals())
                else:
                    return render(request,'question/ask-question.html',locals())
        else:
            return redirect('/question/default/')
    else:
        return redirect('/question/login/')

def get_quest(request,question):
    request.session['quest_id'] = question
    Quest = Question.objects.get(id=question)
    if Quest.img_location:
        img = Quest.img_location
        return render(request,'question/each-quest-img.html',locals())
    else:
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
                if Quest.img_location:
                    img = Quest.img_location
                    return render(request,'question/answer-img.html',locals())
                else:
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
        quests = Question.objects.filter(question_type=q)
        return render(request,'question/search-result.html',locals())
    else:
        message = '查找结果为空'
        return HttpResponse(message)

def practice_ask_answer(request):
    if request.session.get('is_login'):
        if request.session.get('quest_id'):
            quest_id = request.session['quest_id']
            quest_type = Question.objects.get(id=quest_id).question_type
            print(quest_type)
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
                return redirect('/question/practice-show-answer/')
            else:
                Quest=Question.objects.get(id=quest_id)
                if Quest.img_location:
                    img = Quest.img_location
                    return render(request,'question/practice-ask-question-img.html',locals())
                else:
                    return render(request,'question/practice-ask-question.html',locals())
        else:
            return redirect('/question/practice/')
    else:
        return redirect('/question/login/')

def practice_quest(request,question):
    request.session['quest_id'] = question
    print(request.session['quest_id'])
    Quest = Question.objects.get(id=question)
    if Quest.img_location:
        img = Quest.img_location
        return render(request,'question/practice-each-quest-img.html',locals())
    else:
        return render(request,'question/practice-each-quest.html',locals())

def practice(request):
    if request.session.get('is_login'):
        quest_type = 61
        Quest = Question.objects.filter(question_type=quest_type)
        return render(request,'question/practice.html',locals())
    else:
        return redirect('/question/login/')

def practice_show_answer(request):
    if request.session.get('is_login'):
        if request.session.get('quest_id'):
            if request.session.get('version'):
                uname = request.session.get('username')
                questid = request.session.get('quest_id')
                Quest = Question.objects.get(id=questid)
                myUser = MyUser.objects.get(username=uname)
                vers = request.session.get('version')
                Answer = Entry.objects.filter(question=questid).filter(username=uname).get(version=vers)
                request.session['userAnswer'] = Answer.user_answer
                if config.const.DEBUG:
                    answer_keyword = Quest.answer_keyword.split(",")
                    unansweredKeyword = calculation.get_userAnswer_UnansweredKeyword(Answer.user_answer,answer_keyword)
                    answeredKeyword = calculation.get_userAnswer_keyword(Answer.user_answer,answer_keyword)
                    correct_rate = calculation.get_userAnswer_keyword_percent(unansweredKeyword,answer_keyword)
                    unansweredKeywordStr = ",".join(unansweredKeyword)
                    answeredKeywordStr = ",".join(answeredKeyword)
                    correct_rate = "%.2f" % correct_rate
                    if Quest.img_location:
                        img=Quest.img_location
                        return render(request,'question/practice-answer-debug-img.html',locals())
                    else:
                        return render(request,'question/practice-answer-debug.html',locals())
                else:
                    if Quest.img_location:
                        img = Quest.img_location
                        return render(request,'question/practice-answer-img.html',locals())
                    else:
                        return render(request,'question/practice-answer.html',locals())
            else:
                return redirect('/question/ask-question/')
        else:
            return redirect('/question/default')
    else:
        return redirect('/question/login/')

"""
有两种问题策略：
    第一种(根据学生作答情况问题进行作答)
        61 -> 51|41|32 -> 31 -> 11|21
        按关键词寻找学生的答题要求，依据关键词踩点情况，推荐下一道题。
        1、首先提问61(实验题)，统计学生没有达到的关键词，标记为集合A
        2、搜索51(色素),41(因素),32(生物物质在过程中的作用)的所有题目，统计题目所对应的关键词在集合A中的数量
        3、选取覆盖集合A数量最高的题目为下一题目
        4、若有多个题目覆盖数目一样，随机选择一个题目为下一题
        5、若学生仍旧打错、选择31(生物过程的原料和产物)为下一题，同样统计关键词的覆盖情况
        6、若学生完全答对，上升一个题目难度类型
    第二种(随机抽取一道题目，进行作答)
"""
def practice_continue(request):
    if request.session.get('is_login'):
        if request.session.get('quest_id'):
            if config.const.STRATEGY ==1:
                difficulty = Dfile.read_file(config.const.DIFFICULTY_FILE)
                quest_id = request.session['quest_id']
                quest_type = Question.objects.get(id=quest_id).question_type
                user_answer = request.session['userAnswer']
                answer_keyword = Question.objects.get(id=quest_id).answer_keyword.split(',')
                unansweredKeyword = calculation.get_userAnswer_UnansweredKeyword(user_answer,answer_keyword)
                print(unansweredKeyword)
                # 如果正确率大于一个常量(const.CORRECT_RATE)，题目上升一个难度
                # 反之，如果正确率不足常量(const.CORRECT_RATE)，题目下降一个难度
                correct_rate = calculation.get_userAnswer_keyword_percent(unansweredKeyword,answer_keyword)
                print(correct_rate)
                i=0   # 难度系数最高
                for diff in difficulty:
                    if diff.find(str(quest_type)) != -1:
                        break
                    else:
                        i=i+1
                        continue
                    pass
                if correct_rate<config.const.CORRECT_RATE and i<len(difficulty)-1:
                    difficult = difficulty[i+1]
                    pass
                elif correct_rate>=config.const.CORRECT_RATE and i>0:
                    difficult = difficulty[i-1]
                    pass
                else:
                    difficult = difficulty[i]
                    pass
                question_types = difficult.split(",")
                all_answer_keywords = {}
                for question_type in question_types:
                    Quests = Question.objects.filter(question_type=question_type)
                    for Quest in Quests:
                        eachquestion_keyword=Quest.answer_keyword.split(',')
                        # 用户没作答的关键词和问题的关键词求交集
                        intersection = [element for element in eachquestion_keyword if element in unansweredKeyword]
                        all_answer_keywords[Quest.id]=len(intersection)
                        pass
                # 关键词匹配度进行比较,并得到将要出题的类型
                next_question = calculation.get_next_question_id(all_answer_keywords)
                request.session['quest_id'] = next_question
                Quest = Question.objects.get(id=next_question)
                if Quest.img_location:
                    img = Quest.img_location
                    return render(request,'question/practice-each-quest-img.html',locals())
                else:
                    return render(request,'question/practice-each-quest.html',locals())
            else:
                last = Question.objects.count() -1
                index = random.randint(0,last)
                Quest = Question.objects.all()[index]
                request.session['quest_id']=Quest.id
                if Quest.img_location:
                    img = Quest.img_location
                    return render(request,'question/practice-each-quest-img.html',locals())
                else:
                    return render(request,'question/practice-each-quest.html',locals())
        else:
            return redirect('/question/practice/')
    else:
        return redirect('/question/login/')
    pass













