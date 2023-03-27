from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('Employee_attrition.pkl', 'rb'))

@app.route("/")
def Home():
 return render_template('index.html')

@app.route("/employeePredict",methods=['POST','GET'])
def employeePredict():
  if request.method=='POST':
   print("...................................................")
   age= int(request.form['age'])
   dfh= int(request.form['dfh'])
   mi=int(request.form['MonthlyIncome'])
   hr= int(request.form['HourlyRate'])
   mr =int( request.form['MonthlyRate'])
   dr =int( request.form['DailyRate'])
   ycm = int(request.form['ycm'])
   ycr = int(request.form['ycr'])
   yac=int(request.form['yac'])
   psh=int(request.form['psh'])
   ncw=int(request.form['ncw'])
   twy=int(request.form['twy'])
   ov=(request.form['OverTime'])
   if ov=="1":
    v=1
   else:
    v=0
   ef=(request.form['EducationField'])
   ef=int(ef)
   jr=(request.form['JobRole'])
   jr=int(jr)
   x=[dr,dfh,ef,hr,jr,mi,mr,ncw,v,psh,twy,yac,ycr,ycm,age]
   print(x)
   result=model.predict([[dr,dfh,ef,hr,jr,mi,mr,ncw,v,psh,twy,yac,ycr,ycm,age]])[0]
   print(result)
  if result==1:
    return  render_template('index.html',res="Employee discontinued.")
  else:
    return render_template('index.html',res="employee continued")
if __name__=="__main__":
 app.run(debug=True)

