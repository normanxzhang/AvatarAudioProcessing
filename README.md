Created By Norman Z, Roberto VA, Mahit V, Thomas Y

Included Files:
    pg_init.py
    animation.py
    audio.py
    sprite_sheet.py
    README
    Sprite Sheets (contains slime_spritesheet)


Summary: 

Purpose (Why): To explore real-time audio processing techniques and to allow users to express themselves virutally to foster a happier online experience utilizing the pygame and pyaudio modules

Main features:
- Visual
    Allow users to pick from a list of default templates of 2D avatars for them to use

    How:
    2D avartars are created from a sprite sheet containing PNG characters with multiple positions or frames
    There are multiple PNGs of the same sprite design, the only differences between different sprites are colours and the frame they are frozen in, depicting whether the program is detecting user microphone input, in this case, the slime jumping/bouncing means the program is detecting audio input, while the slime rolling is the idle animation (no audio input)    
    The avatar can be added as a visual source in OBS and the virtual camera OBS feature which allows for the avatar to be displayed in place of visual input from a webcam

- Audio
    Voice activity detection in order to determine whether the user is talking or not. The program can be adjusted so that a certain volume is required in order to make the sprite animated. Additionally, a delay was implemented in order to prevent any jittery movement of the sprite when talking (natural miniscule pauses in speech do not immediately send the sprite into its idle animation, program must detect a sufficient duration of no audio input)

- UI
    Provides the user a preview of each of the four sprite and allowing the user to select which colour sprite they desire. Each sprite is identical, simply varying colours


Running Instructions:

The program is simple to utilize, simply run the program, add it as a source in OBS, and enable your virtual camera. Chroma key will be necessary in order to remove the background of the sprite, however, the background colours of the sprites are chosen to intentionally be opposite from the slime itself, preventing accidental removal of the slime. Audio input threshold can be adjusted in RMS in audio.py and the delay between audio input and no audio input can be edited in pg_init.py when assigning audioManager. The last argument is the desired delay timer in milliseconds (a common multiple of 40 and 80 is recommended in order to ensure smoothness of the sprite's animation)

