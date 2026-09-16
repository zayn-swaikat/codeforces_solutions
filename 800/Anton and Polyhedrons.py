n = int(input())
result = 0
for i in range(n):
    polyhedron = input()
    match polyhedron:
        case 'Tetrahedron':
            result += 4
        case 'Cube':
            result += 6
        case 'Octahedron':
            result += 8
        case 'Dodecahedron':
            result += 12
        case 'Icosahedron':
            result += 20
print(result)