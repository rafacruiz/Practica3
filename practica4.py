#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import feedparser
import web
from web import form
import pymongo
from pymongo import Connection

web.config.debug = False

urls = (
     '/inicio', 'inicio',
     '/sobre', 'sobre',
     '/sign', 'sign',
     '/', 'register',
     '/modif', 'modif',
     '/show', 'show',
     '/estadistica', 'estadistica',
     '/mapa','mapa',
     '/logout', 'logout',
    '/(.*)', 'hello'
)

app = web.application(urls, globals())
ses = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'ide':0,'seg1':0,'seg2':0,'v':0,'z':0,'x':0,'y':0,'e':0})
tem = web.template.render('templates')

######################################################################BD##########################################################################
###						Creamos la base de datos, con unos datos iniciales						   ###
##################################################################################################################################################     

client = Connection ()
db = client.test_database
datuser = db.datuser

##################################################################################################################################################
##									Formularios								   ###
##################################################################################################################################################

#####################################################################Formulario Login#########################################################################
	    
formulario = form.Form(
  form.Textbox("usuario", form.notnull, description = "", value="username"),
  form.Password("passw", form.notnull, description = "", value="pass"),
)


#################################################################Formulario Registro inicial##################################################################

vpass = form.regexp(r".{6,10}$", 'Caracteres minimo 6, caracteres maximo 10')
vemail = form.regexp(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", "Direccion de e-mail incorrecta")
ncuent = form.regexp(r"([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})", 'Formato incorrecto. Espacio o guion')

formularionuevo= form.Form(     
    form.Textbox("nombre", form.notnull, description = "Nombre ", value="nombre"),
    form.Textbox("apellido", form.notnull, description = "Apellidos ", value="apellidos"),
    form.Textbox("email", vemail, form.notnull, description = "Email ", value="email"),
    form.Textbox("nvisa", ncuent, form.notnull, description = "Nu Visa ", value="0000"),
    form.Dropdown("dia", [(1, '1'), (2, '2'), (3, '3'), (4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12'),(13, '13'),(14, '14'),(15, '15'),(16, '16'),(17, '17'),(18, '18'),(19, '19'),(20, '20'),(21, '21'),(22, '22'),(23, '23'),(24, '24'),(25, '25'),(26, '26'),(27, '27'),(28, '28'),(29, '29'),(30, '30'),(31, '31')]),
    form.Dropdown("mes", [('enero', 'Enero'), ('febrero', 'Febrero'), ('marzo', 'Marzo'), ('abril', 'Abril'),('mayo', 'Mayo'),('junio', 'Junio'),('julio', 'Julio'),('agosto', 'Agosto'),('septiembre', 'Septiembre'),('octubre', 'Octubre'), ('noviembre', 'Noviembre'),('diciembre', 'Diciembre')]),
    form.Dropdown("anio", [(2003, '2003'),(2004, '2004'),(2005, '2005'),(2006, '2006'),(2007, '2007'),(2008, '2008'),(2009, '2009'),(2010, '2010'),(2011, '2011'), (2012, '2012'), ('2013', '2013')]),
    form.Textarea("direccion", form.notnull, description = "Direccion ", value="direccion"),
    form.Password("contrasena", vpass, form.notnull, description = "Contrasenia ", value="contrasenia"),
    form.Password("verificacion", vpass, form.notnull, description = "Verificacion ", value="verificacion"),
    form.Radio("forma", [('contra', 'Contra Reembolso'), ('visa', 'Visa')]),
    form.Checkbox("valor", form.Validator("Acepta la clausula", lambda i:"valor" not in i), description = "Clausulas "),
    form.Button("Enviar"),
    validators = [form.Validator("Contrasenia no coindice con su verificacion", lambda v: v.contrasena == v.verificacion)]
)

##################################################Funcion Formulario Modificacion de datos usuario###############################################
      
def formodifica(vsession):
  ses.ide = vsession
  contenido = datuser.find({"nombre":ses.ide})
  for info in contenido:
    nom=info['nombre']
    ap=info['apellido']
    em=info['email']
    nu=info['numvisa']
    d=info['dia']
    m=info['mes']
    a=info['anio']
    dr=info['direccion']
    con=info['contrasena']
    ve=info['verificacion']
    fo=info['forma']
    
  vpass = form.regexp(r".{6,10}$", 'Caracteres minimo 6, caracteres maximo 10')
  vemail = form.regexp(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", "Direccion de e-mail incorrecta")
  ncuent = form.regexp(r"([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})", 'Formato incorrecto. Espacio o guion')

  formulariomodify= form.Form(     
    form.Textbox("nombre", form.notnull, description = "Nombre ", value=nom),
    form.Textbox("apellido", form.notnull, description = "Apellidos ", value=ap),
    form.Textbox("email", vemail, form.notnull, description = "Email ", value=em),
    form.Textbox("nvisa", ncuent, form.notnull, description = "Nu Visa ", value=nu),
    form.Dropdown("dia", [(1, '1'), (2, '2'), (3, '3'), (4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12'),(13, '13'),(14, '14'),(15, '15'),(16, '16'),(17, '17'),(18, '18'),(19, '19'),(20, '20'),(21, '21'),(22, '22'),(23, '23'),(24, '24'),(25, '25'),(26, '26'),('27', '27'),(28, '28'),(29, '29'),(30, '30'),(31, '31')], value=d),
    form.Dropdown("mes", [('enero', 'Enero'), ('febrero', 'Febrero'), ('marzo', 'Marzo'), ('abril', 'Abril'),('mayo', 'Mayo'),('junio', 'Junio'),('julio', 'Julio'),('agosto', 'Agosto'),('septiembre', 'Septiembre'),('octubre', 'Octubre'), ('noviembre', 'Noviembre'),('diciembre', 'Diciembre')], value=m),
    form.Dropdown("anio", [(2003, '2003'),(2004, '2004'),(2005, '2005'),(2006, '2006'),(2007, '2007'),(2008, '2008'),(2009, '2009'),(2010, '2010'),(2011, '2011'), (2012, '2012'), ('2013', '2013')], value=a),
    form.Textarea("direccion", form.notnull, description = "Direccion ", value=dr),
    form.Password("contrasena", vpass, form.notnull, description = "Contrasenia ", value=con),
    form.Password("verificacion", vpass, form.notnull, description = "Verificacion ", value=ve),
    form.Radio("forma", [('contra', 'Contra Reembolso'), ('visa', 'Visa')], value=fo),
    form.Checkbox("valor", form.Validator("Acepta la clausula", lambda i:"valor" not in i), description = "Clausulas "),
    form.Button("Enviar"),
    validators = [form.Validator("Contrasenia no coindice con su verificacion", lambda v: v.contrasena == v.verificacion)]
  )
  
  b = formulariomodify()
  return b
  
##################################################################Funcion RSS###################################################################

def rss_function( ):
  dbrss = client.rss_database
  datrss = dbrss.datrss
  lista = []
  titls = lista
  
  ses.seg1 = t1 = time.time()  
  ttiemp = ses.seg1 - ses.seg2
  
  if ttiemp > 600:
    ses.seg2 = time.time()
        
    python_wiki_rss_url = "http://ep00.epimg.net/rss/tags/ultimas_noticias.xml"
    d = feedparser.parse( python_wiki_rss_url )
    
    d['feed']['title']
    dbrss.datrss.remove()
    datrss.insert({'rss':d.feed.title})
    for item in d['items']:
      datrss.insert({'rss':item['title']})
        
    for varn in datrss.find( ):
      titls.append(varn['rss'])
      
  else:
    for varn in datrss.find( ):
      titls.append(varn['rss'])
  return titls
  
##############################################################################################################################################
##								CLASES										##	
##############################################################################################################################################

class inicio:
    def GET(self):
      if ses.ide == 0:
	return tem.login(mej = "No has iniciado sesion")
      else:
	ses.v = ses.v + 1
	return tem.index(ses.ide, noticias = rss_function())
        
class sobre:
    def GET(self):
      if ses.ide == 0:
	return tem.login(mej = "No has iniciado sesion")
      else:
	ses.x = ses.x + 1 
	return tem.about(ses.ide)

#################################################################signup.html###################################################################
##Envia el formulario a signup.html, cuando recibe los datos comprueba las validaciones y si la fecha es correcta, si esto es asi 		 ##
##sobrescribe los datos d	e la base de datos almacenando los datos en example.db. Si algun validador es erroneo vuelve a enviar el formulario.## 						#
###############################################################################################################################################
        
class sign:       
    def GET(self):
      fnew = formularionuevo()
      return tem.signup(fnew,mej="")
    
    def POST(self): 
      fnew = formularionuevo()
      inc=nu=0
      
      if not fnew.validates():			###Comprobacion de errores
	nu = 1
      
      year = int(fnew.d.anio)
      day = int(fnew.d.dia)
      
      if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:		###Comprobacion de fecha/anio bisiesto
	if (fnew.d.mes == 'febrero' and day > 29):
	  inc=nu = 1
      elif (fnew.d.mes == 'febrero' and day >= 29):
	inc=nu = 1
      
      if (nu!=0):
	if(inc==1):				### Mensaje de error cuando la fecha no es correcta
	  return tem.signup(fnew,mej = "Fecha Incorrecta")
	else:
	  return tem.signup(fnew,mej = "")
      else:
	datuser.insert({
	  'nombre': fnew.d.nombre, 
	  'apellido':fnew.d.apellido, 
	  'email':fnew.d.email, 
	  'numvisa':fnew.d.nvisa, 
	  'dia':fnew.d.dia, 
	  'mes':fnew.d.mes, 
	  'anio':fnew.d.anio, 
	  'direccion':fnew.d.direccion, 
	  'contrasena':fnew.d.contrasena, 
	  'verificacion':fnew.d.verificacion, 
	  'forma':fnew.d.forma
	})
	ses.ide = fnew.d.nombre
	return tem.index(ses.ide,noticias = rss_function())
	    
#####################################################################Login.html##############################################################################
###Llama a login.html y comprueba usuario esta en la bd para poder loguearse, si lo esta entra en index.html							##
### y crea una variable de sesion con el nombre del usuario "ses.ide"												##
#############################################################################################################################################################

class register:
    def GET(self):
      f = formulario()
      if ses.ide != 0:
	return tem.index(ses.ide,noticias = rss_function())
      else:
	return tem.login(mej="")

    def POST(self):
      f = formulario()
      if not f.validates():
	return tem.login(mej)
      
      x = datuser.find({"nombre":f.d.usuario}).count()  ###Comprobamos que existen usuarios con ese nombre.
      if(x != 0):
	x = datuser.find({"nombre":f.d.usuario})
	for post in x:
	  us = post['nombre']
	  ps = post['contrasena']
	  
	if(f.d.usuario == us and f.d.passw == ps):	###Comprobamos que usuario y contrasenia corresponden.
	  ses.ide = f.d.usuario
	  return tem.index(ses.ide, noticias = rss_function())
	else:
	  return tem.login(mej = "Contrasenia incorrecta") 
      else:
	return tem.login(mej = "No estas registrado") 
	
######################################################################modidat.html############################################################################
##					Modificacion de los datos del usuario, mediante un formulario.							###
##############################################################################################################################################################

class modif:
    def GET(self):
      if ses.ide == 0:
	return tem.login(mej = "No has iniciado sesion")
      
      else:
	ses.y = ses.y + 1
	fmo = formodifica(ses.ide)
	return tem.modidat(fmo,mej = "")

    def POST(self):
      fmo = formodifica(ses.ide)
      xv = datuser.find({"nombre":ses.ide})
      for varn in xv:
	nom=varn['nombre']
	ap=varn['apellido']
	em=varn['email']
	nu=varn['numvisa']
	d=varn['dia']
	m=varn['mes']
	a=varn['anio']
	dr=varn['direccion']
	con=varn['contrasena']
	ve=varn['verificacion']
	fo=varn['forma']
      
      inc=nu=0
      if not fmo.validates():			###Comprobacion de errores
	nu = 1
      
      year = int(fmo.d.anio)
      day = int(fmo.d.dia)
      
      if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:   ###Comprobacion de fecha/anio bisiesto
	if (fmo.d.mes == 'febrero' and day > 29):
	  inc=nu = 1
      
      elif (fmo.d.mes == 'febrero' and day >= 29):
	  inc=nu = 1

      if (nu!=0):
	if(inc==1):				### Mensaje de error cuando la fecha no es correcta
	  return tem.modidat(fmo,mej = "Fecha Incorrecta")
	
	else:
	  return tem.modidat(fmo,mej = "")
      
      else:
	datuser.insert({
	  'nombre': fmo.d.nombre, 
	  'apellido':fmo.d.apellido, 
	  'email':fmo.d.email, 
	  'numvisa':fmo.d.nvisa, 
	  'dia':fmo.d.dia, 
	  'mes':fmo.d.mes, 
	  'anio':fmo.d.anio, 
	  'direccion':fmo.d.direccion, 
	  'contrasena':fmo.d.contrasena, 
	  'verificacion':fmo.d.verificacion, 
	  'forma':fmo.d.forma
	})
	ses.ide = fmo.d.nombre
	return tem.index(ses.ide,noticias = rss_function())

######################################################################data.html################################################################################
####		Muestra los datos registrados en el formulario, que estan guardados en en la bd.Y Modificacion de datos de usuario.				####
###############################################################################################################################################################
	
class show:
    def GET(self):
      if ses.ide == 0:
	return tem.login(mej = "No has iniciado sesion")
      else:
	ses.z = ses.z + 1
	x = datuser.find({"nombre":ses.ide})
	for vari in x:
	  nom=vari['nombre']
	  ap=vari['apellido']
	  em=vari['email']
	  nu=vari['numvisa']
	  d=vari['dia']
	  m=vari['mes']
	  a=vari['anio']
	  dr=vari['direccion']
	  con=vari['contrasena']
	  ve=vari['verificacion']
	  fo=vari['forma']
	return tem.data(nom,ap,em,nu,d,m,a,dr,con,ve,fo)

	
###################################################################estadistica########################################################################
####						Recopila informacion de las paginas web visitadas y las refleja en un grafico "".html			###
######################################################################################################################################################	

class estadistica:
   def GET(self):
    if ses.ide == 0:
      return tem.login(mej = "No has iniciado sesion")
    else:
      return tem.estadist(ses.v,ses.x,ses.z,ses.y,ses.e)

###################################################################mapa########################################################################
####						
###############################################################################################################################################	

class mapa:
   def GET(self):
    if ses.ide == 0:
      return tem.login(mej = "No has iniciado sesion")
    else:
      ses.e = ses.e + 1
      return tem.mapa()
      
######################################################################logout##########################################################################
####						Destruye la variable de sesion y redirige a login.html							###
######################################################################################################################################################

class logout:
    def GET(self):
        ses.kill()
        return tem.login(mej = "Adios. Hasta pronto!!")

#######################################################################hello##########################################################################
####						Error 404, si no encuentra la clase a la que se hace referencia					###
######################################################################################################################################################
        
class hello:        
    def GET(self,name):
      return "<html><title>Error 404</title><body><h1>Error 404</h1> Pagina no enconstrada</body></html>"
      
if __name__ == "__main__": 
  app.run()