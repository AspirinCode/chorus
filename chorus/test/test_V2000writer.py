#
# (C) 2014-2017 Seiji Matsuoka
# Licensed under the MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import unittest

from chorus.demo import MOL
import chorus.v2000reader as reader
import chorus.v2000writer as writer


class TestV2000Writer(unittest.TestCase):
    @unittest.skip("")
    def test_sdf(self):
        compound = reader.mol_from_text(MOL["Phe"])
        print(writer.mols_to_text([compound]))
