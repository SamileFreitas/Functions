#recebe como entrada a localização atual do usuário (x,y)
x = 10
y = 8
#lista de localização dos taxis disponiveis
taxisx = [21,40,35,17,-42,82,60,-1,-15,25,29,0]
taxisy = [25,30,-1,45,-20,60,0,26,-10,52,36,-1]
#d((xi, yi),(xj , yj ) = p(xi − xj )2 + (yi − yj )2 formula de baskara
dist_min = (taxisx[0] - x)**2 + (taxisy[0] - y)**2
#deifinir a distancia mais proxima
dist_mais_prox = 0

for i in range(len(taxisx)):
    distancia = (taxisx[i] - x)**2 + (taxisy[i] - y)**2
    if distancia < dist_min:
        dist_min = distancia
        dist_mais_prox = i

print(dist_mais_prox)

input('Pressione ENTER para sair')