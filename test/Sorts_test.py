import sys
import unittest

# Añadir el directorio src al path para que los módulos puedan ser importados
sys.path.append('./src')
from gnome import gnome_sort
from headsort import heap_sort
from mergeSort import merge_sort
from quicksort import quicksort
from selection1 import selection_sort
from shellSort import shell_sort
from countingSort import radixSort

class TestSortAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_data = [121, 432, 564, 23, 1, 45, 788]
        self.sorted_data = sorted(self.test_data)

    def test_gnome_sort(self):
        result = gnome_sort(self.test_data[:])
        self.assertEqual(result, self.sorted_data)

    def test_heap_sort(self):
        data = self.test_data[:] 
        heap_sort(data)
        self.assertEqual(data, self.sorted_data)

    def test_merge_sort(self):
        result = merge_sort(self.test_data[:])
        self.assertEqual(result, self.sorted_data)

    def test_quick_sort(self):
        data = self.test_data[:]
        quicksort(data, 0, len(data) - 1)
        self.assertEqual(data, self.sorted_data)

    def test_selection_sort(self):
        data = self.test_data[:] 
        selection_sort(data) 
        self.assertEqual(data, self.sorted_data) 

    def test_shell_sort(self):
        result = shell_sort(self.test_data[:])
        self.assertEqual(result, self.sorted_data)

    def test_radix_sort(self):
        data = self.test_data[:]
        radixSort(data)
        self.assertEqual(data, self.sorted_data)

if __name__ == '__main__':
    unittest.main()
