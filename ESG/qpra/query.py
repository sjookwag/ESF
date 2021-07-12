
sqModelUser = '''
  SELECT m.id,m.modelname,c.name AS category,d.name AS fdist,m.param10,m.param20,e.name AS sdist,m.param11,m.param21,m.param31,m.fdist AS fabbr,m.sdist AS sabbr 
  FROM model m, category c, distribution d, distribution e 
  WHERE m.category=c.abbr AND m.fdist=d.abbr AND m.sdist=e.abbr AND m.user_id={0}
  ORDER BY m.id DESC
'''
sqModelID = '''
  SELECT m.id,m.modelname,m.category,m.fdist,m.param10,m.param20,m.sdist,m.param11,m.param21,m.param31 
  FROM model m
  WHERE m.id={0}
'''
sqDelModel = '''
  DELETE FROM model WHERE id={0}
'''