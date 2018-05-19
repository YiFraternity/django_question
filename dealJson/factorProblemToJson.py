from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=41
    index=4
    input_file="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/factor/FactorProblem.txt"
    output_file="../data/factorProblemJson.json"
    ProcessFile().topfuction(input_file,output_file,question_type,index)


