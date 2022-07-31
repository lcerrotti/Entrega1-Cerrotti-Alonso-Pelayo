<em>Entrega1-   Cerrotti  Pelayo   Alonso </em>

<h1 aling="center" >Primera entrega del Proyecto Final.</em>

### Indice:

:page_facing_up:Templates:
* Inicio.
* Registro
* Registrado / Registrar Preferencias
* Preferencias Agregadas
* Buscar Preferencias
* Resutlados Preferencias
* About
* Blog Index
* Blog Post
* Blog View

:wrench:Modelos:

* Modelo de Registro
* Modelo de Preferencias
* Modelo de Blog Entry

:spiral_notepad:Formularios: 
* Formulario de Preferencias

:hammer:Funcionalidades del proyecto
* :hammer:Registrar usuarios. Tenemos la funcionalidad de guardar datos que ingresan nuestros usuarios en la Base de datos.
* :hammer:Registrar Preferecias. Tenemos la funcionalidad de guardar las preferencias ingresadas por nuestros usuarios en la Base de datos.
* :hammer:Filtrar preferencias. Tenemos la funcionalidad de revisar las preferencias de nuestros usuarios.
* :hammer:Realizar Posteos. Tenemos la funcionalidad de realizar posteos, reflejarlos en la Base de datos y mostrarlos a eleccion dentro de todo el sitio.

:abc:Orden de Prueba:
* Registro / Preferencias / Busqueda / Blog.

<br></br>
<h2 aling="center" >Templates</h2>


1) Templates / Inicio:
   
   [![Index-Nuevo.png](https://i.postimg.cc/vHVQBMdp/Index-Nuevo.png)](https://postimg.cc/GHb07WtQ)
   
   * En el index podemos encontrar un encabezado donde nos da la Bienvenida
   * Podemos encontrar una barra de navegacion que nos guiara a cada una de nuestras funcionalidades.
   * En la parte inferior de el Index se muestran los blogs que nosotros elegimos para mostrar (mas informacion en Models)
   * Dentro del encabezado existen 2 botones que nos redirigen al formulario de Registro y al About.
   
    Proximo a implementar:
   * Construir la funcionalidad para que el usuario coloque su email para que nosotros podamos contactarlo.
   <br></br>
   
2) Templates / Registro:
    
    [![Registro-Primer-formulario.png](https://i.postimg.cc/s2wBcyxT/Registro-Primer-formulario.png)](https://postimg.cc/p95XWwDj)
    
    * El template de Registro , es una extencion del Index , se agrega unicamente Un formulario y una generalizacion de las actividades que se pueden realizar.
    <br></br>
    
3) Templates / Registrado / Registrar Preferencias:
    
    [![Blog-registro-OK-Agregar-Preferencias.png](https://i.postimg.cc/YSY7rxKY/Blog-registro-OK-Agregar-Preferencias.png)](https://postimg.cc/f3zp5mbR)
    
    * El template de Registrar preferencias es la Extencion del Index y es una renderizacion de la vista registrar.
    * Se agrega una descripcion donde explicamos para que utilizamos las preferencias y por debajo un formulario para agregarlas.
    <br></br>
 
4) Templates / Preferencias Agregadas:
    
    [![Preferencias-Agregadas.png](https://i.postimg.cc/02nd3gzJ/Preferencias-Agregadas.png)](https://postimg.cc/SJXM2v7y)
    
    * El template es una extencion de Index , se agrega solamente un mensaje de Confirmacion.
    <br></br>
    
5) Templates / Buscar Preferencias:
    
    [![Busqueda-Preferencias.png](https://i.postimg.cc/WbYqgsDS/Busqueda-Preferencias.png)](https://postimg.cc/kB85d3vt)
    
    * El template es una extencion del Index , unicamente se conserva la navbar y se agrega un formulario para buscar las preferencias atravez de un Lenguaje.
    <br></br>
    
6) Templates / Resultados Preferencias:
      
      [![Resultado-Busqueda-Preferencias.png](https://i.postimg.cc/K8qYCf7N/Resultado-Busqueda-Preferencias.png)](https://postimg.cc/JsXmkb2D)
      
      * El template es una extencion del Index , unicamente se conserva la navbar y se agregan listas que muestran los resultados de la busqueda.
    
7) Templates / About:
    
    
    
    * Es un template individual , contiene una descripcion individual de cada uno de los integrantes
    * Al final del template se puede econtrar una seccion donde Estan los integrantes.
    <br></br>
    
8) Templates / Blog Index: 
    
    [![Blog-Index-Nuevo.png](https://i.postimg.cc/XYXHkNsv/Blog-Index-Nuevo.png)](https://postimg.cc/CRTsF0Ty)
    
    * Blog Index es un template Individual , contiene una navbar propia.
    * El proposito de Blog Index es resaltar un Blog de nuestra eleccion  (Mas informacion en Models) y mostrar todos los blogs creados por los usuarios.
    <br></br>
 
9) Templates / Blog Post: 
    
    [![Blog-Post.png](https://i.postimg.cc/fLMY5BMv/Blog-Post.png)](https://postimg.cc/yJrJ8hgJ)
    
    * Blog Post es un template extendido del Index, solo se conserva la nabvar.
    * Contiene un formulario para ingresar un blog completo
    * Se puede agregar un autor , contenido , imagen , asunto.
    <br></br>
    
10) Templates / Blog View:
    
    [![Blog-Publicado.png](https://i.postimg.cc/W3pJ0z7W/Blog-Publicado.png)](https://postimg.cc/XZhJbVmd)
    
    * Blog View es un template Individual.
    * Reenderiza un objeto de Blog 
    * Renderiza Autor,Contenido,Imagen y asunto.
    <br></br>
    

<br></br>
<h2 aling="center" >Modelos</h2>

 
1) Modelos / Registro_usuarios.
   
   ```Python 
   class Registro_usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre + " " + self.email
   ```
   * Nombre - Email - Contraseña - Create (Determina automaticamente la fecha de creacion del registro.)
     <br></br>
     
 2) Modelos / Preferencias_Usuario:
      
    ```Python
    class Preferencias_Usuario(models.Model):
    lenguaje = models.CharField(max_length=40)
    backOfront = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    trabajo = models.CharField(max_length=40)

    def __str__(self):
        return self.lenguaje + " " + self.backOfront + " " + self.pais + " " + self.trabajo

    class Meta():
        verbose_name = "Preferencias"
    ```
    * Lenguaje - Backend o Frontend - Pail - Trabajo. 
      <br></br>
 
 3) Modelos / Blog Entry:
      
    ```Python  
    class Entry(models.Model):

    options= (
        ('draft', 'Draft'),
        ('publicado', 'Publicado'),
    )

    options2= (
        ('si', 'Si'),
        ('no', 'No'),
    )



    nombre = models.CharField(max_length=100)
    contenido = models.TextField(max_length=1000)
    imagen = models.URLField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    publicado = models.CharField(max_length=10, choices=options, default='draft')
    muestra_inferior = models.CharField(max_length=10, choices=options2, default='no')
    muestra_superior = models.CharField(max_length=10, choices=options2, default='no')


    def __str__(self):
        return self.nombre + " - " + self.autor + " - " + str(self.fecha)
    ```
    * Nombre - Contenido - Imagen - Autor - Fecha (Se agrega de manera auto) - Publicado - Muestra Inferior (Determinamos si puede mostrarse o no debajo del index)
      Muestra superior (Determianmos si va a estar en el Header de Blog Index.)
    
    
<br></br>
<h2 aling="center" >Formularios</h2>


1) Formulario de Preferencias:
   
   ```Python
   class PreferenciasFormulario(forms.Form):

    lenguaje = forms.CharField()
    backofront = forms.CharField()
    pais = forms.CharField()
    trabajo = forms.CharField()
   ```

<br></br>
<h2 aling="center" >Funcionalidades del Proyecto</h2>

* :hammer:Registrar usuarios. Tenemos la funcionalidad de guardar datos que ingresan nuestros usuarios en la Base de datos.
   ```Python
   def registrarse(request):
    return render(request, 'registrarse.html')

   def registro(request):
    if request.method == 'POST':
        print("POST")

        #Obteniendo datos del registro (Form)
        nombre = request.POST['Usuario']
        email = request.POST['Email']
        password = request.POST['Contraseña']
        password2 = request.POST['Contraseña2']
    
        #Guardando los datos en la DB
        User_registred = Registro_usuarios(nombre=nombre, email=email, password=password)
        User_registred.save()
            
        documentoDeTexto = f"Integrante creado con exito: {nombre} {email} {password} {password2}"
        return render(request, "indexregistrado.html", {'documentoDeTexto': documentoDeTexto})
   ```
* :hammer:Registrar Preferecias. Tenemos la funcionalidad de guardar las preferencias ingresadas por nuestros usuarios en la Base de datos.
   ```Python
   def preferencias(request):
    if request.method == "POST":
        print("POST")
        #Obteniendo datos del registro (Form)
        preferenciasUsuarioForm = PreferenciasFormulario(request.POST)    
        
        if preferenciasUsuarioForm.is_valid():

            data = preferenciasUsuarioForm.cleaned_data

            #Guardando los datos en la DB
            Pref = Preferencias_Usuario(lenguaje=data["lenguaje"], backOfront=["backofront"], pais=["pais"], trabajo=["trabajo"])
            Pref.save()

        return render(request, "preferenciasenviadas.html")
   ```
* :hammer:Filtrar preferencias. Tenemos la funcionalidad de revisar las preferencias de nuestros usuarios.
   ```Python
   def buscarPreferencias(request):
    return render(request, 'buscarpreferencias.html')


   def resultadoPreferencias(request):
    if request.GET["lenguaje"]:

        lenguaje = request.GET["lenguaje"]
        preferencias = Preferencias_Usuario.objects.filter(lenguaje__icontains=lenguaje)

        return render(request, 'resultadopreferencias.html', {'preferencias': preferencias, 'lenguaje': lenguaje})
   ```
* :hammer:Realizar Posteos. Tenemos la funcionalidad de realizar posteos, reflejarlos en la Base de datos y mostrarlos a eleccion dentro de todo el sitio.
   ```Python
   class PostDetalle(DetailView):
    model = Entry
    context_object_name = 'post'
    template_name = 'GeneralPost.html'


   def NewPostSave(request):
    if request.method == 'POST':
        print("POST")
     #Obteniendo datos del registro (Form)
        nombre = request.POST['nombre']
        contenido = request.POST['contenido']
        imagen = request.POST['imagen']
        autor = request.POST['autor']
        
        #Guardando los datos en la DB
        Entrys = Entry(nombre=nombre, contenido=contenido, imagen=imagen, autor=autor)
        Entrys.save()
        
    return render(request, 'indexBase.html')


   def NewPost(request):
    return render(request, 'makeanewpost.html')


   def blog_general_index(self):

    post= Entry.objects.all()
    # post_sup= Entry.objects.filter(muestra_superior= 'si')
   

    return render(self, 'Blog_Generalindex.html', {'post': post})

   def verpost(request):
    print(request)
    return render(request, 'indexBase.html')
   ```

<br></br>
<h2 aling="center" >Orden de Prueba</h2>

Para probar todo el contenido recomendamos una secuencia que lo llevara atravez de cada funcionalidad implementada al momento.

   * Iniciamos por index. Simplemente ingresando al link http://127.0.0.1:8000/ podemos visualizar el index completo
   * Seguimos por el registro, haciendo click en el boton Registrarte
