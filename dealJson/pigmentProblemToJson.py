from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=51
    index=4
    parent_path="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/pigment/"
    input_filename="PigmentProblem.txt"
    keyword_filename="Pigment.txt"
    keyword_file=parent_path+keyword_filename
    input_file=parent_path+input_filename
    output_file="../data/pigmentProblemJson.json"
    keywords = ProcessFile().get_keyword(keyword_file,index=1,is_question=False)
    ProcessFile().topfuction(input_file,output_file,question_type,index,keywords=keywords)


