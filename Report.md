Exercise 1:

The max_bright value was 55,000 and the min_bright was 37,000.

Exercise 2:

Updated exercise_sound.py to play twinkle twinkle little star

Exercise 3:

Some of the changes we made to exercise_game.py include adding a scoring function, connecting the Pi Pico to the internet, and finally posting the json file to a firestone data base. Focusing in on the aspect that uploads the json to the cloud server, we first needed to connect the Pi Pico to the internet. We did this by using the network library and conncet8ing to BU Guest. From there we uploaded the json to teh firestone realtime database by http. We took the users email that they entered on the Thonny terminal and stored it in a folder. From there they could acess this folder using a web app we developed.