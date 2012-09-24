# Sublime Text 2 Beanstalk Tools #

## Introduction ##

A set of handy tools for using Sublime Text 2 editor with Beanstalkapp (http://beanstalkapp.com).

## Usage ##

Open the root directory of your Git or Subversion working copy in Sublime Text 2.

* Press `Ctrl + Shift + P` (`Cmd + Shift + P` in OSX) and select `Beanstalk: Open File` or just press `Ctrl + Shift + ^` (`Cmd + Shift + ^`) to open currently edited file in Beanstalk.
* Press `Ctrl + Shift + P` (`Cmd + Shift + P`) and select `Beanstalk: Blame` to open blame for currently edited file in Beanstalk.
* More features will be available later.

## Get it installed ##

### On Mac ###

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
git clone git://github.com/temochka/sublime-text-2-beanstalk.git Beanstalk
```

### On Linux ###

```bash
cd ~/.config/sublime-text-2/Packages/
git clone git://github.com/temochka/sublime-text-2-beanstalk.git Beanstalk
```

### Windows ###

Sorry, but Beanstalk tools are currently available only for OS X and Linux users.

## Known issues ##

Only works for Git and Subversion repositories. Mercurial is not supported yet.