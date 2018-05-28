#-*- coding:utf-8 -*-
import json

"""
根据固定长度来进行将文件编码
"""
class ProcessFile:

    def __init(self):
        pass

    """
    将问题和答案格式化
    """
    def format_qa(self,content):
        if content.startswith('问题') or content.startswith('答案'):
            content=content[3:]
        content=content.replace("\n","")
        return content

    """
    获得所有的问题和答案
    """
    def get_txt_data(self,file):
        """
        获取txt数据
        """
        f=open(file)
        content=[]
        line=f.readline() #调用文件的readline()方法
        while line:
            #print(line)
            line=self.format_qa(line)
            content.append(line)
            line=f.readline()
        f.close()
        return content

    """
    将问题和答案进行匹配
    """
    # index:两个问题之间的行数差，如果非固定值，需手动调整下
    def trans_qa_to_pair(self,data,index):
        lists=[
            data[i:i+index]
            for i in range(0,len(data),index)
        ]
        contents=[]
        for lst in lists:
            str0=lst[0]
            str1="".join(lst[1:])
            print(str1)
            content=[]
            content.append(str0)
            content.append(str1)
            contents.append(content)
        print(len(contents))
        return contents

    def write_json_data(self,content,question_type,pk_value,keyword=""):
        data={
            "model":"question.Question",
            "pk":pk_value,
            "fields":{
                "quest":content[0],
                "answer":content[1],
                "question_type":question_type,
                "answer_keyword":keyword,
            }
        } #model应该是question吧，不对再试
        result=json.dumps(data,ensure_ascii=False)
        result.encode('utf-8')
        #print(result)
        return result

    def write_json_file(self,file,data):
        f= open(file,"w")
        f.write(data)
        f.close()
        pass

    """
    获取关键词
    算法流程：
    1、从文件中按行读取关键词
    2、判断是否有问题的关键词
    3、若有问题的关键词，只读取答案的关键词
    4、答案的关键词有几行
    5、将每道题答案的关键词添加到list
    6、为每道题的答案进行组合
    key_lines : 答案关键词有几行
    index : 一道题目问题及答案的关键词有几行
    is_quest : 是否有问题的关键词
    """
    def get_keyword(self, file, key_lines=1, index=1, is_question=True, delimiter=" "):
        contents = []
        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.replace("\n", "")
                contents.append(line)
                pass
            pass
        if is_question:
            lists = [
                contents[i+1:i + index]
                for i in range(0, len(contents),index)
            ]
            pass
        else:
            lists = [
                contents[i:i + index]
                for i in range(0, len(contents), index)
            ]
        keywords = []
        for list in lists:
            content = []
            for lst in list:
                content.extend(lst.split(sep=delimiter))
                pass
            key = ",".join(content)
            keywords.append(key)
            pass
        print(keywords)
        return keywords


    """
    input_file:输入文件
    output_file:输出文件
    question_type:问题类型（1-6,分别代表原来，产物，原料和产物，因素，光和色素，实验）
    """
    def topfuction(self,input_file,output_file,question_type,index,keywords=[]):
        results=[]
        data=self.get_txt_data(input_file)
        contents=self.trans_qa_to_pair(data,index)
        num=1
        key_num=0
        for content in contents:
            pk_value=""
            if num<10:
                pk_value="00"+str(num)
            elif (num<100) and (num>=10):
                pk_value="0"+str(num)
            else:
                pk_value=str(num)
            pk_value="0"+(str(question_type))+(pk_value)
            print(pk_value)
            if len(keywords)>0:
                i = key_num % len(keywords)
                keyword = keywords[i]
                pass
            else:
                keyword=""
            result=self.write_json_data(content,question_type,pk_value,keyword=keyword)
            num=num+1
            key_num=key_num+1
            results.append(result)
        print(results)
        string=",\n".join(results)
        string="["+string+"]"
        self.write_json_file(output_file,string)


if __name__=="__main__":
    question_type=1
    input_file="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/experiment/Problem.txt"
    output_file="./test.json"
    index=6
    ProcessFile().topfuction(input_file,output_file,question_type,index)

