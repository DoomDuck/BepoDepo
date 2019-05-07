
CPPC = g++
FLAGS = -lsfml-graphics -lsfml-window -lsfml-system
BIN_FOLDER = Bin
OBJECT_FOLDER = Object
SOURCE_FOLDER = Source
FONT_FOLDER = Font

run: $(BIN_FOLDER)/app $(BIN_FOLDER)/$(FONT_FOLDER)/uwch.ttf
	env --chdir=$(BIN_FOLDER) ./app
	
$(BIN_FOLDER)/$(FONT_FOLDER):
	mkdir $(BIN_FOLDER)/$(FONT_FOLDER)

$(BIN_FOLDER)/$(FONT_FOLDER)/uwch.ttf: $(FONT_FOLDER)/uwch.ttf $(BIN_FOLDER)/$(FONT_FOLDER)
	cp $(FONT_FOLDER)/uwch.ttf $(BIN_FOLDER)/$(FONT_FOLDER)/uwch.ttf

$(BIN_FOLDER)/app: $(OBJECT_FOLDER)/main.o $(BIN_FOLDER)
	$(CPPC) $(OBJECT_FOLDER)/main.o -o $(BIN_FOLDER)/app $(FLAGS) -Wall

$(BIN_FOLDER):
	mkdir $(BIN_FOLDER)

$(OBJECT_FOLDER)/main.o: $(SOURCE_FOLDER)/main.cpp $(OBJECT_FOLDER)
	$(CPPC) -c $(SOURCE_FOLDER)/main.cpp -o $(OBJECT_FOLDER)/main.o -Wall

$(OBJECT_FOLDER):
	mkdir $(OBJECT_FOLDER)

clean:
	rm -R $(BIN_FOLDER) $(OBJECT_FOLDER) 
