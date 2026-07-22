import sys

scores = []
for i in sys.argv[1:]: ## bucle convertir los argumento en int
	try:  
		scores.append(int(i)) ## int(i) son cada argumento ya que sys.argv[i] es una lista
	except ValueError:
		print(f"Invalid parameter: {i}")

print(sum(scores))
print(len(scores))
