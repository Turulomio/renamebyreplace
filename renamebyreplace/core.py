import argparse
import os

try:
    t=gettext.translation('renamebyreplace',pkg_resources.resource_filename("renamebyreplace","locale"))
    _=t.gettext
except:
    _=str


def maxlenarr(arr):
    r=0
    for item in arr:
        if len(item)>r:
            r=len(item)
    return r

## @param parameters is a list. For example ['--search',]
def main(parameters):
    parser=argparse.ArgumentParser(_('Rename by replace'))
    parser.add_argument('--search', help=_('String to search'), action='store')
    parser.add_argument('--replace', help=_('String to replace'), action='store')
    parser.add_argument('--write', help=_('Renames the files'), action='store_true', default=False)
    args=parser.parse_args(parameters)

    arrFrom=[]
    arrTo=[]
    files = os.listdir(os.getcwd())

    for file in files:
        if file.find(args.search)!=-1:
            arrFrom.append(file)
            arrTo.append(file.replace(args.search,args.replace))

    maxarr=maxlenarr(arrFrom)
    for i in range(len(arrFrom)):
        print ("{} ==> {}".format(arrFrom[i].ljust(maxarr),arrTo[i]))
        if args.write==True:
            os.rename(arrFrom[i],arrTo[i])