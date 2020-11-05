def dijkstra(matrix):
    source = int(input("\nInserisci il nodo sorgente: "))
    usati = {"nodi": [], "pesi": [], "precedente": []}
    dist = [100000000 for _ in range(0, len(matrix))]
    dist[source] = 0
    successori = [i for i in range(0, len(matrix))]
    prec = source
    while len(successori) > 0:
        u = min(dist)
        nodo = successori.pop(dist.index(u))
        dist.remove(u)
        usati["nodi"].append(nodo)
        usati["pesi"].append(u)
        usati["precedente"].append(prec)
        for nodiVicini in matrix[nodo]:
            if nodiVicini > 0 and matrix[nodo].index(nodiVicini) in successori:
                # matrix[nodo].index(nodiVicini) --> posizione nella matrice
                # successori.index(matrix[nodo].index(nodiVicini)) --> posizione nodo in successori
                # nodiVicini + u --> nuova distanza
                if nodiVicini + u < dist[successori.index(matrix[nodo].index(nodiVicini))]:
                    dist[successori.index(matrix[nodo].index(nodiVicini))] = nodiVicini + u
            matrix[nodo][matrix[nodo].index(nodiVicini)] = 0
        prec = nodo
    return usati