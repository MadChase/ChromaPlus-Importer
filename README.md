
Imports Beat Saber Chroma+ Changes based on a .dat that holds them and puts it in a difficulty.dat custom data.

 #

How to Run the skript:

-Download VSCode from here: https://code.visualstudio.com/download  

-Then Download Python form here: https://www.python.org/downloads/  

-Then download The offical Python plugin for VSCode here: https://marketplace.visualstudio.com/items?itemName=ms-python.python

# 

How to use:

NOTE: I HIGHLY suggest making a backup of you map before running any script.  

-Put the skript in the folder with your difficulty.dat and your Environment.dat file  

-Name the file with env changes "env.dat" and the diff file you want to add it to "ExpertPlusStandard.dat" or change the 2 names in the file that say "ExpertPlusStandard.dat" to your file name.  

-Then open up the folder in VSCode and hit the Run button in the top left corner while the script is open 

# 

How to Format the env.dat:

-It needs to stay in this format with "xxxxxx" representing the env changes (side note, its untested but might work with anything inside the brackets as long as its in this format):   
{
    "customData":{
             environment": [xxxxxx]
     }
}
