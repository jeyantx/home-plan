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
  ('BW-05', 12.0,13.5, 0,1.5, 'planter', 4, 'Planter pillar in front of the neem tree (flowering plant on top), between the gates'),
  ('BW-06', 20.25,21.0, 0,0.75, 'pillar', 6, 'Gate post at the west boundary, for the small gate'),
  ('BW-01', 0,0.375, 0.75,89.375, 'comp', 6, 'East compound wall, front part (new)'),
  ('BW-02', 0,1.375, 89.0,89.375, 'comp', 6, 'East compound wall, 1\' step at the back'),
  ('BW-03', 1.0,1.375, 89.375,105.95, 'comp', 6, 'East compound wall, back part (new)'),
  ('GW-01', 2.75,3.5, 40.5,73.75, 'outer', 10.5, 'East outer wall of foyer, living, kitchen, toilet 2'),
  ('GW-02', 2.75,8.5, 40.5,41.25, 'outer', 10.5, 'Main door wall, between porch and foyer'),
  ('GW-03', 8.5,9.25, 30.75,41.25, 'outer', 10.5, 'Porch-side wall of study and bedroom 1'),
  ('GW-04', 8.5,21.0, 30.75,31.5, 'outer', 10.5, 'Front wall of study and toilet 1, facing parking'),
  ('GW-05', 20.25,21.0, 30.75,95.125, 'outer', 10.5, 'West outer wall, on the boundary (apartment side)'),
  ('GW-06', 2.75,10.25, 73.0,73.75, 'outer', 10.5, 'Back wall of toilet 2, facing side garden'),
  ('GW-07', 9.5,10.25, 73.0,95.125, 'outer', 10.5, 'East wall of stair hall and bedroom 2, facing side garden'),
  ('GW-16', 9.875,10.25, 67.625,73.0, 'part', 10.5, 'Toilet 2 | stair hall (partition, inside the house)'),
  ('GW-08', 9.5,21.0, 94.375,95.125, 'outer', 10.5, 'Back wall of bedroom 2, facing back garden'),
  ('GW-09', 8.875,9.25, 41.25,46.375, 'part', 10.5, 'Foyer | bedroom 1'),
  ('GW-10', 13.75,14.125, 31.5,36.0, 'part', 10.5, 'Study | toilet 1'),
  ('GW-11', 13.75,20.25, 36.0,36.375, 'part', 10.5, 'Toilet 1 | bedroom 1'),
  ('GW-12', 8.875,20.25, 46.375,46.75, 'part', 10.5, 'Bedroom 1 | living room'),
  ('GW-13', 3.5,20.25, 58.75,59.125, 'part', 10.5, 'Living room | kitchen and dining (arch O-01)'),
  ('GW-14', 3.5,9.875, 67.625,68.0, 'part', 10.5, 'Kitchen | toilet 2'),
  ('GW-15', 10.25,20.25, 80.25,80.625, 'part', 10.5, 'Stair hall | bedroom 2'),
 ],
 'F': [
  ('FW-01', 9.5,10.25, 73.125,97.375, 'outer', 10.0, 'East wall of landing and bedroom 3'),
  ('FW-02', 9.5,21.0, 73.125,73.875, 'outer', 10.0, 'Front wall of landing; 53\' from PW-03 (future hall back wall)'),
  ('FW-03', 20.25,21.0, 73.125,97.375, 'outer', 10.0, 'West wall, on the boundary'),
  ('FW-04', 9.5,21.0, 96.625,97.375, 'outer', 10.0, 'Back wall of bedroom 3 (projects 2\'3" past bedroom 2 below)'),
  ('FW-05', 10.25,20.25, 79.875,80.25, 'part', 10.0, 'Landing | bedroom 3 lobby and toilet 3'),
  ('FW-06', 13.875,14.25, 80.25,84.875, 'part', 10.0, 'Bedroom 3 lobby | toilet 3'),
  ('FW-07', 14.25,20.25, 84.5,84.875, 'part', 10.0, 'Toilet 3 | bedroom 3'),
  ('PW-01', 2.75,11.667, 15.5,15.875, 'para', 3, 'Front parapet of balcony 2'),
  ('PW-02', 2.75,3.125, 15.5,77.875, 'para', 3, 'East parapet of balcony, terrace and terrace corner'),
  ('PW-03', 11.667,21.0, 19.75,20.125, 'para', 3, 'Front parapet of terrace, behind staircase 1'),
  ('PW-04', 20.625,21.0, 20.125,73.125, 'para', 3, 'West parapet of terrace'),
  ('PW-05', 3.125,9.5, 77.5,77.875, 'para', 3, 'Back parapet of terrace corner'),
 ]}

# ---------- rooms / areas: id, name, polygon or rect, kind ----------
def R(x1,x2,y1,y2): return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
def back_y(x): return 106.0-(x-1)/20.0           # back boundary line
ROOMS = {
 'G': [
  ('G-01','Parking',R(0.375,21.0,0.75,30.75),'out'),
  ('G-02','Porch',R(2.75,8.5,30.75,40.5),'porch'),
  ('G-03','Foyer',R(3.5,8.875,41.25,46.75),'in'),
  ('G-04','Living room',R(3.5,20.25,46.75,58.75),'in'),
  ('G-05','Bedroom 1',R(9.25,20.25,36.375,46.375),'bed'),
  ('G-06','Study',R(9.25,13.75,31.5,36.375),'bed'),
  ('G-07','Toilet 1',R(14.125,20.25,31.5,36.0),'wet'),
  ('G-08','Kitchen',R(3.5,13.5,59.125,67.625),'kit'),
  ('G-09','Open area (future dining)',R(13.5,20.25,59.125,68.0),'in'),
  ('G-10','Stair hall',R(10.25,20.25,68.0,80.25),'in'),
  ('G-11','Toilet 2',R(3.5,9.875,68.0,73.0),'wet'),
  ('G-12','Bedroom 2',R(10.25,20.25,80.625,94.375),'bed'),
  ('G-13','Side passage',R(0.375,2.75,30.75,73.75),'out'),
  ('G-14','Side garden',[(0.375,73.75),(9.5,73.75),(9.5,back_y(9.5)-0.375),(1.375,back_y(1.375)-0.375),(1.375,89.375),(0.375,89.375)],'garden'),
  ('G-15','Back garden',[(9.5,95.125),(21.0,95.125),(21.0,back_y(21)-0.375),(9.5,back_y(9.5)-0.375)],'garden'),
 ],
 'F': [
  ('F-01','Balcony 2',R(3.125,11.667,15.875,20.125),'terr'),
  ('F-02','Open terrace',R(3.125,20.625,20.125,73.125),'terr'),
  ('F-03','Terrace corner',R(3.125,9.5,73.125,77.5),'terr'),
  ('F-04','Stair landing',R(10.25,20.25,73.875,79.875),'in'),
  ('F-05','Bedroom 3',R(10.25,20.25,84.875,96.625),'bed'),
  ('F-06','Bedroom 3 lobby',R(10.25,13.875,80.25,84.875),'bed'),
  ('F-07','Toilet 3',R(14.25,20.25,80.25,84.5),'wet'),
 ]}

# ---------- openings: id, floor, wall, a, b (along wall), type, hinge('a'|'b'), swing(+/-), height, sill, note ----------
# type: door, double, window, vent, arch, gate
OPENINGS = [
 ('D-01','G','GW-02', 4.25,8.25,'double',None,'+', 7.0,0,'Main door, double leaf, opens into foyer'),
 ('D-02','G','GW-12', 9.5,12.5,'door','a','-', 7.0,0,'Bedroom 1 door, from living room'),
 ('D-03','G','GW-11', 14.5,17.0,'door','a','-', 7.0,0,'Toilet 1 door, from bedroom 1'),
 ('O-01','G','GW-13', 13.75,18.75,'arch',None,None, 7.0,0,'Arch from living room to dining'),
 ('W-12','G','GW-13', 5.5,11.5,'fold',None,None, 4.0,3.0,'Folding glass window, kitchen to living. Opens left and right; curtain on the living side'),
 ('D-04','G','GW-16', 69.0,71.5,'door','a','-', 7.0,0,'Toilet 2 door, from stair hall, opens inward'),
 ('D-05','G','GW-07', 74.75,77.75,'door','b','-', 7.0,0,'Garden door, stair hall to side garden'),
 ('D-06','G','GW-15', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 2 door, from stair hall'),
 ('W-01','G','GW-04', 9.75,13.25,'window',None,None, 4.0,3.0,'Study window to parking'),
 ('V-01','G','GW-04', 16.25,18.25,'vent',None,None, 1.5,6.0,'Toilet 1 ventilator'),
 ('W-02','G','GW-03', 37.0,40.25,'window',None,None, 4.0,3.0,'Bedroom 1 window to porch'),
 ('W-03','G','GW-01', 42.5,45.5,'window',None,None, 4.0,3.0,'Foyer window to side passage'),
 ('W-04','G','GW-01', 48.0,52.0,'window',None,None, 4.0,3.0,'Living room window 1'),
 ('W-05','G','GW-01', 53.75,57.75,'window',None,None, 4.0,3.0,'Living room window 2'),
 ('W-06','G','GW-01', 61.0,65.0,'window',None,None, 3.5,3.5,'Kitchen window over counter'),
 ('V-02','G','GW-01', 69.5,71.5,'vent',None,None, 1.5,6.0,'Toilet 2 ventilator'),
 ('W-07','G','GW-07', 85.0,89.0,'window',None,None, 4.0,3.0,'Bedroom 2 side window to side garden'),
 ('W-08','G','GW-08', 14.75,19.25,'window',None,None, 4.0,3.0,'Bedroom 2 back window to back garden'),
 ('D-10','G','GW-08', 10.75,13.5,'door','a','-', 7.0,0,'Bedroom 2 back door to back garden'),
 ('GT-01','G','FRONT', 0.75,12.0,'gate',None,'+', 6.0,0,'Large gate, 11\'3", double leaf, east of the planter pillar'),
 ('GT-02','G','FRONT', 13.5,20.25,'gate',None,'-', 6.0,0,'Small gate, 6\'9", double leaf, opens out toward the road, west of the planter pillar'),
 ('D-07','F','FW-05', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 3 door, from landing'),
 ('D-08','F','FW-06', 81.0,83.5,'door','a','+', 7.0,0,'Toilet 3 door, from bedroom 3 lobby'),
 ('D-09','F','FW-01', 74.25,77.25,'door','a','-', 7.0,0,'Landing door to terrace corner'),
 ('W-09','F','FW-02', 13.0,16.5,'window',None,None, 4.0,3.0,'Landing window to terrace'),
 ('W-10','F','FW-01', 88.5,92.5,'window',None,None, 4.0,3.0,'Bedroom 3 side window'),
 ('W-11','F','FW-04', 13.0,17.5,'window',None,None, 4.0,3.0,'Bedroom 3 back window'),
]

# ---------- building outlines (outer wall faces) for built-up area ----------
GF_OUTLINE=[(8.5,30.75),(21,30.75),(21,95.125),(9.5,95.125),(9.5,73.75),(2.75,73.75),(2.75,40.5),(8.5,40.5)]
FF_OUTLINE=R(9.5,21.0,73.125,97.375)
BRANCH_NOTES='''<section class="ask"><h2>Proposal v3: furniture, fixtures, types</h2>
<ol>
<li><b>Hover</b> over any item to see its name.</li>
<li><b>Kitchen:</b> burner FU-52 at window W-06, with a slim chimney ducted out above the window. Sink FU-51 near the GW-14 corner. Fridge FU-18 against GW-13. The back counter FU-16 is now full length and modular. Overhead shelves above both counters: FU-19, FU-19.2, FU-19.3.</li>
<li><b>Living:</b> FU-03.2 starts where FU-03.1 ends, so every seat is usable.</li>
<li><b>Bedroom 1 AC outdoor FU-45</b> is on GW-04, above study window W-01.</li>
<li><b>Side garden tap area FU-53</b> is in the corner of BW-02 and BW-03.</li>
<li><b>Store FU-56</b> is only at the low end of staircase 1. The top part stays open, and the car is back in its earlier place.</li>
<li><b>Small gate GT-02</b> is double leaf, 6'9", and opens out toward the road. There is no west wall, just a gate post BW-06 at the boundary.</li>
<li><b>Toilet 2:</b> being redesigned from online research (next update).</li>
</ol></section>
<section class="ask"><h2>Layout (final): approved changes</h2>
<ol>
<li><b>Living room</b> is 12' deep (was 14').</li>
<li><b>GW-16</b>, the wall between toilet 2 and the stair hall, is a 4½" partition.</li>
<li><b>53' rule:</b> PW-03 to FW-02 is exactly 53'. That fixes the spiral stair and bedroom 3 block in place, so the stair hall absorbs the 2' from the living room and is now 12'3" deep.</li>
<li>Foyer, house position, bedroom 2 (13'9") and garden door D-05 are as before.</li>
<li><b>Bedroom 2 back door D-10</b> to the back garden; window W-08 moves to the west part of that wall.</li>
<li>The bikes are shown in the parking.</li>
</ol></section>
'''

# ---------- existing features ----------
BOREWELL=(6.0, back_y(6.0)-25.0)   # given: 25' from the back (south) boundary, 6' from the east boundary

# ---------- drawing positions (layout specific) ----------
LABELPOS={'G-01':(8.0,24.5),'G-02':(5.6,37.6),'G-03':(6.2,44.6),'G-04':(11.5,53.0),'G-05':(11.45,39.4),'G-06':(11.5,33.6),'G-07':(17.2,33.4),
          'G-08':(8.0,63.4),'G-09':(16.3,66.7),'G-10':(15.0,71.0),'G-11':(6.0,70.6),'G-12':(16.2,92.8),'G-13':(1.55,36.0),'G-14':(5.0,94.0),'G-15':(15.2,100.2),
          'F-01':(7.4,18.6),'F-02':(11.9,47.0),'F-03':(5.6,75.4),'F-04':(12.15,78.0),'F-05':(15.9,95.3),'F-06':(12.05,82.9),'F-07':(17.25,82.5)}
LABELSIZE={'G-05':0.42,'G-12':0.42,'F-05':0.42,'G-09':0.4,'G-13':0.36,'G-06':0.4,'G-07':0.42,'G-11':0.42,'G-03':0.42,'G-02':0.42,'F-06':0.36,'F-07':0.42,'G-10':0.42,'F-04':0.45,'F-03':0.42,'F-01':0.45,'G-09':0.45,'G-01':0.6,'F-02':0.8}
TAGPOS={'GW-01':(3.125,53.0),'GW-05':(20.625,51.0),'GW-07':(9.875,91.5),'BW-01':(0.19,50.0),'GW-04':(19.0,31.125),'GW-13':(12.62,58.94),'GW-12':(17.6,46.56),
        'GW-03':(8.875,33.6),'GW-02':(3.6,40.875),'GW-11':(19.0,36.19),'GW-08':(11.0,94.75),'GW-06':(8.2,73.375),'GW-16':(10.06,72.2),'PW-02':(2.94,40.0),'PW-04':(20.81,40.0),
        'FW-01':(9.875,94.0),'FW-03':(20.625,92.0),'FW-02':(18.4,73.5),'FW-04':(19.0,97.0),'FW-05':(18.0,80.06),'PW-03':(19.4,19.94),'PW-01':(5.0,15.69),'PW-05':(6.0,77.69),
        'GW-15':(18.4,80.44),'GW-14':(5.0,67.81),'GW-10':(13.94,34.6),'GW-09':(9.06,43.0),'BW-03':(1.19,98.0),'BW-02':(0.6,89.19)}
OPENTAGOFF={'W-01':-0.75,'V-01':-0.75,'W-02':0.9,'W-03':-1.0,'W-04':-1.0,'W-05':-1.0,'W-06':-1.0,'V-02':-1.0,'W-07':-1.0,'W-08':0.8,'D-01':-1.4,'D-02':-2.2,'D-03':-1.6,
            'O-01':-0.8,'D-04':-2.6,'D-05':-1.5,'D-06':1.7,'D-07':1.7,'D-08':1.6,'D-09':-1.6,'W-09':-0.8,'W-10':-1.0,'W-11':0.8,'W-12':-0.85,'D-10':0.9}
SPC=(17.0,76.875); SPR=3.0
CH_G_E=[0,30.75,40.5,41.25,46.75,58.75,59.125,67.625,68.0,73.0,73.75,89.0,106.0]
CH_G_W=[0,4.333,16.0,19.5,30.75,31.5,36.0,36.375,46.375,46.75,58.75,59.125,68.0,80.25,80.625,94.375,95.125,105.0]
CH_G_BACK_Y=104.0
CH_F_W=[15.5,20.125,73.125,73.875,79.875,80.25,84.5,84.875,96.625,97.375]
CH_F_BACK_Y=98.6

# ---------- furniture and fixtures (proposal) ----------
# id, floor, name, x1, x2, y1, y2, kind, side, note
# side = which edge is the head (bed) / back (sofa, WC): 'x1','x2','y1','y2'. Y grows toward the back.
FURNITURE = [
 ('FU-01','G','Shoe rack',7.25,8.5,33.5,36.5,'cab',None,'Porch, 3\' x 1\'3", against GW-03'),
 ('FU-02','G','Console with mirror',8.0,8.875,43.5,46.25,'cab',None,'Foyer, keys and mirror'),
 ('FU-03.1','G','3-seat sofa',3.5,6.0,48.0,54.25,'sofa','x1','Living, 6\'3" x 2\'6", back to GW-01 under the windows'),
 ('FU-03.2','G','2-seat sofa',6.0,10.25,54.25,56.75,'sofa','y2','Living, 4\'3" x 2\'6", starts where FU-03.1 ends so both seats are free; 2\' walkway behind it'),
 ('FU-04','G','Coffee table',6.75,9.75,49.5,53.0,'table',None,'Living, 3\' x 3\'6"'),
 ('FU-05','G','TV, showcase and bookshelf wall unit',18.917,20.25,47.25,58.25,'tvwall',None,'Living, 11\' x 1\'4", full height on GW-05: TV in the middle, showcase and book shelves on both sides'),
 ('FU-06','G','Queen bed',13.75,20.25,41.25,46.25,'bed','x2','Bedroom 1, 6\'6" x 5\', head to GW-05 (east-west), side against GW-12'),
 ('FU-09.1','G','Wardrobe, part 1',17.25,20.25,36.375,38.375,'ward',None,'Bedroom 1, 3\' x 2\' on GW-11, with loft'),
 ('FU-09.2','G','Wardrobe, part 2',18.25,20.25,38.375,41.125,'ward',None,'Bedroom 1, 2\'9" x 2\' on GW-05; L-shape with part 1, total 5\'9"'),
 ('FU-10','G','Study desk',9.5,13.5,31.5,33.5,'desk',None,'Study, 4\' x 2\', under W-01'),
 ('FU-11','G','Bookshelf',12.5,13.75,33.75,36.25,'shelf',None,'Study, on GW-10'),
 ('FU-12','G','Western WC',18.0,20.25,33.9,35.4,'wc','x2','Toilet 1, wall-mounted cistern'),
 ('FU-13','G','Wash basin',14.125,15.5,31.5,32.9,'basin',None,'Toilet 1'),
 ('FU-14','G','Shower area',17.25,20.25,31.5,33.6,'shower',None,'Toilet 1, geyser above'),
 ('FU-15','G','Kitchen counter, east',3.5,5.5,59.125,67.625,'counter',None,'Kitchen, 8\'6" x 2\' on GW-01'),
 ('FU-16','G','Kitchen counter, back (modular)',5.5,9.875,65.625,67.625,'counter',None,'Kitchen, 4\'4½" x 2\' on GW-14, with base drawers'),
 ('FU-17','G','Breakfast counter',6.0,11.5,59.125,60.375,'counter2',None,'Kitchen, 5\'6" x 1\'3", under the folding glass W-12'),
 ('FU-18','G','Fridge',11.5,13.75,59.125,61.625,'fridge',None,'Kitchen, single door, back against GW-13 beside the breakfast counter'),
 ('FU-19','G','Overhead shelves, back',5.5,9.875,66.375,67.625,'over',None,'Kitchen, above the back counter (dashed)'),
 ('FU-19.2','G','Overhead shelves, east',3.5,4.75,65.0,67.625,'over',None,'Kitchen, above the east counter beside the window (dashed)'),
 ('FU-19.3','G','Overhead shelves, east',3.5,4.75,59.125,61.0,'over',None,'Kitchen, above the east counter beside the window (dashed)'),
 ('FU-25','G','Store cupboard, full height',17.75,20.25,59.5,67.5,'store2',None,'Open area, 8\' x 2\'6", floor to ceiling, on GW-05 (no separate store room)'),
 ('FU-26','G','Indian WC',3.75,5.75,68.5,70.75,'iwc',None,'Toilet 2, Indian (squat) pan'),
 ('FU-27','G','Wash basin',7.75,9.25,71.6,73.0,'basin',None,'Toilet 2'),
 ('FU-28','G','Shower area',3.5,6.75,71.0,73.0,'shower',None,'Toilet 2, geyser above'),
 ('FU-29','G','Washing machine',3.25,5.25,74.25,76.25,'wm',None,'Side garden utility, covered by the terrace corner'),
 ('FU-30','G','Wash basin with tap',5.5,7.0,74.25,75.5,'basin',None,'Side garden, next to garden door D-05'),
 ('FU-31','G','Queen bed',13.75,20.25,85.0,90.0,'bed','x2','Bedroom 2, head to GW-05'),
 ('FU-32','G','Side table',18.75,20.25,83.25,84.75,'cab',None,'Bedroom 2'),
 ('FU-33','G','Side table',18.75,20.25,90.25,91.75,'cab',None,'Bedroom 2'),
 ('FU-34','G','Wardrobe with loft',14.0,20.25,80.625,82.625,'ward',None,'Bedroom 2, 6\'3" x 2\', on GW-15'),
 ('FU-35','G','Dressing table',10.25,11.75,89.25,91.25,'desk',None,'Bedroom 2, on GW-07'),
 ('FU-36','F','Queen bed',13.75,20.25,89.0,94.0,'bed','x2','Bedroom 3, head to FW-03'),
 ('FU-37','F','Side table',18.75,20.25,87.25,88.75,'cab',None,'Bedroom 3'),
 ('FU-38','F','Side table',18.75,20.25,94.25,95.75,'cab',None,'Bedroom 3'),
 ('FU-39','F','Sliding wardrobe with loft',14.5,20.25,84.875,86.875,'ward',None,'Bedroom 3, 5\'9" x 2\', on FW-07'),
 ('FU-40','F','Study desk',10.25,11.75,88.5,92.5,'desk',None,'Bedroom 3, under W-10'),
 ('FU-41','F','Western WC',18.0,20.25,80.5,82.0,'wc','x2','Toilet 3'),
 ('FU-42','F','Wash basin',17.0,18.4,83.1,84.5,'basin',None,'Toilet 3'),
 ('FU-43','F','Shower area',18.5,20.25,82.25,84.5,'shower',None,'Toilet 3, exhaust fan (no outside wall)'),
 ('FU-44','G','AC indoor unit',9.25,9.92,37.25,40.25,'acin',None,'Bedroom 1, on GW-03 above window W-02, about 7\'6" high'),
 ('FU-45','G','AC outdoor unit',9.0,11.67,29.58,30.75,'acout',None,'Bedroom 1, on GW-04 parking face, bracket above window W-01 (about 7\'6"); pipe runs inside the study corner'),
 ('FU-46','G','AC indoor unit',10.25,10.92,81.75,84.75,'acin',None,'Bedroom 2, on GW-07 facing the bed'),
 ('FU-47','G','AC outdoor unit',8.33,9.5,82.0,84.67,'acout',None,'Bedroom 2, on GW-07 side-garden face'),
 ('FU-48','F','AC indoor unit',10.25,10.92,93.0,96.0,'acin',None,'Bedroom 3, on FW-01 facing the bed'),
 ('FU-49','F','AC outdoor unit',8.33,9.5,93.25,95.92,'acout',None,'Bedroom 3, wall bracket on FW-01 outside'),
 ('FU-51','G','Kitchen sink',3.75,5.25,65.5,67.25,'sinkbowl',None,'Kitchen, near the GW-14 corner'),
 ('FU-52','G','Hob (burner) with small chimney',3.6,5.4,62.0,64.0,'hob',None,'Kitchen, at window W-06; slim chimney ducted out through the wall above the window head'),
 ('FU-53','G','Tap and wash platform',1.375,4.875,89.375,91.875,'washpad',None,'Side garden, paved with drain, in the corner of BW-02 and BW-03'),
 ('FU-54','G','Wash basin with tap',19.25,20.75,95.25,96.5,'basin',None,'Back garden, against GW-08 beside window W-08'),
 ('FU-55','G','Tap and wash platform',17.75,20.75,96.75,99.25,'washpad',None,'Back garden, paved, with floor drain'),
 ('FU-56','G','Low store under staircase 1',17.5,21.0,4.75,10.75,'store',None,'Parking, 3\'6" x 6\', under the low end of the flight (up to about 3\'8" high); top part left open so the car door can open'),
]
# door and window types (proposal)
SPEC = {
 'D-01':'Teak wood, double leaf, with safety grill door',
 'D-02':'Flush door, hardwood frame', 'D-06':'Flush door, hardwood frame', 'D-07':'Flush door, hardwood frame',
 'D-03':'WPC waterproof door', 'D-04':'WPC waterproof door', 'D-08':'WPC waterproof door',
 'D-05':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'D-09':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'D-10':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'O-01':'Plastered arch opening, no shutter',
 'W-12':'Bi-fold glass window, aluminium or UPVC frame, curtain on the living side',
 'GT-01':'MS swing gate, double leaf (no room on the wall for a sliding gate)', 'GT-02':'MS double-leaf hinged gate, opens outward',
}
for _o in OPENINGS:
    if _o[5]=='window' and _o[0] not in SPEC: SPEC[_o[0]]='UPVC 3-track sliding: 2 glass + 1 mosquito mesh, MS safety grill, 1\'6" sunshade outside'
    if _o[5]=='vent' and _o[0] not in SPEC: SPEC[_o[0]]='Louvred glass ventilator with exhaust fan opening'
SPEC['V-03']='Louvred glass ventilator with exhaust fan opening'
CAR=(11.25,17.25,13.75,28.75)
BIKES=(10.0,16.5,23.0)
CH_G_FRONT=[0,0.75,12.0,13.5,20.25,21.0]
