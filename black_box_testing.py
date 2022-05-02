# Jeffrey Ngo
# HW1: Black Box Testing
# Method: I did everything manually
# Started with an empty string
# Then entered valid credit cards for each issuer
# with the correct prefixes and check digits
# Then tested for length and prefix boundaries and other invalid inputs


import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    # Found bug 1
    def test_input(self):
        card = ''
        self.assertFalse(credit_card_validator(card).format(card))

    # Found Bug 3
    # Tests valid credit card numbers
    def test_visa(self):
        card = 4646133805258440
        self.assertTrue(credit_card_validator(card).format(card))

    def test_master(self):
        card = 5372071926177635
        self.assertTrue(credit_card_validator(card).format(card))

    def test_master2(self):
        card = 2500123456789107
        self.assertTrue(credit_card_validator(card).format(card))

    # Found Bug 4
    def test_am(self):
        card = 349686358567606
        self.assertTrue(credit_card_validator(card).format(card))

    # Found Bug 4
    def test_aex(self):
        card = 379686358567609
        self.assertTrue(credit_card_validator(card).format(card))

    # _cd Tests for invalid check digits
    def test_visa_cd(self):
        card = 4646133805258441
        self.assertFalse(credit_card_validator(card).format(card))

    def test_master_cd(self):
        card = 5372071926177632
        self.assertFalse(credit_card_validator(card).format(card))

    def test_master2_cd(self):
        card = 2500123456789103
        self.assertFalse(credit_card_validator(card).format(card))

    # Found Bug 4
    def test_am_cd(self):
        card = 349686358567604
        self.assertFalse(credit_card_validator(card).format(card))

    # Found Bug 4
    def test_aex_cd(self):
        card = 379686358567605
        self.assertFalse(credit_card_validator(card).format(card))

    # Tests length boundaries for Visa
    def test_v10(self):
        card = 4506264755
        self.assertFalse(credit_card_validator(card).format(card))

    def test_v11(self):
        card = 45062647586
        self.assertFalse(credit_card_validator(card).format(card))

    def test_v12(self):
        card = 450626475872
        self.assertFalse(credit_card_validator(card).format(card))

    def test_v13(self):
        card = 4506264758782
        self.assertFalse(credit_card_validator(card).format(card))

    def test_v14(self):
        card = 45062647587804
        self.assertFalse(credit_card_validator(card).format(card))

    # Found bug 2
    def test_v15(self):
        card = 450626475878085
        self.assertFalse(credit_card_validator(card).format(card))

    def test_v17(self):
        card = 45062647235878087
        self.assertFalse(credit_card_validator(card).format(card))

    def test_v18(self):
        card = 450626472358780887
        self.assertFalse(credit_card_validator(card).format(card))

    def test_v19(self):
        card = 4506264723587808817
        self.assertFalse(credit_card_validator(card).format(card))

    # Tests length boundaries for master card 51-55
    def test_m10(self):
        card = 5372071927
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m11(self):
        card = 53720719268
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m12(self):
        card = 537207192619
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m13(self):
        card = 5372071926172
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m14(self):
        card = 53720719261769
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m15(self):
        card = 537207192617630
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m17(self):
        card = 53720719226177635
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m18(self):
        card = 537207192261776352
        self.assertFalse(credit_card_validator(card).format(card))

    def test_m19(self):
        card = 5372071922617763518
        self.assertFalse(credit_card_validator(card).format(card))

    # Tests length boundaries for master card 2221-2720
    def test_mm10(self):
        card = 2500123464
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm11(self):
        card = 25001234670
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm12(self):
        card = 250012346780
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm13(self):
        card = 2500123467893
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm14(self):
        card = 25001234678919
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm15(self):
        card = 250012346789102
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm17(self):
        card = 25001234526789103
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm18(self):
        card = 250012345267891071
        self.assertFalse(credit_card_validator(card).format(card))

    def test_mm19(self):
        card = 25001234526789107126
        self.assertFalse(credit_card_validator(card).format(card))

    # Tests length boundaries for american express 34
    def test_am10(self):
        card = 3496863550
        self.assertFalse(credit_card_validator(card).format(card))

    def test_am11(self):
        card = 34968635564
        self.assertFalse(credit_card_validator(card).format(card))

    def test_am12(self):
        card = 349686355679
        self.assertFalse(credit_card_validator(card).format(card))

    def test_am13(self):
        card = 3496863556764
        self.assertFalse(credit_card_validator(card).format(card))

    def test_am14(self):
        card = 34968635567603
        self.assertFalse(credit_card_validator(card).format(card))

    # Found Bug 5
    def test_am16(self):
        card = 3496863585167600
        self.assertFalse(credit_card_validator(card).format(card))

    def test_am17(self):
        card = 34968635851676066
        self.assertFalse(credit_card_validator(card).format(card))

    def test_am18(self):
        card = 349686358516760612
        self.assertFalse(credit_card_validator(card).format(card))

    def test_am19(self):
        card = 3496863585167606121
        self.assertFalse(credit_card_validator(card).format(card))

    # Tests length boundaries for american express 37
    def test_aex10(self):
        card = 3796863581
        self.assertFalse(credit_card_validator(card).format(card))

    def test_aex11(self):
        card = 37968635856
        self.assertFalse(credit_card_validator(card).format(card))

    def test_aex12(self):
        card = 379686358563
        self.assertFalse(credit_card_validator(card).format(card))

    def test_aex13(self):
        card = 3796863585675
        self.assertFalse(credit_card_validator(card).format(card))

    def test_aex14(self):
        card = 37968635856763
        self.assertFalse(credit_card_validator(card).format(card))

    # Found Bug 5
    def test_aex16(self):
        card = 3796863585676094
        self.assertFalse(credit_card_validator(card).format(card))

    def test_aex17(self):
        card = 37968635856760942
        self.assertFalse(credit_card_validator(card).format(card))

    def test_aex18(self):
        card = 379686358567609426
        self.assertFalse(credit_card_validator(card).format(card))

    def test_aex19(self):
        card = 3796863585676094267
        self.assertFalse(credit_card_validator(card).format(card))

    # Tests prefix boundaries
    def test_short_v(self):
        card = 3312345678901238
        self.assertFalse(credit_card_validator(card).format(card))

    def test_short_m(self):
        card = 5012345678901236
        self.assertFalse(credit_card_validator(card).format(card))

    def test_short_m2(self):
        card = 4912345678901236
        self.assertFalse(credit_card_validator(card).format(card))

    def test_short_mm(self):
        card = 2220123456789015
        self.assertFalse(credit_card_validator(card).format(card))

    def test_short_mm2(self):
        card = 2120123456789016
        self.assertFalse(credit_card_validator(card).format(card))

    def test_short_mm3(self):
        card = 2210123456789016
        self.assertFalse(credit_card_validator(card).format(card))

    def test_short_am(self):
        card = 330987654321016
        self.assertFalse(credit_card_validator(card).format(card))

    def test_short_aex(self):
        card = 361234567890122
        self.assertFalse(credit_card_validator(card).format(card))

    def test_high_v(self):
        card = 5912345678901237
        self.assertFalse(credit_card_validator(card).format(card))

    def test_high_m(self):
        card = 5612345678901230
        self.assertFalse(credit_card_validator(card).format(card))

    def test_high_mm(self):
        card = 2721123456789019
        self.assertFalse(credit_card_validator(card).format(card))

    def test_high_mm2(self):
        card = 2729123456789011
        self.assertFalse(credit_card_validator(card).format(card))

    def test_high_mm3(self):
        card = 2702123456789019
        self.assertFalse(credit_card_validator(card).format(card))

    def test_high_am(self):
        card = 351234567890124
        self.assertFalse(credit_card_validator(card).format(card))

    def test_high_aex(self):
        card = 381234567890128
        self.assertFalse(credit_card_validator(card).format(card))

    def test_1(self):
        card = 1234567890123452
        self.assertFalse(credit_card_validator(card).format(card))

    def test_2(self):
        card = 123456789012347
        self.assertFalse(credit_card_validator(card).format(card))

    def test_3(self):
        card = 9123456789012348
        self.assertFalse(credit_card_validator(card).format(card))

    def test_4(self):
        card = 912345678901238
        self.assertFalse(credit_card_validator(card).format(card))

    def test_5(self):
        card = 6123456789012344
        self.assertFalse(credit_card_validator(card).format(card))

    def test_6(self):
        card = 612345678901231
        self.assertFalse(credit_card_validator(card).format(card))

    def test_7(self):
        card = 7123456789012342
        self.assertFalse(credit_card_validator(card).format(card))

    def test_8(self):
        card = 712345678901230
        self.assertFalse(credit_card_validator(card).format(card))

    def test_9(self):
        card = 8123456789012340
        self.assertFalse(credit_card_validator(card).format(card))

    def test_10(self):
        card = 812345678901239
        self.assertFalse(credit_card_validator(card).format(card))


if __name__ == '__main__':
    unittest.main()