#include <cstdlib>
#include <iostream>
#include <SFML/Graphics.hpp>

int main()
{
	// Some varibles :
	const std::string file_path =  "Font/uwch.ttf";
	sf::RenderWindow window( sf::VideoMode( 800, 640 ), "TEXT" );
	window.setVerticalSyncEnabled( true );
	window.setFramerateLimit( 60 );


	sf::Event event;

	// Todo provide adequate project structure
	sf::Font font;
	if ( !font.loadFromFile( file_path ) )
		return EXIT_FAILURE; // SFML has it's own error messages

	
	sf::String text_to_type( L"Hello I am the message you need to write" );

	sf::Text text;
	text.setString( text_to_type );
	text.setFont( font );
	text.setCharacterSize( 32 );
	text.setStyle( sf::Text::Regular );
	text.setFillColor( sf::Color::Black );
	
	// Typing variables
	std::size_t index = 0;
	int score = 0;

	// Main loop
	while ( window.isOpen() )
	{
		// Event loop
		while ( window.pollEvent( event ) )
		{
			if ( event.type == sf::Event::Closed )
				window.close();
			else if ( event.type == sf::Event::KeyPressed )
			{
				if ( event.key.code == sf::Keyboard::Key::Q && event.key.control )
					window.close();
			}
			else if ( event.type == sf::Event::TextEntered )
			{
				if ( event.text.unicode == text_to_type[ index ] )
				{
					index ++;
					std::cout << index << std::endl;
					score ++;
					sf::Vector2f pos = text.findCharacterPos( index );
					std::cout << pos.x << "," << pos.y << std::endl;
					pos *= -1.0f;
					text.setPosition( pos );
				}
				else
				{
					score --;
				}
			}
		}

		window.clear( sf::Color::White );
		window.draw( text );
		window.display();
	}

	return EXIT_SUCCESS;
}
