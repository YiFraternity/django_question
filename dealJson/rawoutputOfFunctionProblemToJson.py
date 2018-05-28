from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=32
    index=2
    parent_path="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/raw_output/function/"
    input_filename = "FunctionProblem.txt"
    output_file="../data/rawoutputOfFunctionProblemJson.json"
    input_file = parent_path + input_filename
    keywords = ["原料"]
    ProcessFile().topfuction(input_file,output_file,question_type,index,keywords=keywords)


