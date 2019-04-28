#include <cstdlib>
#include <iostream>
#include <SFML/Graphics.hpp>

inline bool isValidKeyStroke( sf::Uint32 encoding )
{
  return 20 <= encoding;
}

int main()
{
	// Some varibles :
	const std::string file_path =  "../fonts/uwch.ttf";
	sf::RenderWindow window( sf::VideoMode( 800, 640 ), "TEXT" );
	window.setVerticalSyncEnabled( true );
	window.setFramerateLimit( 60 );


	sf::Event event;

	// Todo provide adequate project structure
	sf::Font font;
	if ( !font.loadFromFile( file_path ) )
    return EXIT_FAILURE; // SFML has it's own error messages



	sf::String msg( "" );

	sf::Text text;
	text.setString( msg );
	text.setFont( font );
	text.setCharacterSize( 32 );
	text.setStyle( sf::Text::Regular );
	text.setFillColor( sf::Color::Black );

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
				else if ( event.key.code == sf::Keyboard::Key::BackSpace )
				{
					static std::size_t length;
					if ( ( length = msg.getSize() ) > 0 )
					{
						msg.erase( length - 1 ); // Erase last char
						text.setString( msg );
					}
				}
			}
			else if ( event.type == sf::Event::TextEntered )
			{
				if ( isValidKeyStroke( event.text.unicode ) )
				{
					msg += event.text.unicode;
					text.setString( msg );
				}
			}
		}

		window.clear( sf::Color::White );
		window.draw( text );
		window.display();
	}

	return EXIT_SUCCESS;
}

// Code example :
// int main()
// {
//
//     sf::RenderWindow window(sf::VideoMode(200, 200), "SFML works!");
//     sf::CircleShape shape(100.f);
//     shape.setFillColor(sf::Color::Green);
//
//     while (window.isOpen())
//     {
//         sf::Event event;
//         while (window.pollEvent(event))
//         {
//             if (event.type == sf::Event::Closed)
//                 window.close();
//         }
//
//         window.clear();
//         window.draw(shape);
//         window.display();
//     }
//
//     return 0;
// }
