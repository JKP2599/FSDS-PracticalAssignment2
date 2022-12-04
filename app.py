# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from application_logging import logger
import pickle

app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    file_object = open("application_logging/logfile.txt", 'a+')
    log_writer = logger.App_Logger()
    if request.method == 'POST':
        try:
            log_writer.log(file_object, "Taking User Input")

            rate_marriage = float(request.form['rate_marriage'])
            yrs_married = float(request.form['yrs_married'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            educ = float(request.form['educ'])
            occupation = float(request.form['occupation'])
            occupation_husb = float(request.form['occupation_husb'])

            log_writer.log(file_object, "Separating sccupation and occupation_husb variables for the model")
            occ_2, occ_3, occ_4, occ_5, occ_6 = [int(occupation == 2),
                                                 int(occupation == 3),
                                                 int(occupation == 4),
                                                 int(occupation == 5),
                                                 int(occupation == 6)]
            occ_husb_2, occ_husb_3, occ_husb_4, occ_husb_5, occ_husb_6 = [int(occupation_husb == 2),
                                                                          int(occupation_husb == 3),
                                                                          int(occupation_husb == 4),
                                                                          int(occupation_husb == 5),
                                                                          int(occupation_husb == 6)]


            logReg_model = 'logReg_model.pickle'
            scale_model = 'scale_model.pickle'

            log_writer.log(file_object, "Initialising Logistic Regression Model")
            logReg = pickle.load(open(logReg_model, 'rb'))  # loading the Linear Regression model from file
            log_writer.log(file_object, "Initializing Scaling model")
            scaler = pickle.load(open(scale_model, 'rb'))  # loading the standard scaler model from file
            # predictions using the loaded model file

            log_writer.log(file_object, "Input Scaling")
            scaled_input = scaler.transform([[occ_2, occ_3, occ_4, occ_5, occ_6,
                                              occ_husb_2, occ_husb_3, occ_husb_4, occ_husb_5, occ_husb_6,
                                              rate_marriage, yrs_married, children, religious, educ]])
            log_writer.log(file_object, "Generating Prediction using Trained model")
            prediction = logReg.predict(scaled_input)

            if prediction == 1:
                affair = 'This Woman probably Had an affair'
            else:
                affair = 'This Woman probably Did Not Have an affair'

            log_writer.log(file_object, affair)
            print(affair)
            return render_template("results.html", prediction=affair)
        except Exception as e:
            log_writer.log(file_object, "Error Occurred!!")
            log_writer.log(file_object, f'The Exception message is: {e}')
            print('The Exception message is: ', e)
            return 'something went wrong'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app
