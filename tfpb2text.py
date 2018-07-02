import tensorflow
import sys
from google.protobuf import text_format

if len(sys.argv) != 3:
    print("no enough args")
    quit()

graph_def = tensorflow.GraphDef()

with tensorflow.gfile.FastGFile(sys.argv[1], 'rb') as f:
    graph_def.ParseFromString(f.read())

with tensorflow.gfile.FastGFile(sys.argv[2], 'w') as f:
    f.write(text_format.MessageToString(graph_def))

