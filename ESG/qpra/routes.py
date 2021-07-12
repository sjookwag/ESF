from flask import render_template, request, Blueprint, url_for, flash, redirect
# import copy
from ESG import db
from ESG.models import Model, Category, Distribution
from ESG.qpra.forms import ModelForm, SimForm, DIST
from ESG.qpra.query import sqModelUser,sqDelModel,sqModelID
from ESG.qpra.distributions import DTPerti,DTTriangPerc,DTLognormal,DTNormal,DTIntuniform,DTUniform,DTGamma,DTExponential,DTBinomial,DTPoisson,DTBernoulli,DTPertPerc,DTTriangPerc,DTTriangular
qpra = Blueprint('qpra', __name__)

@qpra.route("/qpra", methods = ['POST', 'GET'])
def home():    
  user_id = 0
  sql = sqModelUser.format(user_id)  
  models= db.session.execute(sql)
  # varValues = copy.deepcopy(models)
  # [var for var in models]
  varValues = []
  for varValue in models:
    fprob = 0.0; sprob = 0.0
    fabbr = varValue[10];param10 = varValue[4];param20 = varValue[5]
    sabbr = varValue[11];param11 = varValue[7];param21 = varValue[8];param31 = varValue[9]
    # print('0modelname:',varValue[1],'fabbr:',fabbr,'sabbr:',sabbr)
    if fabbr=='BIN':
      fprob = DTBinomial(param10,param20)
    elif fabbr=='POI':
      fprob = DTPoisson(param10)
    elif fabbr=='BER':
      fprob = DTBernoulli(param10)
    elif fabbr=='INT':
      fprob = DTIntuniform(param10,param20)  
    
    if sabbr=='UNI':
      sprob = DTUniform(param11,param21)
    elif sabbr=='TRI':
      sprob = DTTriangular(param11,param21,param31)  
    elif sabbr=='TRP':
      sprob = DTTriangPerc(param11,param21,param31)        
    elif sabbr=='PER':  
      sprob = DTPerti(param11,param21,param31)  
    elif sabbr=='GAM':
      sprob = DTGamma(param11,param21)
    elif sabbr=='PEP':
      sprob = DTPertPerc(param11,param21,param31)  
    elif sabbr=='LOG':
      sprob = DTLognormal(param11,param21)  
    elif sabbr=='NOR':
      sprob = DTNormal(param11,param21)  
    elif sabbr=='EXP':
      sprob = DTExponential(param11)    

    dic = {'id':varValue[0],'modelname':varValue[1],'category':varValue[2],'fdist':varValue[3],'param10':param10,'param20':param20, \
      'sdist':varValue[6],'param11':param11,'param21':param21,'param31':param31,'fabbr':fabbr,'sabbr':sabbr,'fprob':fprob,'sprob':sprob }
    print('1modelname:',varValue[1],'fabbr:',fabbr,'sabbr:',sabbr,'fprob:',fprob,'sprob:',sprob)
    # print(dic,'\n')    
    varValues.append(dic)
  
  mform = ModelForm()# user id를 매개변수로 전달하여 쿼리하여 모델과 시뮬레이션 정보 장전
  sform = SimForm()
  return render_template('qpra.html',models=varValues,modelform=mform,simform=sform)

@qpra.route("/qpra/newmodel", methods = ['POST'])
def newModel():  
  mform = ModelForm()# user id를 매개변수로 전달하여 쿼리하여 모델과 시뮬레이션 정보 장전
  if mform.validate_on_submit() or request.method == 'POST':  
    modelname= mform.ModelName.data
    category = mform.Category.data    
    
    frqdist  = mform.FrqDist.data
    param10  = mform.Parameter10.data
    if DIST[frqdist][1]==2:
      param20  = mform.Parameter20.data
    else:
      param20  = None
    
    sDist    = mform.SvrDist.data
    param11  = mform.Parameter11.data
    if DIST[sDist][1]==2:
      param21  = mform.Parameter21.data
    elif DIST[sDist][1]==3:   
      param21  = mform.Parameter21.data
      param31  = mform.Parameter31.data 
    else:
      param21  = None
      param31  = None 

    model = Model(modelname=modelname,category=category,fdist=frqdist,param10=param10,param20=param20,sdist=sDist,param11=param11,param21=param21,param31=param31,user_id=0)
    db.session.add(model)
    db.session.commit()
    flash('새 모델({0})이 추가되었습니다'.format(modelname), 'success')    
  return redirect(url_for('qpra.home'))

@qpra.route("/qpra/<int:id>/updatemodel", methods = ['POST', 'GET'])
def updateModel(id):  
  mform = ModelForm()# user id를 매개변수로 전달하여 쿼리하여 모델과 시뮬레이션 정보 장전  
  if mform.validate_on_submit() or request.method == 'POST':  
    modelname= mform.ModelName.data
    category = mform.Category.data    
    frqdist  = mform.FrqDist.data
    param10  = mform.Parameter10.data
    param20  = None
    if DIST[frqdist][1]==2:
      param20  = mform.Parameter20.data
    else:
      param20  = None
    
    sDist    = mform.SvrDist.data
    param11  = mform.Parameter11.data
    param21  = None
    param31  = None
    if DIST[sDist][1]==2:
      param21  = mform.Parameter21.data
    elif DIST[sDist][1]==3:   
      param21  = mform.Parameter21.data
      param31  = mform.Parameter31.data 
    else:
      param21  = None
      param31  = None  

    model = db.session.query(Model).filter(Model.id==id).update({
      'modelname':modelname,'category':category,'fdist':frqdist,'param10':param10,'param20':param20,'sdist':sDist,'param11':param11,'param21':param21,'param31':param31
    })    
    db.session.commit()
    flash('모델 {0}이 업데이트되었습니다'.format(modelname), 'success')    
    return redirect(url_for('qpra.home'))
  else:    
    sql = sqModelID.format(id)  
    varValues = db.session.execute(sql)
    varValue = [var for var in varValues]
    _,mform.ModelName.data,mform.Category.data,mform.FrqDist.data,mform.Parameter10.data,mform.Parameter20.data,mform.SvrDist.data,mform.Parameter11.data,mform.Parameter21.data,mform.Parameter31.data = varValue[0]
    mform.submit.label.text = 'Update'
    return render_template('update_model.html',id=id,modelform=mform)

@qpra.route("/qpra/<int:id>/delmodel", methods = ['POST','GET'])
def delModel(id):  
  # model = Model.query.get_or_404(id)
  # db.session.delete(model)
  sql = sqDelModel.format(id)
  db.session.execute(sql)
  db.session.commit()
  flash('해당 모델이 삭제되었습니다', 'success')
  return redirect(url_for('qpra.home'))

@qpra.route("/qpra/runsim", methods = ['POST'])
def runSim():
  mform = ModelForm() # user id를 매개변수로 전달하여 쿼리하여 모델과 시뮬레이션 정보 장전
  sform = SimForm()
  if sform.validate_on_submit() or request.method == 'POST':  
    samples = sform.Samples.data
    iter    = sform.Iterations.data
    minimum = sform.Minimum.data
    maximum = sform.Maximum.data
    mean    = sform.Mean.data
    median  = sform.Median.data
    mode    = sform.Mode.data
    stdev   = sform.Standard_Deviation.data
    skew    = sform.Skewness.data
    kurt    = sform.Kurtosis.data
    pct1    = sform.Percentile1.data
    pct2    = sform.Percentile2.data
    tar1    = sform.Target1.data
    tar2    = sform.Target2.data
    bins    = sform.Bins.data
    print(samples,iter,minimum,maximum,mean,median,mode,stdev,skew,kurt,pct1,pct2,tar1,tar2,bins)
  return render_template('qpra.html', modelform=mform,simform=sform)
