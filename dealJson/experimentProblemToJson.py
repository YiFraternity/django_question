"""
由于experiment题中
问题与答案行数相差不是固定值，所以手动修改下
生成的json文件
"""
from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=61
    index=6
    input_file="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/experiment/Problem.txt"
    output_file="../data/experimentProblemJson.json"
    ProcessFile().topfuction(input_file,output_file,question_type,index)


