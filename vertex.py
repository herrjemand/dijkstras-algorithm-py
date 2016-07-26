
class Vertex():
    def __init__(self, name):
        self.name     = name
        self.vertexes = {}

    def connect_vertex(self, vertex, distance, *args, update=False):
        assert self.vertexes.get(vertex.name, None) == None

        self.vertexes[vertex.name] = {
            'vertex'   : vertex,
            'distance' : distance
        }

        if not update:
            vertex.connect_vertex(self, distance, update=True)

    def disconnect_vertex(self, vertex):
        self.vertexes[vertex.name] != None

    def __str__(self):
        vertexes = ''
        for index in self.vertexes:
            vertex = self.vertexes[index]
            spacing = ' ' * (len(self.name) + 2)
            vertexes += '\n{spacing}-- {distance} --> ({name})'.format(spacing=spacing, distance=vertex['distance'], name=vertex['vertex'].name)

        string = '({name}){vertexes}'.format(name=self.name,vertexes=vertexes)

        return string