Pad-JS-Comments
===============

Pad-JS-Comments is a [Sublime Text](http://www.sublimetext.com/) plug-in to add a custom padded
JS comment to a line. For example, if the command is run with the following text selected:

        Life, The Universe, Everything

...the result will be:

        /********************** Life, The Universe, Everything ***********************/

...where the actual width of the padding corresponds either to a provided package-specific width
setting, the last ruler you defined in your user settings, or 80 spaces.

This allows you to easily insert 'heading' comments in Javascript files, with the 'section' title
precisely centered.

Installation
------------

### Automatic Installation using Package Control

Pad-JS-Comments can be installed using the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) package manager plug-in. Use the command palette to launch the "Package Control: Install Package" command and search for Pad.

### Manual Installation

Install by cloning this repository to your Packages directory.

* For Windows:

        cd "%APPDATA%\Sublime Text 3\Packages"
        git clone https://github.com/andfaulkner/pad-js-comments.git

* For Mac OS X:

        cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
        git clone https://github.com/andfaulkner/pad-js-comments.git

After cloning the repository to your packages directory, Sublime Text should
automatically load the package.

How to Use
----------

First, move the cursor to the line you want to pad or select the region of text
in the line that should be padded. You may use multiple cursors to pad multiple
lines at once. Then, use the command palette (`Ctrl+Shift+P`) to find and run
the "Pad: Add Padding to Line or Selection" command. You will
be prompted for alignment and fill character. The line/selected text will be
padded with the fill character up to the first ruler (or column 80 if no rulers
are being used).

You can also use the command-alt-ctrl-p hotkey to automatically centre pad your
selection (or the whole row).

More Examples
-------------

###Pad: centre pad line or selection with * character

* Use no selection to pad the entire line. If your width is set to 80 (setting or ruler), this:

        RUN AWAY IT'S A BEAR EATING A STICK OF BUTTER!!!

becomes:

        /************* RUN AWAY IT'S A BEAR EATING A STICK OF BUTTER!!! **************/

* The same result occurs if you select all text on the line.


###Pad: Add Padding to Line or Selection

* Use no selection to pad the entire line.

        This is some text.

 becomes

        /*-------------------------- This is some text. --------------------------*/

* Use multiple selections to batch pad.

        /* This is some text. */
        /* This is some more text. */
        /* And here is even more text. */

 becomes

        /* ----------------------- This is some text. ----------------------- */
        /* --------------------This is some more text.--------------------- */
        /* ------------------And here is even more text.------------------- */

* Perform the command on an empty line to fill the entire line with a character.

 ` `

 becomes

        **********************************************************************

Limitations
-----------
* Padding only works for one region of text per line.
* Multi-line selection padding does not work properly.
  * Workaround: Use multiple cursors / multiple single-line selections to pad
    multiple lines at once.
