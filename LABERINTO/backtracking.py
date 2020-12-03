from array2d import Array2D:
class LaberintoADT:
    """
    0 pasillo, 1 pared, S salida y E entrada
    pasillo es una tupla ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
    """
    
    def __init__(self, rens, cols, pasillos ): 
        self.__laberinto=Array2D(rens, cols, '1')
        for pasillo in pasillos:
            self.laberinto.set_item(pasillo[0])

    def to_string(self):
        self.__laberinto.to_string()

'''
    Establece la entrada 'E', en la matriz, verificar limites
    '''
    def set_entrada( self, ren, col ):
        #terminar la validacion de las coordenadas
        self.__laberinto.set_item( ren, col, 'E')

    '''
    Establece la salida 'S', en la matriz, verificar limites periféricos
    '''
    def set_salida( self, ren, col ):
        #terminar la validacion de las coordenadas
        self.__laberinto.set_item( ren, col, 'S')

    def es_salida( self, ren, col ):
        return self.__laberinto.get_item( ren, col ) == 'S'
    
    def buscar_entrada( self ):
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows() ):
            for columna in range(self.__laberinto.get_num_cols() ):   
                if self.__laberinto.get_item(renglon, columna) == 'E':
                    self.__camino.push( renglon, columna )
                    encontrado = True
        return encontrado

    def set_previa( self, pos_previa):
        self.__previa = pos_previa
    
    def get_preiva( self ):
        return self.__previa
    
    def resolver_laberinto( self ):
        #aplicar reglas
        pass        



#El siguiente codigo en COLAB
pasillos=((2,1))