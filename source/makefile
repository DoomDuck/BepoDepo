
CPPC = g++
FLAGS = -lsfml-graphics -lsfml-window -lsfml-system

run: app
	./app

app: main.o
	$(CPPC) main.o -o app $(FLAGS)

main.o: main.cpp
	$(CPPC) -c main.cpp

clear:
	rm *.o
