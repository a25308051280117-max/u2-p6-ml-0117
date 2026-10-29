import pandas as pd
import numpy as np
serie_amigos=["morquecho","ian","axel","el pirata morgan","jesse","nava","mario","pedro"]
print("Series listado de amigos NC 0117")
amigos=pd.Series(serie_amigos)
print(amigos)
serie_billetes=[20,50,100,200,500,1000]
billetes=pd.Series(serie_billetes)
print("Series listado de billetes MX NC 0117")
print(billetes)
serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte","cicuenta","cien","docientos","quinientos","mil"]
print("-----Series listado de billetes MX NC 0117")
tablabilletes=pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)
# diccionario dataframe
# diccionario de valor monedas y nombre
print("datos de diccionario a dataframe en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["veinte","cicuenta","cien","docientos","quinientos","mil"]

}
tabmatias=pd.DataFrame(dic_monedas,index=["a","b","c","d","e","f"])
print(tabmatias)
print("Casa de cambio de Matias Lopez NC 0117")