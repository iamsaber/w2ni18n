# SPDX-FileCopyrightText: 2016 - Akshay Nagpal <akshaynagpal@user.noreplay.github.com>
# SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-FileCopyrightText: 2022 - AmirMohammad Babaei <AmirMohamadBabaee@users.noreply.github.com>
# SPDX-License-Identifier: MIT

import unittest
import sys
import logging
from word2numberi18n import w2n

class TestW2N(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestW2N, cls).setUpClass()
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        log = logging.getLogger("SYSTEM")
        log.info(f"Testsystem is {sys.implementation.name} v{sys.version_info.major}.{sys.version_info.minor}@{sys.platform}")
        
    
    def test_positives_fa(self):
        instance = w2n.W2N(lang_param="fa")
        # test persian
        self.assertEqual(instance.word_to_num("دو میلیون و سه هزار و نهصد و هشتاد و چهار"), 2003984)
        self.assertEqual(instance.word_to_num("نوزده"), 19)
        self.assertEqual(instance.word_to_num("دو هزار و نوزده"), 2019)
        self.assertEqual(instance.word_to_num("دو میلیون و سه هزار و نوزده"), 2003019)
        self.assertEqual(instance.word_to_num('سه میلیارد'), 3000000000)
        self.assertEqual(instance.word_to_num('سه میلیون'), 3000000)
        self.assertEqual(instance.word_to_num('صد و بیست و سه میلیون چهارصد و پنجاه و شش هزار و هفتصد و هشتاد و نه'), 123456789)
        self.assertEqual(instance.word_to_num('یازده'), 11)
        self.assertEqual(instance.word_to_num('نوزده میلیارد و نوزده'), 19000000019)
        self.assertEqual(instance.word_to_num('صد و چهل و دو'), 142)
        self.assertEqual(instance.word_to_num('112'), 112)
        self.assertEqual(instance.word_to_num('11211234'), 11211234)
        self.assertEqual(instance.word_to_num('پنج'), 5)
        self.assertEqual(instance.word_to_num('دو میلیون و بیست و سه هزار و چهل و نه'), 2023049)
        self.assertEqual(instance.word_to_num('دو ممیز سه'), 2.3)
        self.assertEqual(instance.word_to_num('دو میلیون و بیست و سه هزار و چهل و نه ممیز دو سه شش نه'), 2023049.2369)
        self.assertEqual(instance.word_to_num('یک میلیارد و دو میلیون و بیست و سه هزار و چهل و نه ممیز دو سه شش نه'), 1002023049.2369)
        self.assertEqual(instance.word_to_num('نه تریلیون و یک میلیارد و دو میلیون و بیست و سه هزار و چهل و نه ممیز دو سه شش نه'), 9001002023049.2369)
        self.assertEqual(instance.word_to_num('ممیز یک'), 0.1)
        self.assertEqual(instance.word_to_num('ممیز'), 0)
        self.assertEqual(instance.word_to_num('ممیز نوزده'), 0)
        self.assertEqual(instance.word_to_num('صد و سی و پنج'), 135)
        self.assertEqual(instance.word_to_num('صد'), 100)
        self.assertEqual(instance.word_to_num('هزار'), 1000)
        self.assertEqual(instance.word_to_num('میلیون'), 1000000)
        self.assertEqual(instance.word_to_num('میلیارد'), 1000000000)
        self.assertEqual(instance.word_to_num('تریلیون'), 1000000000000)
        self.assertEqual(instance.word_to_num("یک میلیون و هزار"), 1_001_000)
        self.assertEqual(instance.word_to_num('نه ممیز نه نه نه'), 9.999)
        self.assertEqual(instance.word_to_num('هفتم ممیز نوزده'), 0)
        self.assertEqual(instance.word_to_num('هفت میلیون، هشتصد و شصت و سه هزار، دویست، پنجاه و چهار'), 7863254)
        self.assertEqual(instance.word_to_num('دویست'), 200)
        # self.assertEqual(instance.word_to_num('صفر نهصد و دوازده'), 912)  # TODO

        # test cases https://github.com/akshaynagpal/w2n/issues/54
        self.assertEqual(instance.word_to_num('سه ممیز نه هفت'), 3.97)
        self.assertEqual(instance.word_to_num('دو ممیز هفت هشت'), 2.78)
        self.assertEqual(instance.word_to_num('یک ممیز هشت شش'), 1.86)
        self.assertEqual(instance.word_to_num('دو ممیز هفت دو'), 2.72)
        self.assertEqual(instance.word_to_num('یک ممیز هشت چهار'), 1.84)
        self.assertEqual(instance.word_to_num('دو ممیز دو هشت'), 2.28)
        self.assertEqual(instance.word_to_num('دو ممیز چهار هفت'), 2.47)
        self.assertEqual(instance.word_to_num('یک ممیز پنج نه'), 1.59)
        
        # test for kylosnite repository
        self.assertEqual(instance.word_to_num("نه میلیون و نه هزار"), 9009000)
        
        # in different to w2n it is ok, in result of str:112 is not different to int:112
        self.assertEqual(instance.word_to_num('112'), 112)
        self.assertEqual(instance.word_to_num(112),112)
        
        # special name
        # self.assertEqual(w2n.word_to_num('dozen'), 12)
        
        # https://github.com/akshaynagpal/w2n/issues/38
        self.assertEqual(instance.word_to_num("صد و بیست"),120)

        # https://github.com/akshaynagpal/w2n/issues/44
        self.assertEqual(instance.word_to_num('دو میلیون و هزار'),2_001_000)
        
        #https://github.com/akshaynagpal/w2n/issues/27
        self.assertEqual(instance.word_to_num("یک میلیون و صد و هشتاد و دو هزار"),1_182_000)
        self.assertEqual(instance.word_to_num("یک میلیون و هشتاد و دو هزار"),1_082_000)
        
        #https://github.com/akshaynagpal/w2n/issues/58
        self.assertEqual(instance.word_to_num("عنوان نمونه - فصل یک صد و پانزده"), 115)
        self.assertEqual(instance.word_to_num("عنوان نمونه - نود و هشت"), 98)
        
        #https://github.com/akshaynagpal/w2n/issues/61
        self.assertEqual(instance.word_to_num("سه هزار و چهارصد و پنجاه"), 3450)

    def test_negatives_en(self):
        instance = w2n.W2N(lang_param="fa")
        self.assertRaises(ValueError, instance.word_to_num, '112-')
        self.assertRaises(ValueError, instance.word_to_num, '-')
        self.assertRaises(ValueError, instance.word_to_num, 'ون')
        self.assertRaises(ValueError, instance.word_to_num, 'میلیون میلیون')
        self.assertRaises(ValueError, instance.word_to_num, 'سه میلیون میلیون')
        self.assertRaises(ValueError, instance.word_to_num, 'میلیون چهار میلیون')
        self.assertRaises(ValueError, instance.word_to_num, 'هزار میلیون')
        self.assertRaises(ValueError, instance.word_to_num, 'هزار تریلیون')
        self.assertRaises(ValueError, instance.word_to_num, 'یک میلیارد ممیز دو میلیون بیست و سه هزار و چهل و نه ممیز دو سه شش نه')
        self.assertRaises(ValueError, instance.word_to_num, 'یک هزار و پنج میلیون')
        self.assertRaises(ValueError, instance.word_to_num, 'سه میلیون ممیز دو میلیون')
        self.assertRaises(ValueError, instance.word_to_num, 'سه میلیون ممیز دویست و پنج')
        
        
    def test_null_fa(self):
        instance = w2n.W2N(lang_param="fa")
        noneValue :str = None 
        self.assertRaises(ValueError, instance.word_to_num, noneValue)
        noneValue = ""
        self.assertRaises(ValueError, instance.word_to_num, noneValue)


if __name__ == '__main__':
    unittest.main()
