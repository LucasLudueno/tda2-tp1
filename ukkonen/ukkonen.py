LEAF_END = -1 # Indica la posicion final de las hojas. Ya que es unica, es una variable global.

class Node:
    """ Nodo de un Arbol de sufijos.

    Contiene:
      - Sus nodos hijos
      - Las posiciones inciales y finales del String S.
      - Los suffix index y link
      - Si es o no una hoja
    """

    def __init__(self, start, end = None, suffix_link = None, suffix_index = -1, is_leaf = False):
        self.childrens = {}
        self.start = start
        self.end = end
        self.suffix_index = suffix_index
        self.suffix_link = suffix_link
        self.is_leaf = is_leaf

    def get_end(self):
        """ Devuelve la posicion final del nodo y si es una hoja, LEAF_END """
        if self.is_leaf:
            return LEAF_END
        return self.end


class Ukkonen:
    def __init__(self, string):
        """ Algoritmo de Ukkonen

        string (S): String a partir del cual se fabrica el arbol de sufijos
        root:       Nodo padre del arbol
        active_node: Active Node utilizado por el algoritmo (inicialmente el root)
        active_edge: La rama del active node (indica la posicion del caracter de S)
        active_length: La longitud a la cual se encuentra el caracter desde el active node,
                      por la rama active edge

        remaining_suffix_count: Indica si debe seguir iterandose o no por las extensiones dentro de una fase.

        last_new_node: Indica el nodo que debera linkear cuando se deba producir el link
        """

        self.string = string

        self.root = None
        self.root = Node(start = -1, end = -1, suffix_link = self.root)

        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0

        self.remaining_suffix_count = 0 # replace it

        self.last_new_node = None

        """ Build suffix tree """
        self.build_suffix_tree()


    def build_suffix_tree(self):
        """ Build suffix tree """
        for pos in range(len(self.string)):
            self.extend_suffix_tree(pos)


    def walk_down(self, node):
        """
        Skip/Count Trick (APCFWD)

        Bajamos por la rama del nodo actual hacia el proximo nodo hijo.
        En caso de encontrar en la rama, la posicion del string buscada, se
        devuelve False. En caso de no encontrarla, se setea al nodo actual como
        active_node y se devuelve True.
        """

        # Improvement: realizar el walk_down iterativo hasta encontrar el nodo buscado

        length = node.get_end() - node.start + 1

        if self.active_length < length:
            return False

        self.active_edge += length
        self.active_length -= length
        self.active_node = node
        return True


    def extend_suffix_tree(self, pos):
        """
        Extend suffix tree, extiende el caracter en la posicion pos de S al arbol
        de sufijos.
        Cada llamada al mismo, representa el inicio de una nueva fase
        """

        global LEAF_END

        # Extension Rule 1: Asigna al LEAF_END la posicion actual del S dado que las hojas tendran
        # ese valor al finalizar la fase
        LEAF_END = pos

        # Incrementa remaining_suffix_count indicando el comienzo de una nueva fase
        self.remaining_suffix_count += 1

        # last_new_node se asigna como None al iniciar la fase, indicand que no habra
        # un nodo interno esperando por un suffix link
        self.last_new_node = None

        # Comienzan las extensiones de la fase
        while self.remaining_suffix_count > 0:

            if self.active_length == 0:
                # Cuando active_length es 0, significa que no se producira un walk_down,
                # por lo tanto se lo setea con la posicion actual
                self.active_edge = pos  # APCFALZ

            # nuevo nodo, en base a la posicion actual o al active edge de la extension anterior
            actualCharacter = self.string[self.active_edge]

            if self.active_node.childrens.get(actualCharacter) is None:
                # Extension Rule 2: Si no existe una arista que contenga al nuevo nodo, a partir del
                # actual entonces hay que crearlo como hoja (al inicio el active_node sera el root)

                newNode = Node(start = pos, end = LEAF_END, suffix_link = self.root, is_leaf = True)
                self.active_node.childrens[actualCharacter] = newNode

                # Una vez agregada la hoja al actual active node, en caso de que no exista un nodo
                # interno esperando a realizar un suffix link al nodo actual, se realiza el enlace
                # y se setea el last new node en None, indicando que no hay otro esperando a linkear
                if self.last_new_node is not None:
                    self.last_new_node.suffix_link = self.active_node
                    self.last_new_node = None

            else:
                # Llegamos aca ya que uno de los hijos del active node, posee una rama que comienza
                # con el caracter actual, por lo tanto tendremos que recorrer el arbol a partir de
                # esta rama.
                next_node = self.active_node.childrens.get(actualCharacter)

                """ Skip/Count Trick """
                if self.walk_down(next_node):
                    # En caso de que se pueda bajar por otro nodo, el mismo quedara seteado como
                    # active node y se continuara el proceso desde el mismo
                    continue

                """ Extension Rule 3: El caracter ya existe en la arista """
                if self.string[next_node.start + self.active_length] == self.string[pos]:
                    # En el caso de que un nodo este esperando para realizar un suffix link,
                    # se linkea al mismo con el nodo actual
                    if (self.last_new_node is not None) and (self.active_node != self.root):
                        self.last_new_node.suffix_link = self.active_node
                        self.last_new_node = None

                    # Stop phase trick (APCFER3)
                    # Por el truco mencionado, se corta la fase y se comienza desde la siguiente,
                    # quedando el active node seteado como el nodo actual
                    self.active_length += 1
                    break

                """ Extension Rule 2: el caracter no esta en la arista """
                # En el caso en que se haya producido el walk down sobre las ramas el arbol todo
                # lo posible, y no se haya encontrado el caracter, entonces se procede a
                # realizar un split de la rama actual, agregando el caracter como una hoja y el
                # resto del string sobre otra

                new_node_start = next_node.start
                new_node_end = next_node.start + self.active_length - 1

                # Split node del nodo actual (pisamos el que estaba). Pasa a ser un nodo interno
                split_node = Node(start = new_node_start, end = new_node_end, suffix_link = self.root)
                self.active_node.childrens[actualCharacter] = split_node

                # Nueva hoja desde el split node
                split_node.childrens[self.string[pos]] = Node(start = pos, end = LEAF_END, suffix_link = self.root, is_leaf = True)

                # Agregamos la otra rama desde el split node
                next_node.start += self.active_length
                split_node.childrens[self.string[next_node.start]] = next_node


                # A esta instancia, tenemos un nuevo nodo interno.
                if self.last_new_node is not None:
                    # En el caso de que exista otro nodo interno esperando para
                    # realizar un suffix link, se linkea al mismo
                    self.last_new_node.suffix_link = split_node

                # Ahora hacemos que el nodo creado quede como nodo interno esperando
                # a realizar un suffix link de otra extension.
                # En la proxima extension entonces (de la misma fase), cuando se agregue
                # la proxima hoja (o sea cuando se cumpla la regla 2 sobre la proxima
                # extension) se producira un link entre el internal node siguiente y el
                # actual
                self.last_new_node = split_node

            # A esta instancia, el caracter (sufijo) fue aniadido al arbol.
            # Decrementamos la cantidad de sufijos a agregar
            self.remaining_suffix_count -= 1
            if (self.active_node == self.root) and (self.active_length > 0): # APCFER2C1
                self.active_length -= 1
                self.active_edge = pos - self.remaining_suffix_count + 1
            elif self.active_node != self.root:  # APCFER2C2
                self.active_node = self.active_node.suffix_link


    def match_sub_string(self, substr, actual_node):
        """ Llamada recursiva para matchear el sub string buscado """
        start, end = actual_node.start, actual_node.get_end()

        actual_node_string = self.string[start: end + 1]
        string_to_match = substr[:len(actual_node_string)]

        if string_to_match != actual_node_string:
            return False

        substr = substr[len(actual_node_string):]

        if substr == '':
            return True

        for node in actual_node.childrens.values():
            if node:
                result = self.match_sub_string(substr, node)
                if result:
                    return True
        return False


    def match(self, patron):
        """ Busca que el patron exista en el String S """
        return self.match_sub_string(patron, self.root)
