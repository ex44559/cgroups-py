import unittest
from .. import cgroup


class CgroupTestCase(unittest.TestCase):
    def setUp(self):
        for g in cgroup.list_blkio_cgroup():
            cgroup.del_blkio_cgroup(g)

    def testAddGroup(self):
        cgroup.add_blkio_cgroup("test")
        self.assertEqual(cgroup.list_blkio_cgroup(), ["test"])

    def testDelGroup(self):
        cgroup.del_blkio_cgroup("test")
        self.assertEqual(cgroup.list_blkio_cgroup(), [])

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CgroupTestCase("testAddGroup"))
    suite.addTest(CgroupTestCase("testDelGroup"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
