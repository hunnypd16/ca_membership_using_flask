from flask import Flask, request
from camembership import detail_of_chartedaccountant
app = Flask(__name__)
@app.route('/camembership', methods = ['GET', 'POST'])
def detailofchartedaccountant():
    caMembership_number = request.values.get("CA_membership_Number")
    data1 = detail_of_chartedaccountant(caMembership_number)
    return data1
if __name__ == '__main__':
    app.run()