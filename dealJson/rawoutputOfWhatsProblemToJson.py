from encodeFileToJson import ProcessFile

if __name__=="__main__":
    question_type=31
    index=2
    input_file="/home/lyh/java/eclipse-workspace/QuestionGeneration/src/data/raw_output/problem.txt"
    output_file="../data/rawoutputOfWhatsProblemJson.json"
    ProcessFile().topfuction(input_file,output_file,question_type,index)


