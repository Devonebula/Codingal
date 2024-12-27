students={
    "id1":{
        "name":"Keshav",
        "subject": "English" "Science" "Maths" "History"
    },   
    "id2":{
        "name":"Amit",
        "subject": "English" "Science" "Maths" "History"
    },   
    "id3":{
        "name":"Raj",
        "subject": "English" "Science" "Maths" "History"
    }   

}

result={}
for key, value in students.items():
    if value not in result.values():
        result[key]=value
print(result)