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
  ('BW-07', 20.625,21.0, 0.75,29.75, 'comp', 6, 'West compound wall, front part (new, 4½", 6\' high), along the apartment, from the gate post to the house'),
  ('BW-08', 20.625,21.0, 95.125,104.95, 'comp', 6, 'West compound wall, back part (new, 4½", 6\' high), along the apartment, from the house to the back wall'),
  ('GW-01', 2.75,3.5, 40.5,67.375, 'outer', 10.5, 'East outer wall of foyer, living and kitchen; ends at the bore court'),
  ('GW-02', 2.75,8.5, 40.5,41.25, 'outer', 10.5, 'Main door wall, between porch and foyer'),
  ('GW-03', 8.5,9.25, 29.75,41.25, 'outer', 10.5, 'Porch-side wall of study and bedroom 1'),
  ('GW-04', 8.5,21.0, 29.75,30.5, 'outer', 10.5, 'Front wall of study and toilet 1, facing parking'),
  ('GW-05', 20.25,21.0, 29.75,95.125, 'outer', 10.5, 'West outer wall, on the boundary (apartment side)'),
  ('GW-06', 6.0,10.25, 73.125,73.875, 'outer', 10.5, 'Back wall of toilet 2, facing the side-garden utility'),
  ('GW-17', 2.75,6.0, 66.625,67.375, 'outer', 10.5, 'Kitchen | bore court (north side of the court)'),
  ('GW-18', 6.0,6.75, 66.625,73.875, 'outer', 10.5, 'Toilet 2 | bore court (east wall of toilet 2, with V-02)'),
  ('GW-19', 10.25,11.75, 73.125,73.5, 'part', 10.5, 'Toilet 2 | stair hall (south end)'),
  ('GW-07', 9.5,10.25, 73.125,95.125, 'outer', 10.5, 'East wall of stair hall and bedroom 2, facing side garden'),
  ('GW-16', 11.75,12.125, 66.625,73.5, 'part', 10.5, 'Toilet 2 | stair hall (partition, inside the house); moved 1\'10" west for the bore court'),
  ('GW-08', 9.5,21.0, 94.375,95.125, 'outer', 10.5, 'Back wall of bedroom 2, facing back garden'),
  ('GW-09', 8.875,9.25, 41.25,46.375, 'part', 10.5, 'Foyer | bedroom 1'),
  ('GW-10', 13.75,14.125, 30.5,35.0, 'part', 10.5, 'Study | toilet 1'),
  ('GW-11', 13.75,20.25, 35.0,35.375, 'part', 10.5, 'Toilet 1 | bedroom 1'),
  ('GW-12', 8.875,20.25, 46.375,46.75, 'part', 10.5, 'Bedroom 1 | living room'),
  ('GW-13', 3.5,20.25, 58.25,58.625, 'part', 10.5, 'Living room | kitchen and dining (arch O-01)'),
  ('GW-14', 6.75,12.125, 66.625,67.0, 'part', 10.5, 'Kitchen | toilet 2 (kitchen now 8\' deep)'),
  ('GW-15', 10.25,20.25, 80.25,80.625, 'part', 10.5, 'Stair hall | bedroom 2'),
 ],
 'F': [
  ('FW-01', 9.5,10.25, 73.125,95.125, 'outer', 10.0, 'East wall of landing and bedroom 3'),
  ('FW-02', 9.5,21.0, 73.125,73.875, 'outer', 10.0, 'Front wall of landing; 53\' from PW-03 (future hall back wall)'),
  ('FW-03', 20.25,21.0, 73.125,95.125, 'outer', 10.0, 'West wall, on the boundary'),
  ('FW-04', 9.5,21.0, 94.375,95.125, 'outer', 10.0, 'Back wall of bedroom 3, right over GW-08'),
  ('FW-05', 10.25,20.25, 79.875,80.25, 'part', 10.0, 'Landing | bedroom 3'),
  ('FW-07', 1.75,9.5, 79.875,80.25, 'outer', 10.0, 'South wall of toilet 3 (where the parapet PW-05 was)'),
  ('FW-08', 1.75,2.125, 73.125,79.875, 'outer', 10.0, 'East wall of toilet 3, on the line of PW-02 (the slab cantilevers 1\' over the side garden, as under the terrace)'),
  ('FW-09', 1.75,9.5, 73.125,73.5, 'outer', 10.0, 'North wall of toilet 3, facing the open terrace'),
  ('PW-01', 2.75,9.625, 15.5,15.875, 'para', 3, 'Front parapet of balcony 2'),
  ('PW-02', 1.75,2.125, 15.5,73.125, 'para', 3, 'East parapet of balcony and terrace, up to toilet 3; the slab cantilevers 1\' east past GW-01 over the side passage, so a future hall here gets 1\' more width with no new pillar'),
  ('PW-03', 9.625,21.0, 19.75,20.125, 'para', 3, 'Front parapet of terrace, behind staircase 1 (now from the top of ST-1B)'),
  ('PW-04', 20.625,21.0, 20.125,73.125, 'para', 3, 'West parapet of terrace'),
  ('PW-06', 9.5,9.875, 95.125,98.125, 'para', 3, 'East parapet of balcony 3'),
  ('PW-07', 9.5,21.0, 97.75,98.125, 'para', 3, 'Back parapet of balcony 3 (3\' balcony, RCC cantilever)'),
  ('PW-08', 20.625,21.0, 95.125,97.75, 'para', 3, 'West parapet of balcony 3'),
 ]}

# ---------- rooms / areas: id, name, polygon or rect, kind ----------
def R(x1,x2,y1,y2): return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
def back_y(x): return 106.0-(x-1)/20.0           # back boundary line
ROOMS = {
 'G': [
  ('G-01','Parking',[(0.375,0.75),(21.0,0.75),(21.0,29.75),(8.5,29.75),(8.5,32.75),(2.75,32.75),(2.75,30.75),(0.375,30.75)],'out'),   # with the 2' bay in front of the porch steps
  ('G-02','Porch',R(2.75,8.5,32.75,40.5),'porch'),
  ('G-03','Foyer',R(3.5,8.875,41.25,46.75),'in'),
  ('G-04','Living room',R(3.5,20.25,46.75,58.25),'in'),
  ('G-05','Bedroom 1',R(9.25,20.25,35.375,46.375),'bed'),
  ('G-06','Study',R(9.25,13.75,30.5,35.375),'bed'),
  ('G-07','Toilet 1',R(14.125,20.25,30.5,35.0),'wet'),
  ('G-08','Kitchen',R(3.5,13.5,58.625,66.625),'kit'),
  ('G-09','Open area (future dining)',R(13.5,20.25,58.625,68.0),'in'),
  ('G-10','Stair hall',[(12.125,66.625),(13.5,66.625),(13.5,68.0),(20.25,68.0),(20.25,80.25),(10.25,80.25),(10.25,73.5),(12.125,73.5)],'in'),
  ('G-11','Toilet 2',R(6.75,11.75,67.0,73.125),'wet'),
  ('G-12','Bedroom 2',R(10.25,20.25,80.625,94.375),'bed'),
  ('G-13','Side passage',R(0.375,2.75,30.75,73.75),'out'),
  ('G-14','Side garden',[(0.375,73.75),(2.75,73.75),(2.75,73.875),(9.5,73.875),(9.5,back_y(9.5)-0.375),(1.375,back_y(1.375)-0.375),(1.375,89.375),(0.375,89.375)],'garden'),
  ('G-16','Bore court',R(2.75,6.0,67.375,73.875),'out'),
  ('G-15','Back garden',[(9.5,95.125),(21.0,95.125),(21.0,back_y(21)-0.375),(9.5,back_y(9.5)-0.375)],'garden'),
 ],
 'F': [
  ('F-01','Balcony 2',R(2.125,9.625,15.875,20.125),'terr'),
  ('F-02','Open terrace',[(2.125,20.125),(20.625,20.125),(20.625,73.125),(2.125,73.125)],'terr'),
  ('F-04','Stair landing',R(10.25,20.25,73.875,79.875),'in'),
  ('F-05','Bedroom 3',R(10.25,20.25,80.25,94.375),'bed'),
  ('F-07','Toilet 3',R(2.125,9.5,73.5,79.875),'wet'),
  ('F-08','Balcony 3',R(9.5,21.0,95.125,98.125),'terr'),
 ]}

# ---------- openings: id, floor, wall, a, b (along wall), type, hinge('a'|'b'), swing(+/-), height, sill, note ----------
# type: door, double, window, vent, arch, gate
OPENINGS = [
 ('D-01','G','GW-02', 4.25,8.25,'door','a','+', 7.0,0,'Main door, one 4\' teak leaf hinged on the east side, opens into foyer'),
 ('D-13','G','GW-02', 4.25,8.25,'double',None,'-', 7.0,0,'Steel safety door in front of the main door, black, double leaf 2\' + 2\', opens out onto the porch; each leaf folds back to 90 deg against a floor stopper'),
 ('D-02','G','GW-12', 9.5,12.5,'door','a','-', 7.0,0,'Bedroom 1 door, from living room'),
 ('D-03','G','GW-11', 14.5,17.0,'door','a','-', 7.0,0,'Toilet 1 door, from bedroom 1'),
 ('O-01','G','GW-13', 13.75,17.75,'arch',None,None, 7.0,0,'Arch from living room to open area, 4\' wide; ends at the FU-25 cupboard face'),
 ('W-12','G','GW-13', 5.5,11.5,'fold',None,None, 4.0,3.0,'Sliding glass window, kitchen to living: 3-track black aluminium, three 2\' clear-glass sashes, two slide behind the third (opens two thirds); two 3\' venetian blinds with lift cords on the living side (like W-01)'),
 ('D-04','G','GW-16', 67.75,70.25,'door','a','-', 7.0,0,'Toilet 2 door, from stair hall, opens inward; hinged at its north end, so the leaf folds back over the shower area, clear of the basin'),
 ('D-05','G','GW-07', 74.25,77.25,'door','a','-', 7.0,0,'Garden door, stair hall to side garden; opens out, hinged at its north end, so the leaf folds back against the toilet-2 wall GW-06 and the way out to the garden stays clear'),
 ('D-06','G','GW-15', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 2 door, from stair hall'),
 ('W-01','G','GW-04', 9.75,13.25,'window',None,None, 4.0,3.0,'Study window to parking'),
 ('V-01','G','GW-04', 16.25,18.25,'vent',None,None, 1.5,6.0,'Toilet 1 ventilator'),
 ('W-02','G','GW-03', 36.6,40.6,'window',None,None, 4.0,3.0,'Bedroom 1 window to porch, 4\' wide (standard), sliding'),
 ('W-04','G','GW-01', 48.0,52.0,'window',None,None, 4.0,3.0,'Living room window 1'),
 ('W-05','G','GW-01', 53.75,57.75,'window',None,None, 4.0,3.0,'Living room window 2'),
 ('W-06','G','GW-01', 61.0,65.0,'window',None,None, 2.0,3.25,'Kitchen window over the hob, 4\' x 2\', sill 3\'3", head 5\'3", so the chimney hood sits at the standard 2\'6" above the counter'),
 ('V-02','G','GW-18', 70.875,72.875,'vent',None,None, 1.5,6.0,'Toilet 2 ventilator over the WC platform, opens onto the bore court'),
 ('W-07','G','GW-07', 85.0,89.0,'window',None,None, 4.0,3.0,'Bedroom 2 side window to side garden'),
 ('W-08','G','GW-08', 13.0,17.0,'window',None,None, 5.0,2.0,'Bedroom 2 back window to the back garden, 4\' wide (same as W-07) x 5\', low 2\' sill; replaces the back door D-10'),
 ('GT-01','G','FRONT', 0.75,12.0,'gate',None,'+', 6.0,0,'Large gate, 11\'3", bi-fold double leaf (4 panels), folds inward over the level crest, east of the planter pillar'),
 ('GT-02','G','FRONT', 13.5,20.25,'gate',None,'+', 6.0,0,'Small gate, 6\'9", bi-fold double leaf (4 panels), folds inward over the level crest, west of the planter pillar'),
 ('D-07','F','FW-05', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 3 door, from the landing; opens into the bedroom, hinged at its east end so it folds back against FW-01, clear of the wardrobe FU-39'),
 ('D-09','F','FW-01', 77.0,79.5,'door','b','-', 7.0,0,'Toilet 3 door, 2\'6", from the landing, at its south end (next to bedroom 3); opens into the toilet, hinged at its south end so it folds back against FW-07; leaves the north part of the landing free for the terrace door D-12'),
 ('V-03','F','FW-07', 5.75,7.25,'vent',None,None, 1.5,6.0,'Toilet 3 ventilator, 1\'6" x 1\'6" at 6\', between the WC and the basin, opening to the side garden; louvred glass'),
 ('D-14','F','FW-02', 10.5,13.25,'door','a','-', 7.0,0,'Grill door on the terrace face of D-12, black MS, one 2\'9" leaf hinged at the east end, opens out onto the terrace to 90 deg against a floor stopper'),
 ('D-12','F','FW-02', 10.5,13.25,'door','a','+', 7.0,0,'Landing door to the open terrace, 2\'9" (in place of the old window W-09), east of the spiral stair; opens into the landing, hinged at its east end so it folds back against FW-01 (the toilet door D-09 is now at the south end, out of its way); 1" raised sill and a weather bar outside against rain'),
 ('W-10','F','FW-01', 85.75,89.75,'window',None,None, 4.0,3.0,'Bedroom 3 side window, centred straight in front of the bed FU-36'),
 ('W-11','F','FW-04', 14.75,18.25,'window',None,None, 4.0,3.0,'Bedroom 3 back window, over the study desk'),
 ('D-11','F','FW-04', 11.0,13.75,'door','a','+', 7.0,0,'Bedroom 3 to balcony 3, single door 2\'9", near the east corner, hinged at its east end; opens fully against the wall'),
]

# ---------- building outlines (outer wall faces) for built-up area ----------
GF_OUTLINE=[(8.5,29.75),(21,29.75),(21,95.125),(9.5,95.125),(9.5,73.875),(6.0,73.875),(6.0,67.375),(2.75,67.375),(2.75,40.5),(8.5,40.5)]
FF_OUTLINE=R(9.5,21.0,73.125,95.125)
# site levels, in feet above the road crown in front of the gate (house floor = +3.5)
LEVELS=dict(road=0.0,hump=0.5,parking=2.0,garden=2.5,floor=3.5)
RAMP=dict(y_hump=1.0,y_crest=3.25,y_top=10.75,ease=1.5,drain=(2.5,3.25))   # gate bevel to Y 1', crest to 3'3" (drain at its inner edge), ramp to Y 10'9": 1'6" at 1 in 8, 4'6" at 1 in 4 (14 deg), 1'6" at 1 in 8; for the car gate GT-01 only
# small gate GT-02: three 6" steps up from the crest (risers in line with ST-1's treads), then a level platform at parking height between the tree well and ST-1A;
# its east edge is a retaining kerb along the car's ramp (16" high at the north end, nothing where the ramp reaches the parking at Y 10'9")
SIDE_PLATFORM=dict(well=(12.75,4.75,2.25),x1=13.5,x2=17.125,steps=(2.667,3.5,4.333),xe=12.5,y_end=10.75)
BRANCH_NOTES='''<section class="ask"><h2>Areas for the engineer (built-up and parking cover)</h2>
<ol>
<li><b>Built-up area: 1,386 sq ft</b> (outside faces of the walls): ground floor rooms with the foyer 967, porch 56, bore court (roofed) 21; first floor bedroom 3, landing and wardrobe area 253, toilet 3 55 (on the terrace corner), balcony 3 34. The open terrace is not counted (it is the ground floor's roof).</li>
<li><b>Car parking cover: 229 sq ft</b>: the parking under the roof slab in front of the house and the porch, including the part under balcony 2 (counted here, not again as built-up).</li>
</ol></section>
<section class="ask"><h2>Garden plan (branch garden-v1, for review)</h2>
<ol>
<li><b>Idea:</b> low-care plants that Tamil Nadu homes use every day (pooja flowers, kitchen greens, herbs), in beds and pots, with the walks, the car route, the bores and the utility kept clear. The existing back bed FU-73 (PL-01 to PL-12) and the neem tree stay as they are.</li>
<li><b>Porch (shade):</b> areca palm GD-01 in a big pot beside the main door, anthurium GD-02 and syngonium GD-03 in pots on the sides, clear of the walk from the steps to the door.</li>
<li><b>Side passage:</b> kept clear for walking (no wall pots); the pillars C-03 to C-11 stick 7½" into it, leaving 1'9"</li>
<li><b>Side garden (about 5 hours of midday sun):</b> on the east wall: climbing jasmine (mullai) GD-05 opposite the garden door, dwarf banana GD-06 (fed with rinse water from the utility basin), a raised vegetable bed GD-07 (tomato, brinjal, chilli, keerai) and a drumstick tree GD-08 in the south-east corner. A small herb bed GD-09 (mint, ajwain leaf, coriander, vallarai) and two aloe pots GD-10 south of the house corner.</li>
<li><b>Back garden:</b> kept open round the wash platform; only a lemon tree in a big pot GD-11 in the open south-west corner, by the wash platform and its tap.</li>
<li><b>Kept clear:</b> nothing over the septic tank, soak pit or sump (all at the front, under the paving); 3' or more round the bore chambers BR-01 and BR-02 for the rig; the D-05 step, the utility platform, the AC unit FU-47 and the recharge pit UG-04 stay open. No coconut, mango or other big tree: no spot is 10' from the house and the walls, and coconuts falling on the path are dangerous. The drumstick is the only tree; cut it back to about 8' after each crop.</li>
<li><b>Watering:</b> a hose from the low tap of the utility basin FU-30 and the back tap FU-55; a simple drip line with a timer for the vegetable and herb beds; mulch (dry leaves) on all beds to keep the soil cool in summer. Beds are raised 1' so monsoon rain drains away.</li>
<li><b>Plant list:</b> GD-01 Areca palm · GD-02 Anthurium · GD-03 Syngonium · GD-05 Mullai (climbing jasmine) · GD-06 Banana (dwarf) · GD-07 Vegetables: tomato, brinjal, chilli, keerai · GD-08 Drumstick (PKM-1) · GD-09 Herbs: mint, ajwain leaf, coriander, vallarai · GD-10 Aloe vera · GD-11 Lemon.</li>
<li><b>3D:</b> the porch pots, the wall-pot ferns and the aloe are free CC0 models from Poly Haven; the palm, banana, drumstick, lemon, jasmine and the bed plants are made in code. Hover any plant for its code and name.</li>
</ol></section>
<section class="ask"><h2>Modular kitchen (see the Kitchen tab)</h2>
<ol>
<li><b>Kitchen now 8' deep</b> (was 7'3"): the living room is 11'6" long (GW-13 moved 6" north) and toilet 2 is 3" shorter (GW-14 and GW-17 moved 3" south), so the standing space between the breakfast counter and the back counter is 4'9" (was 4'). The east-run corner cupboards get wider doors; the stove and window stay put.</li>
<li><b>Units K-01A to K-17B</b>, sized for daily Tamil Nadu cooking: two <b>L-shaped corner cupboards</b> with L-shaped shelves and one L-shaped door in 2 parts joined by a corner hinge, which folds and swings open in one go (K-01A and K-01B at the breakfast-counter corner for big vessels and plates, K-03A and K-03B at the sink corner for pans and bottles), so no corner is wasted; <b>gas cylinder unit K-02</b> under the stove with a plain door, no trolley, on a low 2" plinth with a bottom board, 29½" clear for the 26" cylinder; sink unit with two bins (K-04), low-counter units for water pots and rice and atta (K-05, K-06), breakfast-counter units for tiffin boxes, cutlery, glasses and dry stores (K-08 to K-11), wall units K-12 and K-13 (dish drainer) both from 5'3", glass unit K-15, and lofts with <b>normal hinged doors</b> to the ceiling (K-16, K-18 over the RO and wet grinder, K-17A, K-17B, K-17C over the chimney); two orange plastic water kudams in K-05.</li>
<li><b>Chimney FU-81, 60 cm wide</b>, over the stove; a 6" round duct goes straight back from the top of its body through GW-01 at 6'4" (hidden behind the chimney) to a steel cowl FU-82 outside (downward opening, back-draft flap); the loft K-17C above it closes the gap between K-17A and K-17B.</li>
<li><b>Kitchen tab:</b> a 3D model of just the kitchen. Click any door or drawer to open or close it, or use Open all and Close all; Sizes shows the width, height and depth of every unit and the size of each drawer front; the Unit list gives the contents and the reason for each unit.</li>
<li><b>RO purifier FU-66</b> moved next to the sink, over the east end of the low counter, so water pots fill standing on the 2' counter; <b>wet grinder FU-65</b> moved to the west end of the low counter, where the RO was.</li>
</ol></section>
<section class="ask"><h2>Side garden utility and bedroom 2 window (branch utility-v1, for review)</h2>
<ol>
<li><b>Utility basin on BW-01</b>, across the side garden from BR-01: utility basin FU-30 (granite counter, deep steel sink, tall tap and a low bucket tap) on a 4" tiled platform FU-77 with a floor drain, with white tiles on the east compound wall behind it. The way out of D-05 into the garden stays clear; the AC outdoor unit FU-47 is south of window W-07. The washing machine FU-29 stands in the bore court (covered), under the drying rack FU-75. A garden tap FU-54 with a wash platform FU-55 is on the east wall further south, by the vegetable bed.</li>
<li><b>D-05</b> opens out to the side garden, hinged at its north end so it folds back against the toilet-2 wall; a granite step FU-79 outside it, since its sill is 1' above the garden.</li>
<li><b>Bedroom 2 back door D-10 removed.</b> The back wall gets one big picture window W-08 instead: 8'6" wide and 5' high with a low 2' sill, fixed glass in the middle and a sliding pane each side. In place of bars, an <b>invisible grill</b> of thin stainless-steel wires 2" apart, so the view of the back garden stays open. The back garden is reached through D-05 and the side garden.</li>
</ol></section>
<section class="ask"><h2>Water and drainage</h2>
<ol>
<li><b>Septic tank UG-01: the tank already on the plot</b> (2" from the west boundary, 1' in from the road, 7'3" x 10' outside), about 8,000 L assumed (6'3" x 9' inside, 5'3" of liquid, two chambers) until it is checked on site. 18.8 m from borewell BR-02 (guideline at least 15 m). Openings raised about 2' to the new ground with tile-in covers on the small-gate platform and the gate crest; the cleaning truck reaches it from the road. The engineer must support the foot of the outside stair ST-1A, which stands over it, and check its roof under the small-gate steps and the fill.</li>
<li><b>Soak pit UG-02</b>, new, just inside the car gate on the east side: 19.5 m from BR-02 (guideline at least 18 m). If the town has an underground sewer on this road, connect to it instead and drop the soak pit.</li>
<li><b>Sump UG-03, 6,000 L, now at the front</b> under the east walkway beside the bikes (inside 5' x 7'6", 6'5" deep), so a water lorry fills it from the road with a short hose; 10' from the septic tank and 12' from the soak pit. Tile-in lockable cover in the walkway; bores and the town supply feed it, a pump lifts water to the overhead tank FU-71.</li>
<li><b>Pumps:</b> no motor room or surface motor is needed. Both pumps are submersible: an openwell submersible pump (1 HP) sits inside the sump UG-03, and the bore pump sits down in BR-02. Above ground there are only two wall control panels, both under cover: the sump pump control inside the EB meter box FU-87 on GW-04 in the parking ( with automatic float switches for sump low and tank full) and FU-86 in the bore court (bore pump). The sump pipe goes up the porch wall to the terrace, along PW-02 and up FW-02 by the ladder FU-72 to the tank FU-71; bore water goes to the sump, or straight to the tank by a valve.</li>
<li><b>Rainwater recharge pit UG-04</b> in the side garden, between the bores BR-01 and BR-02 by the east wall BW-01: roof water through a filter into a 3' x 6' pebble pit, for the bores.</li>
<li><b>To check on site:</b> the existing tank's depth, walls, partition and outlet; any neighbour's well near the soak pit (keep 18 m); the soil for the soak pit.</li>
</ol></section>
<section class="ask"><h2>Parking plan (branch exterior-v2, for review)</h2>
<ol>
<li><b>Parking floor: PT-1</b> (chosen): vitrified grey parking tile, 400 x 400 mm, matt, with a printed herringbone of small bricks (like Code36603, about ₹64 per sq ft), from the gate drain inwards: ramp, level parking, the small-gate platform and the bay in front of the porch steps. On the 1 in 4 ramp ask for its anti-skid (R11) grade, as plain matt tile gets slippery when wet. The gate bevel and crest (road edge to the drain) are plain light cement.</li>
<li><b>Car:</b> VW Virtus size (14'11" x 5'9"), <b>reversed in</b>: nose to the gate, back 1' from the front wall, on the level parking (Y 14'9" to 29'9"), as far west as it can go (centre X 14', its west side 3" off the stair), leaving 5'6" between the scooter and the car. <b>Route along the east side</b> (owner's sketch): coming in, it comes from the west, stops just past the gate and reverses in. <b>Going out it must head west</b> (the main road is only that way): it drives out forward (one short back-and-forth to clear the low end of ST-1A) through GT-01, turning east, backs into the gate mouth, then drives out again turning west along the near lane, a 3-point turn using the gate opening. Checked with a route planner using the Virtus turning circle; the gate stays as it is.</li>
<li><b>Tree well FU-76</b>: 4'6" across, centred 6" south of the trunk, because the trunk leans south and must stay inside the ring up to the platform height. The ring has one level top, 1" above the small-gate platform, so on the ramp side it stands as a raised bed (up to 1'7" above the drive). Keep at least 10" of open soil round the trunk.</li>
<li><b>Two-wheelers along BW-01:</b> TW-1 (motorcycle, Honda VFR800 size: 6'11" long) and TW-2 (Ather 450X) side by side against the east wall between C-01 and C-03, ridden in forward (front to the house) up the east walkway without passing the car. The space under the high end of ST-1A is left open (no store FU-56), so the car's mirror clears the stair.</li>
<li><b>Porch 2' shorter:</b> the three porch steps start 2' in from the front line (Y 32'9"), leaving a 2' bay of parking in front of them, so there is 4'6" between the parked bikes and the first step. The porch floor is 5'3" deep; the shoe rack moves beside the main door.</li>
<li><b>Small gate GT-02: steps, not ramp.</b> Three 6" granite steps just inside GT-02 (in line with the first treads of ST-1A) lead up to a level platform at parking height (+2'0") between the tree well and ST-1A, for walking in from the small gate. Its east edge is a retaining kerb along the car ramp, 1'4" high at the steps and running out to nothing where the ramp meets the parking at Y 10'9". The ramp now serves the car gate GT-01 only. The tree-well ring holds the platform on its west side.</li>
<li><b>ST-1 as cast:</b> both flights are steps on a 6" sloping waist slab and the landing ST-1L is a 6" slab, all cast as one RCC piece; the sloping underside of each flight runs into the flat underside of the landing (no step in the soffit). Landing level, risers and treads unchanged.</li>
<li><b>Pillar C-01</b> moved 2'4½" east against the compound wall BW-01; beam B-01 extended to it (19'11" span, engineer to size, about 1'9" deep) and B-10 rests on B-01. The parking is now clear of pillars.</li>
</ol></section>
<section class="ask"><h2>Outside windows and colours (branch exterior-v2, for review)</h2>
<ol>
<li><b>Window frame WF-1</b> on every outside window: a box frame round the window, 6" wide and 4" out from the wall, with a deeper 1'3" hood on top that works as the sunshade, and a thin black drip edge. Ventilators get a slimmer 4" frame, except V-01 (plain, no frame). RCC fins and hood, clad in the same wood-look brown as the balcony louvers and the gate slats (HPL or aluminium wood finish).</li>
<li><b>W-01 (study, facing the parking):</b> same box frame WF-1 and scalloped sunshade as the other front windows, black grill.</li>
<li><b>Plinth band:</b> removed; the plinth below the floor is in the same outside wall colour.</li>
<li><b>Paint plan: Sage and clay</b> (chosen, kept cost-efficient). <b>Inside:</b> one light sage green emulsion on every room wall (one shade, so it is bought in bulk and touch-ups are easy); ceilings in a light clay (soft terracotta) tint like the reference photo, with the ceiling band round the edge in white, so the clay reads as a soft panel and the edges stay bright; the clay tint is the same white ceiling paint with a little stainer added, so it costs about the same; the only accent is clay (terracotta) on the living-room TV niches; bedroom headboard walls keep their oak-look panels; kitchen and toilets are tiled to 7', sage above. Toilets and kitchen above the tiles: washable (anti-fungal) emulsion in the same sage. <b>Outside:</b> sage green weather-proof exterior emulsion on all the walls (a light green, so the walls stay fairly cool), clay (terracotta) only as lining: the slab bands and the parapet and wall copings; a dark brown plinth that hides splash marks; gates and grills stay as they are. Sage and clay are used inside and outside, so it is still only a few paints.</li>
<li><b>Windows (chosen):</b> frosted glass over the full pane in every window (privacy and safety). <b>Open out (casement, opens fully):</b> W-01, W-07, W-08, W-10, where nothing outside is in the way. <b>2-pane sliding:</b> W-02 (porch, widened to 4'), W-04, W-05 (side passage, with top vent), W-11 (balcony 3). W-06 kitchen: fixed lower glass, opening top pane. Ventilators: frosted louvres; all frames black (anthracite) UPVC to match the grills, steel door and gates; plain black bar grills (GR-1). Living W-04, W-05: sliding with a 1' top-hung vent for hot air. Kitchen W-06: fixed glass below, opening top pane (no reaching over the flame). Bedrooms W-07, W-10, W-11 and the sides of W-08: casements that open fully, grill inside, pleated mesh; W-10 heat-cut glass. W-02 frosted lower half (porch privacy). W-01 stays sliding (tight parking). Toilet ventilators: frosted louvres. Rough cost ₹1.5–1.8 lakh plus grills ₹22–28k.</li>
<li><b>Store cupboard FU-25 (civil work):</b> four kadappa bays (one 4' tall-things bay with an adjustable shelf) with UPVC wood-look shutters and a loft above 7'6"; inverter and battery at the foot of S-4 behind a louvred shutter, with their own socket and MCB. See the Store tab.</li>
<li><b>Plan check fixes (chosen):</b> terrace and balcony 2 slab cantilever 1' east over the side passage (parapet PW-02 moved out), so a future first-floor hall gets 1' more width with no new pillar; AU-01 pillar C-22 with beams B-24 and B-25 under the toilet 3 corner (engineer to confirm sizes); AU-02 ventilator V-03 in toilet 3; AU-04 the 2' of fill compacted in 6" layers and anti-termite soil treatment before the floors; AU-08 3'6" x 3'6" granite landing outside the garden door D-05; AU-12 drying rack dropped, so the counter beside the sink is free; AU-16 wardrobes 1'11" deep (hangers fit across), bedroom 2 and 3 wardrobes sliding; AU-17 bedroom 2 bed and side tables 6" south; AU-18 bedroom 3 bed and side tables 9" north (2'7½" for the desk chair); AU-19 every AC bottom at 7'10", above the curtain rods; AU-20 slim black grill on W-08; AU-22 toilet 3 WC 4" west; AU-23 toilet 3 door 2'6"; AU-27 EB meter on the road face of the planter pillar, read from the road; AU-28 smaller palm pot, 3" clear of the steel door; AU-33 bedroom 3 AC outdoor unit on the balcony 3 floor.</li>
<li><b>Civil touches (chosen, low cost):</b> FU-01 open wooden shoe rack on the porch; CD-02 sunken doormat well at the steel door; CD-03 rough granite porch steps with a black edge strip and a black handrail;  CD-07 window seat with storage under W-08 in bedroom 2; CD-08 tiled shower niches in all three toilets (the toilet 2 bath rack is dropped); CD-09 no step at any toilet door, floors sloped to a 2'6" steel linear drain; CD-10 grab rails beside every WC, walls behind them and on both sides of the stair kept solid brick for more rails later; CD-11 all outside wall corners inside the house plastered round (1" radius); CD-19 the rainwater recharge pit UG-04 in the back garden (already planned).</li>
<li><b>Curtains, window length only:</b> in every room the curtain rod sits 6" above the window (7'6") and the curtain ends 6" below the sill, instead of hanging from the ceiling: about half the cloth, neater, and the ACs above the windows stay clear. Only the balcony door D-11 gets a full-length curtain, from its own rod.</li>
<li><b>80s Tamil touches (chosen, low cost):</b> window and ventilator grills in black powder-coat (GC-1, mint blue was tried and dropped), matching the black gates with brown slats; <b>VD-03</b> front and back window sunshades (east and west windows face the neighbours, so they get no outside frame) with a scalloped front edge and a thin red oxide line above; <b>VD-05</b> main door D-01 in teak with four raised panels and a brass knob (other doors stay flush). Costly items such as Athangudi tiles are left out.</li>
<li><b>Owner changes (2026-11-05):</b> FU-92 loft over the toilet 1 door removed; bedside table FU-101 (1'3" x 1', oak, one drawer) between the bed head and wardrobe FU-09.2, under the phone-charging point BS-1; full-length mirror 1'2" x 5' on the south shutter of FU-09.2; FU-10 study desk replaced by a sewing machine table (white top, ruler strip, black iron stand, foot pedal) under W-01; W-01 gets a venetian blind with 2" faux-wood slats that tilt. Walls stay sage green; the 3D colours now keep their true shade in daylight (they had looked faded and dark).</li>
<li><b>Parking garden (chosen):</b> real nursery plants in pots: PG-1 plain leaf mulch in the neem tree well; PG-2 bougainvillea in the planter on pillar BW-05; PG-3 eight terracotta pots in wall rings on BW-01, 4'6" up; PG-5 ten low terracotta pots on the ground below them (croton, jasmine, ixora, hibiscus); PG-4 cement trough of portulaca under W-01; PG-8 plant water channels with gratings to the gate drain; PG-9 drip line on two taps with timers. About ₹14k to ₹20k. The car's path, the bike lane and the walkway are not touched.</li>
<li><b>Colours: EX-8</b> (chosen, sage and clay): sage green house, clay bands and copings, dark brown plinth, wood-brown frames. Compound walls and gate pillars in a darker warm grey-beige, so they read apart from the house, with white coping on top. Gates GD-1 (slats) and kitchen finish KT-1 are also fixed; the other options are dropped.</li>
</ol></section>
<section class="ask"><h2>Raised site levels (branch levels-v1, sample for review)</h2>
<ol>
<li><b>Levels above the road:</b> gate hump +6", parking +2'0", gardens, side passage and back yard +2'6", house floor +3'6" (1' plinth above the gardens).</li>
<li><b>Gate:</b> a 1' bevel from the road to a 6" crest, a 2'3" level strip at the crest, then a covered drain across the drive (to the rainwater pit and the road drain).</li>
<li><b>Drive ramp:</b> short and steep: 1 in 4 (14 deg) in the middle with 1'6" of 1 in 8 at the top and bottom, from Y 3'3" to 10'9", rising 1'6" to the parking; level from 10'9" inside the gate. The 1 in 8 ends keep each change of slope to about 7 deg, so the Virtus clears it (it scrapes beyond about 15 deg). Brush-finished pavers or grooved concrete for grip.</li>
<li><b>Gates GT-01 and GT-02</b> become inward folding (bi-fold) gates, so their leaves stay over the level crest and never hit the ramp. Shown folded open in 3D, so you can walk out to the road (the view follows the ramp).</li>
<li><b>Outside stair ST-1</b> now starts at the crest by the small gate: 27 risers of about 6½" (17 in ST-1A from Y 2'8", landing, 10 in ST-1B); balcony 2 unchanged.</li>
<li><b>Neem tree:</b> trunk kept at today's ground in a 5'6" tree well FU-76 with a low retaining ring; no fill against the trunk.</li>
<li><b>Porch:</b> 3 steps of 6" from the parking. Side passage starts 6" above the parking.</li>
<li><b>Headroom over the parking:</b> about 7'2" under ST-1B at the car's west edge and about 7'1" under the landing ST-1L (with a 6" landing slab); more toward the east.</li>
<li><b>Compound walls</b> step down along the ramp and hold back the fill at the bottom (thicker base, weep holes): engineer to detail. About 2' of earth filling over the plot.</li>
</ol></section>
<section class="ask"><h2>Tree pit and terrace door (approved, from spiral-v1)</h2>
<ol>
<li><b>Tree pit FU-76:</b> a 5' round bed of open soil round the neem trunk, with a 4" granite kerb ring 1" above the pavers. Pavers stop at the kerb, so growing roots cannot lift them; water poured here stays at the roots.</li>
<li><b>Door D-09</b> (landing to terrace corner) now opens inward, hinged at its north end, folding back against FW-02; a 1" raised sill outside keeps rain out.</li>
</ol></section>
<section class="ask"><h2>Terrace over the bore court (approved, from spiral-v1)</h2>
<ol>
<li><b>Terrace slab is full</b> over the bore court G-16 now; the cut and parapets PW-06 to PW-09 are removed, PW-02 runs straight to the back parapet PW-05. F-02 and F-03 are plain rectangles.</li>
<li><b>Bore court</b> stays open at the ground floor (to the side passage) for the borewell; only its top is closed.</li>
<li><b>C-20 and C-21</b> (the two inner pillars at the bore court) now stop at the ground-floor roof: no stubs on the terrace, so the future hall stays clear in the middle; it will stand on the side pillars only (C-01 to C-12 on the east and west lines).</li>
<li><b>Bedroom 3</b> finished in 3D in the same design as bedrooms 1 and 2; toilet 3 fitted out; all first-floor doors shown open.</li>
</ol></section>
<section class="ask"><h2>Back garden (approved, from spiral-v1)</h2>
<ol>
<li><b>BW-09 back wall</b> (existing, of the houses behind) now shown in 3D, with the houses behind it.</li>
<li><b>Flower bed FU-73</b>, 1'6" deep, all along the back wall, 9" brick kerb. A row of 12 plants common in Tamil Nadu homes, east to west: Sembaruthi (red hibiscus), Malli (jasmine), Kanakambaram (orange crossandra), Nandiyavattai (white crape jasmine), Nithya kalyani (pink periwinkle), Karuveppilai (curry leaf), Malli, Vetchi / Idly poo (red ixora), Rose, Kanakambaram, Nithya kalyani, Sembaruthi. Tall ones at the ends, low ones in between.</li>
<li><b>Clothes drying rack FU-75</b>: a ceiling pulley rack in the bore court by BR-02, under the terrace slab, so clothes dry out of the rain and the floor stays clear for the bore rig.</li>
</ol></section>
<section class="ask"><h2>Toilet 2 re-planned (approved, from spiral-v1)</h2>
<ol>
<li><b>Door D-04</b> now opens inward, hinged at its north end; the leaf folds back over the shower area.</li>
<li><b>Shower FU-28</b> moves to the north end (5' x 2'10½"), rose and geyser FU-58 on GW-14, bath rack FU-70 on GW-16 north of the door.</li>
<li><b>Indian WC FU-26</b> sits on a bigger 4" platform FU-26.1 in the south-east corner: 3'6" front to back (east-west, the way you face) x 2'6" side to side; user faces west; V-02 moved over it; bucket and bib tap FU-57 on the front of the platform, on GW-06, on the left hand.</li>
<li><b>Basin FU-27</b> on GW-06 in the corner by the door, beside the platform, clear of the swing, mirror above.</li>
</ol></section>
<section class="ask"><h2>Spiral stair ST-2 (approved, from spiral-v1)</h2>
<ol>
<li><b>Size:</b> 5'10" across, in the stair hall against GW-05, centre 17' from east and 76'10½" from the road. Clear walking width about 2'7" (31"), 4½" steel centre pole.</li>
<li><b>Steps:</b> 21 risers of about 6½" (167 mm) for the 11'6" floor height, 20 oak treads of 25½° (about 14 per full turn) plus a 60° landing. The stair turns the same total angle as before, so it starts and arrives at the same places. Tread depth is 6⅜" at the inner walk line and 10¼" where you normally walk; outer edge 15⅓". Easier to climb than the old 7⅔" risers.</li>
<li><b>Headroom:</b> about 7'7" under the next turn and 6'11" under the landing, more than the 6'6" rule.</li>
<li><b>Direction:</b> start at the west side facing south (coming from the dining side along GW-05), climb anticlockwise with the handrail on your right, arrive facing east onto the landing F-04, next to D-07 and D-09.</li>
<li><b>Compared with ready kits:</b> 6' kits (Salter, Iron Shop) use 30° treads with up to 9½" risers and need a 6'2" square hole; Arke Kloè 160 cm uses 8¼" to 9¼" risers. Ours is a gentler 6½", close to a normal staircase.</li>
<li><b>Structure:</b> 6' round hole in the slab over the stair hall, with edge beams round it (engineer to size). Pole bolted to the ground floor and to the landing edge.</li>
<li><b>Finish:</b> black MS pole, frames and balusters (4 per tread, gaps under 4"), oak treads and oak handrail at 3'. Black MS rail with oak top round the hole on the first floor.</li>
</ol></section>
<section class="ask"><h2>Staircase ST-1 (approved, from stair-v1)</h2>
<ol>
<li><b>25 risers of 6"</b> from the parking floor (1' below the house floor, to be confirmed) to the balcony at the first-floor level: 15 in ST-1A, 10 in ST-1B. Treads 10", width 3'6".</li>
<li><b>ST-1A</b> runs along the new west compound wall BW-07 (moved 4½" east of the boundary), from Y 4'4" to 16'; <b>landing ST-1L</b> 3'6" x 3'6" at +7'6" above the parking; <b>ST-1B</b> turns east over the car, 7'6" long, arriving on balcony 2.</li>
<li><b>Balcony 2</b> is 2' shorter (6'6" x 4'3"); PW-01 shortened and PW-03 extended to meet the top of ST-1B.</li>
<li><b>Finish:</b> grey flamed granite treads and risers, plastered sides in the outside colour, black MS railing with 4" gaps and a wood-look handrail at 3'. The high end of ST-1A is open underneath (no store), so the car clears it; the low end of the stair is solid.</li>
</ol></section>
<section class="ask"><h2>Bore change (branch bore-v1, for review)</h2>
<ol>
<li><b>Two existing bores:</b> BR-01 at 13'3" from west and 27' from south (side garden), BR-02 at 17' from west and 34' from south. BR-02 was inside toilet 2.</li>
<li><b>Kitchen</b> is 7'3" deep (was 8'6"), so toilet 2 moves 1'3" north and the stair hall gets more room beside the spiral stair.</li>
<li><b>Bore court G-16:</b> an open-to-sky court, 3'3" x 6'9", cut out of the house next to the kitchen and joined to the side passage. BR-02 sits in it, 2' from the nearest wall.</li>
<li><b>Toilet 2</b> is 5' x 6'4½" (same area): pan on the court wall GW-18 with V-02 above, bucket and basin on the north wall, shower across the south end. GW-16 moves 1'10" into the stair hall.</li>
<li><b>Garden door D-05</b> moves 6" north (Y 74'3" to 77'3") and opens out from its south hinge, so you step out 1'5" or more north of BR-01. Washing machine and outside basin stay where they were.</li>
<li><b>Structure:</b> C-13 removed, new pillars C-20 and C-21 and beams B-18 to B-20 round the court; C-14 stays at the GW-06 / GW-07 corner. The terrace loses a small corner over the court (new parapets PW-06 to PW-09).</li>
</ol></section>
<section class="ask"><h2>Proposal v4: for final review</h2>
<ol>
<li><b>Hover</b> over any item to see its name.</li>
<li><b>Toilet 2:</b> Indian pan FU-26 against GW-01 (the V-02 wall) in the corner, user facing south. Ventilator V-02 is moved over it. Bucket and tap FU-57 are west of the pan, on the user's right hand. The shower FU-28 has its own 3'3" x 2'6" area along GW-06. Basin FU-27 is in the dry corner by the door.</li>
<li><b>Toilet 3:</b> door D-08 is now 2'3" wide and moved toward the bedroom end. Basin FU-42 is right beside the door. The WC FU-41 is on the landing-side wall, facing south. The shower FU-43 takes the whole west end, 2'3" x 4'3" (was 1'9" x 2'3"), with geyser FU-60, curtain FU-61 and exhaust fan FU-62 ducted to the roof.</li>
<li><b>Wardrobes</b> FU-09.1, FU-09.2, FU-34 and FU-39 are 16" deep. The bedroom 1 L-wardrobe is now 6'5" long in total.</li>
<li><b>FU-25 cupboard</b> is 10' x 2'6", full height. Arch O-01 now ends at the cupboard face, so the GW-13 stub by the west wall is exactly as deep as the cupboard.</li>
<li><b>Small gate GT-02</b> opens inward. Its east leaf, fully open, just reaches the tree trunk, so limit it to about 80°.</li>
<li><b>Kitchen:</b> burner at the window with a slim chimney, sink near the GW-14 corner, fridge on GW-13, modular back counter, overhead shelves on both counters.</li>
<li>Also in this version: L-sofa, 11' TV and showcase wall unit, ACs in all 3 bedrooms, garden tap areas, small store under staircase 1, planter pillar between the gates.</li>
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
# two existing bores (site survey 2026-10-18): distances from the west boundary (X 21) and the south (back) boundary
# existing back boundary wall of the houses behind (slanted with the back line), 4½" inside our line, 6' high
BACK_WALL=dict(id='BW-09',h=6.0,t=0.375,pts=[(1.0,back_y(1.0)),(21.0,back_y(21.0))],note='Back compound wall (existing, of the houses behind), 4½", about 6\' high')
# plants in the back flower bed FU-73 (east to west)
_bed=lambda x:back_y(x)-0.375-0.75
PLANTS=[('PL-01','sembaruthi',2.2),('PL-02','malli',3.8),('PL-03','kanakambaram',5.4),('PL-04','nandiyavattai',7.0),('PL-05','nithyakalyani',8.6),('PL-06','karuveppilai',10.2),
        ('PL-07','malli',11.8),('PL-08','vetchi',13.4),('PL-09','rose',15.0),('PL-10','kanakambaram',16.6),('PL-11','nithyakalyani',18.2),('PL-12','sembaruthi',19.8)]
PLANTS=[(c,t,x,_bed(x)) for c,t,x in PLANTS]
PLANT_NAMES={'malli':'Malli (Jasmine)','sembaruthi':'Sembaruthi (Hibiscus, red)','nandiyavattai':'Nandiyavattai (Crape jasmine)','vetchi':'Vetchi / Idly poo (Ixora, red)',
 'kanakambaram':'Kanakambaram (Crossandra, orange)','nithyakalyani':'Nithya kalyani (Periwinkle, pink)','rose':'Rose (pink)','karuveppilai':'Karuveppilai (Curry leaf)','tulsi':'Tulsi (Holy basil)'}
PLANT_COL={'malli':'#ffffff','sembaruthi':'#c8102e','nandiyavattai':'#ffffff','vetchi':'#e03a24','kanakambaram':'#ff7a1f','nithyakalyani':'#e2558c','rose':'#c2185b','karuveppilai':'#3d6b2b','tulsi':'#7a4a7e'}
# ---------- garden plan: plantings GD-xx ----------
# kind: 'pot' (x,y = centre, r = pot radius, z = 'porch' (house floor) or 'garden'), 'wallpots' (pots hung on a wall: wall face x, list of y, bottom height zb above the garden),
#       'creeper' (wall bed x1..x2, y1..y2, trellis height h), 'tree' (x,y = trunk, r = basin ring, h = height, cr = crown radius), 'bed' (raised bed x1..x2, y1..y2, kerb height kh, plants = (type, x, y)),
#       'path' (segments of stepping stones, w = width)
# model: which 3D model draws it; 3d/assets/plants/*.glb are CC0 models from Poly Haven, the rest are code-made (3d/models/garden-plants.js, tn-plants.js)
GARDEN=[
 # parking garden PG-1..PG-4 (owner's choice 2026-11-05): nothing on the car's path (it passes 2'7" or more from them), the bike lane and the 5'6" walkway stay clear
 dict(id='PG-1',name='Neem tree well, plain mulch',kind='treebed',x=12.75,y=4.75,r=2.25,
      where='Parking, inside the tree well FU-76 round the neem',note='Red soil kept loose, covered with dry neem leaves as mulch and 5 river stones; nothing planted, as in most real tree wells; water once a week'),
 dict(id='PG-2',name='Bougainvillea in the planter pillar',kind='gatepot',x=12.75,y=0.75,h=6.0,two=1,
      where='Front, in the planter on top of pillar BW-05, between the two gates',note='Pink and white bougainvillea planted together in the pillar planter, a ¾" weep pipe at the base to the gate drain, kept bushy at about 2\' above the top and spilling a little over the sides; trimmed twice a year so it never reaches the gate leaves; low water'),
 dict(id='PG-3',name='Wall ring pots on the east wall',kind='potrow',x=0.375,tray=1,ys=[7.75,9.25,10.75,12.25,13.75,15.25,16.75,18.25],r=0.4,zb=4.5,
      plants=['nithyakalyani','portulaca','kanakambaram','nithyakalyani','portulaca','kanakambaram','nithyakalyani','portulaca'],
      where='Parking, on BW-01 from 7\'4" to 18\'8" in from the gate, 4\'6" up, above the bikes\' handlebars and mirrors',note='8 terracotta pots, 10" across, in black MS wall rings, 1\'6" apart: pink periwinkle, moss rose, orange kanakambaram; each pot sits in a small steel drip tray with a ¼" tube down the wall to the channel PG-8; watered by the drip line PG-9'),
 dict(id='PG-5',name='Ground pots along the east wall',kind='potrow',x=0.375,chan=(7.0,19.5),ys=[7.5,8.75,10.0,11.25,12.5,13.75,15.0,16.25,17.5,18.75],r=0.33,zb=0,
      plants=['croton','malli','vetchi','croton','sembaruthi','croton','malli','vetchi','croton','sembaruthi'],
      where='Parking, on the ground at the foot of BW-01 from 7\'2" to 19\'1" in from the gate (clear of the soak pit UG-02), under the wall pots',note='10 terracotta pots, 8" across, in a row 1\'3" apart, kept trimmed below 2\': croton, jasmine, red ixora, red hibiscus; 9" out from the wall, so the bike pegs and body pass clear and the car passes 2\' or more away'),
 dict(id='PG-8',name='Plant water channels',kind='note',
      where='Under the ground pots PG-5 (foot of BW-01, Y 7\' to 19\'6")',note='6" wide, 3" deep cement channels with black steel gratings; the pots sit on two steel bars over them; 1" fall to the gate end, into the covered drain across the drive (to the rain pit and the road drain), never into the soak pit'),
 dict(id='PG-9',name='Drip line and garden taps',kind='drip',
      taps=[(0.55,19.6,'Garden tap with hose reel, on BW-01 beside the sump UG-03 (pump line)'),(12.75,1.62,'Garden tap on the inner face of pillar BW-05, town supply')],
      runs=[[(0.5,19.6,0.15),(0.5,7.0,0.15)],[(0.43,19.3,0.15),(0.43,19.3,4.4),(0.43,7.5,4.4)],[(12.75,1.62,0.3),(12.75,1.62,4.0)]],
      where='Along BW-01 (two lines: ground pots and wall pots), and up into the BW-05 planter',note='½" black drip pipe with one dripper per pot, a ₹1,500 battery tap timer on each tap set to 10 minutes each morning (20 in May)'),
 dict(id='PG-4',name='Cement trough under W-01',kind='winbox',x1=9.75,x2=13.25,y1=29.08,y2=29.75,zb=2.6,bh=0.67,
      where='Parking, on GW-04 under the study window W-01, its top 1\'3" below the sill so the casement W-01 swings out clear over it',note='3\'3" x 8" x 8" grey cement trough on two brackets, 2\'7" to 3\'3" above the parking, behind the car boot; portulaca (moss rose), almost no water; the AC drain from FU-45 above drips into it'),
 dict(id='GD-01',name='Areca palm (butterfly palm) in a big pot',kind='pot',x=3.72,y=39.4,r=0.5,z='porch',h=5.0,model='areca',lab=(4.75,39.3),
      where='Porch, east corner beside the main door',note='Big terracotta pot, 1\' across, inside the porch handrail FU-91 and clear of the steel door leaf; bright shade under the porch roof suits it; water twice a week, a cup of compost every 2 months'),
 dict(id='GD-02',name='Anthurium (red) in a pot',kind='pot',x=3.8,y=37.95,r=0.5,z='porch',h=1.9,model='anthurium',
      where='Porch, east side, clear of the walk to the door',note='Shade plant, red flowers most of the year; water when the top inch is dry; keep out of the afternoon sun'),
 dict(id='GD-03',name='Syngonium (arrowhead plant) in a pot',kind='pot',x=3.85,y=36.6,r=0.55,z='porch',h=2.0,model='syngonium',
      where='Porch, east side by the steps',note='Easy shade plant like a money plant; water once or twice a week'),
 dict(id='GD-05',name='Mullai (climbing jasmine) on a wire trellis',kind='creeper',x1=0.375,x2=1.125,y1=78.0,y2=82.0,h=6.0,model='mullai',
      where='Side garden, on BW-01 opposite the garden door D-05',note='Planted in a 9" wall bed, trained on 4 steel wires up the wall; scented white flowers at the door; water every 2 days in summer, prune after flowering'),
 dict(id='GD-06',name='Banana (dwarf, Poovan or Grand Naine), a clump of 3',kind='tree',x=2.3,y=86.35,r=1.3,h=7.0,cr=2.5,model='banana',
      where='Side garden, by the east wall, just south of the utility platform FU-77 (its ring clears the platform)',note='Soft, shallow roots, safe near the wall; it needs a lot of water: give it the rinse water from the utility basin FU-30 (not the soapy machine water); keep only 3 stems, cut the old one after the bunch'),
 dict(id='GD-07',name='Vegetable bed (raised)',kind='bed',x1=1.5,x2=4.0,y1=89.75,y2=95.75,kh=1.0,
      plants=[('thakkali',2.15,90.6),('thakkali',3.35,90.6),('kathiri',2.15,92.1),('kathiri',3.35,92.1),('milagai',2.15,93.5),('milagai',3.35,93.5),('keerai',2.15,94.9),('keerai',3.35,94.9)],
      where='Side garden, along the east wall BW-03',note='2\'6" x 6\', 1\' high brick kerb, red soil with compost; tomato, brinjal, chilli and keerai (greens); about 5 hours of sun (midday); water every morning, a drip line with a timer from the utility tap makes it easy'),
 dict(id='GD-08',name='Drumstick tree (Murungai, PKM-1, kept low)',kind='tree',x=3.2,y=100.75,r=1.0,h=10.0,cr=2.2,model='moringa',
      where='Side garden, south-east corner',note='The only tree: light shade, deep roots that do not lift walls; still only 6\'3" from the house, so cut it back to about 8\' after each crop (PKM-1 is the annual kind grown that way); pods and leaves for the kitchen'),
 dict(id='GD-09',name='Herb bed (raised)',kind='bed',x1=7.0,x2=9.25,y1=98.0,y2=101.5,kh=1.0,
      plants=[('pudina',7.55,98.7),('karpooravalli',8.7,98.7),('kothamalli',7.55,99.8),('vallarai',8.7,99.8),('pudina',7.55,100.85),('karpooravalli',8.7,100.85)],
      where='Side garden, south of the house corner, near the kitchen way',note='2\'3" x 3\'6", 1\' high; pudina (mint), karpooravalli (ajwain leaf), kothamalli (coriander), vallarai; water daily in summer'),
 dict(id='GD-10',name='Aloe vera (Sothu kathalai) pots, 2',kind='pot',x=8.1,y=102.35,r=0.45,z='garden',h=1.4,model='aloe',xs=[7.6,8.65],lab=(8.1,103.15),
      where='Side garden, south end of the herb bed',note='Full sun, needs water only once a week; for skin and hair'),
 dict(id='GD-11',name='Lemon (Elumichai) in a big pot',kind='pot',x=19.1,y=101.3,r=0.85,z='garden',h=5.0,model='elumichai',
      where='Back garden, south-west corner, beside the wash platform FU-55',note='2\' pot in the open, sunny corner, next to the tap; a pot keeps its roots small and away from the house; clear of the clothes line and the path'),
]
def garden_stones(g):
    # stepping stones of a 'path' item: (cx, cy, along-x?) for each slab, evenly spaced along each straight run, one slab at each corner
    import math as _m
    out=[]
    for poly in g['segs']:
        for i,(a,b) in enumerate(zip(poly[:-1],poly[1:])):
            L=_m.hypot(b[0]-a[0],b[1]-a[1]); n=max(1,round(L/g['pitch']))
            for k in range(0 if i==0 else 1,n+1):
                t=k/n; out.append((a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t,abs(b[0]-a[0])>abs(b[1]-a[1])))
    return out
GARDEN_NAMES={'thakkali':'Thakkali (Tomato)','kathiri':'Kathirikkai (Brinjal)','milagai':'Milagai (Chilli)','keerai':'Keerai (Amaranth greens)',
 'pudina':'Pudina (Mint)','karpooravalli':'Karpooravalli (Ajwain leaf)','kothamalli':'Kothamalli (Coriander)','vallarai':'Vallarai (Gotu kola)'}
BORES=[('BR-01',21.0-13.25, back_y(21.0-13.25)-27.0,"13'3\" from west, 27' from south"),('BR-02',21.0-17.0, back_y(21.0-17.0)-34.0,"17' from west, 34' from south")]
BOREWELL=BORES[0][1:3]

# ---------- drawing positions (layout specific) ----------
LABELPOS={'G-01':(8.0,24.5),'G-02':(5.6,37.6),'G-03':(6.2,44.6),'G-04':(11.5,53.0),'G-05':(11.45,39.4),'G-06':(11.5,33.6),'G-07':(17.2,33.4),
          'G-08':(8.0,63.4),'G-09':(15.6,64.6),'G-10':(16.0,70.6),'G-11':(9.25,69.6),'G-16':(3.9,70.1),'G-12':(16.2,92.8),'G-13':(1.55,36.0),'G-14':(7.85,93.65),'G-15':(15.2,100.2),
          'F-01':(6.4,18.0),'F-02':(11.9,47.0),'F-04':(12.15,78.0),'F-05':(15.9,93.3),'F-07':(7.6,77.3),'F-08':(15.2,96.6)}
LABELSIZE={'G-14':0.34,'G-16':0.24,'F-07':0.3,'G-09':0.34,'G-11':0.3,'G-05':0.42,'G-12':0.42,'F-05':0.42,'G-09':0.4,'G-13':0.36,'G-06':0.4,'G-07':0.42,'G-11':0.42,'G-03':0.42,'G-02':0.42,'F-06':0.36,'F-07':0.42,'G-10':0.42,'F-04':0.45,'F-03':0.42,'F-01':0.45,'G-09':0.45,'G-01':0.6,'F-02':0.8}
TAGPOS={'GW-01':(3.125,53.0),'GW-05':(20.625,51.0),'GW-07':(9.875,91.5),'BW-01':(0.19,50.0),'GW-04':(19.0,31.125),'GW-13':(12.62,58.44),'GW-12':(17.6,46.56),
        'GW-03':(8.875,33.6),'GW-02':(3.6,40.875),'GW-11':(19.0,35.19),'GW-08':(11.0,94.75),'GW-06':(8.0,73.5),'GW-16':(11.94,71.6),'GW-17':(4.4,67.0),'GW-18':(6.375,72.3),'PW-02':(1.94,40.0),'PW-04':(20.81,40.0),
        'FW-01':(9.875,94.0),'FW-03':(20.625,92.0),'FW-02':(18.4,73.5),'FW-04':(19.0,97.0),'FW-05':(18.0,80.06),'PW-03':(19.4,19.94),'PW-01':(5.0,15.69),'PW-05':(6.0,77.69),
        'GW-15':(18.4,80.44),'GW-14':(8.0,66.81),'GW-10':(13.94,34.6),'GW-09':(9.06,43.0),'BW-03':(1.19,98.0),'BW-07':(20.81,25.0),'BW-08':(20.81,100.5),'BW-02':(0.6,89.19)}
OPENTAGOFF={'W-01':-0.75,'V-01':-0.75,'W-02':0.9,'W-04':-1.0,'W-05':-1.0,'W-06':-1.0,'V-02':-1.0,'W-07':-1.0,'W-08':0.8,'D-01':1.4,'D-13':-1.9,'D-02':-2.2,'D-03':-1.6,
            'O-01':-0.8,'D-04':1.6,'D-05':-1.5,'D-06':1.7,'D-07':1.7,'D-08':-1.4,'D-09':-1.6,'D-12':-0.8,'D-14':1.3,'W-10':-1.0,'W-11':0.8,'W-12':-0.85,'D-10':0.9}
SPC=(17.0,76.875); SPR=35/12   # ST-2 spiral: centre and outer radius (5'10" across)
# ST-2: 21 risers of 6 4/7" (11'6" floor to floor), 20 oak treads of 25.5 deg + a 60 deg landing at the first floor (same total turn as before, so the top lands the same way).
# Climbs anticlockwise (outer handrail on your right going up). Tread 1 starts on the 345 deg line (plan angle: 0 = west, 90 = south),
# so you walk onto it heading south along GW-05; the landing (135-195 deg) opens east onto F-04. RCC well: 6' round hole.
ST2=dict(n=21,ang=25.5,start=345,land=60,well=3.0,col=2.25/12)
CH_G_E=[0,30.75,40.5,41.25,46.75,58.25,58.625,66.625,67.375,73.875,89.0,106.0]
CH_G_W=[0,4.333,16.0,19.5,29.75,30.5,35.0,35.375,46.375,46.75,58.25,58.625,68.0,80.25,80.625,94.375,95.125,105.0]
CH_G_BACK_Y=104.0
CH_F_W=[15.5,20.125,73.125,73.875,79.875,80.25,94.375,95.125,98.125]
CH_F_BACK_Y=98.6

# ---------- furniture and fixtures (proposal) ----------
# id, floor, name, x1, x2, y1, y2, kind, side, note
# side = which edge is the head (bed) / back (sofa, WC): 'x1','x2','y1','y2'. Y grows toward the back.
FURNITURE = [
 ('FU-01','G','Shoe rack',7.25,8.5,35.25,38.25,'shelf',None,'Porch, on GW-03: open wooden shoe rack in walnut tone, 3\' long x 1\'3" deep x 2\'2" high, 3 open shelves and a top (keys, a small plant), open back (as the owner\'s photo); under the W-02 sill'),
 ('FU-90','G','Sunken doormat well (CD-02)',4.5,8.0,38.5,40.5,'mat',None,'Porch floor in front of D-13: 3\'6" x 2\', 3/4" deep, black granite edge, coir mat flush with the floor; nothing to trip on'),
 ('FU-91','G','Porch step handrail (CD-03)',3.05,3.2,32.75,40.35,'rail',None,'Black MS pipe 1 1/2" on posts, 2\'9" above the step noses, along the east side of the 3 porch steps and on along the whole open east edge of the porch to the main-door wall, on the porch side kerb; the steps get flamed (rough) granite treads with a 2" black granite edge strip'),
 ('FU-95','G','Window seat with storage (CD-07)',10.25,18.75,92.625,94.375,'seat',None,'Bedroom 2, under the picture window W-08: brick seat 1\'6" high x 1\'9" deep, black granite top, three storage bays with shutters below; 2\'7" clear to the bed foot'),
 ('FU-96','G','Shower niche (CD-08)',18.0,19.5,30.5,30.85,'niche',None,'Toilet 1 shower, in GW-04: 1\'6" wide x 1\'2" high x 4" deep, 3\'6" up, tiled, sloped granite base'),
 ('FU-97','G','Shower niche (CD-08)',6.75,7.1,67.6,69.1,'niche',None,'Toilet 2 shower, in GW-18: 1\'6" wide x 1\'2" high x 4" deep, 3\'6" up, tiled, sloped granite base (replaces the bath rack FU-70)'),
 ('FU-98','F','Shower niche (CD-08)',2.125,2.475,74.0,75.5,'niche',None,'Toilet 3 shower, in FW-08 below the geyser: 1\'6" wide x 1\'2" high x 4" deep, 3\'6" up, tiled, sloped granite base'),
 ('FU-99','G','Linear shower drain (CD-09)',17.5,20.0,32.45,32.6,'drain',None,'Toilet 1: steel channel 2\'6" long at the edge of the shower; whole floor level with the bedroom (no step at D-03), sloped 1 in 50 to it'),
 ('FU-99.2','G','Linear shower drain (CD-09)',7.25,9.75,69.45,69.6,'drain',None,'Toilet 2: steel channel 2\'6" long at the edge of the shower; no step at D-04, floor sloped 1 in 50'),
 ('FU-99.3','F','Linear shower drain (CD-09)',2.3,4.8,76.0,76.15,'drain',None,'Toilet 3: steel channel 2\'6" long under the curtain line; no step at D-09, floor sloped 1 in 50'),
 ('FU-100','G','Grab rail (CD-10)',18.0,19.5,34.85,35.0,'rail',None,'Toilet 1, on GW-11 beside the WC, 1\'6" steel rail at 2\'9"; wall behind kept solid brick'),
 ('FU-100.2','G','Grab rail (CD-10)',7.0,8.5,72.975,73.125,'rail',None,'Toilet 2, on GW-06 beside the Indian WC, 1\'6" steel rail at 2\'3" to help standing up; wall kept solid'),
 ('FU-100.3','F','Grab rail (CD-10)',2.125,2.275,76.9,78.4,'rail',None,'Toilet 3, on FW-08 beside the WC, 1\'6" steel rail at 2\'9"; wall kept solid'),
 ('FU-03.1','G','3-seat sofa',3.5,6.0,49.5,55.75,'sofa','x1','Living, 6\'3" x 2\'6", back to GW-01 under the windows, moved toward GW-13'),
 ('FU-03.2','G','2-seat sofa',6.0,10.25,55.75,58.25,'sofa','y2','Living, 4\'3" x 2\'6", back against GW-13 (below the folding glass sill); starts where FU-03.1 ends so every seat is free'),
 ('FU-04','G','Coffee table',7.0,10.0,50.75,54.25,'table',None,'Living, 3\' x 3\'6", centred in the L'),
 ('FU-05','G','TV, showcase and bookshelf wall unit',18.917,20.25,46.75,58.25,'tvwall',None,'Living, 11\'6" x 1\'4", full height on GW-05, wall to wall: TV in the middle, showcase and book shelves on both sides'),
 ('FU-06','G','Queen bed',13.75,20.25,41.25,46.25,'bed','x2','Bedroom 1, 6\'6" x 5\', head to GW-05 (east-west), side against GW-12'),
  ('FU-09.1','G','Wardrobe',18.3333,20.25,35.375,39.6,'ward',None,'Bedroom 1, one straight rectangle on GW-05 (no L): 4\'3" x 1\'11", three oak shutters with loft, full-length mirror 1\'2" x 5\' on the south shutter'),
  ('FU-09.2','G','Bedside and accessory niche column',18.3333,20.25,39.6,40.875,'ward',None,'Bedroom 1, south end of the wardrobe by the bed head, same depth and loft: closed cupboard to 1\'9", then one tall open cut-out to 6\'5" (open on the front and the bed side, rounded edges) for the phone at night (charging point BS-1 inside), make-up and accessories on two small set-back shelves with rounded corners; closed above'),
 ('FU-10','G','Sewing machine table',10.0,13.25,30.6,32.25,'desk',None,'Study, under W-01: white top 3\'3" x 1\'8" at 2\'6" with a ruler strip on the front edge, black iron stand, foot pedal; Singer-type machine'),
 ('FU-12','G','Western WC',18.0,20.25,32.9,34.4,'wc','x2','Toilet 1, wall-mounted cistern'),
 ('FU-13','G','Wash basin',14.125,15.5,30.5,31.9,'basin',None,'Toilet 1'),
 ('FU-14','G','Shower area',17.25,20.25,30.5,32.6,'shower',None,'Toilet 1, open (no screen), floor slopes to a 5" square floor trap, geyser above'),
 ('FU-63','G','Bath rack, 2 shelves',15.6,16.9,30.5,30.95,'over',None,'Toilet 1, wall-mounted on GW-04 between the basin and the shower, for soap, shampoo and toothbrushes'),
 ('FU-15','G','Kitchen counter, east',3.5,5.5,58.625,66.625,'counter',None,'Kitchen, 8\' x 2\' on GW-01'),
 ('FU-16','G','Kitchen counter, back (modular)',5.5,8.6,64.625,66.625,'counter',None,'Kitchen, 3\'1" x 2\' on GW-14, with base drawers and the sink'),
 ('FU-16.2','G','Low counter, wet grinder and water',8.6,12.125,64.625,66.625,'counter',None,'Kitchen, 3\'6½" x 2\' on GW-14 up to the toilet 2 wall, top at 2\' from the floor: wet grinder at the sink end, water pots under the RO purifier at the other end'),
 ('FU-17','G','Breakfast counter',5.5,13.5,58.625,59.875,'counter2',None,'Kitchen, 8\' x 1\'3" on GW-13, under the folding glass W-12; joins the east counter with no gap, extended into the old fridge place, microwave at its west end'),
 ('FU-18','G','Fridge, double door',17.75,20.25,58.625,61.17,'fridge',None,'Open area, double door, 67 W x 68 D x 175 H cm (2\'2½" x 2\'2¾" x 5\'9"), in the fridge bay at the north end of the store cupboard FU-25 (one unit: same front line, end panel and loft), a 2\'6½" wide slot: 2" air each side and at the back; 1\' clear above its top (to 6\'9") for a stabilizer, then the loft'),
 ('FU-19','G','Overhead cabinets, back',4.75,8.25,65.375,66.625,'over',None,'Kitchen, on GW-14 above the back counter and sink, glass doors on the unit above the sink, RO purifier below them (dashed)'),
 ('FU-68','G','Top storage, back',4.75,12.125,65.375,66.625,'over',None,'Kitchen, second row of cabinets on GW-14 from 7\' up to the ceiling, right along to the end of the low counter, over the RO purifier and the wet grinder (K-16 and K-18) (dashed)'),
 ('FU-69','G','Top storage, east',3.5,4.75,58.625,66.625,'over',None,'Kitchen, second row of cabinets on GW-01 from 7\' up to the ceiling, right across above the window and chimney (dashed)'),
 ('FU-19.2','G','Overhead shelves, east',3.5,4.75,65.0,66.625,'over',None,'Kitchen, corner unit above the east counter beside the window (dashed)'),
 ('FU-19.3','G','Overhead shelves, east',3.5,4.75,58.625,61.0,'over',None,'Kitchen, above the east counter beside the window, glass door (dashed)'),
 ('FU-25','G','Store cupboard, civil work',17.75,20.25,61.25,71.375,'store2',None,'Open area and stair hall, 10\'1½" x 2\'6", joined to the fridge FU-18 (1½" air gap for the fridge side), floor to 9\'4" on GW-05: four kadappa bays S-1 to S-4 (S-3 a 4\' tall-things bay with an adjustable shelf) with UPVC wood-look shutters and a loft above 7\'6"; inverter and battery at the foot of S-4 (see the Store tab)'),
 ('FU-26.1','G','WC platform, 4" high',6.75,10.25,70.625,73.125,'plat',None,'Toilet 2, tiled platform in the south-east corner (GW-18 and GW-06): 3\'6" front to back (east-west, the way the user faces) x 2\'6" side to side, room to squat comfortably'),
 ('FU-26','G','Indian WC (Orissa pan)',7.05,8.97,71.145,72.605,'iwc',None,'Toilet 2, centred on the 4" platform FU-26.1 against the east wall GW-18, user faces west, V-02 above; health faucet on GW-06 on the left hand'),
 ('FU-57','G','Bucket, tap and health faucet',9.25,10.15,72.15,73.05,'bucket',None,'Toilet 2, on the front of the platform on the user\'s left, bib tap on GW-06; health faucet on GW-06 beside the pan'),
 ('FU-27','G','Wash basin, wall-hung',10.3,11.72,71.96,73.125,'basin',None,'Toilet 2, 1\'5" x 1\'2" on GW-06 in the corner by the door, beside the platform (clear of the door swing); mirror above; rim 2\'8"'),
 ('FU-28','G','Shower area',6.75,11.75,67.0,69.625,'shower',None,'Toilet 2, 5\' x 2\'7½" across the whole north end, open (no screen); rose on GW-14 at 6\'9"; floor trap in the middle; floor slopes 1:60; the door folds back over it'),
 ('FU-58','G','Geyser',7.0,8.4,67.0,67.475,'geyser',None,'Toilet 2, on GW-14 above the shower, clear of the rose, bottom at about 6\'3"'),
 ('FU-79','G','Landing outside D-05 (AU-08)',6.0,9.5,73.875,77.375,'plat',None,'Granite landing 3\'6" x 3\'6", 6" up from the garden; D-05 is 1\' above the garden, so one 6" step down to the landing and one to the garden; the door leaf opens over it, room to stand with a laundry basket'),
 ('FU-77','G','Utility platform',0.375,2.625,82.0,84.75,'plat',None,'Side garden utility, along BW-01 opposite bore BR-01, 4" above the garden, grey anti-skid tiles, floor drain in front of the basin; white tiles on BW-01 behind them'),
 ('FU-29','G','Washing machine, front-load 8 kg',3.5,5.45,67.45,69.45,'wm',None,'Bore court G-16, under the terrace slab (no sun or rain), back to GW-17, front to the south; the drying rack FU-75 starts right beside it, so you wash and hang in one place; tap, socket and drain come through GW-17 from the kitchen sink line; 60 x 60 x 85 cm; about 2\'8" clear in front, to BR-02; move it out if the bore is ever serviced'),
 ('FU-30','G','Utility wash basin with tap',0.375,1.875,82.5,84.25,'basin',None,'Side garden utility, against the east compound wall BW-01, straight across from its old place on GW-07: granite counter 2\'9" high with a deep steel sink, tall swan-neck tap, a low tap for buckets, white tiles behind'),
 ('FU-31','G','Queen bed',13.75,20.25,85.5,90.5,'bed','x2','Bedroom 2, head to GW-05'),
 ('FU-32','G','Drawer unit under the mirror',19.75,20.25,83.75,85.21,'cab',None,'Bedroom 2, slim, part of the mirror unit joined to the wardrobe FU-34: 3 drawers, 2\' high x 6" deep, oak veneer to match the wardrobe, black pulls: powder, comb and such'),
 ('FU-102','G','Full-length mirror',20.15,20.25,83.79,85.17,'mirror',None,'Bedroom 2, on GW-05 in the slim mirror unit, over the drawers FU-32: 1\'4" wide, from 2\' to 7\' above the floor'),
 ('FU-103','G','Accessory racks',19.75,20.25,82.54,83.75,'cab',None,'Bedroom 2, slim (6" deep), north side of the mirror, joined to the wardrobe FU-34: closed oak base to 2\', two open racks for accessories at 3\'7" and 5\'2", loft above 7\'7" like the wardrobe'),
 ('FU-33','G','Side table',18.85,20.25,90.75,92.25,'cab',None,'Bedroom 2, floating oak side table with a drawer and a lamp at the bed end, on GW-05'),
 ('FU-34','G','Sliding wardrobe with loft',14.4,19.75,80.625,82.5417,'ward',None,'Bedroom 2, 5\'4" x 1\'11", on GW-15: 5" shorter at the door end for the switch board SB-9 and stopping 6" short of the west wall, in line with the mirror unit, so no shutter is ever behind the racks FU-103; the 6" corner is a closed oak filler; three 1\'9" sliding shutters on two tracks (one bay opens at a time), 2\'11" clear in front to the bed (AU-16, AU-17)'),
 ('FU-36','F','Queen bed',13.75,20.25,85.25,90.25,'bed','x2','Bedroom 3, head to FW-03'),
 ('FU-37','F','Drawer unit under the mirror',19.75,20.25,83.38,84.84,'cab',None,'Bedroom 3, slim, part of the mirror unit joined to the wardrobe FU-39 (as bedroom 2): 3 drawers, 2\' high x 6" deep, oak veneer to match the wardrobe, black pulls'),
 ('FU-104','F','Full-length mirror',20.15,20.25,83.42,84.80,'mirror',None,'Bedroom 3, on FW-03 in the slim mirror unit, over the drawers FU-37: 1\'4" wide, from 2\' to 7\' above the floor'),
 ('FU-105','F','Accessory racks',19.75,20.25,82.17,83.38,'cab',None,'Bedroom 3, slim (6" deep), north side of the mirror, joined to the wardrobe FU-39: closed oak base to 2\', two open racks at 3\'7" and 5\'2", loft above 7\'7" like the wardrobe'),
 ('FU-38','F','Side table',18.75,20.25,90.5,92.0,'cab',None,'Bedroom 3'),
 ('FU-39','F','Sliding wardrobe with loft',14.5,19.75,80.25,82.1667,'ward',None,'Bedroom 3, 5\'3" x 1\'11" (AU-16), on FW-05 (where toilet 3 was), stopping 6" short of the west wall in line with the mirror unit, so no shutter is ever behind the racks FU-105; the 6" corner is a closed oak filler; three 1\'9" sliding shutters'),
 ('FU-40','F','Study desk',14.5,18.5,92.875,94.375,'desk',None,'Bedroom 3, on FW-04 under the back window W-11, chair in front; the east side by W-10 is left clear as the way to the balcony door'),
 ('FU-41','F','Western WC',2.458,4.708,78.25,79.875,'wc','y2','Toilet 3, in the south-east corner, cistern on FW-07, faces north; 2\' clear in front'),
 ('FU-42','F','Wash basin, wall-hung',7.4,8.9,73.5,74.875,'basin',None,'Toilet 3, on FW-09 (north wall) near the door, clear of the door swing; mirror above'),
 ('FU-43','F','Shower area',2.125,6,73.5,76.25,'shower',None,'Toilet 3, 3\'10" x 2\'9" in the north-east corner; floor trap in the middle'),
 ('FU-60','F','Geyser',2.125,2.575,74.0,75.4,'geyser',None,'Toilet 3, on FW-08 above the shower, bottom at about 6\'3"'),
 ('FU-61','F','Shower curtain rod',2.125,6,76.15,76.25,'curtain',None,'Toilet 3, keeps the WC side dry'),
 ('FU-62','F','Exhaust fan',2.125,2.6,76.75,77.75,'fan',None,'Toilet 3, on the outside wall FW-08, high up, blowing out over the side garden'),
 ('FU-71','F','Overhead water tank, 2000 L',15.2,20.2,89.2,94.2,'over',None,'On the bedroom 3 roof (above F-05), 5\' across x 5\' high on a 1\' RCC stand near FW-03; highest point for good pressure, clear of the future hall'),
 ('FU-72','F','Cat ladder to the bedroom 3 roof',18.0,19.5,72.6,73.125,'over',None,'MS ladder on the terrace face of FW-02, for reaching the water tank'),
 ('FU-44','G','AC indoor unit',9.25,9.92,37.1,40.1,'acin',None,'Bedroom 1, on GW-03 above window W-02, about 7\'6" high'),
 ('FU-45','G','AC outdoor unit',9.0,11.67,28.58,29.75,'acout',None,'Bedroom 1, on GW-04 parking face, bracket above window W-01 (about 7\'6"); pipe runs inside the study corner'),
 ('FU-46','G','AC indoor unit',10.25,10.92,85.5,88.5,'acin',None,'Bedroom 2, on GW-07 centred above window W-07 (about 7\'7"), blows straight across the bed'),
 ('FU-47','G','AC outdoor unit',8.33,9.5,89.6,92.27,'acout',None,'Bedroom 2, on the GW-07 side-garden face, south of window W-07 (moved for the utility)'),
 ('FU-48','F','AC indoor unit',10.25,10.92,86.25,89.25,'acin',None,'Bedroom 3, on FW-01 centred above window W-10, straight in front of the bed FU-36 (about 7\'10"), blows along the bed'),
 ('FU-49','F','AC outdoor unit',18.0,20.625,96.5,97.75,'acout',None,'Bedroom 3, on the balcony 3 floor at the west end on a 6" stand, easy to service (AU-33); pipe along the FW-04 outside face'),
 ('FU-51','G','Kitchen sink',6.5,8.4,64.875,66.375,'sinkbowl',None,'Kitchen, single bowl on the back counter FU-16, against GW-14'),
 ('FU-64','G','Mixer grinder',3.75,4.6,59.0,59.85,'appl',None,'Kitchen, east counter in the GW-13 corner, socket on GW-01'),
 ('FU-65','G','Wet grinder, table-top',10.75,11.95,64.95,66.15,'appl',None,'Kitchen, on the west end of the 2\' low counter FU-16.2 (where the RO purifier was), socket on GW-14'),
 ('FU-66','G','RO water purifier, wall-mounted',8.488,9.637,65.706,66.625,'over',None,'Kitchen, on GW-14 in the place of wall unit K-14 (removed), 558 x 350 x 280 mm (H x W x D), bottom at 5\' from the floor; water pots fill standing on the 2\' low counter below'),
 ('FU-67','G','Microwave oven',11.82,13.33,58.67,59.85,'appl',None,'Kitchen, on the black counter top over the open baskets K-11, at the west end of the breakfast counter FU-17; 20 L solo microwave, 46 x 28 x 36 cm (downloaded model, archibase.net); socket behind it on GW-13'),
 ('FU-52','G','Gas stove, 3 burner, glass top (free-standing)',4.015,5.360,61.500,63.797,'hob',None,'Kitchen, stands on the counter over the cylinder unit K-02, 1\' north of the drying rack (not built in, lift it off to clean), 70 x 41 x 13 cm; gas hose down through a grommet to the cylinder in K-02 below; chimney hood above, just over the window head'),
 ('FU-81','G','Chimney hood, 60 cm, ducted',3.5,5.082,61.666,63.634,'over',None,'Kitchen, over the stove FU-52: wall chimney 60 cm wide, about 41 cm high and 48 cm deep (sloping black glass hood and a short upright body), bottom at 5\'4" (2\'6" above the counter, just over the W-06 head); a 6" (150 mm) round aluminium duct goes straight back from the top of the body through GW-01 at 6\'4" (core-cut hole just above the window lintel), so no pipe shows; needs 61 cm clear between the cabinets (dashed)'),
 ('FU-82','G','Chimney duct outlet with cowl',2.55,2.95,62.35,62.95,'over',None,'Outside on the east face of GW-01, 6\'4" up: a steel cowl with a downward opening and a back-draft flap, so rain and birds cannot come in (dashed)'),
 ('FU-83','G','Slab over the washing machine',2.75,6.0,67.375,70.0,'over',None,'Bore court: 2" RCC (or kadappa stone) slab 4\'9" above the court floor (high enough to open the lid of a top-load machine later), wall to wall between GW-17 and GW-18, with a 3" drip edge at the front, and a 4½" side wall under it on the open side-passage side, so rain cannot reach the machine; its top is a shelf for detergent (dashed)'),
 ('FU-87','G','EB meter and sump pump control box',15.55,17.55,29.25,29.75,'panel',None,'Parking, on GW-04 just west of the parking board PB-1 and the study window W-01: one 2\' x 1\'7" x 6" deep grey box, 4\'5" to 6\' above the parking (above bike and child height); left half the EB meter and main switch behind a reading glass, right half the sump pump starter and dry-run cut-off, one lockable door'),
 ('FU-88','G','Wall tap with hose',0.375,0.625,28.75,29.25,'tap',None,'Parking, on the east compound wall BW-01 just in front of the bikes, before the porch steps: one brass tap on a ½" GI pipe at 2\'6", a hose on a wall reel above it for the plants, the car and the bikes, and a small floor drain; only 3" out from the wall, so the way into the side passage is fully open (the wash basin is dropped)'),
 ('FU-86','G','Bore pump control panel (BR-02)',5.5,6.0,72.3,73.5,'panel',None,'Bore court, on GW-18 at 4\'6" to 5\'9", a 6" deep box, the wiring hidden inside the wall: starter and capacitor box for the submersible pump in BR-02, with dry-run, voltage and overload protection; no motor unit above ground; the bore head has a non-return valve and a gate valve; bore water goes to the sump UG-03, or straight up to the tank FU-71 by a valve'),
 ('FU-54','G','Garden tap point',1.375,2.2,97.0,98.35,'gtap',None,'Side garden, south-east, on the east compound wall BW-03 between the vegetable bed GD-07 and the drumstick GD-08: a brass wall tap (bib cock with a hose union) 2\' up on white wall tiles, a 4" grey tiled step with a floor drain under it and a wall hose reel beside it; for watering the garden and filling buckets; no sink'),
 ('FU-55','G','Wash platform',2.2,4.2,96.4,98.95,'washpad',None,'Side garden, south-east, grey anti-skid paving in front of the garden tap FU-54, sloping to a floor drain'),
 ('FU-76','G','Tree well round the neem',10.5,15.0,2.5,7.0,'treepit',None,'Parking, 4\'6" across, centred 6" south of the trunk because the trunk leans south (it stays inside the ring up to the platform height): the trunk stays at today\'s ground; a low retaining ring, 4½" brick with a granite coping; about 10" of open soil with leaf mulch all round the 1\'6" trunk; small so the car can pass'),
 ('FU-73','G','Flower bed along the back wall',1.375,20.625,103.14,105.6,'fbed',None,'Back and side garden, 1\'6" deep all along the back wall BW-09, 9" brick kerb, red soil; a row of Tamil Nadu flowering plants PL-01 to PL-12'),
 ('FU-75','G','Clothes drying rack, ceiling pulley',3.1,5.65,70.25,78.25,'airer',None,'Bore court and the covered side garden under toilet 3, just south of the washing-machine slab FU-83: 5 steel rods 8\' long on a ceiling pulley under the slab; lower it to 5\'6" to hang clothes straight from the machine, pull it up to 8\' to dry; under cover, so clothes dry in the monsoon too, and the floor stays clear for the bore rig (dashed)'),
]
# door and window types (proposal)
SPEC = {
 'D-01':'Teak wood, one 4\' leaf hinged on the east side; the steel door D-13 is in front of it',
 'D-14':'MS grill door, black powder-coat, same make as D-13: 1"x1" box frame, 1/2" square bars at 4", middle rail, 1\'6" sheet panel at the foot; one leaf, tower bolts and a lock',
 'D-13':'MS safety door, black powder-coat: 1"x1" box frame, 1/2" square bars at 4", middle rail, 1\'6" sheet panel at the foot; double leaf, centre joint in line with D-01; tower bolts top and bottom, a lock and floor stoppers',
 'D-02':'Flush door, hardwood frame', 'D-06':'Flush door, hardwood frame', 'D-07':'Flush door, hardwood frame',
 'D-03':'WPC waterproof door', 'D-04':'WPC waterproof door', 'D-08':'WPC waterproof door',
 'D-05':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'W-01':'UPVC sliding window; black grill; inside: venetian blind with 2" faux-wood slats that tilt (wand) and pull up (cord); outside box frame WF-1 with the scalloped sunshade, same as the other front windows',
 'D-09':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'O-01':'Plastered arch opening, no shutter',
 'W-12':'Bi-fold glass window, aluminium or UPVC frame, curtain on the living side',
 'GT-01':'MS swing gate, double leaf (no room on the wall for a sliding gate)', 'GT-02':'MS double-leaf hinged gate, opens inward',
}
for _o in OPENINGS:
    if _o[5]=='window' and _o[0] not in SPEC: SPEC[_o[0]]='UPVC 3-track sliding: 2 glass + 1 mosquito mesh, MS safety grill, 1\'6" sunshade outside'
    if _o[5]=='vent' and _o[0] not in SPEC: SPEC[_o[0]]='Louvred glass ventilator with exhaust fan opening'
SPEC['W-08']='Back window, 4\' wide: two UPVC casements (2\' each) with mosquito mesh; slim black MS grill, the same as the other windows (AU-20; the invisible wire grill is dropped, as it is child-safe but not theft-proof); 1\'6" sunshade outside'
SPEC['V-03']='Louvred glass ventilator with exhaust fan opening'

# ---------- store cupboard FU-25 as civil work (owner's queue item 3; inverter and battery at the foot of S-4) ----------
# 10'4.5" x 2'6" on GW-05, Y 61' to 71'4.5" (joined to the fridge FU-18), floor to 9'4" (under the band). 1½" kadappa uprights make four bays (S-3 is 4' wide for tall things); 1" kadappa shelves sit 1" into the uprights;
# a 3" brick plinth with a kadappa top keeps the floor dry when mopping. Shutters: UPVC wood-look (oak film), soft hinges, black J handles; loft shutters separate above 7'6".
# heights in feet from the floor; contents are a starting plan, to be resized when the owner sends their item list.
STORE=dict(fu='FU-25',plinth=0.25,loftz=7.5,top=9.33,depth=2.5,inner=2.25,
 bays=[dict(id='S-1',name='Grains and dry stock',y1=61.25,y2=63.375),dict(id='S-2',name='Vessels and appliances',y1=63.375,y2=65.375),
       dict(id='S-3',name='Tall things, adjustable shelf',y1=65.375,y2=69.375,adjustable=True),dict(id='S-4',name='Inverter, battery and supplies',y1=69.375,y2=71.375,power=True)],
 # cells: id, bays it spans, bottom and top (feet from the floor), use. The slab on top of each cell is kadappa unless it is the loft line or the S-3 adjustable shelf.
 # S-1.1 (bottom) and S-1.4 (top) are wide cells across S-1 and S-2: the upright between those bays runs only from 2'3" to 5'6".
 cells=[
  dict(id='S-1.1',bays=('S-1','S-2'),z1=0.25,z2=2.25,use='Wide low cell: rice and atta drums (2 x 25 kg), big vessels, idli steamer, big pressure cookers'),
  dict(id='S-1.2',bays=('S-1',),z1=2.25,z2=4.0,use='Tall cell'),
  dict(id='S-1.3',bays=('S-1',),z1=4.0,z2=5.5,use='Tall cell'),
  dict(id='S-2.2',bays=('S-2',),z1=2.25,z2=4.25,use='Tall cell'),
  dict(id='S-2.3',bays=('S-2',),z1=4.25,z2=5.5,use='Cell'),
  dict(id='S-1.4',bays=('S-1','S-2'),z1=5.5,z2=7.5,use='Wide tall top cell over S-1 and S-2 (no upright between them here)'),
  dict(id='S-3.1',bays=('S-3',),z1=0.25,z2=5.0,use='Big and tall things (below the shelf): vacuum cleaner, ironing board, 5-step ladder, broom, mop and bucket, folding cot, big suitcase, water cooler, 25 L cans; hooks on the side walls',slab='adjustable'),
  dict(id='S-3.2',bays=('S-3',),z1=5.0,z2=7.5,use='Cleaning stock (above the shelf): detergent, cleaner, toilet rolls, spare mop heads'),
  dict(id='S-4.1',bays=('S-4',),z1=0.25,z2=1.5,use='Battery: lithium, 53 x 18 x 27.5 cm (1\'9" x 7" x 10¾" high), lying along the bay, 3" clear above for the terminals and cables'),
  dict(id='S-4.2',bays=('S-4',),z1=1.5,z2=2.5,use='Inverter: 36 x 35 x 20 cm (1\'2" x 1\'1¾" x 8" high), front to the shutter, air on the sides and top; louvred shutter'),
  dict(id='S-4.3',bays=('S-4',),z1=2.5,z2=3.75,use='Tool box, drill, extension boards'),
  dict(id='S-4.4',bays=('S-4',),z1=3.75,z2=5.0,use='First-aid box and medicines (eye level, easy to find)'),
  dict(id='S-4.5',bays=('S-4',),z1=5.0,z2=6.25,use='Documents file box, chargers, batteries, bulbs'),
  dict(id='S-4.6',bays=('S-4',),z1=6.25,z2=7.5,use='Emergency lamp, spare fuses, paint and plumbing spares, warranty cards'),
 ],
 upright=0.125,shelf_t=1/12,
 loft=[('L-1','Suitcases and travel bags',61.25,64.708),('L-2','Festival and seasonal items',64.708,68.042),('L-3','Spare bedding, blankets, pillows',68.042,71.375)],
 power=['16 A socket and its own 25 A MCB inside S-4 for the inverter; the inverter output runs to the main board (lights and fans on inverter)','Battery cable under 3\' long, inverter above the battery, both on kadappa (no wood under them)','Louvred UPVC shutter on S-4 below 2\'6" (vents top and bottom); lithium needs little air, but the inverter fan needs a path','The inverter display faces out at about 2\' high; open the S-4 lower shutter to read it or switch modes'],
 assumed='Owner\'s sizes: inverter 36 x 35 x 20 cm, battery 53 x 18 x 27.5 cm. The S-4 bay is 1\'10½" wide and 2\'3" deep inside. Battery space: plinth to the shelf at 1\'6" gives 1\'2" high, so the 10¾" battery has 3" over it. Inverter space: 1\'6" to 2\'6" gives 11" high for the 8" inverter. Both fit with air round them.',
 adjust='S-3 adjustable shelf: black powder-coated slotted steel strips (2 on each side wall, front and back) with slots every 2", screwed to the kadappa uprights; a pair of brackets per strip carries a 1" kadappa or 18 mm marine-ply shelf, 3\'10" x 2\'2". Lift it out and hook it in at any height from 1\' to 7\'. About ₹2–3k.',
 cost='Kadappa uprights and shelves about 200 sq ft at ₹90–115: ₹18–23k; plinth and labour ₹6–8k; UPVC wood-look shutters about 90 sq ft at ₹500–650: ₹45–58k. Total about ₹70–90k (a full carpentry cupboard of this size is about ₹1.3–1.6 lakh).')

# store shutters: one shutter per cell (two leaves when the cell is wider than 3'), louvred on the inverter and battery cells; the loft has its own; the fridge bay
# (FU-18) is the north end of the same unit: open slot for the fridge, 1' stabilizer space, then a loft shutter on the fridge-top line
def _store_shutters(S):
    B={b['id']:b for b in S['bays']};out=[]
    for c in S['cells']:
        y1,y2=B[c['bays'][0]]['y1'],B[c['bays'][-1]]['y2'];n=2 if y2-y1>3 else 1
        for k in range(n): out.append(dict(cell=c['id'],y1=y1+k*(y2-y1)/n,y2=y1+(k+1)*(y2-y1)/n,z1=c['z1'],z2=c['z2'],hinge='a' if (n==1 or k==0) else 'b',louvred=c['id'] in ('S-4.1','S-4.2')))
    for L in S['loft']: out.append(dict(cell=L[0],y1=L[2],y2=L[3],z1=S['loftz'],z2=S['top'],hinge='a',louvred=False))
    return out
STORE['shutters']=_store_shutters(STORE)
STORE['fridge']=dict(fu='FU-18',y1=58.625,y2=61.17,top=175/30.48,stab=1.0)

# ---------- windows (chosen 2026-11-05 from window-catalogue.html): type, frame, glass, grill, mesh ----------
# WT-1 3-track sliding, WT-2 casement (side-hung, opens out, grill inside), WT-3 sliding with a 1' top-hung vent, WT-4 fixed glass with an opening top pane, WT-5 louvre
# WF-B black (anthracite) UPVC; WG-1 clear 5 mm, WG-2 frosted lower half, WG-3 heat-cut (solar control), WG-4 frosted; GR-1 plain black bars; WM-1 sliding mesh pane, WM-2 pleated mesh
WINDOWS={
 'W-01':dict(type='WT-2',frame='WF-B',glass='WG-1',grill='GR-1',mesh='WM-2',why='opens out over the parked car: the sash bottom is about 6\' above the parking, higher than the car roof; the trough PG-4 is lowered clear of it'),
 'W-02':dict(type='WT-1',frame='WF-B',glass='WG-2',grill='GR-1',mesh='WM-1',why='porch: people and the shoe rack below, so it slides; widened to 4\' for more opening'),
 'W-04':dict(type='WT-3',frame='WF-B',glass='WG-1',grill='GR-1',mesh='WM-1',why='the top vent lets hot air out all day'),
 'W-05':dict(type='WT-3',frame='WF-B',glass='WG-1',grill='GR-1',mesh='WM-1',why='the top vent lets hot air out all day'),
 'W-06':dict(type='WT-4',frame='WF-B',glass='WG-1',grill='GR-1',mesh='WM-2',why='no reaching over the flame; wind cannot blow out the burner'),
 'W-07':dict(type='WT-2',frame='WF-B',glass='WG-1',grill='GR-1',mesh='WM-2',why='opens fully onto the side garden'),
 'W-08':dict(type='WT-2',frame='WF-B',glass='WG-1',grill='GR-1',mesh='WM-2',why='4\' wide like W-07; two casements open fully'),
 'W-10':dict(type='WT-2',frame='WF-B',glass='WG-3',grill='GR-1',mesh='WM-2',why='first floor, morning sun: heat-cut glass'),
 'W-11':dict(type='WT-1',frame='WF-B',glass='WG-1',grill='GR-1',mesh='WM-1',why='opens onto balcony 3 where people walk, so it slides'),
 'W-12':dict(type='fold',frame='WF-B',glass='WG-1',grill=None,mesh=None,why='inside window, frame matches the others'),
 'V-01':dict(type='WT-5',frame='WF-B',glass='WG-4',grill='GR-1',mesh=None,why='air and privacy, exhaust fan cut-out'),
 'V-02':dict(type='WT-5',frame='WF-B',glass='WG-4',grill='GR-1',mesh=None,why='air and privacy, exhaust fan cut-out'),
 'V-03':dict(type='WT-5',frame='WF-B',glass='WG-4',grill='GR-1',mesh=None,why='air and privacy, exhaust fan cut-out'),
}
WIN_NAMES={'WT-1':'3-track sliding (2 glass + 1 mesh)','WT-2':'casement, side-hung, opens out (grill inside)','WT-3':'3-track sliding with a 1\' top-hung vent above','WT-4':'fixed glass below, top-hung opening pane above','WT-5':'louvre ventilator','fold':'bi-fold glass',
 'WF-B':'black (anthracite) UPVC frame','WG-1':'clear 5 mm glass','WG-2':'clear glass, frosted lower half','WG-3':'heat-cut (solar control) glass','WG-4':'frosted glass','GR-1':'plain black MS bars, 12 mm at 5"','WM-1':'sliding mosquito mesh pane','WM-2':'pleated mosquito mesh'}
for _k,_w in WINDOWS.items():
    _t=', '.join(WIN_NAMES[v] for v in (_w['type'],_w['frame'],_w['glass'],_w['grill'],_w['mesh']) if v)
    if _k=='W-08': _t='Back window, 4\' wide: two casements (2\' each), '+', '.join(WIN_NAMES[v] for v in (_w['frame'],_w['glass'],_w['grill'],_w['mesh']))
    SPEC[_k]=_t+'; '+_w['why']+'; outside: box frame WF-1 and scalloped sunshade on the front and back walls only'*( _k in ('W-01','W-08','W-11'))
# underground tanks and pits: (code, name, shape, geometry, inside size note, covers, note)
#   rect geometry = outer (x1,x2,y1,y2); circle geometry = (cx,cy,outer r); covers = list of (x1,x2,y1,y2) or (cx,cy,r)
UNDERGROUND=[
 ('UG-01','Septic tank, about 8,000 L (existing)','rect',(13.583,20.833,1.0,11.0),"existing tank, 7'3\" x 10' outside; assumed 6\" walls, about 6'3\" x 9' inside, 5'3\" of liquid, a partition making two chambers (to confirm on site)",[(14.6,16.6,7.0,9.0),(14.6,16.6,1.05,2.55)],
  "The tank already on the plot, 2\" from the west boundary and 1' in from the road: 18.8 m from BR-02 (the guideline is at least 15 m). Its openings are raised about 2' to the new ground: one tile-in cover on the small-gate platform (first chamber) and one on the gate crest (second chamber); a cleaning truck reaches them from the road through GT-02. The foot of the outside stair ST-1A and the small-gate steps stand over it, so the engineer must give the stair foot its own support (for example a beam on the tank walls) and check or recast the roof for the steps and about 2' of fill. Vent pipe 4\" up the west compound wall beside the small gate. The neem trunk is under 1' from its wall: no digging near the roots."),
 ('UG-02','Soak pit for the septic tank','circle',(3.5,5.5,2.25),"4' across inside, about 8' deep, honeycomb brick with gravel round it",[(3.5,5.5,1.0)],
  "New, just inside the car gate on the east side: 19.5 m from BR-02 (the guideline is at least 18 m) and 12' from the sump. A pipe from the septic tank's outlet runs across the gate crest, north of the tree well. Final depth from a soil (percolation) test. Heavy-duty round cover on the drive."),
 ('UG-03','Underground water tank (sump), 6,000 L','rect',(2.75,8.75,20.0,28.5),"inside 5' x 7'6\", 6'5\" deep (5'8\" of water)",[(5.75,7.75,23.0,25.0)],
  "At the front, under the east walkway beside the bikes, so a water lorry on the road fills it with about 25' of hose through GT-01; the town supply comes in from the road too. 10' from the septic tank and 12' from the soak pit (keep at least 10'). Waterproofed RCC with a heavy-duty top; a lockable tile-in cover in the walkway, clear of the bikes and the car. The bores at the back feed it by a pipe along the side passage, and a pump lifts the water to the overhead tank FU-71."),
 ('UG-04','Rainwater recharge pit','circle',(2.1,75.8,1.5),"3' across, 6' deep, filled with pebbles, gravel and sand",[(2.1,75.8,1.5)],
  "Side garden, between the two bores BR-01 and BR-02 and next to the east compound wall BW-01 (about 4' from BR-02 and 6' from BR-01, so it recharges right where the bores draw), in the covered utility strip under toilet 3. Roof downpipes run to it through a first-flush filter; it recharges the ground water for the bores (rainwater harvesting is compulsory in Tamil Nadu). Grated cover. The drive drain at the gate goes to the road drain."),
]

# ---------------- modular kitchen (KT-1: oak base units, cream wall units, black granite top) ----------------
# Plan feet like the rest of the model. Base units: 4" plinth, 18 mm carcass, 18 mm shutters, 40 mm granite top.
# face = the side the fronts face: 'x+' (east run, faces west), 'y-' (back run, faces north), 'y+' (breakfast counter, faces south).
# Fronts: k = drawer / door / lift (flap opens upward) / pullout / blind (fixed); a,b along the run; za,zb heights; hinge 'a' or 'b' end; what = contents.
KCH,KTOP,KPL,KLOW,KBF=2.83,0.13,0.33,2.0,2.70      # counter top 2'10", top 40 mm, plinth 4", low counter 2'; breakfast counter units 2'8" + 40 mm top, the same height as the east run
KUP1,KUP2,KLOFT2=4.9,7.0,9.988                      # wall units 4'11" to 7', loft to the ceiling
KUP1R=5.25                                            # wall units over the drying rack start higher, 5'3"
RO_Z1,RO_H=5.0,558/304.8                              # RO purifier FU-66: bottom 5' from the floor, 558 mm high
def _drawers(a,b,z1,z2,mm,what):
    # drawer stack from the bottom up; mm = front heights in mm (bottom first), 3 mm gaps
    out,z=[],z1
    for h,w in zip(mm,what):
        hf=h/304.8; out.append(dict(k='drawer',a=a,b=b,za=round(z+0.005,3),zb=round(z+hf-0.005,3),what=w)); z+=hf+0.01
    return out
_B1,_B2=KPL,KCH-KTOP          # base fronts 0.33 to 2.70 ft (722 mm)
_L1,_L2=KPL,KLOW-KTOP         # low counter fronts (469 mm)
_F1,_F2=KPL,KBF               # breakfast counter fronts (722 mm, the same as the base fronts)
KITCHEN_MODULES=[
# two L-shaped corner cupboards (like the owner's photo): each is two parts that open into one L, with an L-shaped shelf and one L-shaped door in 2 parts
# (k='leaf': the part joined to the door 'of' by a corner hinge; it folds onto that door, which is hinged to the cabinet)
 dict(id='K-01A',name='Corner cupboard, north (L-shaped), east part',run='East run',face='x+',x1=3.5,x2=5.5,y1=58.625,y2=61.625,z1=0,z2=KCH,shelfZ=[1.45],
      fronts=[dict(k='door',a=59.875,b=61.625,za=_B1,zb=_B2,hinge='b',what='one L-shaped door in 2 parts, hinged to the cabinet at its south end next to K-02; the K-01B part folds onto it: big vessels, idli steamer, pressure cookers on the L-shaped shelves')],
      inside='opens through to K-01B behind the breakfast counter: one L-shaped space with an L-shaped shelf at 1\'5", no blind corner',need='use the north corner fully'),
 dict(id='K-02',name='Gas cylinder unit',run='East run',face='x+',x1=3.5,x2=5.5,y1=61.625,y2=63.125,z1=0,z2=KCH,plinth=2/12,
      fronts=[dict(k='door',a=61.625,b=63.125,za=_B1,zb=_B2,hinge='a',what='LPG cylinder (26" high) on the bottom board; simple door, no trolley')],
      inside='18 mm bottom board on a low 2" base, no shelf: 2\'5½" (29½") clear above the board for the 26" cylinder (28 to 29" needed); the 4" black kick board and the door line up with the units beside it (1" lip to lift the cylinder over); vent slots in the plinth and at the bottom of the door; the hose goes up through a grommet to the stove FU-52 above',need='the cylinder right under the stove, at the lowest cost'),
 dict(id='K-03A',name='Corner cupboard, south (L-shaped), east part',run='East run',face='x+',x1=3.5,x2=5.5,y1=63.125,y2=66.625,z1=0,z2=KCH,shelfZ=[1.45],
      fronts=[dict(k='door',a=63.125,b=64.625,za=_B1,zb=_B2,hinge='a',what='one L-shaped door in 2 parts, hinged to the cabinet at its north end; the K-03B part folds onto it: kadai, tawa, frying pans and pots on the L-shaped shelves')],
      inside='one L-shaped space round the corner with K-03B, an L-shaped shelf at 1\'5", no sealed corner',need='use the south corner fully, pans one step from the stove'),
 dict(id='K-03B',name='Corner cupboard, south (L-shaped), back part',run='Back run',face='y-',x1=5.5,x2=6.45,y1=64.625,y2=66.625,z1=0,z2=KCH,open_end='a',shelfZ=[1.45],
      fronts=[dict(k='leaf',of='K-03A',a=5.5,b=6.45,za=_B1,zb=_B2,what='door part on the sink side, joined to the K-03A part by a corner hinge: oil and spice bottles, mixer jars')],
      inside='opens into K-03A round the corner',need='reach the south corner from the sink side too'),
 dict(id='K-04',name='Sink unit',run='Back run',face='y-',x1=6.45,x2=8.6,y1=64.625,y2=66.625,z1=0,z2=KCH,
      fronts=[dict(k='door',a=6.45,b=7.525,za=_B1,zb=_B2,hinge='a',what='two-bin pull-out: wet and dry waste'),
              dict(k='door',a=7.525,b=8.6,za=_B1,zb=_B2,hinge='b',what='cleaning things on a steel tray; RO purifier filter line')],
      inside='aluminium tray on the floor of the unit against leaks; two-bin pull-out; tray for cleaning things',need='waste bins and cleaning things under the sink'),
 dict(id='K-05',name='Low counter unit, water pots',run='Low counter',face='y-',x1=8.6,x2=9.875,y1=64.625,y2=66.625,z1=0,z2=KLOW,
      fronts=[dict(k='door',a=8.6,b=9.875,za=_L1,zb=_L2,hinge='a',what='2 plastic water kudams (about 12 L each, 10" across, 14" high), one behind the other')],
      inside='no shelf, so two kudams stand one behind the other (18" clear inside); RO purifier FU-66 above, so pots fill standing on the low counter',need='filling and keeping drinking water at a low, easy height'),
 dict(id='K-06',name='Low counter unit, 2 drawers',run='Low counter',face='y-',x1=9.875,x2=12.125,y1=64.625,y2=66.625,z1=0,z2=KLOW,
      fronts=_drawers(9.875,12.125,_L1,_L2,[300,160],['rice and atta bins (25 kg)','wet grinder stone, batter boxes']),
      inside='deep bottom drawer for rice and atta bins; wet grinder FU-65 on the counter above',need='rice and atta by the wet grinder; batter making at a low, comfortable height'),
 dict(id='K-01B',name='Corner cupboard, north (L-shaped), breakfast part',run='Breakfast counter',face='y+',x1=5.5,x2=7.1,y1=58.637,y2=59.875,z1=0,z2=KBF,open_end='a',shelfZ=[1.45],
      fronts=[dict(k='leaf',of='K-01A',a=5.5,b=7.1,za=_F1,zb=_F2,what='door part on the breakfast side, joined to the K-01A part by a corner hinge: plates and bowls')],inside='opens into K-01A: one L-shaped space with an L-shaped shelf',need='everyday plates near the table, and the corner used'),
 dict(id='K-08',name='Breakfast counter unit, 3 drawers',run='Breakfast counter',face='y+',x1=7.1,x2=8.7,y1=58.637,y2=59.875,z1=0,z2=KBF,
      fronts=_drawers(7.1,8.7,_F1,_F2,[288,288,140],['tiffin boxes','table linen, foil and bags','cutlery tray: ladles, spatulas, spoons']),inside='shallow drawers (300 mm deep); cutlery tray in the top drawer',need='tiffin boxes, table things and cutlery'),
 dict(id='K-09',name='Breakfast counter unit, glasses and cups',run='Breakfast counter',face='y+',x1=8.7,x2=10.3,y1=58.637,y2=59.875,z1=0,z2=KBF,
      fronts=[dict(k='door',a=8.7,b=10.3,za=_F1,zb=_F2,hinge='b',what='glasses, cups and tumblers (1 shelf)')],inside='one shelf',need='glasses and cups near the table'),
 dict(id='K-10',name='Breakfast counter unit, 3 drawers',run='Breakfast counter',face='y+',x1=10.3,x2=11.9,y1=58.637,y2=59.875,z1=0,z2=KBF,
      fronts=_drawers(10.3,11.9,_F1,_F2,[288,288,140],['snacks and biscuit tins','pulses and dals in jars','tea, coffee, sugar']),inside='shallow drawers (300 mm deep)',need='dry stores in jars'),
 dict(id='K-11',name='Breakfast counter unit, open steel baskets',run='Breakfast counter',face='y+',x1=11.9,x2=13.5,y1=58.637,y2=59.875,z1=0,z2=KBF,
      # k='open': no door; rows = steel wire baskets (floor height, basket height, how many side by side), bottom row first
      fronts=[dict(k='open',a=11.9,b=13.5,za=_F1,zb=_F2,rows=[(0.42,0.72,2),(1.38,0.45,2),(2.0,0.45,1)],what='open, no door: each row of stainless-steel wire baskets slides out on full-extension runners; for things kept in the air: top row one basket (bananas, lemons), middle row 2 (onions, garlic and ginger), bottom row taller, 2 (potatoes, coconuts)')],
      inside='open front with sliding stainless-steel wire baskets in 3 rows (each row pulls out on its own): top 1 basket, middle 2, bottom 2 and taller (about 11" inside); air flows through, so onions and fruit keep well; socket for the microwave FU-67 above',need='dry vegetables and fruit (onion, banana, coconut) kept airy and in reach'),
 dict(id='K-12',name='Wall unit',run='Wall units, back',face='y-',x1=4.75,x2=6.5,y1=65.375,y2=66.613,z1=KUP1R,z2=KUP2,
      fronts=[dict(k='door',a=4.75,b=6.5,za=KUP1R+0.012,zb=KUP2-0.012,hinge='a',what='masala dabba and spices (2 shelves)')],inside='2 shelves; starts at 5\'3" to clear the drying rack below',need='spices at eye level near the stove'),
 dict(id='K-13',name='Dish drainer over the sink',run='Wall units, back',face='y-',x1=6.5,x2=8.25,y1=65.375,y2=66.613,z1=KUP1R,z2=KUP2,
      fronts=[dict(k='lift',a=6.5,b=8.25,za=KUP1R+0.012,zb=KUP2-0.012,what='steel plate and glass rack, drips straight into the sink')],inside='stainless-steel plate rack and glass rack, open bottom with a drip tray',need='dry washed plates and glasses right over the sink'),
 dict(id='K-15',name='Wall unit, glass door',run='Wall units, east',face='x+',x1=3.512,x2=4.75,y1=58.637,y2=61.0,z1=KUP1,z2=KUP2,
      fronts=[dict(k='door',a=58.637,b=61.0,za=KUP1+0.012,zb=KUP2-0.012,hinge='a',what='glass jars on show (2 shelves)',glass=True)],inside='2 glass shelves',need='jars on show'),
 dict(id='K-16',name='Loft, back',run='Loft',face='y-',x1=4.75,x2=9.875,y1=65.375,y2=66.613,z1=KUP2+0.05,z2=KLOFT2,open_end='a',
      fronts=[dict(k='leaf',of='K-17B',a=4.75,b=6.5,za=KUP2+0.062,zb=KLOFT2-0.012,what='corner door part on the back side, joined to the K-17B part by a corner hinge: big vessels used for functions'),dict(k='door',a=6.5,b=8.25,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='a',what='festival and pooja vessels'),
              dict(k='door',a=8.25,b=9.875,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='b',what='spare stock')],inside='opens into the corner of K-17B (one L-shaped loft at the corner); the corner door in 2 parts and 2 hinged doors (easy to close from a step stool)',need='things used a few times a year'),
 dict(id='K-18',name='Loft, back (over the RO and wet grinder)',run='Loft',face='y-',x1=9.875,x2=12.125,y1=65.375,y2=66.613,z1=KUP2+0.05,z2=KLOFT2,
      fronts=[dict(k='door',a=9.875,b=11.0,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='a',what='spare rice and atta bags, wet grinder spare stone'),dict(k='door',a=11.0,b=12.125,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='b',what='spare water cans, RO filter cartridges')],
      inside='2 hinged doors, one shelf; continues K-16 to the end of the low counter, starting just above the RO purifier (7\' 0½")',need='more storage above the low counter'),
 dict(id='K-17A',name='Loft, east (north of the chimney)',run='Loft',face='x+',x1=3.512,x2=4.75,y1=58.637,y2=62.15,z1=KUP2+0.05,z2=KLOFT2,
      fronts=[dict(k='door',a=58.637,b=60.4,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='a',what='spare stock'),dict(k='door',a=60.4,b=62.15,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='b',what='light things only (next to the chimney)')],
      inside='2 hinged doors',need='things used a few times a year'),
 dict(id='K-17B',name='Loft, east (south of the chimney)',run='Loft',face='x+',x1=3.512,x2=4.75,y1=63.15,y2=66.613,z1=KUP2+0.05,z2=KLOFT2,
      fronts=[dict(k='door',a=63.15,b=65.375,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='a',what='one L-shaped corner door in 2 parts, hinged at its north end next to K-17C; the K-16 part folds onto it: spare stock')],
      inside='the corner loft: opens into K-16, so the corner is used (no blind corner, no gap)',need='things used a few times a year'),
 dict(id='K-17C',name='Loft, east (over the chimney)',run='Loft',face='x+',x1=3.512,x2=4.75,y1=62.15,y2=63.15,z1=KUP2+0.05,z2=KLOFT2,
      fronts=[dict(k='door',a=62.15,b=63.15,za=KUP2+0.062,zb=KLOFT2-0.012,hinge='a',what='light things (dry, away from the stove heat)')],
      inside='1 hinged door; closes the gap between K-17A and K-17B so the east lofts run in one line',need='a clean top line over the chimney, and a little more storage'),
]
KITCHEN_NOTES=[
 'Finish KT-1: oak-look laminate base units, cream wall units and loft, black granite top 40 mm, matte black handles; 18 mm BWP plywood carcass (boiling-water-proof, for a wet kitchen).',
 'Base units: 2\'10" to the top of the counter (865 mm), 4" plinth, 600 mm deep. Low counter for the wet grinder and water: 2\' (610 mm). Breakfast counter: the same 2\'10" as the east run, so the L-shaped corner cupboard K-01A/K-01B has one level top; 375 mm deep.',
 'Hardware: soft-close hinges and full-extension soft-close drawer runners; L-corner (bi-fold) hinges on the two corner doors; L-profile handles in matte black along the bottom edge of the wall units and lofts, easy to pull from below; the two corners are L-shaped cupboards with L-shaped shelves (no carousels, no trolleys) to keep the cost down; a gas strut only on the dish-drainer flap K-13.',
 'Free-standing 3-burner glass-top stove FU-52 (70 x 41 x 13 cm) on the counter over K-02, with the gas cylinder below it; chimney 60 cm wide above it, its duct going straight back through GW-01 to a vent cowl; sink FU-51 over K-04 with the dish drainer K-13 above it; RO purifier FU-66 (558 x 350 x 280 mm) in the place of wall unit K-14, over the low counter; wet grinder FU-65 on the west end of the low counter; mixer FU-64 on the east run; microwave FU-67 on the breakfast counter.',
]

CAR=(11.125,16.875,13.75,28.75)   # VW Virtus size, 14'11" x 5'9" (4561 x 1752 mm), reversed in: nose to the gate, back 1' clear of GW-04; as far west as it can go (3" off the stair line); one short back-and-forth (2'5" forward, 10" back) on the way out
# two-wheelers: (code, model, centre X, centre Y, length, width, facing); facing 'N' = front to the gate, 'S' = front to the house (length along Y)
# side by side along BW-01, between C-01 and C-03, ridden in forward (front to the house); reached up the east walkway without passing the car
BIKES=[('TW-1','Honda VFR800',1.755,24.23,6.96,2.41,'S'),('TW-2','Ather 450X',4.41,24.685,6.03,2.42,'S')]   # moved 6" back (to the road), earlier for the front wash basin (now only the wall tap FU-88)
CH_G_FRONT=[0,0.75,12.0,13.5,20.25,21.0]

# ---------- structure (proposal): RCC frame with side pillars only, no pillar inside any room ----------
# Columns 1' x 9" (engineer's size), the 1' along the wall, so each column hides inside a 9" outer wall.
# id, floors, x1, x2, y1, y2, note.  floors: 'G' = ground floor, continues up later for the future hall; 'G+F' = up to the first-floor roof
COL_SIZE="1' x 9\""
COLUMNS = [
 ('C-01','G', 0.375,1.125, 19.75,20.75,'East, moved against the east compound wall BW-01 so the parking is clear for the two-wheelers; carries the extended B-01'),
 ('C-02','G', 20.25,21.0, 19.75,20.75,'West, front edge of the terrace slab, just behind the ST-1 landing'),
 ('C-03','G', 2.125,2.875, 30.75,31.75,'East, porch front corner; shifted 7½" east to sit under the terrace parapet PW-02 (sticks 7½" into the side passage, leaving 1\'9")'),
 ('C-04','G', 20.25,21.0, 29.75,30.75,'West, corner of GW-04 and GW-05'),
 ('C-05','G', 2.125,2.875, 34.7,35.7,'East, porch side, in line with GW-11; shifted 7½" east to sit under the terrace parapet PW-02 (sticks 7½" into the side passage, leaving 1\'9")'),
 ('C-06','G', 20.25,21.0, 34.7,35.7,'West, in GW-05 where GW-11 meets it'),
 ('C-07','G', 2.125,2.875, 46.0,47.0,'East, in GW-01 at the foyer | living line; shifted 7½" east to sit under the terrace parapet PW-02 (sticks 7½" into the side passage, leaving 1\'9")'),
 ('C-08','G', 20.25,21.0, 46.0,47.0,'West, in GW-05 where GW-12 meets it'),
 ('C-09','G', 2.125,2.875, 57.94,58.94,'East, in GW-01 where GW-13 meets it; shifted 7½" east to sit under the terrace parapet PW-02 (sticks 7½" into the side passage, leaving 1\'9")'),
 ('C-10','G', 20.25,21.0, 57.94,58.94,'West, in GW-05 where GW-13 meets it'),
  ('C-11','G', 2.125,2.875, 66.375,67.375,'East, end of GW-01 at the bore court corner; shifted 7½" east to sit under the terrace parapet PW-02 (sticks 7½" into the side passage, leaving 1\'9")'),
  ('C-12','G', 20.25,21.0, 66.375,67.375,'West, in GW-05 behind the FU-25 store cupboard, in line with GW-14'),
  ('C-20','G0', 6.0,6.75, 66.625,67.625,'Bore court corner: GW-17, GW-18 and GW-14; footing kept away from bore BR-02. Ground floor only: stops at the roof slab, no stub on the terrace, so the future hall has no pillar in the middle'),
  ('C-21','G0', 6.0,6.75, 72.875,73.875,'Bore court corner: GW-18 and GW-06; eccentric footing needed, it is close to bore BR-02. Ground floor only: stops at the roof slab, no stub on the terrace'),
  ('C-22','G0', 2.75,3.5, 79.25,80.25,'AU-01: south-east corner of toilet 3, in the side garden; ground floor only, carries toilet 3 (beams B-24, B-25). The side passage stays 2\'4" clear'),
 ('C-14','G+F', 9.5,10.25, 73.125,74.125,'Corner of GW-06 and GW-07; runs up in FW-01'),
 ('C-15','G+F', 20.25,21.0, 73.0,74.0,'West, in GW-05 under FW-02; runs up in FW-03'),
 ('C-16','G+F', 9.5,10.25, 79.94,80.94,'In GW-07 where GW-15 meets it; runs up in FW-01'),
 ('C-17','G+F', 20.25,21.0, 79.94,80.94,'West, in GW-05 where GW-15 meets it; runs up in FW-03'),
 ('C-18','G+F', 9.5,10.25, 94.125,95.125,'Back corner of GW-07 and GW-08; runs up in FW-01'),
 ('C-19','G+F', 20.25,21.0, 94.125,95.125,'Back corner of GW-05 and GW-08; runs up in FW-03'),
]
# Beams 9" wide. id, level ('G' = ground-floor roof, 'F' = first-floor roof), x1, x2, y1, y2, depth, note
BEAMS = [
 ('B-01','G', 0.375,21.0, 19.75,20.5, "1'9\"",'Front beam over the parking, C-01 (now at the east wall) to C-02, 19\'11" span: engineer to size; balcony 2 cantilevers 4\'3" in front of it; B-10 rests on it'),
 ('B-02','G', 8.5,21.0, 29.75,30.5, "1'6\"",'Over GW-04 (moved 1\' north), to C-04'),
 ('B-02A','G', 2.75,8.5, 30.75,31.5, "1'6\"",'Over the porch front, C-03 to GW-03'),
 ('B-03','G', 2.75,21.0, 34.825,35.575, "1'6\"",'Over GW-11, across the porch and the study corner opening, C-05 to C-06'),
 ('B-04','G', 2.75,21.0, 46.125,46.875, "1'6\"",'Over GW-12 (bedroom 1 | living), C-07 to C-08'),
 ('B-05','G', 2.75,21.0, 58.065,58.815, "1'6\"",'Over GW-13 (living | kitchen), C-09 to C-10'),
  ('B-06','G', 2.75,21.0, 66.5,67.25, "1'6\"",'Over GW-14 and across the open area, C-11 to C-12'),
  ('B-07','G', 9.5,21.0, 73.125,73.875, "1'6\"",'Under FW-02, C-14 to C-15'),
 ('B-08','G', 9.5,21.0, 80.065,80.815, "1'3\"",'Over GW-15, C-16 to C-17'),
 ('B-09','G', 9.5,21.0, 94.375,95.125, "1'3\"",'Over GW-08, C-18 to C-19'),
  ('B-10','G', 2.75,3.5, 19.75,67.375, "1'3\"",'East edge beam over GW-01 and the porch side, from B-01 (beam on beam) to C-11'),
  ('B-11','G', 9.5,10.25, 73.125,95.125, "1'3\"",'East edge beam over GW-07, C-14 to C-18'),
  ('B-18','G', 6.0,6.75, 66.625,73.875, "1'3\"",'Over GW-18 (bore court | toilet 2), C-20 to C-21'),
  ('B-19','G', 2.75,6.75, 66.625,67.375, "1'3\"",'Over GW-17 (kitchen | bore court), C-11 to C-20'),
  ('B-24','G', 2.75,3.5, 73.875,79.25, "1'3\"",'AU-01: under FW-08 (toilet 3 east wall), B-20 to the new pillar C-22'),
  ('B-25','G', 3.5,9.5, 79.5,80.25, "1'3\"",'AU-01: under FW-07 (toilet 3 south wall), C-22 to C-16'),
  ('B-20','G', 2.75,10.25, 73.125,73.875, "1'3\"",'Over GW-06, C-21 to C-14; cantilevers 3\'3" east; toilet 3 above now sits on beams B-24 and B-25 and pillar C-22 (no long cantilever)'),
 ('B-12','G', 20.25,21.0, 19.75,95.125, "1'3\"",'West edge beam over GW-05, C-02 to C-19'),
 ('B-13','F', 9.5,21.0, 73.125,73.875, "1'3\"",'Over FW-02, C-14 to C-15'),
 ('B-14','F', 9.5,21.0, 79.875,80.625, "1'3\"",'Over FW-05, C-16 to C-17'),
 ('B-15','F', 9.5,21.0, 94.375,95.125, "1'3\"",'Over FW-04, right over GW-08'),
 ('B-16','F', 9.5,10.25, 73.125,95.125, "1'3\"",'Over FW-01, C-14 to C-18'),
 ('B-17','F', 20.25,21.0, 73.125,95.125, "1'3\"",'Over FW-03, C-15 to C-19'),
]
STRUCT_NOTES=[
 'Staircase ST-1: RCC waist-slab stair. ST-1A rests on the ground at its foot and on the landing; the landing ST-1L is carried by a short cantilever beam from pillar C-02; ST-1B spans from the landing to the balcony slab edge at X 9\'7½". No new pillar in the parking.',
 'Bore court: bore BR-02 sits in a court covered by the terrace slab and open to the side passage; the pump is pulled out sideways through the passage, or through a removable cover in the slab if a rig needs a straight lift (engineer to advise). C-13 is removed; C-20 and C-21 need eccentric footings that stay clear of the bore. Bore BR-01 is about 1\'9" from the GW-07 face, so that footing needs checking too.',
 'Pillars only in the outer walls (east and west sides). No pillar stands inside any room, and the future first-floor hall stays pillar-free.',
 'Pillars C-01 to C-19 are 1\' x 9" (engineer\'s size), set with the 1\' along the wall so they hide inside the 9" walls.',
 'Cross beams B-01 to B-07 span the full width, about 17\'6" clear, and sit over the cross walls where there is one. Edge beams run along both side walls.',
 'Beam depths shown are first estimates for the engineer: 1\'6" for the 17\'6" cross spans, 1\'3" for the rest. Roof slab 5".',
 'C-01 to C-12, C-20 and C-21 stop at the terrace for now; leave their bars sticking up for the future hall. C-14 to C-19 go up to the first-floor roof.',
 'Cantilevers: balcony 2 (4\'3" in front of B-01), the terrace corner (4\'1" behind B-07) and the bedroom 3 back wall FW-04 (2\'3" past C-18 and C-19).',
 'Also needed: plinth beams under all walls and a footing under each pillar. The engineer sizes these, and checks pillar sizes for the future floor.',
]
PORCH_STEPS_X=(3.5,8.25)
PORCH_STEPS_Y=32.75   # porch 2' shorter: the steps start 2' in from the front line, so there is 4'6" between the parked bikes and the first step

# ---------- electrical plan AU-03 (2026-11-05): plain modular one-way switches (no smart switches: cheap to repair), every point on a wall face ----------
# point: id, floor, x, y (wall face, plan feet), height from that floor (feet), kind, circuit, what it has
# kinds: DB board, SB switchboard, BS bedside board, S6 6 A socket (plain 3-pin, with its own switch), S16 16 A socket, AC 16 A AC socket, GY geyser socket,
#        EV car charging, IP outdoor IP65 socket or isolator, LO outdoor light, NT data / CCTV / bell
ELEC_POINTS=[
 # boards
 ('DB-1','G',9.25,33.5,5.0,'DB','-','Main distribution board, 16 ways, recessed in the study wall GW-03 (10 ft cable run from the EB meter FU-87): 63 A main switch, 100 mA RCCB for the lighting side, 30 mA RCCB for all sockets, wet areas and outside, one MCB per circuit; inverter changeover for C1 to C3'),
 ('DB-2', 'F', 14.92, 73.875, 5.0, 'DB', 'C11', 'First-floor sub-board, 8 ways, on the landing north wall FW-02 just west of SB-10, clear of the spiral stair and of the terrace door D-12 swing: its own 30 mA RCCB'),
 ('NT-5', 'F', 14.92, 73.875, 6.55, 'NT', 'C11', 'Router B (mesh, D-Link 35.3 x 25.7 x 5.6 cm): on a small oak wall shelf 7\' up on the landing north wall FW-02, above the sub-board DB-2, clear of the spiral stair; 6 A socket with switch and a LAN port fed by its own 1" conduit from router A (wired link, full speed); covers bedroom 3, the landing, the terrace and, through the stair well, the stair hall and bedroom 2'),
 # entrance, foyer, living
 ('NT-1', 'G', 3.9, 40.5, 4.5, 'NT', 'C3', 'Door bell push on the porch face of GW-02, just east of the main door D-01/D-13 (the west side has no wall left beside W-02); chime in the foyer; video door phone can use the same conduit'),
 ('SB-1', 'G', 8.875, 41.6, 4.0, 'SB', 'C1', 'Foyer, beside the main door, one 2-row plate: foyer light, porch light, parking lights, gate pillar lamps, side passage lights (two-way with SB-4), spare; 6 A socket with switch (lamp, vacuum)'),
 ('SB-2', 'G', 13.05, 46.75, 4.0, 'SB', 'C1', 'Living, on GW-12 east of the bedroom 1 door, one 2-row plate: 2 downlight groups, band LED strip, open-area light (two-way with SB-4), fan 1 and fan 2 with plain step regulators, 3 spare switches for points added later'),
 ('S-2', 'G', 3.5, 49.0, 1.25, 'S16', 'C3', 'Living, beside the 3-seat sofa arm: 16 A socket with switch (heater, vacuum, or a phone charger on the sofa side table)'),
 ('S-3', 'G', 3.5, 56.2, 1.25, 'S6', 'C3', 'Living, sofa corner: 6 A socket with switch (lamp, charger)'),
 ('S-4', 'G', 10.6, 58.25, 1.25, 'S6', 'C3', 'Living, beside the 2-seat sofa: 6 A socket with switch'),
 ('S-5', 'G', 20.13, 52.5, 4.3, 'S6', 'C3', 'TV wall FU-05, on the centre panel behind the TV (hidden): 2 x 6 A sockets (TV, set-top box) on the inverter, switched from the S-17 plate on the shelf; HDMI and TV cable conduit to the console'),
 ('S-18', 'G', 20.13, 52.5, 1.43, 'S6', 'C3', 'TV wall FU-05, centre, inside the floating TV console (hidden, cable cut-out at its back): 6 A socket for the sound bar or anything added later, switched from the S-17 plate'),
 ('NT-2', 'G', 20.15, 56.75, 7.4, 'NT', 'C3', 'Router A (main, D-Link 35.3 x 25.7 x 5.6 cm, 4 antennas): lying flat inside the closed top cupboard of the FU-05 right tower (hidden; inside 3\' x 1\'3" x 1\'4", room for the antennas upright): 6 A socket with switch, fibre from the road and the LAN cable to router B; covers living, foyer, bedroom 1, study, kitchen, porch and the parking cameras'),
 ('S-17', 'G', 20.15, 56.75, 3.75, 'S6', 'C3', 'FU-05 right tower, open LED shelf (3\'5" to 5\'), one 2-row plate on the back panel: top row the 3 switches for the TV sockets S-5 (2) and the console socket S-18; bottom row 2 x 6 A sockets with switches (lamp, speaker, phone on the shelf)'),
 ('AC-0', 'G', 3.5, 54.6, 7.5, 'AC', 'C10', 'Living, spare AC point high on GW-01 (east wall), for a future split AC centred above the two windows W-04 and W-05 (between their heads and the ceiling band), blowing west down the hall: 16 A socket with switch and red light, own 4 mm² line pulled now'),
 # kitchen: 4 mm² lines, 16 A sockets 10" above the counter, none within 2' of the sink or beside the gas hob
 ('SB-3', 'G', 12.05, 58.625, 4.3, 'SB', 'C1', 'Kitchen, one plate on GW-13 just inside the arch side, west of the W-12 frame and above the microwave: kitchen downlights, under-cabinet LED strip, open-area light; 16 A socket with switch for the microwave FU-67 (old K-6)'),
 ('K-1', 'G', 3.5, 60.3, 3.67, 'S16', 'C5', 'Kitchen, east counter on GW-01 between the mixer FU-64 and the W-06 frame: 16 A + 6 A sockets, each with its switch (mixer, kettle or a small appliance)'),
 ('K-2','G',3.5,62.65,6.75,'S16','C5','Kitchen, chimney FU-81: 6 A socket hidden behind the hood top'),
 ('K-3', 'G', 3.5, 65.6, 3.67, 'S16', 'C5', 'Kitchen, east counter south corner on GW-01: 16 A + 6 A sockets with switches (kettle or a future induction plate)'),
 ('K-4', 'G', 10.2, 66.625, 3.4, 'S16', 'C5', 'Kitchen, one plate on GW-14 above the low counter and the water pots, between the RO purifier and the wet grinder: 16 A for the wet grinder FU-65 and 6 A for the RO purifier FU-66, each with its switch (old K-5 joined here)'),
 ('K-8', 'G', 20.25, 59.75, 6.3, 'S16', 'C5', "Fridge FU-18: 16 A socket with switch on GW-05 in the 1' space above the fridge (for the stabilizer that sits on top), easy to reach, not behind its hot back"),
 # open area, stair hall, toilet 2, store cupboard
 ('SB-4', 'G', 12.125, 70.65, 4.0, 'SB', 'C1', 'Stair hall, on GW-16 just south of the toilet 2 door D-04 frame: toilet 2 light and exhaust, geyser (20 A switch with red light), stair hall light, spiral stair light'),
 ('S-6', 'G', 11.0, 73.5, 1.0, 'S6', 'C4', 'Stair hall, on GW-19 (south end wall of toilet 2), low and out of sight from the hall: 6 A socket with switch for the vacuum and mopping machine'),
 ('S-7', 'G', 20.25, 70.4, 0.9, 'S16', 'C2', 'FU-25 cell S-4.1/S-4.2: inverter input, 16 A socket with switch on its own MCB, on the back wall GW-05 inside the cupboard (hidden by the shutter); inverter output cable back to DB-1'),
 ('SB-5','G',10.25,73.9,4.0,'SB','C1','Stair hall, beside the garden door D-05: side-garden lights (2), back-garden lights (2), bore-court and clothes-rack light, utility light'),
 ('GY-2','G',8.7,67.0,6.75,'GY','C8','Toilet 2 geyser FU-58: 16 A socket with a splash cover, 6\'9" up, out of the shower spray'),
 ('S-8', 'G', 10.0, 73.125, 4.5, 'S6', 'C4', 'Toilet 2, beside the mirror over the basin FU-27: 6 A socket with switch and a splash cover (IP44)'),
 # bedroom 1, study, toilet 1
 ('SB-6', 'G', 13.3, 46.375, 4.0, 'SB', 'C1', 'Bedroom 1, inside at the D-02 latch, one 2-row plate: room light (two-way with BS-1), fan on/off switch (two-way with BS-1) and its step regulator; 3 spare switches for points added later (tube light, wall fan); no AC switch here, the AC has its own switch on AC-1'),
 ('BS-1', 'G', 20.25, 40.2, 2.25, 'BS', 'C1', 'Bedroom 1, inside the bedside cut-out of FU-09.2 (the phone rests on the cut-out shelf): room light and fan on/off, both two-way with SB-6 at the door, and a 6 A socket with switch'),
 ('AC-1','G',9.25,40.6,7.5,'AC','C6','Bedroom 1 AC FU-44: 16 A socket beside the indoor unit, own 4 mm² line'),
 ('S-9','G',9.25,42.0,1.0,'S6','C4','Bedroom 1: 6 A socket for the iron, by the wardrobe side'),
 ('SB-7', 'G', 14.05, 35.375, 4.0, 'SB', 'C1', 'Bedroom 1, on GW-11 between the study wall and the toilet 1 door D-03 frame, one 2-row plate (old SB-8 joined here): toilet 1 light, exhaust (in V-01), geyser (20 A switch with red light); study light and the small study fan with its regulator'),
 ('GY-1','G',20.0,30.5,6.75,'GY','C7','Toilet 1 geyser: 16 A socket with a splash cover, 6\'9" up on GW-04, out of the spray'),
 ('S-10', 'G', 14.125, 32.2, 4.5, 'S6', 'C4', 'Toilet 1, beside the mirror (south of it): 6 A socket with switch and a splash cover (IP44)'),
 ('S-11', 'G', 9.25, 31.2, 2.75, 'S6', 'C3', 'Sewing table FU-10: 2 x 6 A sockets with switches for the machine and a lamp, and a data point (LAN), 3" above the table'),
 # bedroom 2
 ('SB-9', 'G', 13.95, 80.625, 4.0, 'SB', 'C1', 'Bedroom 2, inside at the D-06 latch, between the door frame and the (shortened) wardrobe FU-34, one 2-row plate: room light and fan switch (both two-way with BS-4), fan step regulator; window-seat reading light and 3 spare switches; no AC switch here, the AC has its own switch on AC-2'),
 ('BS-4', 'G', 20.25, 90.95, 2.5, 'BS', 'C1', 'Bedroom 2, bed head (south), above the side table FU-33 (phone and laptop on the table), clear of its lamp: room light and fan on/off (two-way with SB-9 at the door), a 6 A socket with its own switch and an Ethernet (RJ45, Cat6) port wired back to router A'),
 ('AC-2','G',10.25,88.9,7.5,'AC','C9','Bedroom 2 AC FU-46: 16 A socket beside the indoor unit, own 4 mm² line'),
 ('S-19', 'G', 10.25, 92.2, 1.25, 'S16', 'C4', 'Bedroom 2, on GW-07 (east wall) just north of the window seat FU-95, at sofa-socket height like S-2: 16 A socket with switch (heater, vacuum, a lamp or charger at the seat)'),
 # utility, bore court
 ('S-14', 'G', 4.475, 67.375, 3.6, 'S16', 'C4', 'Bore court, centred over the washing machine FU-29 on GW-17, under the slab FU-83, so machine and socket read as one: 16 A socket with switch and a splash cover (IP44)'),
 # outside: IP65 boxes with spring flaps, under a roof or overhang, 3'6" up, cables enter from below with a drip loop
 ('PS-1','G',14.3,29.75,4.6,'S16','C13','Parking board PB-1 on GW-04 (one modular 12-module plate, 1\'2" x 9", in a grey IP65 cover), just west of the study window W-01 (clear of its frame), nearest the bikes for charging, 4\'4" to 5\'3" above the parking for safety, with the EB meter and sump box FU-87 beside it: 16 A IP65 socket with a flap, for a pressure washer, vacuum or a portable car charger (3.3 kW, no separate EV point)'),
 ('PS-2','G',15.1,29.75,4.6,'S16','C13','Parking board PB-1 on GW-04 (one modular 12-module plate, 1\'2" x 9", in a grey IP65 cover): second 16 A IP65 socket, for tools or a pump'),
 ('PS-3','G',14.7,29.75,4.6,'S6','C13','Parking board PB-1 on GW-04 (one modular 12-module plate, 1\'2" x 9", in a grey IP65 cover): 6 A IP65 socket, for a phone charger or a small light'),
 ('SB-14','G',14.7,29.75,5.05,'SB','C1','Parking board PB-1 on GW-04 (one modular 12-module plate, 1\'2" x 9", in a grey IP65 cover) behind the car: switches for the parking ceiling lights LO-1 and the gate pillar lamps, two-way with SB-1 in the foyer'),
 ('IP-1', 'G', 0.375, 26.0, 4.5, 'IP', 'C13', 'Two-wheeler charging on BW-01 by the bikes: 16 A IP65 socket with a hood (scooter charger), own 30 mA RCBO'),
 ('IP-2', 'G', 12.0, 95.125, 3.5, 'IP', 'C13', 'Back garden, on GW-08 under the balcony 3 slab: IP65 box with a hood: 2 x 16 A + 1 x 6 A sockets with switches (garden tools, pump, a lamp)'),
 ('LO-1','G',14.0,24.0,9.0,'LO','C1','Parking: 2 ceiling lights under the slab (Y 24\' and 28\'), switched at SB-1'),
 ('LO-2','G',5.5,36.5,9.0,'LO','C1','Porch ceiling light, switched at SB-1'),
 ('LO-3','G',2.75,50.0,7.0,'LO','C1','Side passage: 3 bulkhead lights IP65 on GW-01 (Y 36\', 50\', 64\'), switched at SB-1 and SB-4'),
 ('LO-4','G',9.5,80.0,7.0,'LO','C1','Side garden: 2 bulkhead lights IP65 on GW-07, switched at SB-5'),
 ('LO-5','G',15.0,95.125,7.0,'LO','C1','Back garden: 2 bulkhead lights IP65 on GW-08 (X 12\', 18\'), switched at SB-5'),
 ('NT-3','G',14.0,29.5,9.0,'NT','C3','CCTV: 2 camera points with a conduit to the router (parking ceiling looking at the gate, and the porch); 6 A from C3'),
 # first floor
 ('SB-10', 'F', 13.85, 73.875, 4.0, 'SB', 'C11', 'Landing, east of the terrace door D-12: landing light, spiral stair light (two-way with SB-4), terrace lights (2)'),
 ('SB-11', 'F', 10.25, 76.63, 4.0, 'SB', 'C11', 'Landing, on FW-01 at the toilet 3 door latch (north of D-09), past the end of the open terrace door D-12: 3-module plate: toilet 3 light, exhaust FU-62, geyser (20 A switch with red light)'),
 ('GY-3','F',2.125,75.7,6.75,'GY','C15','Toilet 3 geyser FU-60: 16 A socket with a splash cover, beside the geyser, out of the spray'),
 ('S-15', 'F', 6.95, 73.5, 4.5, 'S6', 'C11', 'Toilet 3, on FW-09 beside the mirror over the basin FU-42: 6 A socket with switch and a splash cover (IP44)'),
 ('SB-12', 'F', 14.0, 80.25, 4.0, 'SB', 'C11', 'Bedroom 3, inside at the D-07 latch, between the door frame and the wardrobe FU-39, one 2-row plate: room light and fan switch (both two-way with BS-6), fan step regulator; balcony light and 3 spare switches; no AC switch here, the AC has its own switch on AC-3'),
 ('BS-6', 'F', 20.25, 90.6, 2.5, 'BS', 'C11', 'Bedroom 3, bed head (south), above the side table FU-38 (phone and laptop on the table), clear of its lamp: room light and fan on/off (two-way with SB-12 at the door), a 6 A socket with its own switch and an Ethernet (RJ45, Cat6) port wired back to router B'),
 ('S-16', 'F', 16.5, 94.375, 2.75, 'S6', 'C11', 'Bedroom 3 desk FU-40: 2 x 6 A sockets with switches and an Ethernet (RJ45, Cat6) port wired to router B, just above the desk top'),
 ('AC-3', 'F', 10.25, 89.85, 7.5, 'AC', 'C14', 'Bedroom 3 AC FU-48: 16 A socket with switch and red light just south of the indoor unit, own 4 mm² line from DB-1'),
 ('S-20', 'F', 10.25, 91.4, 1.25, 'S16', 'C11', 'Bedroom 3, on FW-01 (east wall), south part, between the W-10 curtain and the reach of the open balcony door D-11, at 1\'3" like S-2 and S-19: 16 A socket with switch (heater, vacuum, iron)'),
 ('IP-3', 'F', 19.3, 95.125, 3.0, 'IP', 'C14', 'Balcony 3: IP65 isolator for the AC outdoor unit FU-49'),
 ('LO-6','F',15.0,95.125,7.0,'LO','C11','Balcony 3 light, IP65, switched at SB-12'),
 ('LO-7','F',17.0,73.125,7.0,'LO','C11','Terrace: 2 bulkhead lights IP65 on FW-02 (X 15\', 19\'), switched at SB-10'),
 ('IP-4','F',19.0,73.125,3.0,'IP','C11','Terrace: 16 A IP65 socket with a hood, on FW-02 (washing, tools)'),
 ('NT-4','F',18.0,73.125,8.0,'NT','-','Solar provision: an empty 1" conduit from the terrace to DB-1 for future rooftop solar'),
]
# plate layout (3D and the electrician): modules left to right, rows split by '|'; sw switch, ind indicator, reg fan regulator, s6 6 A socket, s16 16 A socket, data RJ45/TV/fibre, bell push; 'v' = vertical plate
# face: (axis, side, coordinate) when the plate sits on furniture or a panel instead of the wall face
ELEC_MODS={
 'SB-1':'sw,sw,sw,sw|sw,sw,sw,s6','SB-2':'sw,sw,sw,sw,sw,sw|reg,reg,sw,sw,sw','S-2':'sw,s16','S-3':'sw,s6','S-4':'sw,s6','S-5':'s6,s6','S-18':'s6','NT-2':'sw,s6,data','NT-5':'sw,s6,data','S-17':'sw,sw,sw|sw,s6,sw,s6',
 'AC-0':'ind,sw,s16','SB-3':'sw,sw,sw|sw,s16','K-1':'sw,s16,sw,s6','K-2':'sw,s6','K-3':'sw,s16,sw,s6','K-4':'sw,s16,sw,s6','K-8':'sw,s16',
 'SB-4':'sw,sw,ind,sw|sw,sw','S-6':'sw,s6','S-7':'sw,s16','SB-5':'sw,sw,sw,sw,sw','GY-2':'ind,sw,s16','S-8':'sw,s6','SB-6':'sw,sw,reg|sw,sw,sw','BS-1':'sw,sw,sw,s6',
 'AC-1':'ind,sw,s16','S-9':'sw,s6','SB-7':'sw,sw,ind,sw|sw,sw,reg','GY-1':'ind,sw,s16','S-10':'sw,s6','S-11':'sw,s6,sw,s6,data','SB-9':'sw,sw,reg|sw,sw,sw,sw',
 'BS-4':'sw,sw,sw,s6,data','AC-2':'ind,sw,s16','S-19':'sw,s16','S-14':'sw,s16','SB-10':'sw,sw,sw,sw','SB-11':'sw,sw,ind,sw','GY-3':'ind,sw,s16','S-15':'sw,s6','SB-12':'sw,sw,reg|sw,sw,sw,sw',
 'BS-6':'sw,sw,sw,s6,data','S-16':'sw,s6,sw,s6,data','AC-3':'ind,sw,s16','S-20':'sw,s16','NT-1':'bell','NT-4':'data','IP-1':'sw,s16','IP-2':'sw,s16,sw,s16|sw,s6','IP-3':'ind,sw','IP-4':'sw,s16'}
ELEC_FACE={'S-5':('x',-1,20.13),'S-18':('x',-1,20.13),'NT-2':('x',-1,20.15),'S-17':('x',-1,20.15)}
ELEC_CIRCUITS=[
 ('C1','Ground-floor lights and fans, outside lights','6 A MCB','1.5 mm²','on inverter'),
 ('C2','Inverter input (S-7)','16 A MCB','2.5 mm²',''),
 ('C3','Light-duty sockets: phone charging, TV, router, bell, CCTV','10 A MCB','2.5 mm²','on inverter'),
 ('C4','Ground-floor general sockets (iron, vacuum, mirrors, washing machine)','16 A MCB','2.5 mm²','30 mA RCCB'),
 ('C5','Kitchen power sockets','20 A MCB','4 mm²','30 mA RCCB'),
 ('C6','AC bedroom 1','20 A MCB','4 mm²',''),
 ('C7','Geyser toilet 1','16 A MCB','2.5 mm²','30 mA RCCB'),
 ('C8','Geyser toilet 2','16 A MCB','2.5 mm²','30 mA RCCB'),
 ('C9','AC bedroom 2','20 A MCB','4 mm²',''),
 ('C10','Spare AC point, living','20 A MCB','4 mm²','pulled now, used later'),
 ('C11','First-floor sub-board DB-2 (lights, fans, sockets, toilet 3)','32 A MCB','6 mm²','30 mA RCCB at DB-2'),
 ('C13','Outside sockets IP-1, IP-2','16 A RCBO','2.5 mm²','30 mA'),
 ('C14','AC bedroom 3 with its balcony isolator','20 A MCB','4 mm²',''),
 ('C15','Geyser toilet 3 (from DB-2)','16 A MCB','2.5 mm²','30 mA'),
 ('C16','Sump pump (control in the box FU-87) and bore pump FU-86 (its own panel)','20 A MCB each','4 mm²',''),
]
ELEC_RULES=[
 'Switches: plain modular one-way and two-way rockers (any standard brand), 4\' from the floor, at the latch side of each door. Fans on plain step regulators. Any electrician can change a part in minutes.',
 'Sockets: 1\' from the floor in rooms, 10" above counters in the kitchen, 2\'3" to 2\'6" at bedsides, 7\'6" beside each AC, 6\'9" for geysers. No socket within 2\' of the sink or beside the gas hob.',
 'Every socket is a plain 3-pin socket with its own switch on the same plate (6 A for small loads, 16 A for heavy ones); no USB sockets. Phone charging only where the phone has a place to rest: bedside cut-out or ledge, side tables, drawer tops, desks and the TV-unit shelf.',
 'Grouping: points close to each other share one modular plate (two rows when large), so there are fewer boxes on the walls and they are easier to fit and repair.',
 'Outside water safety: no switch outside at all; every outside light is switched from inside (SB-1, SB-4, SB-5, SB-10, SB-12). Outside sockets are IP65 boxes with a spring flap and a small hood, 3\'6" up, under a roof or overhang where possible; cables come in from below with a drip loop, so water runs away from the box. Bulkhead lights are IP65.',
 'Wet areas: toilet sockets and the washing machine socket have splash covers (IP44) and sit out of the shower spray; geysers have a 20 A switch with a red light outside the toilet door.',
 'Safety: 30 mA RCCB on all sockets, wet areas and outside; earth pit beside the EB meter, plus the earth wire in every point; ISI-marked copper wire in PVC conduit; separate line for each AC and geyser.',
 'Inverter: lights, fans, phone charging, TV and router (C1, C3) run on the inverter; ACs, geysers, kitchen power and pumps do not, so the battery lasts.',
 'Car: TNEB single-phase load may need to go up for a 7.4 kW wall charger; the 16 A socket (3.3 kW) works on the normal supply. The 6 mm² line is laid now so nothing has to be broken later.',
]
ELEC_COST='Wiring, conduits, switches and sockets, two boards and labour for about 1,400 sq ft with plain modular switches: about ₹1.4–1.8 lakh (smart switches would add ₹60k–1 lakh). The EV wall charger itself (₹25–45k) is bought later.'
