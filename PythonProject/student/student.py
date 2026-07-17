student_data = {

    "Student_ID":[1,2,3,4,5,6,7,8,9,10],

    "Course":[
        "AI","AI",
        "Data Science","Data Science",
        "Python","Python",
        "AI","Python",
        "Data Science","AI"
    ],

    "Department":[
        "AI","AI",
        "Data Science","Data Science",
        "Python","Python",
        "AI","Python",
        "Data Science","AI"
    ],

    "Fee":[
        25000,25000,
        30000,30000,
        20000,20000,
        25000,20000,
        30000,25000
    ]
}


student_df = pd.DataFrame(student_data)

student_df