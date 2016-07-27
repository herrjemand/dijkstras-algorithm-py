##########################################################
#                                                        #
# Vertex - implements simple, non-negative graphs vertex #
#                                                        #
##########################################################
class Vertex():
    def __init__(self, name):
        self.name     = name
        self.vertexes = {}

    def connect_vertex(self, vertex, distance, *args, update=False):
        """Connectes two vertexes together"""
        assert self.vertexes.get(vertex.name, None) == None

        self.vertexes[vertex.name] = {
            'vertex'   : vertex,
            'distance' : distance
        }

        if not update:
            vertex.connect_vertex(self, distance, update=True)

    def get_distance(self, name):
        """Returns vertex specified by name """
        return self.vertexes[name]['distance']

    def get_vertexes(self):
        """Returns list of vertexes and their distance"""
        vertexes = {}
        for key in self.vertexes:
            vertexes[key] = self.vertexes[key]['distance']

        return vertexes
        

    def disconnect_vertexes(self, vertex, *args, update=False):
        """Disconnect two vertexes"""
        if not update:
            self.vertexes[vertexes.name]['vertex'].disconnect_vertexes(self, update=True)

        self.vertexes[vertex.name] = None

    def __str__(self):
        """Returns string representation of the vertex and its connections"""
        vertexes = ''
        for index in self.vertexes:
            vertex = self.vertexes[index]
            spacing = ' ' * (len(self.name) + 2)
            vertexes += '\n{spacing}-- {distance} --> ({name})'.format(spacing=spacing, distance=vertex['distance'], name=vertex['vertex'].name)

        string = '({name}){vertexes}\n'.format(name=self.name,vertexes=vertexes)

        return string

    def __repr__(self):
        return self.__str__()