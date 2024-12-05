from nodo import Nodo

class ArbolBinario():
    def __init__(self):
        self.__raiz=None

    def getRaiz(self):
        return self.__raiz
    
    def setRaiz(self,raiz):
        self.__raiz=raiz

    def insertarNodo(self,dato,raiz):#Se van a insertar todos los nodos sin importar si es o no raiz
        #Verificar si la raiz existe o no
        if (raiz==None):
            #Significa que el nodo a insertar el nodo es el primero del arbol o del sub-arbol
            nodo=Nodo(dato)#Crea el nodo con ese dato con 2 hijos nulos
            self.setRaiz(nodo)#Actualizar la raiz con el nuevo nodo creado
            print("Nodo insertado es {} y se agrego con éxito".format(nodo.getDato()))
            #Como es el caso base entonses aqui se rompe
            return
        else:#validar si el dato es < o > a la raiz
            if (raiz.getDato() >= dato):
                #Izquierda
                if (raiz.getIzq() == None):#Si la izquierda es nulo, que lo inserte alli
                    nodo=Nodo(dato)#Creo el nodo con su dato para insertarlo a la izq
                    raiz.setIzq(nodo)
                    nodo.setPadre(raiz)
                    print("Nodo insertado es {} y se agrego con éxito".format(nodo.getDato()))
                    return
                else:#si no es nulo
                    #hago llamado recursivo para que empiece desde arriba
                    self.insertarNodo(dato, raiz.getIzq())

            else:
                #der
                if (raiz.getDer() == None):#Si la derecha es nulo, que lo inserte alli
                    nodo=Nodo(dato)#Creo el nodo con su dato para insertarlo a la der
                    raiz.setDer(nodo)
                    nodo.setPadre(raiz)
                    print("Nodo insertado es {} y se agrego con éxito".format(nodo.getDato()))
                    return
                else:
                    self.insertarNodo(dato,raiz.getDer())


    def recorrerInOrden(self, raiz):
        if raiz != None:
            self.recorrerInOrden(raiz.getIzq())
            print(str(raiz.getDato())+"-> ")#Aqui si nos piden promedios y acumulados se deben hacer
            self.recorrerInOrden(raiz.getDer())

        else:
            return #Caso base

    def recorrerPreorden(self, raiz):
        if raiz != None:
            print(str(raiz.getDato())+" -> ")#Aqui si nos piden promedios y acumulados se deben hacer
            self.recorrerInOrden(raiz.getIzq())
            self.recorrerInOrden(raiz.getDer())
            
        else:
            return #Caso base
        
    def recorrerPostOrden(self, raiz):
        if raiz != None:
            self.recorrerInOrden(raiz.getIzq())
            self.recorrerInOrden(raiz.getDer())
            print(str(raiz.getDato())+" -> ")#Aqui si nos piden promedios y acumulados se deben hacer
        else:
            return #Caso base
        
    def buscarNodo(self,dato,raiz):
        nodoBuscar=None
        if (raiz != None):#Caso base
            if (raiz.getDato() == dato):
                print("Encontramos el dato {} en el arbol".format(dato))
                nodoBuscar=raiz
                return nodoBuscar
            else:
                if (raiz.getDato() >= dato):
                    #izq
                    self.buscarNodo(dato, raiz.getIzq())
                else:
                    #der
                    self.buscarNodo(dato, raiz.getDer())

        else:
            print("El dato {} NO se encontró en el arbol".format(dato))
            return nodoBuscar
        

    def eliminarNodo(self, dato, raiz):
        if(raiz != None):
            if(raiz.getDato() == dato):
                print("El dato {} se encontró en el árbol".format(dato))
                nodoEliminar = raiz
                if(nodoEliminar != None):
                    if(nodoEliminar.getIzq() == None and nodoEliminar.getDer() == None):
                        #eliminarHoja
                        if(nodoEliminar.getPadre().getDato() >= nodoEliminar.getDato()):
                            #izq
                            nodoEliminar.getPadre().setIzq(None)
                            print("El dato {} se eliminó del árbol".format(nodoEliminar.getDato()))
                        else:
                            #der
                            nodoEliminar.getPadre().setDer(None)
                            print("El dato {} se eliminó del árbol".format(nodoEliminar.getDato()))
                    else:
                        #eliminarRama
                        print("El Nodo a eliminar no es una hoja")
            else:
                if(raiz.getDato() >= dato):
                    #izq
                    self.eliminarNodo(dato, raiz.getIzq())
                else:
                    #der
                    self.eliminarNodo(dato, raiz.getDer())
        else:
            print("El dato {} NO se encontró en el árbol".format(dato))
            return None