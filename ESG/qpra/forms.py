from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange

CA = [(None,'Choose..'),('Tot','Total Risk'),('Tec','Technical Risk'),('Log','Logistics Risk'),('Env','Environmental Risk'),('Man','Management related Risk'),('Fin','Financial Risk'),('Soc','Socio-political Risk')]
FD = [(None,'Choose..'),('Ber','Bernoulli'),('Bin','Binomial'),('Poi','Poisson'),('Int','IntUniform')]
SD = [(None,'Choose..'),('Exp','Exponential'),('Gam','Gamma'),('Log','LogNormal'),('Nor','Normal'),('Per','Pert'),('PeP','PertPerc'),('Tri','Triangular'),('TrP','TriangPerc'),('Uni','Uniform')]

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
  Target1 = IntegerField("Target#1", default='30000', render_kw={'type':'number','min':'1','step':'10'})
  Target2 = IntegerField("Target#2", default='40000', render_kw={'type':'number','min':'1','step':'10'})
  Bins = IntegerField("Bins", default='100', render_kw={'type':'number','min':'1','step':'10'})
  submit = SubmitField('Run')

