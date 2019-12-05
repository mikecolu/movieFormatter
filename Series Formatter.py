import os

while(1):
    dirPath = input( "Specify Path: " )
    title = input( "Series Title: " )
    season = int( input( "Season Number: " ) )
    starting_episode = int( input( "Starts with episode number: ") )

    supported_types = ( '.avi', '.mkv', '.mp4' )

    print( "Directory: " + dirPath )

    episode = starting_episode

    for root, dirs, files in os.walk( dirPath ):
        for file in files:
            old_file = os.path.join( root, file )
            print( "File Name: " + file )

            extension = os.path.splitext(file)[1]
            if any( extension in type for type in supported_types ):
                modified_name = title + " "
                modified_name += ( "S0" if season < 10 else "S" ) + str( season )
                modified_name += ( "E0" if episode < 10 else "E" ) + str( episode )
                modified_name += extension

                new_file = os.path.join( root, modified_name )
                print( "New File Name: " + modified_name + "\n" )

                os.rename( old_file, new_file )

                episode += 1
            else:
                print( "[" + extension + "] is not supported!\n" )
