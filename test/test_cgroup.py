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

    def testSetGetGroupWeight(self):
        cgroup.add_blkio_cgroup("test")
        cgroup.set_blkio_cgroup_weight("test", 100)
        self.assertEqual(cgroup.get_blkio_cgroup_weight("test"), 100)
        cgroup.del_blkio_cgroup("test")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CgroupTestCase("testAddGroup"))
    suite.addTest(CgroupTestCase("testDelGroup"))
    suite.addTest(CgroupTestCase("testSetGetGroupWeight"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
