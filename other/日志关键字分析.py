import sys
import os
import getopt
import subprocess
import time
import codecs
import winsound
   
ABSPATH = os.path.dirname(os.path.abspath(__file__))
MONITERCONF = 'moniter_keyword.txt'  # utf8 file
   
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hf:')
    except getopt.GetoptError, err:
        print str(err)
        print __doc__
        return 1
   
    path = ''
    for k, v in opts:
        if k == '-f':
            path = v
        elif k == '-h':
            print __doc__
            return 0
   
    if not (path and os.path.exists(path)):
        print 'Invalid path: %s' % path 
        print __doc__
        return 2
   
    #������Ԫ��
    cmd = ('tail', '-f', path)
    print ' '.join(cmd)
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE)
   
    keywordMap = {}
    #���ؼ�صĹؼ�����Ϣ
    with codecs.open(os.path.join(ABSPATH, MONITERCONF), 'r', 'utf8') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        keyword, wav = line.strip().split(':')
        keywordMap[keyword] = wav
   
    while True:
        line = output.stdout.readline()
        #process code,�õ������Ϣ��Ĵ������
        if not line:
            time.sleep(0.01)
            continue
        line = line.strip().decode('utf8')
        print line
        for keyword in keywordMap:
            if line.find(keyword) > -1:
                winsound.PlaySound(keywordMap[keyword], 
                                   winsound.SND_NODEFAULT)
        #time.sleep(0.01)
    return 0
   
if __name__ == '__main__':
    sys.exit(main())