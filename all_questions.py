import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.0800
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '0.5 * math.log((1 - p) / p)'


    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "The case of Alan who divides the one coin into two coins and then he flips the going to stock market prediction doesn't have any sort of real predictive attribute. The good people of bagging approach carry out well whenever there is at least as much evidence as just a random guess, and these are based on the actual data. Tossing a coin in doing so excludes everything, such as financial data, trends and marketers which play a vital role in the stock market movements. Then, we have more than random guessing with this kind of an ensemble and the lack of interest can serve as a disadvantage."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = "iii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = "i"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = "ii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = "iv"
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "No"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "No, the predictive ability of C2 classifier is not higher than that of C1. In addition to a high TPR C2 also has a higher FPR, showing that it is like a random guess about the problem too, in contrast to C1. This is evident in the ROC curve, where TPR pises FPR."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = "Precision and recall are the metrics that evaluation of C2 and C1 would accurately reflect their performance in this context. They demonstrate that C2 has equal accuracy with C1 but higher recall dimension, hence seeming as a better classifier in accordance with the given evaluation indexes."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "Unlike C1 which tends to miss out on nearly half of the positive cases, C2 comes up as a more efficient classifier thanks to its high recall/TPR and F1-measure. This goes to show the distinction between C2 and other algorithms, as it increasingly manages to find and differentiate accurately among all of these positive examples, providing a better precision and recall balance."
    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "Precision, recall, and F1-measure offer the more detailed information to a classifier’s performance, especially in context of the distributions of class in data. As for classifiers, the model is not only designed to determine positive instances but it has to be precise in the classification process as well."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "While C1 is a poor classifier because of the high number of misclassifications, C3 is the preferred classifier, as it gives the best trade-off between precision, recall, and F1-measure with a lower value of FPR. It has the greatest precision among all which means its the rarest false classifications and its the decent recall rate with the moderate F1-measure."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = '(p*100)/(p*1000)'

    # type: eval_float
    answers['(a) recall for C0'] = 'P'#0.5

    # type: eval_float
    answers['(b) F-measure of C0'] =  '(0.2 * P) / (0.1 + P)'#0.16666


    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] =  0.3#0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
        'recall': 0.533,
        'precision': 0.6154,
        'F-measure': 0.5689,
        'accuracy': 0.8800
    }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'Accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "F-measure is the best metric because it gives a perspective that looks at both precision and recall that are vital when dealing with class imbalances. Accuracy is the worst metric because it does not perceive the imbalance and can be very misleading by reporting higher accuracy scores even when the model performs poorly on the rarer class."

    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "F1"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "The F1 score is to be used to compare both the testing options because it is very useful for balancing the importance of precision and recall. In medical diagnostics particularly cancer detection, the minimization of false negatives is of crucial appearance as failing to find a disease out would mean consquences that are consequentially severe. Hence, F-score is more suitable than it gives the sensitivity and specified equal with the precision.Sensitivity of the test and the level of true positives as well as specificity have to be evaluated."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "If the cost of follow-up testing after a false positive is affordable in terms of financial and the patient's well-being, the TPR becomes the primary parameter even in the presence of high FPR. Here, the ratio TPR/FPR becomes more crucial than the TPR to FPR ratio, and we prioritize decreasing the number of false negatives over false positives."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
