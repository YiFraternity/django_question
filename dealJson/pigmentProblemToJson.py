from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=51
    index=4
    input_file="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/pigment/PigmentProblem.txt"
    output_file="../data/pigmentProblemJson.json"
    ProcessFile().topfuction(input_file,output_file,question_type,index)


