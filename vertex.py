##########################################################
#                                                        #
# Vertex - implements simple, non-negative graphs vertex #
#                                                        #
##########################################################
class Vertex():
    def __init__(self, name):
        self.name          = name
        self.vertexes      = {}
        self.min_distances = {}

    def connect_vertex(self, vertex, distance, *args, update=False):
        """Connectes two vertexes together"""
        assert self.vertexes.get(vertex.name, None) == None

        self.vertexes[vertex.name] = {
            'vertex'   : vertex,
            'distance' : distance
        }

        if not update:
            vertex.connect_vertex(self, distance, update=True)

    def get_distance(self, vertex):
        """Returns distance for specified vertex"""
        return self.vertexes[vertex.name]['distance']

    def get_distances(self):
        """Returns list of vertexes and their distance"""
        vertexes = {}
        for key in self.vertexes:
            vertexes[key] = self.vertexes[key]['distance']

        return vertexes
        
    def get_minimal_distance(self, vertex):
        """Returns minimal distance for specified vertex"""
        return self.min_distances.get(vertex.name, float('inf'))

    def set_minimal_distance(self, vertex, distance):
        """Sets minimal distance for specified vertex"""
        self.min_distances[vertex.name] = distance

    def get_minimal_distances(self):
        """Returns minimal distances"""
        return self.min_distances

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