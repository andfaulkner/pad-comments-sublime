"""
Pad: A Sublime Text 3 plug-in to add custom padding to lines.
Andrew Faulkner<andfaulkner@gmail.com>
(Adapted from code by Matthew Borgerson <mborgerson@gmail.com>)
"""
import sublime, sublime_plugin
import os
import re
from collections import namedtuple

Alignment = {
    'left':   0,
    'center': 1,
    'right':  2
}

def get_default_setting(key, default=None):
    """
    Get requested setting out of the .sublime-settings file.
    """
    settings = sublime.load_settings('Pad-Comments.sublime-settings')
    requested_setting = settings.get(key, default)
    return requested_setting

def get_def_setting(key, placeholder, default=None):
    return get_default_setting(key, default=None)

def get_current_syntax(view):
    current_syntax = view.settings().get('syntax')
    syn_name = re.search(r"[^\/]+((?=\.sublime-syntax)|(?=\.tmLanguage))", current_syntax).group(0)
    return syn_name

def select_setting(key, current_syntax_settings, default=''):
    """
    Grab a setting from the settings file
    """
    if key in current_syntax_settings:
        return current_syntax_settings[key]
    else:
        return get_def_setting(key, default)

def get_settings_tuple(self, current_syntax_settings=False):
    select_func = get_def_setting if (current_syntax_settings == False) else select_setting

    Settings = namedtuple('Settings', 'width left_char right_char fill_char strip all_caps')(
        width=select_func('width', current_syntax_settings, self.DEFAULT_WIDTH),
        left_char=select_func('left_char', current_syntax_settings, self.DEFAULT_LEFT_EDGE_CHAR),
        right_char=select_func('right_char', current_syntax_settings, self.DEFAULT_RIGHT_EDGE_CHAR),
        fill_char=select_func('fill_char', current_syntax_settings, self.DEFAULT_RIGHT_EDGE_CHAR),
        strip=select_func('strip', current_syntax_settings, True),
        all_caps=select_func('all_caps', current_syntax_settings, True)
    )
    return Settings

def determine_alignment_char(align):
    """
    Determine the alignment character to be used in the format string.
    """
    if   align == Alignment['left']:   align_char = '<'
    elif align == Alignment['center']: align_char = '^'
    elif align == Alignment['right']:  align_char = '>'
    return align_char


def trim_setting_handler(strip_setting, contents):
    """
    Strip preceding & trailing whitespace chars if setting 'strip' is true
    """
    if (strip_setting is True):
        contents = contents.strip()
    return contents

def caps_setting_handler(all_caps_setting, contents):
    """
    Convert string to all-caps if setting 'all_caps' is true
    """
    if (all_caps_setting is True):
        contents = contents.upper()
    return contents

def pad_selected_content(contents, format_str, fill_char):
    """
    Slightly pad the selected content
    """    
    spaced_content = " " + contents + " "
    prepped_content = format_str.format(spaced_content or fill_char)
    return prepped_content

def grab_ruler_width(self):
    """
    If width setting did not find a value, check user ruler settings
    """
    try:
        # Use the last ruler listed if there's more than one
        rulers = self.view.settings().get('rulers')
        width = int(rulers[len(rulers) - 1])
    except IndexError:
        print('WARNING: Invalid width setting in Pad-Comments.sublime-settings')
        width = self.DEFAULT_WIDTH
    return width

class PromptPadCommand(sublime_plugin.WindowCommand):
    """
    Prompts the user for the alignment and fill character,
    then runs the pad command.
    """
    def run(self):
        """
        Called when the command is run.
        """
        self._state = 0
        self._command_args = {
            # Default fill character
            'fill_char': '*'
        }
        self._prompt_control()

    def _prompt_control(self):
        """
        A simple state machine to control the order of prompts.
        """
        if self._state == 0:
            # Prompt for alignment
            keys = [
                '%s Aligned' % k.capitalize()
                for k in Alignment
            ]
            self.window.show_quick_panel(keys, self._on_prompt_align_done)

        elif self._state == 1:
            # Prompt for fill character
            self.window.show_input_panel(
                'Fill Character:', '-', self._on_prompt_fill_char_done, None, None
            )

        elif self._state == 2:
            # Perform padding
            view = self.window.active_view()
            if view is not None:
                view.run_command('pad', self._command_args)

    def _on_prompt_align_done(self, index):
        """
        Called after the user has selected the text alignment.
        """
        if index < 0: return
        self._command_args['align'] = Alignment[list(Alignment.keys())[index]]
        self._state += 1
        self._prompt_control()

    def _on_prompt_fill_char_done(self, text):
        """
        Called after the user has entered the fill character.
        """
        if text != '':
            self._command_args['fill_char'] = text[0]
        self._state += 1
        self._prompt_control()

####################################################################################################
### WIP ThreeLinePadHeaderCommand WIP ###
### WIP ThreeLinePadHeaderCommand WIP ###
### WIP ThreeLinePadHeaderCommand WIP ###
class ThreeLinePadHeaderCommand(sublime_plugin.TextCommand):
    DEFAULT_WIDTH = 80
    DEFAULT_FILL_CHAR = "*"
    DEFAULT_LEFT_EDGE_CHAR = "/"
    DEFAULT_RIGHT_EDGE_CHAR = "/"

    ### WIP ###
    def run(self, edit):
        print('ok')
        print('run:')
        print(sublime_plugin.TextCommand)
        print(PadCommand.run(self, edit, 'is_heading'))

        # for region in self.view.sel():
        #     line = self.view.line(region)
        #     contents       = self.view.substr(region)
        #     replace_region = region
### END WIP ThreeLinePadHeaderCommand WIP ###
### END WIP ThreeLinePadHeaderCommand WIP ###
### END WIP ThreeLinePadHeaderCommand WIP ###
####################################################################################################

class PadCommand(sublime_plugin.TextCommand):
    """
    Pad the selected text (or entire line) with a fill char up to the column
    corresponding to one of the following values (in order of precedence):
        1) The width setting in "Pad-Comments.sublime-settings";
        2) The last ruler defined by the user; or
        3) Column 80 (default if no setting is given and no rulers defined)
    """

    DEFAULT_WIDTH = 80
    DEFAULT_FILL_CHAR = "*"
    DEFAULT_LEFT_EDGE_CHAR = "/"
    DEFAULT_RIGHT_EDGE_CHAR = "/"

    def run(self, edit, is_heading=False, fill_char='*', align=Alignment['center'], width=None):
        """
        Called when the command is run.
        """
        current_syntax = get_current_syntax(self.view).lower()

        syntax_settings = get_default_setting('syntax_specific')
        syntax_settings = {k.lower(): v for k, v in syntax_settings.items()}

        if current_syntax in syntax_settings:
            Opts = get_settings_tuple(self, syntax_settings[current_syntax])
        else:
            Opts = get_settings_tuple(self, False)

        # If a width setting was present, set the text padding width to it
        if (Opts.width is not None): width = int(Opts.width)

        if (width is None): width = grab_ruler_width(self)

        # Account for the upcoming pad characters added to the final output (ahead)
        # Also adds 1-space buffer to avoid thwacking the max allowed line width
        width = width - len(Opts.left_char) - len(Opts.right_char)

        align_char = determine_alignment_char(align)

        # Decorate each region.
        for region in self.view.sel():
            line = self.view.line(region)
            if region.empty():
                # No text selected, pad entire line contents.
                contents       = self.view.substr(line)
                format_width   = width
                replace_region = line
            else:
                # Pad inside selected region.
                contents       = self.view.substr(region)
                format_width   = width - line.size() + region.size()
                replace_region = region

            # Generate the final line contents and insert it.
            format_str = '{0:%s%s%d}' % (Opts.fill_char, align_char, format_width)

            contents = trim_setting_handler(Opts.strip, contents)
            contents = caps_setting_handler(Opts.all_caps, contents)

            prepped_content = pad_selected_content(contents, format_str, Opts.fill_char)

            formatted_str = Opts.left_char + prepped_content + Opts.right_char
            if (is_heading != False):
                bookend_line_format = '{0:%s%s%d}' % (Opts.fill_char, align_char, format_width)
                bookend_line = (Opts.left_char +
                                bookend_line_format.format(Opts.fill_char) +
                                Opts.right_char
                )
                formatted_str = bookend_line + "\n" + formatted_str + "\n" + bookend_line

            self.view.replace(edit, replace_region, formatted_str)
