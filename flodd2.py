def out(screen, m, n, x, y, oldC, newC):
	if x<0 or x>= m\
	or y<0 or y>= n or\
	screen[x][y]!= oldC\
	or screen[x][y]== newC:
		return False
	return True



def flood(screen,
			m, n, x,
			y, oldC, newC):
	queue = []
	
	
	queue.append([x, y])

	
	screen[x][y] = newC

	
	while queue:
		
		
		currPixel = queue.pop()
		
		posX = currPixel[0]
		posY = currPixel[1]
		
		
		if out(screen, m, n,
				posX + 1, posY,
						oldC, newC):
			
			
			screen[posX + 1][posY] = newC
			queue.append([posX + 1, posY])
		
		if out(screen, m, n,
					posX-1, posY,
						oldC, newC):
			screen[posX-1][posY]= newC
			queue.append([posX-1, posY])
		
		if out(screen, m, n,
				posX, posY + 1,
						oldC, newC):
			screen[posX][posY + 1]= newC
			queue.append([posX, posY + 1])
		
		if out(screen, m, n,
					posX, posY-1,
						oldC, newC):
			screen[posX][posY-1]= newC
			queue.append([posX, posY-1])




screen =[
[1, 2, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 3, 1, 1, 0, 0],
[1, 0, 0, 1, 1, 0, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[1, 1, 1, 1, 1, 2, 2, 1],
	]
	

m = len(screen)


n = len(screen[0])


x = 4
y = 4
oldC = screen[x][y]

newC = 3

flood(screen, m, n, x, y, oldC, newC)



for i in range(m):
	for j in range(n):
		print(screen[i][j], end =' ')
	print()
