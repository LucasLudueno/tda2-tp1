leafEnd = -1

# DUDAS
# es necesario splitEnd ?
# lastNewNode global ?

class Node:
  def __init__(self, start, end = None, suffixLink = None, suffixIndex = -1, isLeaf = False):
    # Represents a sufix tree node

    self.childrens = {} # TODO: ARRAY ? CHANGE NAME
    self.start = start
    self.end = end
    self.suffixIndex = suffixIndex
    self.suffixLink = suffixLink
    self.isLeaf = isLeaf

  def getEnd(self):
    if (self.isLeaf):
        return leafEnd
    return self.end


class Ukkonen:
  def __init__(self, string):
    """ Initialize Ukkonen algorithm
    
    string:     String to make the suffix tree
    root:
    activeNode: Initially it will be the Root
    ...

    """

    self.string = string

    self.root = None
    self.root = Node(start = -1, end = -1, suffixLink = self.root) # ES NECESARIO PONERLE EL SELF.ROOT ?

    self.activeNode = self.root
    self.activeEdge = -1
    self.activeLength = 0

    self.remainingSuffixCount = 0 # replace it

    self.lastNewNode = None

    """ Build suffix tree """
    self.build_suffix_tree()


  def build_suffix_tree(self):
      for pos in range(len(self.string)):
          self.extend_suffix_tree(pos)


  def walk_down(self, node):
      """ Using Skip/Count Trick, bajamos por las ramas desde el nodo actual, buscando 
          nodos hijos, mientras no se supere el activeLength.

          (APCFWD)
      """

      # TODO: SE PUEDE HACER RECURSIVO HASTA ENCONTRAR TODOS ?

      length = node.getEnd() - node.start + 1

      if (self.activeLength < length):
        return False

      self.activeEdge += length
      self.activeLength -= length
      self.activeNode = node
      return True





  def extend_suffix_tree(self, pos):
    global leafEnd
    """Extension Rule 1, this takes care of extending all leaves created so far in tree"""
    leafEnd = pos

    """Increment remainingSuffixCount indicating that a new suffix added to the list of suffixes yet to be added in tree"""
    self.remainingSuffixCount += 1 # ???

    """lastNewNode to None while starting a new phase, indicating there is no internal node waiting for it's suffix link reset in current phase"""
    self.lastNewNode = None # ???


    # Add sufix to all RAMAS
    while (self.remainingSuffixCount > 0):

      if (self.activeLength == 0):
        # When activeLength is 0, that means there is no walk down needed here
        # so the activeEdge is setted to the current position
        self.activeEdge = pos # APCFALZ
      
      newNode = self.string[self.activeEdge]
      #  There is no outgoing edge starting with activeEdge from activeNode
      if (self.activeNode.childrens.get(newNode) is None):
        # Extension Rule 2: New leaf has been created

        self.activeNode.childrens[newNode] = Node(start = pos, end = leafEnd, suffixLink = self.root, isLeaf = True) # TODO: CHECKEAR SI ESTAN BIEN PASADOS LOS PARAMETROS

        """A new leaf edge is created in above line starting
        from  an existng node (the current activeNode), and
        if there is any internal node waiting for it's suffix
        link get reset, point the suffix link from that last
        internal node to current activeNode. Then set lastNewNode
        to None indicating no more node waiting for suffix link
        reset."""
        if (self.lastNewNode is not None): # NO ENTENDI
            self.lastNewNode.suffixLink = self.activeNode
            self.lastNewNode = None

        # There is an outgoing edge starting with activeEdge from activeNode
      else:
        # Get the next node at the end of edge starting with activeEdge
        nextNode = self.activeNode.childrens.get(self.string[self.activeEdge])

        """ Skip/Count Trick """
        if self.walk_down(nextNode):  # Do walkdown
          # Start from next node (the new activeNode)
          continue

        """ Extension Rule 3 (el caracter ya existe en la arista)"""
        if (self.string[nextNode.start + self.activeLength] == self.string[pos]):
            # If a newly created node waiting for it's
            # suffix link to be set, then set suffix link
            # of that waiting node to curent. active node --- NO ENTENDI
            if((self.lastNewNode is not None) and (self.activeNode != self.root)):
                self.lastNewNode.suffixLink = self.activeNode
                self.lastNewNode = None

            # APCFER3
            self.activeLength += 1
            """ STOP phase and start adding the next position """
            break


        """ Extension Rule 2 (el caracter no esta en la arista)"""
        # Se crea una nueva arista con una hoja
        # y se divide la que estaba

        newNodeStart = nextNode.start
        newNodeEnd = nextNode.start + self.activeLength - 1

        # New internal node (Override actual internal node ?)

        splitNode = Node(start = newNodeStart, end = newNodeEnd, suffixLink = self.root)
        self.activeNode.childrens[self.string[self.activeEdge]] = splitNode

        # New leaf coming out of new internal node
        splitNode.childrens[self.string[pos]] = Node(start = pos, end = leafEnd, suffixLink = self.root, isLeaf = True)


        nextNode.start += self.activeLength
        splitNode.childrens[self.string[nextNode.start]] = nextNode



        """We got a new internal node here. If there is any
          internal node created in last extensions of same
          phase which is still waiting for it's suffix link
          reset, do it now."""
        if (self.lastNewNode is not None):
            # suffixLink of lastNewNode points to current newly
            # created internal node
            self.lastNewNode.suffixLink = splitNode
        """Make the current newly created internal node waiting
          for it's suffix link reset (which is pointing to self.root
          at present). If we come across any other internal node
          (existing or newly created) in next extension of same
          phase, when a new leaf edge gets added (i.e. when
          Extension Rule 2 applies is any of the next extension
          of same phase) at that point, suffixLink of this node
          will point to that internal node."""
        self.lastNewNode = splitNode # NO ENTENDI NADA

      """One suffix got added in tree, decrement the count of suffixes yet to be added."""
      self.remainingSuffixCount -= 1
      if ((self.activeNode == self.root) and (self.activeLength > 0)):  # APCFER2C1
        self.activeLength -= 1
        self.activeEdge = pos - self.remainingSuffixCount + 1
      elif (self.activeNode != self.root):  # APCFER2C2
        self.activeNode = self.activeNode.suffixLink


  def match_sub_string(self, substr, actualNode):
    start, end = actualNode.start, actualNode.getEnd()

    actualNodeString = self.string[start: end + 1]
    stringToMatch = substr[:len(actualNodeString)]

    if (stringToMatch != actualNodeString):
        return False

    substr = substr[len(actualNodeString):]

    if (substr == ''):
        return True

    for node in actualNode.childrens.values(): # TODO: WHAT ABOUT SUFFIX LINKS ??
        if node:
            result = self.match_sub_string(substr, node)
            if (result):
              return True
    return False

  def match(self, p):
    return self.match_sub_string(p, self.root)
