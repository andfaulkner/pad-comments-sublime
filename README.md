Pad
===

Pad is a [Sublime Text 2](http://www.sublimetext.com/) plug-in to add custom
padding to lines.

_Note: This is a new package and is subject to minor changes in behavior._

Installation
------------

Install by cloning this repository to your Packages directory.

* For Windows:

        cd "%APPDATA%\Sublime Text 2\Packages"
        git clone https://github.com/mborgerson/pad.git

* For Mac OS X:

        cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
        git clone https://github.com/mborgerson/pad.git

After cloning the repository to your packages directory, Sublime Text should
automatically load the package.

How to Use
----------

First, move the cursor to the line you want to pad or select the region of text
in the line that should be padded. You may use multiple cursors to pad multiple
lines at once. Then, use the command palette (`Ctrl+Shift+P`) to find and run
the command with the caption "Pad: Add Padding to Line or Selection". You will
be prompted for alignment and fill character. The line/selected text will be
padded with the fill character up to the first ruler (or column 80 if no rulers
are being used).

Examples
--------

* Use no selection to pad the entire line.

        This is some text.

 becomes

        --------------------------This is some text.--------------------------

* Use multiple selections to batch pad.

        /* This is some text. */
		/* This is some more text. */
		/* And here is even more text. */

 becomes

        /* -----------------------This is some text.----------------------- */
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
