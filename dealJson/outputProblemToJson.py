from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=21
    index=2
    parent_path="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/output/"
    input_filename="problem.txt"
    keyword_filename="output.txt"
    keyword_file=parent_path+keyword_filename
    input_file=parent_path+input_filename
    output_file="../data/outputProblemJson.json"
    keywords = ProcessFile().get_keyword(keyword_file,index=2,delimiter=',')
    ProcessFile().topfuction(input_file,output_file,question_type,index,keywords=keywords)
