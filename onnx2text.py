import sys
import onnx
from onnx import helper

if len(sys.argv) != 3:
    print("no enough args")
    quit()

model = onnx.load(sys.argv[1])

with open(sys.argv[2], "w") as f:
    f.write(helper.printable_graph(model.graph))

