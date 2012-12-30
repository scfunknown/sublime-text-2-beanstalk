import sublime, sublime_plugin, webbrowser
from beanstalk import *

class BeanstalkOpenCommand(BeanstalkWindowCommand):
  @require_file
  @with_repo
  def run(self, repo):
    webbrowser.open_new_tab(repo.browse_file_url(self.relative_filename()))
