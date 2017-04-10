import sublime
import sublime_plugin


class SelectHrefCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		hrefs = self.view.find_all('href="[^"]*"')
		self.view.sel().clear()
		[self.view.sel().add(region) for region in hrefs]
