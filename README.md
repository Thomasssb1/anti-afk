# Anti AFK

Need to AFK something in the background, but don't want to keep an autoclicker running 24/7 with the program on screen?
This program allows you to set intervals for reopening the program to reset the AFK timer so that you do not get kicked as well as not needing to have the program open on screen 24/7.

## Arguments

Currently, you can have the following arguments:

- `interval` - any integer followed by 'ms', 's', 'm', 'h' (Defaults to 10m)
- `stop key` - any alphanumeric key used to terminate the program (Defaults to 'q')
- `pause key` - any alphanumeric key used to pause the program (Defaults to 'p')
- `locked` - whether or not the mouse is locked to {position} and the selected window<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- if locked is disabled, you can freely move the mouse whilst clicking (operating the same as an autoclicker)
- `position` - a relative position for the mouse to target when entering the program (Defaults to centre of screen)

Adding arguments can be done as following (you need to maintain the position as shown above):

```zsh
 $ python main.py {interval} {stop key} {pause key} {locked = true/false} {position}
```

You can also add the `-v` flag at the end to enable verbosity.

## Setup

To get started, run

```zsh
$ pip install -r requirements.txt
```

to install all required libraries.
