import unittest
from soft.entities import ItemPatch


class TestEntity(unittest.TestCase):
    item1 = ItemPatch('ROOT')
    item2 = ItemPatch('root')

    def test_get_name(self):
        self.assertEqual(TestEntity.item1.name, 'ROOT')
        self.assertEqual(TestEntity.item2.name, 'ROOT')
        self.assertNotEqual(TestEntity.item2.name, 'root')
        
    def test_is_leaf(self):        
        self.assertFalse(TestEntity.item1.is_leaf())


if __name__ == '__main__':
    unittest.main()
    