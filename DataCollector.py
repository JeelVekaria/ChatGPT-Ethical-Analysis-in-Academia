import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
EXCEL_SHEET = pd.read_excel("results.xlsx")

# Question: Do you think ChatGPT can replace search engines?
def createBarGraph(title, num):
    # Data
    x = [1,2,3,4,5]
    y_data = list(EXCEL_SHEET[title])
    y = []

    # Get # of responses
    for i in range(5):
        count = 0
        for j in range(len(y_data)):
            if y_data[j] == x[i]:
                count += 1
        y.append(count)

    # Setup the graph
    plt.title("Figure " + str(num) + ": " + title)
    plt.xlabel("Least Likely → Most Likely")
    plt.ylabel("# Responses")
    plt.bar(x,y)
    plt.show()

def createPieGraph(title, labels, num):
    # Data for reponses
    y_data = list(EXCEL_SHEET[title])
    y = []

    # Get # of responses for each label
    for i in range(len(labels)):
        count = 0
        for j in range(len(y_data)):
            if y_data[j] == labels[i]:
                count += 1
        y.append(count)

    # Show graph
    plt.title("Figure " + str(num) + ": " + title)
    plt.pie(np.array(y), labels=labels, explode = [0.1,0.1,0,0,0], autopct='%1.0f%%')
    plt.show()

# This graph is going to show the relationship between students
# faculty and ChatGPT's effect on students
def customBarGraph(labels, num):
    # Data for each faculty and its effect
    faculty = list(EXCEL_SHEET["What faculty are you part of?"])
    usage = list(EXCEL_SHEET["Has ChatGPT had any affect on your studies?"])
    y = []

    # Get # of responses for each faculty
    for i in range(len(labels)):
        count = 0
        for j in range(len(usage)):
            # we check the faculty and whether they used ChatGPT the most
            if labels[i] == faculty[j]:
                # the usage will depend on responses between 3-5
                # 3 in the middle, 5 the most effect
                if usage[j] in range(3,6):
                    count += 1
        y.append(count)

    # Show graph
    plt.title("Figure " + str(num) + ": Student Faculty VS. ChatGPT Effect on Studies")
    plt.pie(np.array(y), labels=labels, autopct='%1.0f%%')
    plt.show()

if __name__ == '__main__':
    # Bar Graph 1
    createBarGraph("How likely are you to use ChatGPT on an assignment?", 1)

    # Bar Graph 2
    createBarGraph("Has ChatGPT had any affect on your studies?", 2)

    # Custom Bar Graph (explination in function)
    labels = [  'Faculty of Art',
                'Faculty of Community Services',
                'Faculty of Engineering and Architectural Science',
                'Faculty of Law',
                'Faculty of Science',
                'Other'
             ]
    customBarGraph(labels, 3)

    # Bar Graph 3
    createBarGraph("Do you think ChatGPT can replace search engines?", 4)

    # Pi Graph
    title = "What would you use ChatGPT for the most?"
    labels = ['School/Assignments', 'Entertainment', 'Job/Resume', 'Personal assistance', 'Other']
    createPieGraph(title, labels, 5)
