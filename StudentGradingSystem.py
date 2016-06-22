import statistics

admins = {'fang':'123', 'wang':'456'}
studentDict = {'Justin':[52,66,99],'Eva':[99,85,76],'William':[88,77,66]}


def login():
    print("""

                      Log In
    
    """)
    username = input('           Username:  ')
    password = input('           Password:  ')
    if username in admins:
        if admins[username] == password:
            print('Welcome', username)
            while True:
                main()
        else:
            print('Wrong password, please try again')
    else:
        print(username, 'does not exist in our system.')

        
def enterGrades():
    nameToEnter = input('  Student Name: ')
    gradeToEnter = int(input('  Adding grade: '))

    if nameToEnter in studentDict:
        studentDict[nameToEnter].append(gradeToEnter)
        print(studentDict)
    else:
        print('  ',nameToEnter, 'does not exist in our system.')

def removeStudent():
    nameToEnter = input('  Student Name: ')
    if nameToEnter in studentDict:
        del studentDict[nameToEnter]
    else:
        print('  ',nameToEnter, 'does not exist in our system.')

def avgGrades():
    for eachStudent in studentDict:
        avgGrade = statistics.mean(studentDict[eachStudent])
        print(eachStudent,'\'s average grade is ',avgGrade)


    

def main():
    print("""
    Welcome to Student Grading System!

    Choose an option for your needs:

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Average of Student Grades
    [4] - Exit
    """)
    action = input('  Input a number for your option: ')

    if action == '1':
        enterGrades()
        
    elif action == '2':
        removeStudent()

    elif action == '3':
        avgGrades()

    elif action == '4':
        exit()

    else:
        print('  No valid option was given, please input again.')
        

login()


