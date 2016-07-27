from vertex import Vertex

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')

a.connect_vertex(b, 7)
b.connect_vertex(c, 10)
c.connect_vertex(d, 11)
d.connect_vertex(e, 6)
e.connect_vertex(f, 9)
f.connect_vertex(c, 2)
c.connect_vertex(a, 9)
a.connect_vertex(f, 14)
b.connect_vertex(d, 15)

alldistances = a.find_all_minimal_distances()

print('Unspecified')
for key in sorted(alldistances):
    print('Minimal distance from ', a.name, ' to ', key, ' is ', alldistances[key])

print('\n\nSpecified')
print('Minimal distance from ', a.name, ' to ', e.name, ' is ', a.find_minimal_distance_to(e))