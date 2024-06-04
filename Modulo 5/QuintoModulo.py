# =====================================================================================================
# 🔶 ¿Que es el Machine Learning?
# =====================================================================================================
"""
    El machine learning es una disciplina cientifica del ambito de la inteligencia artificial (IA) que
    crea sistemas que aprenden automaticamente. Aprender, en este contexto, quiere decir identificar
    patrones complejos en millones de datos. La maquina que realmente aprende es un algoritmo que revisa
    los datos y es capaz de predecir comportamientos futuros. Ademas, implica que estos sistemas se
    mejoren de forma automatica con el tiempo (sin intervencion humana)
"""
# =====================================================================================================
# 🔶 Beneficios del Machine Learning.
# =====================================================================================================
"""
    El Machine Learning nos ofrece las siguientes ventajas:
    - Mayor conocimiento de las necesidades, gustos y habitos de compra de los clientes.
    - Innovacion en productos y soluciones tecnologicas.
    - Optimizacion de la produccion y de la productividad.
    - Capacidad de realizar acciones preventivas y correctivas.
    - Prediccion de tendencias y necesidades.
"""
# =====================================================================================================
# 🔶 Tipos de aprendizajes dentro del Machine Learning
# =====================================================================================================
"""
    En el Machine Learning existen 3 tipos de aprendizajes
    - Supervised learning.
    - Unsupervised learning.
    - Reinforcement learning.
"""
# =====================================================================================================
# 🔶 Aprendizaje Supervisado.
# =====================================================================================================
"""
    En el aprendizaje supervisado, los modelos son entrenados utilizando ejemplos etiquetados como una
    entrada donde se conoce el resultado deseado. El mismo recibe un conjunto de entradas junto con los
    resultados correctos correspondientes, y el algoritmo aprende comparando su resultado real con
    resultados correctos para encontrar errores. Luego modifica el modelo en consecuencia, es decir, la
    salida de este algoritmo es conocida.
    Este aprendizaje resuelve problemas de:
    - Clasificacion (Predecir la clase mas probable de un elemento en funcion de un conjunto de variables
                    de entrada. La respuesta va a ser una variable categorica)
    - Regresion     (Predecir valores numericos, es decir, la respuesta es de tipo cuantitativo)

    Los algoritmos mas utilizados son los siguientes:
    - Arboles de decision.
    - KNN.
    - Support Vectorial Machine (SVM).
    - Regresion logistica.
    - Modelos de regresion lineal.
    - Random forest.
    - Entre otros.
"""
# =====================================================================================================
# 🔶 Aprendizaje no Supervisado.
# =====================================================================================================
"""
    El aprendizaje no supervisado, se utiliza contra datos que no tienen etiquetas historicas. No se da
    la respuesta correcta al sistema. El objetivo es explorar los datos y encontrar alguna estructura en
    su interior. Por ejemplo: Identificar segmentos de clientes con atributos similares que despues
    puedan ser tratados de manera semejante en companias de marketing o bien puede encontrar los
    atributos principales que separan los segmentos de clientes.

    Los algoritmos mas utilizados son los siguientes:
    - Clustering o Agrupacion.
    - Reglas de asociacion.
"""
# =====================================================================================================
# 🔶 Clustering o Agrupacion.
# =====================================================================================================
"""
    Las tecnicas de Clustering, o de agrupacion, tienen como principal funcion: Encontrar una estructura
    o un patron en una coleccion de datos no clasificados. Esto significa que, se busca:
    - Las observaciones dentro de un cluster sean similares entre si.
    - Las observaciones entre clusters sean los mas distintas posibles.

    IMPORTANTE: Los algoritmos de Clustering siempre buscan una forma natural de agrupar los datos.
"""
# =====================================================================================================
# 🔶 Reglas de asociacion.
# =====================================================================================================
"""
    Estas refieren a la identificacion de los objetos que se encuentran juntos en un evento o registro
    dado. Tambien se conoce como analisis de canasta de mercado, por su aplicacion en el analisis de
    patrones en las compras de los supermercados.
    Las interpretaciones de las reglas se expresan como "si el articulo A es parte de la transaccion X,
    entonces el articulo B es tambien parte de la transaccion X"

    IMPORTANTE: Las reglas deben ser interpretadas como una asociacion entre dos o mas elementos.
"""
# =====================================================================================================
# 🔶 Disciplina asociadas al Data Scientist.
# =====================================================================================================
"""
    - Big Data: Es la discilina mas relevante ya que a partir de ella conseguimos los datos que luego
    utilizariamos para nuestros modelos. Esta asociada a grandes cantidades y volumenes de datos, donde
    esa gran cantidad de datos que gestionamos son diversos.
    Cloud: La gran mayoria de los servicios que vamos a deployar, corren en la nube.

    - DevOps: Es una disciplina mas orientada a MLOps, es decir, como automatizar los deployments
    constantes de modelos (posiblemente a traves de algun servicio Cloud)

    - Reading intelligents

    - Data mining

    - Inteligencia artificial (IA)

    - Deep Learning
"""
# =====================================================================================================
# 🔶 Actividad propuesta.
# =====================================================================================================
"""
    En el aprendizaje supervisado, la salida es conocida:
    ✅  Verdadero. 
    ❌  Falso.

    No hace falta importar la libreria Scikit-learn para utilizarla:
    ❌ Verdadero.
    ✅ Falso.

    Scikit-learn es una libreria principalmente utilizada para:
    ❌ Analisis estadistico de datos.
    ❌ Limpieza y transformacion.
    ❌ Integracion con bases de datos.
    ✅ Machine Learning (ML).

    "Peugeot 208" es un ejemplo de ...:
    ❌ Caja blanca.
    ❌ Hibrido.
    ✅ Caja negra.
    ❌ Ninguna de las anteriores es correcta.
"""