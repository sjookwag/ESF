from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField, IntegerField, BooleanField
from wtforms.validators import DataRequired

CA = [(None,'Choose..'),('Tot','Total Risk'),('Tec','Technical Risk'),('Log','Logistics Risk'),('Env','Environmental Risk'),('Man','Management related Risk'),('Fin','Financial Risk'),('Soc','Socio-political Risk')]
FD = [(None,'Choose..'),('BER','Bernoulli'),('BIN','Binomial'),('POI','Poisson'),('INT','IntUniform')]
SD = [(None,'Choose..'),('EXP','Exponential'),('GAM','Gamma'),('LOG','LogNormal'),('NOR','Normal'),('PER','Pert'),('PEP','PertPerc'),('TRI','Triangular'),('TRP','TriangPerc'),('UNI','Uniform')]

class ModelForm(FlaskForm):
  ModelName = StringField('Model Name'  , validators=[DataRequired()])
  Category = SelectField('Category'     , choices=CA)
  FrqDist = SelectField('Frequency Dist', choices=FD)
  Parameter10 = FloatField("Parameter#1", render_kw={'type':'number','min':'0','step':'0.01'})
  Parameter20 = FloatField("Parameter#2", render_kw={'type':'number','min':'0','step':'0.01'})
  SvrDist = SelectField('Severity Dist' , choices=SD)
  Parameter11 = FloatField("Parameter#1", render_kw={'type':'number','min':'0','step':'0.01'})
  Parameter21 = FloatField("Parameter#2", render_kw={'type':'number','min':'0','step':'0.01'})
  Parameter31 = FloatField("Parameter#3", render_kw={'type':'number','min':'0','step':'0.01'})
  submit = SubmitField('Add')

class SimForm(FlaskForm):
  Samples = IntegerField('Samples', default=700, render_kw={'type':'number', 'min':'1'})
  Iterations = IntegerField('Iterations', default=200, render_kw={'type':'number', 'min':'1'})
  Minimum = BooleanField('Minimum', default=True, render_kw={'checked': True})
  Maximum = BooleanField('Maximum', default=True, render_kw={'checked': True})
  Mean = BooleanField('Mean', default=True, render_kw={'checked': True})
  Median = BooleanField('Median', default=True, render_kw={'checked': True})
  Mode = BooleanField('Mode', default=False, render_kw={'checked': False})
  Standard_Deviation = BooleanField('Standard Deviation', default=True, render_kw={'checked': True})
  Skewness = BooleanField('Skewness', default=True, render_kw={'checked': True})
  Kurtosis = BooleanField('Kurtosis', default=True, render_kw={'checked': True})
  Percentile1 = FloatField("Percentile#1", default='0.1', render_kw={'type':'number','min':'0.0','max':'1.0','step':'0.1'})
  Percentile2 = FloatField("Percentile#2", default='0.9', render_kw={'type':'number','min':'0.0','max':'1.0','step':'0.1'})
  Target1 = IntegerField("Target#1", default='30000', render_kw={'type':'number','min':'10','step':'10'})
  Target2 = IntegerField("Target#2", default='40000', render_kw={'type':'number','min':'10','step':'10'})
  Bins = IntegerField("Bins", default='100', render_kw={'type':'number','min':'100','step':'10'})
  submit = SubmitField('Run')

DIST = {'BER':['Bernoulli Discrete',1,'p']
  ,'BIN':['Binomial Discrete',2,'n','p']
  ,'POI':['Poisson Discrete',1,'lambda']
  ,'INT':['IntUniform Discrete',2,'min','max']
  ,'EXP':['Exponential Continuous',1,'beta']
  ,'GAM':['Gamma Continuous',2,'alpha','beta']
  ,'LOG':['LogNormal Continuous',2,'miu','sigma']
  ,'NOR':['Normal Continuous',2,'miu','sigma']  
  ,'PER':['Pert Continuous',3,'mode','min','max']
  ,'PEP':['PertPerc Continuous',3,'mode','percmin','percmax']
  ,'TRI':['Triangular Continuous',3,'mode','min','max']
  ,'TRP':['TriangPerc Continuous',3,'mode','percmin','percmax']
  ,'UNI':['Uniform Continuous',2,'min','max']}

if __name__ == '__main__':
  print(DIST('Ber'))