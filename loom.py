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

class Underline2camelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        all_content_region = sublime.Region(0, self.view.size())
        all_content = self.view.substr(all_content_region)
        lines = OrderedDict((self.underline_to_camel(i),None) for i in all_content.split("\n") if i and i.strip())
        result = "\n".join(lines.keys())
        self.view.replace(edit, all_content_region, result)

    @staticmethod
    def underline_to_camel(input_str):
        res = ""
        for word in input_str.split("_"):
            res += word.capitalize()
        res = res.replace("Ios", "iOS")
        return res

class Underline2camel4wordCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                line = self.view.line(region)  
                line_contents = self.view.substr(line)
                res = "\n".join([Underline2camelCommand.underline_to_camel(word) for word
                        in line_contents.split("\n")])
                self.view.replace(edit, region, res)

class Camel2underline4wordCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                line = self.view.line(region)  
                line_contents = self.view.substr(line)
                res = "\n".join([Camel2underlineCommand.camel_to_underline(word) for word
                        in line_contents.split("\n")])
                self.view.replace(edit, region, res)

class Camel2underlineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        all_content_region = sublime.Region(0, self.view.size())
        all_content = self.view.substr(all_content_region)
        lines = OrderedDict((self.camel_to_underline(i),None) for i in all_content.split("\n") if i and i.strip())
        result = "\n".join(lines.keys())
        self.view.replace(edit, all_content_region, result)

    @staticmethod
    def camel_to_underline(input_str):
        res = ""
        input_str = input_str.replace("iOS", "Ios")
        for index, letter in enumerate(input_str):
            pre = "_" if index else ""
            res += letter if not letter.isupper() else "{0}{1}".format(
                pre, letter.lower())
        return res
