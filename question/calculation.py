import random

from . import config
from . import Dfile

"""
计算匹配度
"""
def get_userAnswer_keyword_percent(unansweredKeyword,answer_keyword):
    m = len(unansweredKeyword)
    n = len(answer_keyword)
    error_rate = '%.2f' % (m/n)
    correct_rate =1.00 - float(error_rate)
    return correct_rate

def get_userAnswer_keyword(userAnswer,answer_keyword):
    answeredKeyword = []
    synonym_lst  = Dfile.read_file(file=config.const.SYNONYMS_DICT)
    for keyword in answer_keyword:
        synonym = str_exist_lst(keyword,synonym_lst)
        if synonym:
            keyword_synonym_lsts = synonym.split(",")
            if lstElement_exist_str(keyword_synonym_lsts,userAnswer):
                element = lstElement_exist_str(keyword_synonym_lsts,userAnswer)
                answeredKeyword.append(element)
                continue
            else:
                pass
        else:
            if keyword in userAnswer:
                answeredKeyword.append(keyword)
                pass
            pass
    return answeredKeyword

"""
# 获取用户没有回答的关键词
"""
def get_userAnswer_UnansweredKeyword(userAnswer,answer_keyword):
    unansweredKeyword = []
    synonym_lst  = Dfile.read_file(file=config.const.SYNONYMS_DICT)
    for keyword in answer_keyword:
        synonym = str_exist_lst(keyword,synonym_lst)
        if synonym:
            keyword_synonym_lsts = synonym.split(",")
            if lstElement_exist_str(keyword_synonym_lsts,userAnswer):
                continue
            else:
                unansweredKeyword.append(keyword)
                pass
        else:
            if keyword not in userAnswer:
                unansweredKeyword.append(keyword)
                pass
            pass
    return unansweredKeyword

def str_exist_lst(str,lsts):
    result = ""
    for lst in lsts:
        if str in lst:
            result = lst
            break
        pass
    return result

def lstElement_exist_str(list,str):
    result=""
    for lst in list:
        if lst in str:
            result = lst
            print(result)
            break
    return result

# 从一堆字典中找到自己想要的
# 规则：根据value进行逆排序，找到最大的几个，从最大的几个中随机挑选一个
def get_next_question_id(dictionary):
    #  对字典进行排序
    sorts = sorted(dictionary.items(),key=(lambda item:item[1]),reverse=True)
    for i in range(0,len(sorts),1):
        if sorts[i][1] != sorts[0][1]:
            break
        pass
    if sorts[len(sorts)-1][1] == sorts[0][1]:
        i=i+1
        pass
    lists=sorts[0:i]
    print(lists)
    print(len(lists))
    upperline = len(lists)-1
    rand = random.randint(0,upperline)
    print(rand)
    return lists[rand][0]




