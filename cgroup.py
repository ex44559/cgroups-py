from __future__ import print_function

import getpass
import os

CGROUP_BLK_BASE_PATH = '/sys/fs/cgroup/blkio'


class Cgroup(object):
    def __int__(self):
        self.user = getpass.getuser()

    @staticmethod
    def list_blkio_cgroup():
        path = CGROUP_BLK_BASE_PATH
        blk_groups = [d for d in os.listdir(path) if os.path.isdir(d)]

        if not blk_groups:
            print("no blk groups")

    @staticmethod
    def add_blkio_cgroup(policy):
        path = CGROUP_BLK_BASE_PATH + '/' + policy
        if os.path.isdir(path):
            print("%s exists" % policy)
        else:
            os.mkdir(path)
            print("%s added" % path)

    @staticmethod
    def del_blkio_cgroup(policy):
        path = CGROUP_BLK_BASE_PATH + '/' + policy
        if os.path.isdir(path):
            os.rmdir(path)
            print("policy %s removed" % policy)
        else:
            print("policy %s does not exist" % policy)

    @staticmethod
    def set_blkio_cgroup_weight(policy, weight):
        path = CGROUP_BLK_BASE_PATH + '/' + policy
        if os.path.isdir(path):
            path += '/' + 'blkio.weight'
            with open(path, "w+") as f:
                f.write(str(weight))
            print("weight written")
        else:
            print("policy %s does not exist" % policy)

    @staticmethod
    def get_blkio_cgroup_weight(policy):
        path = CGROUP_BLK_BASE_PATH + '/' + policy
        if os.path.isdir(path):
            path += '/' + 'blkio.weight'
            with open(path, 'r') as f:
                weight = f.read()
                print("weight read")
                return weight
        else:
            print("policy %s does not exist" % policy)
            return -1;

if __name__ == '__main__':
    Cgroup.list_blkio_cgroup()
    Cgroup.add_blkio_cgroup("test")
    Cgroup.set_blkio_cgroup_weight("test", 100)

    weight = Cgroup.get_blkio_cgroup_weight("test")
    print("weight is %d" % int(weight))
    Cgroup.del_blkio_cgroup("test")
