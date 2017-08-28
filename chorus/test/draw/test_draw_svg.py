#
# (C) 2014-2017 Seiji Matsuoka
# Licensed under the MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import unittest

from chorus.draw.svg import SVG
from chorus import v2000reader as reader
from chorus.demo import MOL


class TestDraw(unittest.TestCase):
    def test_draw_mol(self):
        compound = reader.mol_from_text(MOL["demo"])
        # compound = reader.mol_from_text(MOL["Phe"])  # Small
        # compound = reader.mol_from_text(MOL["Goserelin"])  # Large
        # compound = reader.mol_from_text(MOL["CyclosporinA"])  # Atypical bond len
        # compound = reader.mol_from_text(MOL["Carbidopa"])  # Isolated components
        # compound = reader.mol_from_text(MOL["Gadodiamide"])  # Charged
        # compound = reader.mol_from_text(MOL["Premarin"])  # Stereo
        # compound = reader.mol_from_text(MOL["Nitroprusside"])  # Transition metal
        # compound = reader.mol_from_text(MOL["Fondaparinux"])  # Multi-line props
        # compound = reader.mol_from_text(MOL["KCl"])  # No bond, width = 0
        # compound = reader.mol_from_text(MOL["Cyanocobalamin"])
        svg = SVG(compound)
        # svg.save("docs/_static/demo.svg")
