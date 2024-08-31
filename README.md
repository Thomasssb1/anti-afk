# Anti AFK
Need to AFK something in the background, but don't want to keep an autoclicker running 24/7 with the program on screen?
This program allows you to set intervals for reopening the program to reset the AFK timer so that you do not get kicked as well as not needing to have the program open on screen 24/7.

## Arguments
Currently, you can have the following arguments:
- `interval` - any integer followed by 's', 'm', 'h' (Defaults to 10m)
- `stop key` - any alphanumeric key used to terminate the program (Defaults to 'q')
- `position` - a relative position for the mouse to target when entering the program (Defaults to centre of screen)

Adding arguments can be done as following:
```zsh
 $ python main.py {interval} {stop key} {position}
```
