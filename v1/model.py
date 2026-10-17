# Home plan v1 - single source of truth. Units: feet.
# X = distance from EAST boundary (0) toward WEST (21).  Y = distance from ROAD (north, 0) toward BACK (south, ~106).
T9, T4 = 0.75, 0.375
FF_LEVEL = 11.5          # proposed floor-to-floor (23 risers of 6")
PLOT = [(0,0),(21,0),(21,105.0),(1,106.0),(1,89.0),(0,89.0)]

# ---------- walls: id, x1,x2,y1,y2, kind, height, description ----------
# kind: outer(9"), part(4.5"), comp(compound 4.5"), para(parapet 4.5"), exist(existing, not ours)
WALLS = {
 'G': [
  ('BW-04', 0,0.75, 0,0.75, 'pillar', 6, 'Gate pillar, east'),
  ('BW-05', 15.0,15.75, 0,0.75, 'pillar', 6, 'Gate pillar, between the two gates'),
  ('BW-06', 20.25,21.0, 0,0.75, 'pillar', 6, 'Gate pillar, west'),
  ('BW-01', 0,0.375, 0.75,89.375, 'comp', 6, 'East compound wall, front part (new)'),
  ('BW-02', 0,1.375, 89.0,89.375, 'comp', 6, 'East compound wall, 1\' step at the back'),
  ('BW-03', 1.0,1.375, 89.375,105.95, 'comp', 6, 'East compound wall, back part (new)'),
  ('GW-01', 2.75,3.5, 40.5,75.75, 'outer', 10.5, 'East outer wall of foyer, living, kitchen, toilet 2'),
  ('GW-02', 2.75,8.5, 40.5,41.25, 'outer', 10.5, 'Main door wall, between porch and foyer'),
  ('GW-03', 8.5,9.25, 30.75,41.25, 'outer', 10.5, 'Porch-side wall of study and bedroom 1'),
  ('GW-04', 8.5,21.0, 30.75,31.5, 'outer', 10.5, 'Front wall of study and toilet 1, facing parking'),
  ('GW-05', 20.25,21.0, 30.75,95.0, 'outer', 10.5, 'West outer wall, on the boundary (apartment side)'),
  ('GW-06', 2.75,10.25, 75.0,75.75, 'outer', 10.5, 'Back wall of toilet 2, facing side garden'),
  ('GW-07', 9.5,10.25, 69.625,95.0, 'outer', 10.5, 'East wall of stair hall and bedroom 2, facing side garden'),
  ('GW-08', 9.5,21.0, 94.25,95.0, 'outer', 10.5, 'Back wall of bedroom 2, facing back garden'),
  ('GW-09', 8.875,9.25, 41.25,46.375, 'part', 10.5, 'Foyer | bedroom 1'),
  ('GW-10', 13.75,14.125, 31.5,36.0, 'part', 10.5, 'Study | toilet 1'),
  ('GW-11', 13.75,20.25, 36.0,36.375, 'part', 10.5, 'Toilet 1 | bedroom 1'),
  ('GW-12', 8.875,20.25, 46.375,46.75, 'part', 10.5, 'Bedroom 1 | living room'),
  ('GW-13', 3.5,20.25, 60.75,61.125, 'part', 10.5, 'Living room | kitchen and dining (arch O-01)'),
  ('GW-14', 3.5,9.5, 69.625,70.0, 'part', 10.5, 'Kitchen | toilet 2'),
  ('GW-15', 10.25,20.25, 80.125,80.5, 'part', 10.5, 'Stair hall | bedroom 2'),
 ],
 'F': [
  ('FW-01', 9.5,10.25, 73.0,97.25, 'outer', 10.0, 'East wall of landing and bedroom 3'),
  ('FW-02', 9.5,21.0, 73.0,73.75, 'outer', 10.0, 'Front wall of landing, facing terrace'),
  ('FW-03', 20.25,21.0, 73.0,97.25, 'outer', 10.0, 'West wall, on the boundary'),
  ('FW-04', 9.5,21.0, 96.5,97.25, 'outer', 10.0, 'Back wall of bedroom 3 (projects 2\'3" past bedroom 2 below)'),
  ('FW-05', 10.25,20.25, 79.75,80.125, 'part', 10.0, 'Landing | bedroom 3 lobby and toilet 3'),
  ('FW-06', 13.875,14.25, 80.125,84.75, 'part', 10.0, 'Bedroom 3 lobby | toilet 3'),
  ('FW-07', 14.25,20.25, 84.375,84.75, 'part', 10.0, 'Toilet 3 | bedroom 3'),
  ('PW-01', 2.75,11.667, 15.5,15.875, 'para', 3, 'Front parapet of balcony 2'),
  ('PW-02', 2.75,3.125, 15.5,80.375, 'para', 3, 'East parapet of balcony, terrace and terrace corner'),
  ('PW-03', 11.667,21.0, 19.75,20.125, 'para', 3, 'Front parapet of terrace, behind staircase 1'),
  ('PW-04', 20.625,21.0, 20.125,73.0, 'para', 3, 'West parapet of terrace'),
  ('PW-05', 3.125,9.5, 80.0,80.375, 'para', 3, 'Back parapet of terrace corner'),
 ]}

# ---------- rooms / areas: id, name, polygon or rect, kind ----------
def R(x1,x2,y1,y2): return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
def back_y(x): return 106.0-(x-1)/20.0           # back boundary line
ROOMS = {
 'G': [
  ('G-01','Parking',R(0.375,21.0,0.75,30.75),'out'),
  ('G-02','Porch',R(2.75,8.5,30.75,40.5),'porch'),
  ('G-03','Foyer',R(3.5,8.875,41.25,46.75),'in'),
  ('G-04','Living room',R(3.5,20.25,46.75,60.75),'in'),
  ('G-05','Bedroom 1',R(9.25,20.25,36.375,46.375),'bed'),
  ('G-06','Study',R(9.25,13.75,31.5,36.375),'bed'),
  ('G-07','Toilet 1',R(14.125,20.25,31.5,36.0),'wet'),
  ('G-08','Kitchen',R(3.5,13.5,61.125,69.625),'kit'),
  ('G-09','Dining',R(13.5,20.25,61.125,70.0),'in'),
  ('G-10','Stair hall',R(10.25,20.25,70.0,80.125),'in'),
  ('G-11','Toilet 2',R(3.5,9.5,70.0,75.0),'wet'),
  ('G-12','Bedroom 2',R(10.25,20.25,80.5,94.25),'bed'),
  ('G-13','Side passage',R(0.375,2.75,30.75,75.75),'out'),
  ('G-14','Side garden',[(0.375,75.75),(9.5,75.75),(9.5,back_y(9.5)-0.375),(1.375,back_y(1.375)-0.375),(1.375,89.375),(0.375,89.375)],'garden'),
  ('G-15','Back garden',[(9.5,95.0),(21.0,95.0),(21.0,back_y(21)-0.375),(9.5,back_y(9.5)-0.375)],'garden'),
 ],
 'F': [
  ('F-01','Balcony 2',R(3.125,11.667,15.875,20.125),'terr'),
  ('F-02','Open terrace',R(3.125,20.625,20.125,73.0),'terr'),
  ('F-03','Terrace corner',R(3.125,9.5,73.0,80.0),'terr'),
  ('F-04','Stair landing',R(10.25,20.25,73.75,79.75),'in'),
  ('F-05','Bedroom 3',R(10.25,20.25,84.75,96.5),'bed'),
  ('F-06','Bedroom 3 lobby',R(10.25,13.875,80.125,84.75),'bed'),
  ('F-07','Toilet 3',R(14.25,20.25,80.125,84.375),'wet'),
 ]}

# ---------- openings: id, floor, wall, a, b (along wall), type, hinge('a'|'b'), swing(+/-), height, sill, note ----------
# type: door, double, window, vent, arch, gate
OPENINGS = [
 ('D-01','G','GW-02', 4.25,8.25,'double',None,'+', 7.0,0,'Main door, double leaf, opens into foyer'),
 ('D-02','G','GW-12', 9.5,12.5,'door','a','-', 7.0,0,'Bedroom 1 door, from living room'),
 ('D-03','G','GW-11', 14.5,17.0,'door','a','-', 7.0,0,'Toilet 1 door, from bedroom 1'),
 ('O-01','G','GW-13', 13.75,18.75,'arch',None,None, 7.0,0,'Arch from living room to dining'),
 ('D-04','G','GW-07', 71.0,73.5,'door','a','-', 7.0,0,'Toilet 2 door, from stair hall, opens inward'),
 ('D-05','G','GW-07', 76.25,79.25,'door','b','-', 7.0,0,'Garden door, stair hall to side garden'),
 ('D-06','G','GW-15', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 2 door, from stair hall'),
 ('W-01','G','GW-04', 9.75,13.25,'window',None,None, 4.0,3.0,'Study window to parking'),
 ('V-01','G','GW-04', 16.25,18.25,'vent',None,None, 1.5,6.0,'Toilet 1 ventilator'),
 ('W-02','G','GW-03', 37.0,40.25,'window',None,None, 4.0,3.0,'Bedroom 1 window to porch'),
 ('W-03','G','GW-01', 42.5,45.5,'window',None,None, 4.0,3.0,'Foyer window to side passage'),
 ('W-04','G','GW-01', 48.25,52.25,'window',None,None, 4.0,3.0,'Living room window 1'),
 ('W-05','G','GW-01', 55.0,59.0,'window',None,None, 4.0,3.0,'Living room window 2'),
 ('W-06','G','GW-01', 63.0,67.0,'window',None,None, 3.5,3.5,'Kitchen window over counter'),
 ('V-02','G','GW-01', 71.5,73.5,'vent',None,None, 1.5,6.0,'Toilet 2 ventilator'),
 ('W-07','G','GW-07', 84.5,88.5,'window',None,None, 4.0,3.0,'Bedroom 2 side window to side garden'),
 ('W-08','G','GW-08', 13.0,17.5,'window',None,None, 4.0,3.0,'Bedroom 2 back window to back garden'),
 ('GT-01','G','FRONT', 0.375,15.0,'gate',None,None, 6.0,0,'Main gate, 14\'7" (sliding)'),
 ('GT-02','G','FRONT', 15.75,20.25,'gate',None,None, 6.0,0,'Side gate, 4\'6", leads to staircase 1'),
 ('D-07','F','FW-05', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 3 door, from landing'),
 ('D-08','F','FW-06', 80.75,83.25,'door','a','+', 7.0,0,'Toilet 3 door, from bedroom 3 lobby'),
 ('D-09','F','FW-01', 74.5,77.5,'door','a','-', 7.0,0,'Landing door to terrace corner'),
 ('W-09','F','FW-02', 13.0,16.5,'window',None,None, 4.0,3.0,'Landing window to terrace'),
 ('W-10','F','FW-01', 88.0,92.0,'window',None,None, 4.0,3.0,'Bedroom 3 side window'),
 ('W-11','F','FW-04', 13.0,17.5,'window',None,None, 4.0,3.0,'Bedroom 3 back window'),
]
