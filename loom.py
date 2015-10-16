import sublime, sublime_plugin

from collections import OrderedDict

class OnelineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        all_content_region = sublime.Region(0, self.view.size())
        all_content = self.view.substr(all_content_region)
        lines = ['"'+i.strip()+'",' for i in all_content.split("\n") if i and i.rstrip()]
        result = " ".join(lines)[:-1]
        self.view.replace(edit, all_content_region, result)

class MklistCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        all_content_region = sublime.Region(0, self.view.size())
        all_content = self.view.substr(all_content_region)
        lines = ['"'+i.strip()+'",' for i in all_content.split("\n") if i and i.rstrip()]
        result = "\n".join(lines)
        self.view.replace(edit, all_content_region, result)

class DistinctCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        all_content_region = sublime.Region(0, self.view.size())
        all_content = self.view.substr(all_content_region)
        lines = OrderedDict((i,None) for i in all_content.split("\n") if i and i.rstrip())
        result = "\n".join(lines.keys())
        self.view.replace(edit, all_content_region, result)
