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
            #print(content)
            if content.endswith("\n"):
                content=content[:-2]
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

    def trans_qa_to_pair(self,data,index):
        contents=[
            data[i:i+index]
            for i in range(0,len(data),index)
        ]
        lists=[]
        for content in contents:
            list=[]
            for i in content:
                i=i.replace("\n",'')
                list.append(i)
            lists.append(list)
        print(lists)
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

    def write_json_data(self,content,question_type,pk_value):
        data={
            "model":"question.Question",
            "pk":pk_value,
            "fields":{
                "quest":content[0],
                "answer":content[1],
                "question_type":question_type,
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
    input_file:输入文件
    output_file:输出文件
    question_type:问题类型（1-6,分别代表原来，产物，原料和产物，因素，光和色素，实验）
    """
    def topfuction(self,input_file,output_file,question_type,index):
        results=[]
        data=self.get_txt_data(input_file)
        contents=self.trans_qa_to_pair(data,index)
        num=1
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
            result=self.write_json_data(content,question_type,pk_value)
            num=num+1
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

