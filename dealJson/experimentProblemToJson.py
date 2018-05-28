"""
由于experiment题中
问题与答案行数相差不是固定值，所以手动修改下
生成的json文件
"""
from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=61
    index=6
    parent_path="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/experiment/"
    input_filename="Problem.txt"
    keyword_filename="experiment.txt"
    input_file = parent_path+input_filename
    output_file="../data/experimentProblemJson.json"
    ProcessFile().topfuction(input_file,output_file,question_type,index)


