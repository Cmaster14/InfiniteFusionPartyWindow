# InfiniteFusionPartyWindow
A Party display window for the Pokémon fangame Infinite Fusion

# Updated to work with the sprite loading using sprite sheets
Until the main devs approve of the addition of the party window modifications to the game files (which may never happen), you should also reference this repository for the version of the game code that allows the party window: https://github.com/Cmaster14/infinitefusion-hoenn-public-plus-party-window

You may be able to make changes to the game files yourself, but there are no guarantees that the files will stay untouched through hotfixes and those changes may need to be reapplied.

## About:
	
 - This is a very basic transparent party display window to be used with Pokémon Infinite Fusion. It was intended for use as an overlay item
		for any content creation needs. Some changes will need to be made to the Infinite Fusion game files to allow it to work.
  ### Vertical orientation
  ![VerticalSample](https://github.com/user-attachments/assets/0b73ed1f-2c99-4d8b-9e69-8a8540147ae1)
  ### Horizontal orientation
  ![HorizontalSample](https://github.com/user-attachments/assets/f94f86b9-b002-4dd0-ace7-217bfb823afd)
  ### Sprites moved around within the window
  ![MovedAroundSample](https://github.com/user-attachments/assets/1a459da2-6c7e-46d2-9ee5-ba3d0a83a95d)


## Setup:
 
 - Extract the [InfiniteFusionPartyWindow.zip](https://github.com/user-attachments/files/17450107/InfiniteFusionPartyWindow.zip) file to your InfiniteFusion install directory. This should be the same directory where Game.exe is located

 - Copy the files or code changes from [The Party Window fork of the Hoenn repository]( https://github.com/Cmaster14/infinitefusion-hoenn-public-plus-party-window)
	
 - If you want the window to appear in horizontal mode (3 mons on top and bottom), update the first line of InfiniteFusionPartyWindow/orientation.txt to 
       be one of ["horizontal", "h", "horiz", "side", "flat", "trios", "thicc", "small"]. If it's anything else, or nothing, the window will be vertical orientation (3 rows of 2 mons)
	
 - The party sprites should load when you load your game or when making changes to the party. Things shouldn't shift around if you're just moving party member positions without removing and adding party members
	
 - The Sprite images will be loaded into a 'PartyOffload' folder in your InfiniteFusion directory
		
		
## Usage:
  
  - Run PartyWindow.exe 
	
  - To change positioning for one of the pokemon (for overlay or other purposes): 
		- Ensure you have the Party window selected
		- Click on its button at the bottom or press number key 1-6 depending on the pokemon you want to move
		- Click and drag the image to the desired location and it will stay even through the Reload button being clicked
		- You can click the button or key again to deselect the pokemon
	
 - To reload for party changes or sprite changes:
		- Either click the Reload button or press the 'r' key
