
CPPC = g++
FLAGS = -lsfml-graphics -lsfml-window -lsfml-system

run: app
	./app

app: main.o
	$(CPPC) main.o -o app $(FLAGS) -Wall

main.o: main.cpp
	$(CPPC) -c main.cpp -Wall

clean:
	rm *.o app
