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
        self.visited       = False

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

    def find_all_minimal_distances(self):
        """Finds minimal distance to all points on the graph
           using Dijkstra's algorithm"""
        origin = current_vertex = self
        current_distance = 0
        while True:
            closest      = float('inf')
            closest_next = None
            finished = True

            for key in current_vertex.vertexes:
                vertex   = current_vertex.vertexes[key]['vertex']

                if not vertex.visited:
                    distance = current_vertex.vertexes[key]['distance']

                    if distance < closest:
                        closest      = distance
                        closest_next = vertex

                    # print('Min from ', origin.name, ' to ', vertex.name, ' ', current_distance + distance)
                    if current_distance + distance < origin.get_minimal_distance(vertex):
                        origin.set_minimal_distance(vertex, current_distance + distance)

                    finished = False

            if finished:
                break

            current_vertex.visited = True
            current_distance = origin.get_minimal_distance(closest_next)
            current_vertex = closest_next
            # print('Changing to ', closest_next.name)

        return self.get_minimal_distances()

    def find_minimal_distance_to(self, vertex):
        """Finds minimal distance to the point"""
        return self.find_all_minimal_distances().get(vertex.name, float('inf'))