from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=32
    index=2
    input_file="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/raw_output/FunctionProblem.txt"
    output_file="../data/rawoutputOfFunctionProblemJson.json"
    ProcessFile().topfuction(input_file,output_file,question_type,index)


