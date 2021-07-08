from flask import render_template, request, Blueprint
from ESG.models import Model
from ESG.qpra.forms import ModelForm, SimForm

qpra = Blueprint('qpra', __name__)

@qpra.route("/qpra", methods = ['POST', 'GET'])
def home():  
  mform = ModelForm()# user id를 매개변수로 전달하여 쿼리하여 모델과 시뮬레이션 정보 장전
  sform = SimForm()
  return render_template('qpra.html', modelform=mform,simform=sform)

@qpra.route("/qpra/newmodel", methods = ['POST'])
def newModel():  
  mform = ModelForm()# user id를 매개변수로 전달하여 쿼리하여 모델과 시뮬레이션 정보 장전
  sform = SimForm()
  if mform.validate_on_submit(): # or request.method == 'POST':  
    modelname= mform.ModelName.data
    category = mform.Category.data    
    frqdist  = mform.FrqDist.data
    param10  = mform.Parameter10.data
    param20  = mform.Parameter20.data
    sDist    = mform.SvrDist.data
    param11  = mform.Parameter11.data
    param21  = mform.Parameter21.data
    param31  = mform.Parameter31.data 
    print(modelname,category,frqdist,param10,param20,sDist,param11,param21,param31)  
  return render_template('qpra.html', modelform=mform,simform=sform)

@qpra.route("/qpra/runsim", methods = ['POST'])
def runSim():
  mform = ModelForm() # user id를 매개변수로 전달하여 쿼리하여 모델과 시뮬레이션 정보 장전
  sform = SimForm()
  if sform.validate_on_submit():  
    pass
  return render_template('qpra.html', modelform=mform,simform=sform)