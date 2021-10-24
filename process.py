import requests
import pandas as pd
import csv
import pandas as pd
import io
import requests

#Data from the WiFi scanner is uploaded to our API and accessed with get request.
#TODO: replace with calls every 5 seconds
url = "https://retoolapi.dev/vyF7BE/signals"
s=requests.get(url).content
print(s)
data=pd.read_csv(url, sep='\n')

loss_factor = -30
strength = 2

def get_dists():
    dists = []
    for d in data.groupby():
        rssi = d['rssi']
        distance_to_beacon = 10**((loss_factor - (rssi))/(10 * strength))
        dists.append(distance_to_beacon)
    return dists

def trilateration(P1, P2, P3, r1, r2, r3):
  p1 = np.array([0, 0, 0])
  p2 = np.array([P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]])
  p3 = np.array([P3[0] - P1[0], P3[1] - P1[1], P3[2] - P1[2]])
  v1 = p2 - p1
  v2 = p3 - p1

  Xn = (v1)/np.linalg.norm(v1)

  tmp = np.cross(v1, v2)

  Zn = (tmp)/np.linalg.norm(tmp)

  Yn = np.cross(Xn, Zn)

  i = np.dot(Xn, v2)
  d = np.dot(Xn, v1)
  j = np.dot(Yn, v2)

  X = ((r1**2)-(r2**2)+(d**2))/(2*d)
  Y = (((r1**2)-(r3**2)+(i**2)+(j**2))/(2*j))-((i/j)*(X))
  Z1 = np.sqrt(max(0, r1**2-X**2-Y**2))
  Z2 = -Z2

  K1 = P1 + X * Xn + Y * Yn + Z1 * Zn
  K2 = P1 + X * Xn + Y * Yn + Z2 * Zn
  return K1,K2

dists = get_dists()
  
