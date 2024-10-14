# InfiniteFusionPartyWindow
A Party display window for the Pokémon fangame Infinite Fusion

About:
	-This is a very basic party display to be used with Pokémon Infinite Fusion. It was intended for use as an overlay item
		for any content creation needs. Some changes will be made to the Infinite Fusion game files to allow it to work.


Setup:
 -You'll need to make some changes to the Scripts that run Infinite Fusion from the InfiniteFusion\Data\Scripts directory
		See WhatToChangeForPartyWindow.txt for the code changes, and complete those before trying to run PartyWindow
	
 -If you want the window to appear in horizontal mode (3 mons on top and bottom), update the first line of orientation.txt to 
       be one of ["horizontal", "h", "horiz", "side", "flat", "trios", "thicc", "small"]
	        If it's anything else, or nothing, the window will be vertical orientation (3 rows of 2 mons)
	
 -To load the party that will be displayed, you'll need to open up your party menu in Infinite Fusion.
	
 -To load any alternate sprites, you will need to see that sprite load in game. 
		That can be easily done by scrolling through summary screens for example
		
		
Usage:
	-Run PartyWindow.exe 
	
  -To change positioning for one of the pokemon (for overlay or other purposes): 
		-Ensure you have the Party window selected
		-Click on its button at the bottom or press number key 1-6 depending on the pokemon you want to move
		-Click and drag the image to the desired location and it will stay even through the Reload button being clicked
		-You can click the button or key again to deselect the pokemon
	
 -To reload for party changes or sprite changes:
		-Either click the Reload button or press the 'r' key
		
		
 -The sprites_path file will continue to fill up as you play and see sprites
		It condenses to just your party's sprite paths when you start Party Window or hit Reload
