# -*- coding: utf-8 -*-

from scipy import stats
import numpy as np
import random, math

def DTPerti(mode, min, max):
  if(max - min)==0:
    return 0.0
  alpha = (4 * mode + max - 5 * min) / (max - min)
  beta = (5 * max - min - 4 * mode) / (max - min)
  uniform = random.random()
  return stats.beta.ppf(uniform, alpha, beta, loc= min, scale=(max-min))

def DTLognormal(miu, sigma):
  if miu==0:
    return 0
  miuprima = math.log((miu ** 2) / (math.sqrt(sigma ** 2 + miu ** 2)))
  sigmaprima = math.sqrt(math.log(1 + (sigma / miu) ** 2))
  uniform = random.random()
  return stats.lognorm(sigmaprima, scale=np.exp(miuprima)).ppf(uniform)

def DTNormal(miu, sigma):
  uniform = random.random()
  return stats.norm.ppf(uniform, loc=miu, scale=sigma)

def DTIntuniform(min, max):
  return random.randint(min, max)

def DTUniform(min, max):
  return min+(max-min)*random.random()

def DTGamma(alpha, beta):
  uniform = random.random()
  return stats.gamma.ppf(uniform, alpha,0, beta)

def DTExponential(beta):
   uniform = random.random()
   return -beta * math.log(1 - uniform)

def DTBinomial(n, p):
  uniform = random.random()
  return stats.binom.ppf(uniform, n=n, p=p)

def DTPoisson(lamb):
  uniform = random.random()
  return stats.binom.ppf(uniform, n=10000000, p=lamb/ 10000000)

def DTBernoulli(p):
  uniform = random.random()
  return 0 if p<=uniform else 1

def DTPertPerc(mode, minperc, maxperc):
  uniform = random.random()
  min = mode * (1 - minperc)
  max = mode * (1 + maxperc)
  if(max - min)==0:
    return 0.0
  alpha = (4 * mode + max - 5 * min) / (max - min)
  beta = (5 * max - min - 4 * mode) / (max - min)
  return stats.beta.ppf(uniform, alpha, beta, loc=min, scale=max-min)

def DTTriangPerc(mode, minperc, maxperc):
  uniform = random.random()
  min = mode * (1 - minperc)
  max = mode * (1 + maxperc)
  if(max-min)==0:
    return 0.0
  d = (mode - min) / (max - min)
  if uniform <= d :
    return min + math.sqrt(uniform * (max - min) * (mode - min))
  else:
    return max - math.sqrt((1 - uniform) * (max - min) * (max - mode))

def DTTriangular(mode,min,max):
  if(max-min)==0:
    return 0.0
  uniform = random.random()
  d = (mode-min)/(max-min)
  if uniform<=d:
    return min + math.sqrt(uniform * (max - min) * (mode - min))
  else:
    return max - math.sqrt((1 - uniform) * (max - min) * (max - mode))  

def eVal(ref):
  return eval(ref)