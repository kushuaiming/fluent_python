class Gizmo:
    def __init__(self):
        print('Gzimo id: %d' % id(self))

x = Gizmo()
y = Gizmo() * 10

print(dir())