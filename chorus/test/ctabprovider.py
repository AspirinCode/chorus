#
# (C) 2014-2017 Seiji Matsuoka
# Licensed under the MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import glob
import os

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "../../resources/")

CTABS = {}
for path in glob.glob(os.path.join(RESOURCE_DIR, "ctabfiles/*.mol")):
    name = os.path.basename(path).split(".")[0]
    with open(path) as file:
        CTABS[name] = file.read()

for path in glob.glob(os.path.join(RESOURCE_DIR, "DrugBank/*.mol")):
    name = os.path.basename(path).split(".")[0]
    with open(path) as file:
        CTABS[name] = file.read()

for path in glob.glob(os.path.join(RESOURCE_DIR, "PubChem/*.mol")):
    name = os.path.basename(path).split(".")[0]
    with open(path) as file:
        CTABS[name] = file.read()
