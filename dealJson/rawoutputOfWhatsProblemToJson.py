from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=31
    index=2
    parent_path="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/raw_output/whats/"
    input_filename = "problem.txt"
    output_file="../data/rawoutputOfWhatsProblemJson.json"
    keyword_filename = "raw_output.txt"
    keyword_file = parent_path+keyword_filename
    input_file = parent_path + input_filename
    keywords = ProcessFile().get_keyword(keyword_file,index=3,is_question=True,delimiter=",")
    ProcessFile().topfuction(input_file,output_file,question_type,index,keywords=keywords)


