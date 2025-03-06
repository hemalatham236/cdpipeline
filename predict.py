from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)
print(__name__)
print("Hi...!!!!!!")


@app.route("/")
def hello_world():
    return "<p>Hello, World ! Seee varenya now successful!!!!!</p>"


model_pickle = open("classifier.pkl", "rb")
clf = pickle.load(model_pickle)


@app.route("/ping", methods=["GET"])
def pinger():
    return {"MESSAGE": "Hi, I am Pinging ...!!!!!"}


@app.route("/predict", methods=['POST'])
def prediction():
    loan_req = request.get_json()
    print(loan_req)
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}


print("We are happy today!!!!")