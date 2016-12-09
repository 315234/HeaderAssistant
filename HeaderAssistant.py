# Keep the header open in the left pane
import sublime
import sublime_plugin

import os.path

class HeaderAssistant(sublime_plugin.WindowCommand):
    def run(self):
        fullname = os.path.basename(self.window.active_view().file_name())
        basename, extension = os.path.splitext(fullname)

        # File extension mappings
        mappings = { ".cpp": ".h", ".h": ".cpp" }
        if extension in mappings:
            search = basename + mappings[extension]
        else:
            search = basename

        self.window.run_command("show_overlay", args={
            "overlay": "goto",
            "show_files": True,
            "text": search
        })
