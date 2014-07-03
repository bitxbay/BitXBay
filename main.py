#!/usr/bin/env python

import sys, os
import helper, config


def main(argv=sys.argv):
    if len(sys.argv) < 2:
        data_dir = config.path#os.path.join(os.getenv('APPDATA'),'Bitcoin', 'blocks')
        if not os.path.exists(data_dir):
            print('ERROR: Database %s was not found!' % os.path.join(data_dir))
        else:
            print ('Selected Database: %s' % os.path.join(data_dir))
            w = helper.worker(data_dir, config.addresses, config.days)
            w.start()
    else:
        if not os.path.exists(sys.argv[1]):
            print('ERROR: Database %s was not found!' % sys.argv[1])
        else:
            print ('Selected Database: %s' % sys.argv[1])
            w = helper.worker(os.path.join(sys.argv[1]), config.addresses, config.days)
            w.start()
    

if __name__ == '__main__':
    sys.exit(main())
    