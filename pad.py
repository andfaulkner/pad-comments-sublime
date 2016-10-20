"""
Pad: A Sublime Text 2 plug-in to add custom padding to lines.
Matthew Borgerson <mborgerson@gmail.com>
"""

import sublime, sublime_plugin

Alignment = {
    'left':   0,
    'center': 1,
    'right':  2
}

def get_setting(key, default=None):
    settings = sublime.load_settings('Pad-JS-Comments.sublime-settings')
    requested_setting = settings.get(key, default) # settings.get(key, default)
    return requested_setting

class PromptPadCommand(sublime_plugin.WindowCommand):
    """
    Prompts the user for the alignment and fill character, then runs the
    pad command.
    """
    def run(self):
        """Called when the command is run."""
        self._state = 0
        self._command_args = {
            'fill_char': '-' # Default fill character
            }
        self._prompt_control()

    def _prompt_control(self):
        """A simple state machine to control the order of prompts."""
        if self._state == 0:
            # Prompt for alignment
            keys = ['%s Aligned' % k.capitalize() for k in Alignment]
            self.window.show_quick_panel(keys, self._on_prompt_align_done)
        elif self._state == 1:
            # Prompt for fill character
            self.window.show_input_panel('Fill Character:',
                                         '-',
                                         self._on_prompt_fill_char_done,
                                         None,
                                         None)
        elif self._state == 2:
            # Perform padding
            view = self.window.active_view()
            if view is not None:
                view.run_command('pad', self._command_args)

    def _on_prompt_align_done(self, index):
        """Called after the user has selected the text alignment."""
        if index < 0: return
        self._command_args['align'] = Alignment[list(Alignment.keys())[index]]
        self._state += 1
        self._prompt_control()

    def _on_prompt_fill_char_done(self, text):
        """Called after the user has entered the fill character."""
        if text != '':
            self._command_args['fill_char'] = text[0]
        self._state += 1
        self._prompt_control()

class PadCommand(sublime_plugin.TextCommand):
    """
    Pad the selected text (or entire line) with a fill character up to the
    first ruler (or column 80 if no rulers are being used).
    """

    DEFAULT_WIDTH = 80

    def run(self, edit, fill_char='-', align=Alignment['center'], width=None):
        """Called when the command is run."""
        # Get width setting
        width_setting = get_setting('width', None)
        # If a width setting was present, set the padding width to it
        if (width_setting is not None):
            width = int(width_setting)

        # If width setting did not find a value, check user ruler settings
        if (width is None):
            try:
                # Use the last ruler listed if there's more than one
                rulers = self.view.settings().get('rulers')
                width = int(rulers[len(rulers) - 1])
                print("width: " + str(width))
            except IndexError:
                width = self.DEFAULT_WIDTH

        # Determine the alignment character to be used in the format string.
        if   align == Alignment['left']:   align_char = '<'
        elif align == Alignment['center']: align_char = '^'
        elif align == Alignment['right']:  align_char = '>'

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
            format_str = '{0:%s%s%d}' % (fill_char, align_char, format_width)
            formatted_str = "/*" + format_str.format(contents or fill_char) + "*/"
            self.view.replace(edit, replace_region, formatted_str)
            print(width_setting)
