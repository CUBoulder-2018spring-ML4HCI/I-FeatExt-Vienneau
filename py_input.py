import argparse
import math
import time

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
from pythonosc import osc_bundle_builder

SMOOTHING = 10
last_x = []
last_y = []
last_z = []

def avg(x, y, z):
    global last_x
    global last_y
    global last_z
    last_x.append(x)
    last_y.append(y)
    last_z.append(z)
    if len(last_x) == SMOOTHING:
        client = udp_client.SimpleUDPClient("127.0.0.1", 6448)
        x = sum(last_x)/len(last_x)
        y = sum(last_y)/len(last_y)
        z = sum(last_z)/len(last_z)

        last_x = []
        last_y = []
        last_z = []
        client.send_message("/wek/inputs", [x, y, z])

def feature_extract(*args):
    client = udp_client.SimpleUDPClient("127.0.0.1", 6448)
    # arg[1:4] will get just the accelerometer data -- cut out all
    # other TouchOSC data
    accel = args[1:4]
    # Smoothing
    avg(accel[0], accel[1], accel[2])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=6449, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/filter", feature_extract)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
