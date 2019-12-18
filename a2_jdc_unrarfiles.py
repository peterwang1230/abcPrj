# brew install unrar (
# import patoolib
from pyunpack import Archive
import os
from os.path import expanduser

home = expanduser("~")
srcDir = home + '/' + 'JDCYuanSRC'
targetDir = home + '/' + 'JDCYuan'
os.makedirs(srcDir, exist_ok=True)
os.makedirs(targetDir, exist_ok=True)   # extract rar files to '~/JDCYuan'

# TODO: Extract the rar files.
i = 0

for filename in os.listdir(srcDir):
    if filename.endswith(".rar"):
        i = i + 1
        fn = os.path.join(srcDir, filename)
        print('UnRAR file {}. {}...'.format(i, fn))
        Archive(fn).extractall(targetDir)
    else:
        continue

