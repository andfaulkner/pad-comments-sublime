Pad-Comments
============

TODOs
-----
*   TODO: Edit README. It's out of date and still has some vestiges of the original codebase at the point it was forked.
*   TODO: Republish on the Sublime Package Control repository.


Description
-----------
Pad-Comments is a [Sublime Text](http://www.sublimetext.com/) plug-in to add a custom padded
comment to a line. For example, if the command is run in a JS file with the following text
selected (and default settings):
```
Life, The Universe, Everything
```

...the result will be:
```
/********************************* LIFE, THE UNIVERSE, EVERYTHING *********************************/
```

...where the actual width of the padding corresponds either to a provided package-specific width
setting, the last ruler you defined in your user settings, or 80 spaces.

This allows you to easily insert 'heading' comments in Javascript files, with the 'section' title
precisely centered.


Installation
------------
### Automatic installation using Package Control
Pad-Comments can be installed using the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) package manager plug-in. Use the command palette to launch the "Package Control: Install Package" command and search for Pad.

### Manual installation
Install by cloning this repository to your Packages directory.

* For Windows:
```
cd "%APPDATA%\Sublime Text 3\Packages"
git clone https://github.com/andfaulkner/pad-comments-sublime.git
```

*   For Mac OS X:
```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
git clone https://github.com/andfaulkner/pad-comments-sublime.git
```

After cloning the repository to your packages directory, Sublime Text should automatically load the package.


How to use
----------
First, move the cursor to the line you want to pad or select the region of text
in the line that should be padded. You may use multiple cursors to pad multiple
lines at once. Then, use the command palette (`Ctrl+Shift+P`) to find and run
the "Pad: Add Padding to Line or Selection" command. You will be prompted for
alignment and fill character. The line/selected text will be padded with the
fill character up to the first ruler (or column 80 if no rulers are being used).

You can also use the command-alt-ctrl-p hotkey to automatically centre pad your
selection (or the whole row).


More examples
-------------
### Centre pad line or selection with * character

* Use no selection to pad the entire line. With the default settings, the following example: 
```
Redux wrappers
```

...becomes:
```
/***************************************** REDUX WRAPPERS ****************************************/
```

*   Punctuation is preserved. E.g. (with default settings):

```
Run! It's a bear eating a stick of butter!!!
```

...becomes:
```
/************************** RUN! IT'S A BEAR EATING A STICK OF BUTTER!! ***************************/
```

*   The same results occurs if you select all text on the line.

*   The action automatically strips preceding & trailing whitespace, and capitalizes all characters (these can be turned off in settings). E.g.:
```
Third-party components
```

...becomes:
```
/************************************ THIRD-PARTY COMPONENTS *************************************/
```

*   The fill character, left-edge character, and right-edge character can all be customized, and the padding width can be defined. E.g. if your settings are:
```
{
    "width": 80,
    "fill_char": "-"
    "all_caps": true,
    "strip": true,
    "left_char": "#",
    "right_char": "$"
}
```

...then the following sample text:
```
Gr, argh
```

...becomes:
````
-################################# GR, ARGH ##################################$
````

### Add padding to line or selection
To pad around all text on a line, perform action with no text selected:
```
This is some text.
```
... becomes:
```
/***************************** THIS IS SOME TEXT. *****************************/
```

*   Use multiple selections to batch pad:
```
/* This is some text. */
/* This is some more text. */
/* And here is even more text. */
```

...becomes:
```
/* ----------------------- This is some text. ----------------------- */
/* -------------------- This is some more text. --------------------- */
/* ------------------ And here is even more text. ------------------- */
```

* Perform the command on an empty line to fill the entire line with a character.
```
 
```

...becomes:
```
**********************************************************************
```


Limitations
-----------
### Issues with padding around selected text
*   No custom multi-line headers (i.e. lines inserted above and/or below the selection with characters inserted to produce a large, obvious divider in the code).
*   No elimination of left or right-side padding.
*   Left and right edge characters still get inserted around text on lines that are already past the column limit.

### Issues adding padding to line or selection
*   Padding only works for one region of text per line.
*   Multi-line selection padding does not work properly.
    *   Workaround: Use multiple cursors / multiple single-line selections to pad multiple lines at once.
