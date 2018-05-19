from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=21
    index=2
    input_file="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/output/problem.txt"
    output_file="../data/outputProblemJson.json"
    ProcessFile().topfuction(input_file,output_file,question_type,index)

