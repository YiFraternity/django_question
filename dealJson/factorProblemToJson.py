from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=41
    index=4
    parent_path="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/factor/"
    input_filename="FactorProblem.txt"
    keyword_filename="Factors.txt"
    keyword_file=parent_path+keyword_filename
    input_file=parent_path+input_filename
    output_file="../data/factorProblemJson.json"
    keywords = ProcessFile().get_keyword(keyword_file,index=1,is_question=False)
    ProcessFile().topfuction(input_file,output_file,question_type,index,keywords=keywords)


