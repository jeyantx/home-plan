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
  ('BW-07', 20.625,21.0, 0.75,30.75, 'comp', 6, 'West compound wall, front part (new, 4½", 6\' high), along the apartment, from the gate post to the house'),
  ('BW-08', 20.625,21.0, 95.125,104.95, 'comp', 6, 'West compound wall, back part (new, 4½", 6\' high), along the apartment, from the house to the back wall'),
  ('GW-01', 2.75,3.5, 40.5,67.125, 'outer', 10.5, 'East outer wall of foyer, living and kitchen; ends at the bore court'),
  ('GW-02', 2.75,8.5, 40.5,41.25, 'outer', 10.5, 'Main door wall, between porch and foyer'),
  ('GW-03', 8.5,9.25, 30.75,41.25, 'outer', 10.5, 'Porch-side wall of study and bedroom 1'),
  ('GW-04', 8.5,21.0, 30.75,31.5, 'outer', 10.5, 'Front wall of study and toilet 1, facing parking'),
  ('GW-05', 20.25,21.0, 30.75,95.125, 'outer', 10.5, 'West outer wall, on the boundary (apartment side)'),
  ('GW-06', 6.0,10.25, 73.125,73.875, 'outer', 10.5, 'Back wall of toilet 2, facing the side-garden utility'),
  ('GW-17', 2.75,6.0, 66.375,67.125, 'outer', 10.5, 'Kitchen | bore court (north side of the court)'),
  ('GW-18', 6.0,6.75, 66.375,73.875, 'outer', 10.5, 'Toilet 2 | bore court (east wall of toilet 2, with V-02)'),
  ('GW-19', 10.25,11.75, 73.125,73.5, 'part', 10.5, 'Toilet 2 | stair hall (south end)'),
  ('GW-07', 9.5,10.25, 73.125,95.125, 'outer', 10.5, 'East wall of stair hall and bedroom 2, facing side garden'),
  ('GW-16', 11.75,12.125, 66.375,73.5, 'part', 10.5, 'Toilet 2 | stair hall (partition, inside the house); moved 1\'10" west for the bore court'),
  ('GW-08', 9.5,21.0, 94.375,95.125, 'outer', 10.5, 'Back wall of bedroom 2, facing back garden'),
  ('GW-09', 8.875,9.25, 41.25,46.375, 'part', 10.5, 'Foyer | bedroom 1'),
  ('GW-10', 13.75,14.125, 31.5,36.0, 'part', 10.5, 'Study | toilet 1'),
  ('GW-11', 13.75,20.25, 36.0,36.375, 'part', 10.5, 'Toilet 1 | bedroom 1'),
  ('GW-12', 8.875,20.25, 46.375,46.75, 'part', 10.5, 'Bedroom 1 | living room'),
  ('GW-13', 3.5,20.25, 58.75,59.125, 'part', 10.5, 'Living room | kitchen and dining (arch O-01)'),
  ('GW-14', 6.75,12.125, 66.375,66.75, 'part', 10.5, 'Kitchen | toilet 2 (kitchen now 7\'3" deep)'),
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
  ('PW-01', 2.75,9.625, 15.5,15.875, 'para', 3, 'Front parapet of balcony 2'),
  ('PW-02', 2.75,3.125, 15.5,77.875, 'para', 3, 'East parapet of balcony, terrace and terrace corner (terrace now covers the bore court too)'),
  ('PW-03', 9.625,21.0, 19.75,20.125, 'para', 3, 'Front parapet of terrace, behind staircase 1 (now from the top of ST-1B)'),
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
  ('G-08','Kitchen',R(3.5,13.5,59.125,66.375),'kit'),
  ('G-09','Open area (future dining)',R(13.5,20.25,59.125,68.0),'in'),
  ('G-10','Stair hall',[(12.125,66.375),(13.5,66.375),(13.5,68.0),(20.25,68.0),(20.25,80.25),(10.25,80.25),(10.25,73.5),(12.125,73.5)],'in'),
  ('G-11','Toilet 2',R(6.75,11.75,66.75,73.125),'wet'),
  ('G-12','Bedroom 2',R(10.25,20.25,80.625,94.375),'bed'),
  ('G-13','Side passage',R(0.375,2.75,30.75,73.75),'out'),
  ('G-14','Side garden',[(0.375,73.75),(2.75,73.75),(2.75,73.875),(9.5,73.875),(9.5,back_y(9.5)-0.375),(1.375,back_y(1.375)-0.375),(1.375,89.375),(0.375,89.375)],'garden'),
  ('G-16','Bore court',R(2.75,6.0,67.125,73.875),'out'),
  ('G-15','Back garden',[(9.5,95.125),(21.0,95.125),(21.0,back_y(21)-0.375),(9.5,back_y(9.5)-0.375)],'garden'),
 ],
 'F': [
  ('F-01','Balcony 2',R(3.125,9.625,15.875,20.125),'terr'),
  ('F-02','Open terrace',[(3.125,20.125),(20.625,20.125),(20.625,73.125),(3.125,73.125)],'terr'),
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
 ('O-01','G','GW-13', 13.75,17.75,'arch',None,None, 7.0,0,'Arch from living room to open area, 4\' wide; ends at the FU-25 cupboard face'),
 ('W-12','G','GW-13', 5.5,11.5,'fold',None,None, 4.0,3.0,'Folding glass window, kitchen to living. Opens left and right; curtain on the living side'),
 ('D-04','G','GW-16', 67.75,70.25,'door','a','-', 7.0,0,'Toilet 2 door, from stair hall, opens inward; hinged at its north end, so the leaf folds back over the shower area, clear of the basin'),
 ('D-05','G','GW-07', 74.25,77.25,'door','b','-', 7.0,0,'Garden door, stair hall to side garden; opens out, hinged at its south end, 1\'5" north of bore BR-01'),
 ('D-06','G','GW-15', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 2 door, from stair hall'),
 ('W-01','G','GW-04', 9.75,13.25,'window',None,None, 4.0,3.0,'Study window to parking'),
 ('V-01','G','GW-04', 16.25,18.25,'vent',None,None, 1.5,6.0,'Toilet 1 ventilator'),
 ('W-02','G','GW-03', 37.0,40.25,'window',None,None, 4.0,3.0,'Bedroom 1 window to porch'),
 ('W-03','G','GW-01', 42.5,45.5,'window',None,None, 4.0,3.0,'Foyer window to side passage'),
 ('W-04','G','GW-01', 48.0,52.0,'window',None,None, 4.0,3.0,'Living room window 1'),
 ('W-05','G','GW-01', 53.75,57.75,'window',None,None, 4.0,3.0,'Living room window 2'),
 ('W-06','G','GW-01', 61.0,65.0,'window',None,None, 2.0,3.25,'Kitchen window over the hob, 4\' x 2\', sill 3\'3", head 5\'3", so the chimney hood sits at the standard 2\'6" above the counter'),
 ('V-02','G','GW-18', 70.875,72.875,'vent',None,None, 1.5,6.0,'Toilet 2 ventilator over the WC platform, opens onto the bore court'),
 ('W-07','G','GW-07', 85.0,89.0,'window',None,None, 4.0,3.0,'Bedroom 2 side window to side garden'),
 ('W-08','G','GW-08', 14.75,19.25,'window',None,None, 4.0,3.0,'Bedroom 2 back window to back garden'),
 ('D-10','G','GW-08', 10.75,13.5,'door','a','-', 7.0,0,'Bedroom 2 back door to back garden'),
 ('GT-01','G','FRONT', 0.75,12.0,'gate',None,'+', 6.0,0,'Large gate, 11\'3", bi-fold double leaf (4 panels), folds inward over the level crest, east of the planter pillar'),
 ('GT-02','G','FRONT', 13.5,20.25,'gate',None,'+', 6.0,0,'Small gate, 6\'9", bi-fold double leaf (4 panels), folds inward over the level crest, west of the planter pillar'),
 ('D-07','F','FW-05', 10.5,13.5,'door','a','+', 7.0,0,'Bedroom 3 door, from landing'),
 ('D-08','F','FW-06', 82.0,84.25,'door','b','+', 7.0,0,'Toilet 3 door, 2\'3", from bedroom 3 lobby; moved south so its swing clears the WC and basin'),
 ('D-09','F','FW-01', 74.25,77.25,'door','a','+', 7.0,0,'Landing door to terrace corner; opens inward onto the landing, hinged at its north end so it folds back against FW-02; 1" raised sill outside against rain'),
 ('W-09','F','FW-02', 13.0,16.5,'window',None,None, 4.0,3.0,'Landing window to terrace'),
 ('W-10','F','FW-01', 88.5,92.5,'window',None,None, 4.0,3.0,'Bedroom 3 side window'),
 ('W-11','F','FW-04', 13.0,17.5,'window',None,None, 4.0,3.0,'Bedroom 3 back window'),
]

# ---------- building outlines (outer wall faces) for built-up area ----------
GF_OUTLINE=[(8.5,30.75),(21,30.75),(21,95.125),(9.5,95.125),(9.5,73.875),(6.0,73.875),(6.0,67.125),(2.75,67.125),(2.75,40.5),(8.5,40.5)]
FF_OUTLINE=R(9.5,21.0,73.125,97.375)
# site levels, in feet above the road crown in front of the gate (house floor = +3.5)
LEVELS=dict(road=0.0,hump=0.5,parking=2.0,garden=2.5,floor=3.5)
RAMP=dict(y_hump=1.0,y_crest=3.25,y_top=12.25,drain=(2.5,3.25))   # gate bevel to Y 1', crest to 3'3" (drain at its inner edge), ramp 1 in 6 to Y 12'3"
BRANCH_NOTES='''<section class="ask"><h2>Parking plan (branch exterior-v2, for review)</h2>
<ol>
<li><b>Car:</b> VW Virtus size (14'11" x 5'9"), <b>reversed in</b>: nose to the gate, back 1' from the front wall, on the level parking (Y 14'9" to 29'9"). <b>Route along the east side</b> (owner's sketch): it drives out forward in one smooth curve, past the scooter by the neem, through GT-01 near its east leaf, and turns east along the road; coming in, it comes from the west, stops just past the gate and reverses back along the same curve (one stop). Gaps: 7" to the folded east gate leaf, 1' to the east pillar, 6½" to the scooter, 1'6" to the tree well. Checked with a route planner using the Virtus turning circle; the gate stays as it is.</li>
<li><b>Tree well FU-76</b> reduced to 4' across, so the car passes the neem with room to spare. Keep at least 10" of open soil round the trunk; widen the ring later only if the trunk grows.</li>
<li><b>Two-wheelers (three spots):</b> TW-1 (motorcycle, Honda VFR800 size: 6'11" long, 4' high) under the high end of ST-1A and the landing, its windscreen where the underside is 5' or more; TW-2 (Ather 450X) across, by the neem, front to the east, between the tree well and ST-1A; TW-3, a spare spot along BW-07 beside the car (up to 7' long). A second bike behind TW-2 does not fit: the car would need 2 or more back-and-forth turns, and a 7' bike there blocks it. FU-56 store shrinks to a low tool store under the lower middle of ST-1A.</li>
<li><b>Car spot</b> moved 2' east (centre X 12'1½"), leaving a 2'4" aisle to the two-wheelers and an 8'11" walkway on the east side to the porch. Reverse in with one stop, drive out in one curve along the east side (checked with the Virtus turning circle).</li>
<li><b>ST-1 as cast:</b> both flights are steps on a 6" sloping waist slab and the landing ST-1L is a 6" slab, all cast as one RCC piece; the sloping underside of each flight runs into the flat underside of the landing (no step in the soffit). Landing level, risers and treads unchanged.</li>
<li><b>Pillar C-01</b> moved 2'4½" east against the compound wall BW-01; beam B-01 extended to it (19'11" span, engineer to size, about 1'9" deep) and B-10 rests on B-01. The parking is now clear of pillars.</li>
</ol></section>
<section class="ask"><h2>Outside windows and colours (branch exterior-v2, for review)</h2>
<ol>
<li><b>Window frame WF-1</b> on every outside window: a box frame round the window, 6" wide and 4" out from the wall, with a deeper 1'3" hood on top that works as the sunshade, and a thin black drip edge. Ventilators get a slimmer 4" frame, except V-01 (plain, no frame). RCC fins and hood, clad in the same wood-look brown as the balcony louvers and the gate slats (HPL or aluminium wood finish).</li>
<li><b>W-01 (study, facing the parking): small gable frame WF-2</b>: a 4" brown frame that hugs the window, a sill ledge, and a little red clay-tile gable on top (1' high, 6" eaves past the frame, 10" out from the wall), with a light gable panel. Brown scroll ornaments across the middle of the grill.</li>
<li><b>Plinth band:</b> the plinth below the floor is in a dark base colour (textured paint, or stone cladding).</li>
<li><b>Colour schemes</b> (Options → Colour): <b>EX-4</b> white house, light sand first-floor block, charcoal plinth (recommended); <b>EX-5</b> beige house, white first-floor block, dark brown plinth; <b>EX-6</b> light grey house, dark grey first-floor block, charcoal plinth; <b>EX-7</b> light beige house (a lighter EX-5), white first-floor block, brown plinth. All three keep the wood-brown frames, louvers and gates.</li>
</ol></section>
<section class="ask"><h2>Raised site levels (branch levels-v1, sample for review)</h2>
<ol>
<li><b>Levels above the road:</b> gate hump +6", parking +2'0", gardens, side passage and back yard +2'6", house floor +3'6" (1' plinth above the gardens).</li>
<li><b>Gate:</b> a 1' bevel from the road to a 6" crest, a 2'3" level strip at the crest, then a covered drain across the drive (to the rainwater pit and the road drain).</li>
<li><b>Drive ramp:</b> 1 in 6 (steeper, shorter), from Y 3'3" to 12'3", rising 1'6" to the parking; level from 12'3" inside the gate. Round off the top and bottom of the ramp by about 1' so low cars do not scrape. The car parks on the level part (Y 15'3" to 30'3").</li>
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
<li><b>Tulsi maadam FU-74</b> in the side garden with Tulsi PL-13; <b>clothes line FU-75</b> in the back garden.</li>
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
<li><b>Steps:</b> 18 risers of 7⅔" (195 mm) for the 11'6" floor height, 17 oak treads of 30° (12 per full turn) plus a 60° landing. Tread depth is 7½" at the inner walk line and 12" where you normally walk; outer edge 18".</li>
<li><b>Headroom:</b> 7'6" under the next turn and 6'10" under the landing, more than the 6'6" rule.</li>
<li><b>Direction:</b> start at the west side facing south (coming from the dining side along GW-05), climb anticlockwise with the handrail on your right, arrive facing east onto the landing F-04, next to D-07 and D-09.</li>
<li><b>Compared with ready kits:</b> 6' kits (Salter, Iron Shop) use the same 30° treads but up to 9½" risers and need a 6'2" square hole; Arke Kloè 160 cm uses 8¼" to 9¼" risers. Ours is a gentler 7⅔", close to a normal staircase.</li>
<li><b>Structure:</b> 6' round hole in the slab over the stair hall, with edge beams round it (engineer to size). Pole bolted to the ground floor and to the landing edge.</li>
<li><b>Finish:</b> black MS pole, frames and balusters (4 per tread, gaps under 4"), oak treads and oak handrail at 3'. Black MS rail with oak top round the hole on the first floor.</li>
</ol></section>
<section class="ask"><h2>Staircase ST-1 (approved, from stair-v1)</h2>
<ol>
<li><b>25 risers of 6"</b> from the parking floor (1' below the house floor, to be confirmed) to the balcony at the first-floor level: 15 in ST-1A, 10 in ST-1B. Treads 10", width 3'6".</li>
<li><b>ST-1A</b> runs along the new west compound wall BW-07 (moved 4½" east of the boundary), from Y 4'4" to 16'; <b>landing ST-1L</b> 3'6" x 3'6" at +7'6" above the parking; <b>ST-1B</b> turns east over the car, 7'6" long, arriving on balcony 2.</li>
<li><b>Balcony 2</b> is 2' shorter (6'6" x 4'3"); PW-01 shortened and PW-03 extended to meet the top of ST-1B.</li>
<li><b>Finish:</b> grey flamed granite treads and risers, plastered sides in the outside colour, black MS railing with 4" gaps and a wood-look handrail at 3'. Store FU-56 under the high end of ST-1A (4' to 6' high), door facing east; the low end of the stair is solid.</li>
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
# plants in the back flower bed FU-73 (east to west) and the Tulsi maadam
_bed=lambda x:back_y(x)-0.375-0.75
PLANTS=[('PL-01','sembaruthi',2.2),('PL-02','malli',3.8),('PL-03','kanakambaram',5.4),('PL-04','nandiyavattai',7.0),('PL-05','nithyakalyani',8.6),('PL-06','karuveppilai',10.2),
        ('PL-07','malli',11.8),('PL-08','vetchi',13.4),('PL-09','rose',15.0),('PL-10','kanakambaram',16.6),('PL-11','nithyakalyani',18.2),('PL-12','sembaruthi',19.8)]
PLANTS=[(c,t,x,_bed(x)) for c,t,x in PLANTS]+[('PL-13','tulsi',5.25,97.5)]
PLANT_NAMES={'malli':'Malli (Jasmine)','sembaruthi':'Sembaruthi (Hibiscus, red)','nandiyavattai':'Nandiyavattai (Crape jasmine)','vetchi':'Vetchi / Idly poo (Ixora, red)',
 'kanakambaram':'Kanakambaram (Crossandra, orange)','nithyakalyani':'Nithya kalyani (Periwinkle, pink)','rose':'Rose (pink)','karuveppilai':'Karuveppilai (Curry leaf)','tulsi':'Tulsi (Holy basil)'}
PLANT_COL={'malli':'#ffffff','sembaruthi':'#c8102e','nandiyavattai':'#ffffff','vetchi':'#e03a24','kanakambaram':'#ff7a1f','nithyakalyani':'#e2558c','rose':'#c2185b','karuveppilai':'#3d6b2b','tulsi':'#7a4a7e'}
BORES=[('BR-01',21.0-13.25, back_y(21.0-13.25)-27.0,"13'3\" from west, 27' from south"),('BR-02',21.0-17.0, back_y(21.0-17.0)-34.0,"17' from west, 34' from south")]
BOREWELL=BORES[0][1:3]

# ---------- drawing positions (layout specific) ----------
LABELPOS={'G-01':(8.0,24.5),'G-02':(5.6,37.6),'G-03':(6.2,44.6),'G-04':(11.5,53.0),'G-05':(11.45,39.4),'G-06':(11.5,33.6),'G-07':(17.2,33.4),
          'G-08':(8.0,63.4),'G-09':(15.6,64.6),'G-10':(16.0,70.6),'G-11':(9.25,69.6),'G-16':(3.9,70.1),'G-12':(16.2,92.8),'G-13':(1.55,36.0),'G-14':(5.0,94.0),'G-15':(15.2,100.2),
          'F-01':(6.4,18.0),'F-02':(11.9,47.0),'F-03':(7.9,75.6),'F-04':(12.15,78.0),'F-05':(15.9,95.3),'F-06':(12.05,82.9),'F-07':(16.4,83.75)}
LABELSIZE={'G-16':0.24,'F-07':0.3,'G-09':0.34,'G-11':0.3,'G-05':0.42,'G-12':0.42,'F-05':0.42,'G-09':0.4,'G-13':0.36,'G-06':0.4,'G-07':0.42,'G-11':0.42,'G-03':0.42,'G-02':0.42,'F-06':0.36,'F-07':0.42,'G-10':0.42,'F-04':0.45,'F-03':0.42,'F-01':0.45,'G-09':0.45,'G-01':0.6,'F-02':0.8}
TAGPOS={'GW-01':(3.125,53.0),'GW-05':(20.625,51.0),'GW-07':(9.875,91.5),'BW-01':(0.19,50.0),'GW-04':(19.0,31.125),'GW-13':(12.62,58.94),'GW-12':(17.6,46.56),
        'GW-03':(8.875,33.6),'GW-02':(3.6,40.875),'GW-11':(19.0,36.19),'GW-08':(11.0,94.75),'GW-06':(8.0,73.5),'GW-16':(11.94,71.6),'GW-17':(4.4,66.75),'GW-18':(6.375,72.3),'PW-02':(2.94,40.0),'PW-04':(20.81,40.0),
        'FW-01':(9.875,94.0),'FW-03':(20.625,92.0),'FW-02':(18.4,73.5),'FW-04':(19.0,97.0),'FW-05':(18.0,80.06),'PW-03':(19.4,19.94),'PW-01':(5.0,15.69),'PW-05':(6.0,77.69),
        'GW-15':(18.4,80.44),'GW-14':(8.0,66.56),'GW-10':(13.94,34.6),'GW-09':(9.06,43.0),'BW-03':(1.19,98.0),'BW-07':(20.81,25.0),'BW-08':(20.81,100.5),'BW-02':(0.6,89.19)}
OPENTAGOFF={'W-01':-0.75,'V-01':-0.75,'W-02':0.9,'W-03':-1.0,'W-04':-1.0,'W-05':-1.0,'W-06':-1.0,'V-02':-1.0,'W-07':-1.0,'W-08':0.8,'D-01':-1.4,'D-02':-2.2,'D-03':-1.6,
            'O-01':-0.8,'D-04':1.6,'D-05':-1.5,'D-06':1.7,'D-07':1.7,'D-08':-1.4,'D-09':-1.6,'W-09':-0.8,'W-10':-1.0,'W-11':0.8,'W-12':-0.85,'D-10':0.9}
SPC=(17.0,76.875); SPR=35/12   # ST-2 spiral: centre and outer radius (5'10" across)
# ST-2: 18 risers of 7 2/3" (11'6" floor to floor), 17 oak treads of 30 deg + a 60 deg landing at the first floor.
# Climbs anticlockwise (outer handrail on your right going up). Tread 1 starts on the 345 deg line (plan angle: 0 = west, 90 = south),
# so you walk onto it heading south along GW-05; the landing (135-195 deg) opens east onto F-04. RCC well: 6' round hole.
ST2=dict(n=18,ang=30,start=345,land=60,well=3.0,col=2.25/12)
CH_G_E=[0,30.75,40.5,41.25,46.75,58.75,59.125,66.375,67.125,73.875,89.0,106.0]
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
 ('FU-03.1','G','3-seat sofa',3.5,6.0,50.0,56.25,'sofa','x1','Living, 6\'3" x 2\'6", back to GW-01 under the windows, moved toward GW-13'),
 ('FU-03.2','G','2-seat sofa',6.0,10.25,56.25,58.75,'sofa','y2','Living, 4\'3" x 2\'6", back against GW-13 (below the folding glass sill); starts where FU-03.1 ends so every seat is free'),
 ('FU-04','G','Coffee table',7.0,10.0,51.25,54.75,'table',None,'Living, 3\' x 3\'6", centred in the L'),
 ('FU-05','G','TV, showcase and bookshelf wall unit',18.917,20.25,46.75,58.75,'tvwall',None,'Living, 12\' x 1\'4", full height on GW-05, wall to wall: TV in the middle, showcase and book shelves on both sides'),
 ('FU-06','G','Queen bed',13.75,20.25,41.25,46.25,'bed','x2','Bedroom 1, 6\'6" x 5\', head to GW-05 (east-west), side against GW-12'),
 ('FU-09.1','G','Wardrobe, part 1',17.25,20.25,36.375,37.7083,'ward',None,'Bedroom 1, 3\' x 1\'4" on GW-11, with loft'),
 ('FU-09.2','G','Wardrobe, part 2',18.9167,20.25,37.7083,41.125,'ward',None,'Bedroom 1, 3\'5" x 1\'4" on GW-05; L-shape with part 1, total 6\'5"'),
 ('FU-10','G','Study desk',9.5,13.5,31.5,33.5,'desk',None,'Study, 4\' x 2\', under W-01'),
 ('FU-11','G','Bookshelf',12.5,13.75,33.75,36.25,'shelf',None,'Study, on GW-10'),
 ('FU-12','G','Western WC',18.0,20.25,33.9,35.4,'wc','x2','Toilet 1, wall-mounted cistern'),
 ('FU-13','G','Wash basin',14.125,15.5,31.5,32.9,'basin',None,'Toilet 1'),
 ('FU-14','G','Shower area',17.25,20.25,31.5,33.6,'shower',None,'Toilet 1, open (no screen), floor slopes to a 5" square floor trap, geyser above'),
 ('FU-63','G','Bath rack, 2 shelves',15.6,16.9,31.5,31.95,'over',None,'Toilet 1, wall-mounted on GW-04 between the basin and the shower, for soap, shampoo and toothbrushes'),
 ('FU-15','G','Kitchen counter, east',3.5,5.5,59.125,66.375,'counter',None,'Kitchen, 7\'3" x 2\' on GW-01'),
 ('FU-16','G','Kitchen counter, back (modular)',5.5,8.6,64.375,66.375,'counter',None,'Kitchen, 3\'1" x 2\' on GW-14, with base drawers and the sink'),
 ('FU-16.2','G','Low counter, wet grinder and water',8.6,12.125,64.375,66.375,'counter',None,'Kitchen, 3\'6½" x 2\' on GW-14 up to the toilet 2 wall, top at 2\' from the floor: wet grinder at the sink end, water pots under the RO purifier at the other end'),
 ('FU-17','G','Breakfast counter',5.5,13.5,59.125,60.375,'counter2',None,'Kitchen, 8\' x 1\'3" on GW-13, under the folding glass W-12; joins the east counter with no gap, extended into the old fridge place, microwave at its west end'),
 ('FU-18','G','Fridge',17.75,20.25,59.125,61.375,'fridge',None,'Open area, single door, on GW-05 at the north end of the FU-25 cupboard, flush with its face'),
 ('FU-19','G','Overhead cabinets, back',4.75,9.875,65.125,66.375,'over',None,'Kitchen, on GW-14 above the back counter and sink, glass doors on the unit above the sink, RO purifier below them (dashed)'),
 ('FU-68','G','Top storage, back',4.75,9.875,65.125,66.375,'over',None,'Kitchen, second row of cabinets on GW-14 from 7\' up to the ceiling (dashed)'),
 ('FU-69','G','Top storage, east',3.5,4.75,59.125,66.375,'over',None,'Kitchen, second row of cabinets on GW-01 from 7\' up to the ceiling, right across above the window and chimney (dashed)'),
 ('FU-19.2','G','Overhead shelves, east',3.5,4.75,65.0,66.375,'over',None,'Kitchen, corner unit above the east counter beside the window (dashed)'),
 ('FU-19.3','G','Overhead shelves, east',3.5,4.75,59.125,61.0,'over',None,'Kitchen, above the east counter beside the window, glass door (dashed)'),
 ('FU-25','G','Store cupboard, full height',17.75,20.25,61.375,71.375,'store2',None,'Open area and stair hall, 10\' x 2\'6", floor to ceiling on GW-05, south of the fridge; its face lines up with the fridge and the GW-13 end stub'),
 ('FU-26.1','G','WC platform, 4" high',6.75,10.25,70.625,73.125,'plat',None,'Toilet 2, tiled platform in the south-east corner (GW-18 and GW-06): 3\'6" front to back (east-west, the way the user faces) x 2\'6" side to side, room to squat comfortably'),
 ('FU-26','G','Indian WC (Orissa pan)',7.05,8.97,71.145,72.605,'iwc',None,'Toilet 2, centred on the 4" platform FU-26.1 against the east wall GW-18, user faces west, V-02 above; health faucet on GW-06 on the left hand'),
 ('FU-57','G','Bucket, tap and health faucet',9.25,10.15,72.15,73.05,'bucket',None,'Toilet 2, on the front of the platform on the user\'s left, bib tap on GW-06; health faucet on GW-06 beside the pan'),
 ('FU-27','G','Wash basin, wall-hung',10.3,11.72,71.96,73.125,'basin',None,'Toilet 2, 1\'5" x 1\'2" on GW-06 in the corner by the door, beside the platform (clear of the door swing); mirror above; rim 2\'8"'),
 ('FU-28','G','Shower area',6.75,11.75,66.75,69.625,'shower',None,'Toilet 2, 5\' x 2\'10½" across the whole north end, open (no screen); rose on GW-14 at 6\'9"; floor trap in the middle; floor slopes 1:60; the door folds back over it'),
 ('FU-58','G','Geyser',7.0,8.4,66.75,67.225,'geyser',None,'Toilet 2, on GW-14 above the shower, clear of the rose, bottom at about 6\'3"'),
 ('FU-70','G','Bath rack, 2 shelves',11.33,11.75,66.85,67.7,'over',None,'Toilet 2, wall-mounted on GW-16 in the shower, north of the door, for soap and shampoo'),
 ('FU-29','G','Washing machine',3.25,5.25,74.25,76.25,'wm',None,'Side garden utility, covered by the terrace corner, south of the bore court'),
 ('FU-30','G','Wash basin with tap',5.5,7.0,74.25,75.5,'basin',None,'Side garden, under the terrace corner, near garden door D-05'),
 ('FU-31','G','Queen bed',13.75,20.25,85.0,90.0,'bed','x2','Bedroom 2, head to GW-05'),
 ('FU-32','G','Side table',18.75,20.25,83.25,84.75,'cab',None,'Bedroom 2'),
 ('FU-33','G','Side table and dressing shelf',18.85,20.25,90.25,93.65,'cab',None,'Bedroom 2, one long floating oak shelf on GW-05 (3\'5"): side table with a lamp at the bed end, dressing table with a mirror above and a stool at the other end; replaces FU-35'),
 ('FU-34','G','Wardrobe with loft',14.0,20.25,80.625,81.9583,'ward',None,'Bedroom 2, 6\'3" x 1\'4", on GW-15'),
 ('FU-36','F','Queen bed',13.75,20.25,89.0,94.0,'bed','x2','Bedroom 3, head to FW-03'),
 ('FU-37','F','Side table',18.75,20.25,87.25,88.75,'cab',None,'Bedroom 3'),
 ('FU-38','F','Side table',18.75,20.25,94.25,95.75,'cab',None,'Bedroom 3'),
 ('FU-39','F','Sliding wardrobe with loft',14.5,20.25,84.875,86.2083,'ward',None,'Bedroom 3, 5\'9" x 1\'4", on FW-07'),
 ('FU-40','F','Study desk',10.25,11.75,88.5,92.5,'desk',None,'Bedroom 3, under W-10'),
 ('FU-41','F','Western WC',16.25,17.75,80.25,82.5,'wc','y1','Toilet 3, cistern on FW-05, faces south; 2\' clear in front'),
 ('FU-42','F','Wash basin, wall-hung',14.5,15.9,80.25,81.35,'basin',None,'Toilet 3, on FW-05 right beside the door; mirror above'),
 ('FU-43','F','Shower area',18.0,20.25,80.25,84.5,'shower',None,'Toilet 3, 2\'3" x 4\'3" across the west end (was 1\'9" x 2\'3"); floor trap in the middle'),
 ('FU-60','F','Geyser',19.8,20.25,81.5,82.9,'geyser',None,'Toilet 3, on FW-03 above the shower, bottom at about 6\'3"'),
 ('FU-61','F','Shower curtain rod',17.95,18.05,80.25,84.5,'curtain',None,'Toilet 3, keeps the WC side dry'),
 ('FU-71','F','Overhead water tank, 2000 L',15.2,20.2,91.4,96.4,'over',None,'On the bedroom 3 roof (above F-05), 5\' across x 5\' high on a 1\' RCC stand near FW-03; highest point for good pressure, clear of the future hall'),
 ('FU-72','F','Cat ladder to the bedroom 3 roof',18.0,19.5,72.6,73.125,'over',None,'MS ladder on the terrace face of FW-02, for reaching the water tank'),
 ('FU-62','F','Exhaust fan, ducted to roof',18.6,19.6,82.9,83.9,'fan',None,'Toilet 3 has no outside wall: ceiling exhaust fan with a duct up through the roof slab'),
 ('FU-44','G','AC indoor unit',9.25,9.92,37.25,40.25,'acin',None,'Bedroom 1, on GW-03 above window W-02, about 7\'6" high'),
 ('FU-45','G','AC outdoor unit',9.0,11.67,29.58,30.75,'acout',None,'Bedroom 1, on GW-04 parking face, bracket above window W-01 (about 7\'6"); pipe runs inside the study corner'),
 ('FU-46','G','AC indoor unit',10.25,10.92,85.5,88.5,'acin',None,'Bedroom 2, on GW-07 centred above window W-07 (about 7\'7"), blows straight across the bed'),
 ('FU-47','G','AC outdoor unit',8.33,9.5,82.0,84.67,'acout',None,'Bedroom 2, on GW-07 side-garden face'),
 ('FU-48','F','AC indoor unit',10.25,10.92,93.0,96.0,'acin',None,'Bedroom 3, on FW-01 facing the bed'),
 ('FU-49','F','AC outdoor unit',8.33,9.5,93.25,95.92,'acout',None,'Bedroom 3, wall bracket on FW-01 outside'),
 ('FU-51','G','Kitchen sink',6.5,8.4,64.625,66.125,'sinkbowl',None,'Kitchen, single bowl on the back counter FU-16, against GW-14'),
 ('FU-64','G','Mixer grinder',3.75,4.6,59.5,60.35,'appl',None,'Kitchen, east counter in the GW-13 corner, socket on GW-01'),
 ('FU-65','G','Wet grinder, table-top',8.65,9.85,64.7,65.9,'appl',None,'Kitchen, on the 2\' low counter FU-16.2 beside the sink, socket on GW-14'),
 ('FU-66','G','RO water purifier, wall-mounted',10.95,11.75,65.85,66.375,'over',None,'Kitchen, on GW-14 above the west end of the low counter FU-16.2; tap at about 3\'2", so a pot on the low counter fills easily (dashed)'),
 ('FU-67','G','Microwave oven',11.75,13.4,59.15,60.35,'appl',None,'Kitchen, on the west end of the breakfast counter FU-17'),
 ('FU-52','G','Hob (burner) with small chimney',3.6,5.4,62.0,64.0,'hob',None,'Kitchen, under window W-06; chimney hood 2\'6" above the counter, just above the window head, ducted straight out through GW-01'),
 ('FU-53','G','Tap and wash platform',1.375,4.875,89.375,91.875,'washpad',None,'Side garden, paved with drain, in the corner of BW-02 and BW-03'),
 ('FU-54','G','Wash basin with tap',19.125,20.625,95.25,96.5,'basin',None,'Back garden, against GW-08 beside window W-08'),
 ('FU-55','G','Tap and wash platform',17.625,20.625,96.75,99.25,'washpad',None,'Back garden, paved, with floor drain'),
 ('FU-76','G','Tree well round the neem',10.75,14.75,2.25,6.25,'treepit',None,'Parking, 4\' across (was 5\'6"): the trunk stays at today\'s ground; a low retaining ring, 4½" brick with a granite coping; about 10" of open soil with leaf mulch all round the 1\'6" trunk; small so the car can pass'),
 ('FU-73','G','Flower bed along the back wall',1.375,20.625,103.14,105.6,'fbed',None,'Back and side garden, 1\'6" deep all along the back wall BW-09, 9" brick kerb, red soil; a row of Tamil Nadu flowering plants PL-01 to PL-12'),
 ('FU-74','G','Tulsi maadam',4.5,6.0,96.75,98.25,'tulsi',None,'Side garden, 1\'6" square, 3\' high plastered pedestal with a lamp niche facing east, Tulsi PL-13 on top'),
 ('FU-75','G','Clothes drying line',10.25,17.25,101.0,101.5,'cline',None,'Back garden, two black MS posts 6\' high with T-arms, 3 steel wires, 7\' long; clear of the back door D-10 and the wash platform'),
 ('FU-56','G','Low store under staircase 1',17.125,20.625,8.6,12.2,'store',None,'Parking, 3\'6" x 3\'7", under the lower middle of ST-1A (about 1\'10" to 3\'8" high inside), small door facing east, for tools and the hose; the high end of ST-1A is now open for two-wheeler TW-1'),
]
# door and window types (proposal)
SPEC = {
 'D-01':'Teak wood, double leaf, with safety grill door',
 'D-02':'Flush door, hardwood frame', 'D-06':'Flush door, hardwood frame', 'D-07':'Flush door, hardwood frame',
 'D-03':'WPC waterproof door', 'D-04':'WPC waterproof door', 'D-08':'WPC waterproof door',
 'D-05':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'W-01':'UPVC sliding window; grill with brown scroll ornaments; outside small gable frame WF-2 (wood-look brown frame and gable, red clay-tile roof)',
 'D-09':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'D-10':'Steel or UPVC door, glass upper half, plus MS grill shutter',
 'O-01':'Plastered arch opening, no shutter',
 'W-12':'Bi-fold glass window, aluminium or UPVC frame, curtain on the living side',
 'GT-01':'MS swing gate, double leaf (no room on the wall for a sliding gate)', 'GT-02':'MS double-leaf hinged gate, opens inward',
}
for _o in OPENINGS:
    if _o[5]=='window' and _o[0] not in SPEC: SPEC[_o[0]]='UPVC 3-track sliding: 2 glass + 1 mosquito mesh, MS safety grill, 1\'6" sunshade outside'
    if _o[5]=='vent' and _o[0] not in SPEC: SPEC[_o[0]]='Louvred glass ventilator with exhaust fan opening'
SPEC['V-03']='Louvred glass ventilator with exhaust fan opening'
CAR=(9.25,15.0,14.75,29.75)   # VW Virtus size, 14'11" x 5'9" (4561 x 1752 mm), reversed in: nose to the gate, back 1' clear of GW-04; 2'4" aisle to the two-wheelers on its west side, driver (right) door onto the wide east walkway
# two-wheelers: (code, model, centre X, centre Y, length, width, facing); facing 'N' = front to the gate (length along Y), 'E' = front to the east (length along X)
BIKES=[('TW-1','Honda VFR800',18.66,15.78,6.96,2.41,'N'),   # under the high end of ST-1A and the landing (its 4' windscreen where the underside is 5' or more)
       ('TW-2','Ather 450X',13.985,7.71,6.03,2.42,'E'),     # across, by the neem: 3" from the tree-well ring, against the side of ST-1A; the car passes 6" from it
       ('TW-3','Second two-wheeler (spare spot)',18.61,22.62,6.03,2.42,'N')]   # along BW-07 beside the car (fits up to 7' long), front to the gate
CH_G_FRONT=[0,0.75,12.0,13.5,20.25,21.0]

# ---------- structure (proposal): RCC frame with side pillars only, no pillar inside any room ----------
# Columns 1' x 9" (engineer's size), the 1' along the wall, so each column hides inside a 9" outer wall.
# id, floors, x1, x2, y1, y2, note.  floors: 'G' = ground floor, continues up later for the future hall; 'G+F' = up to the first-floor roof
COL_SIZE="1' x 9\""
COLUMNS = [
 ('C-01','G', 0.375,1.125, 19.75,20.75,'East, moved against the east compound wall BW-01 so the parking is clear for the two-wheelers; carries the extended B-01'),
 ('C-02','G', 20.25,21.0, 19.75,20.75,'West, front edge of the terrace slab, just behind the ST-1 landing'),
 ('C-03','G', 2.75,3.5, 30.75,31.75,'East, porch front corner'),
 ('C-04','G', 20.25,21.0, 30.75,31.75,'West, corner of GW-04 and GW-05'),
 ('C-05','G', 2.75,3.5, 35.7,36.7,'East, porch side, in line with GW-11'),
 ('C-06','G', 20.25,21.0, 35.7,36.7,'West, in GW-05 where GW-11 meets it'),
 ('C-07','G', 2.75,3.5, 46.0,47.0,'East, in GW-01 at the foyer | living line'),
 ('C-08','G', 20.25,21.0, 46.0,47.0,'West, in GW-05 where GW-12 meets it'),
 ('C-09','G', 2.75,3.5, 58.44,59.44,'East, in GW-01 where GW-13 meets it'),
 ('C-10','G', 20.25,21.0, 58.44,59.44,'West, in GW-05 where GW-13 meets it'),
  ('C-11','G', 2.75,3.5, 66.125,67.125,'East, end of GW-01 at the bore court corner'),
  ('C-12','G', 20.25,21.0, 66.125,67.125,'West, in GW-05 behind the FU-25 store cupboard, in line with GW-14'),
  ('C-20','G0', 6.0,6.75, 66.375,67.375,'Bore court corner: GW-17, GW-18 and GW-14; footing kept away from bore BR-02. Ground floor only: stops at the roof slab, no stub on the terrace, so the future hall has no pillar in the middle'),
  ('C-21','G0', 6.0,6.75, 72.875,73.875,'Bore court corner: GW-18 and GW-06; eccentric footing needed, it is close to bore BR-02. Ground floor only: stops at the roof slab, no stub on the terrace'),
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
 ('B-02','G', 2.75,21.0, 30.75,31.5, "1'6\"",'Over GW-04 and the porch front, C-03 to C-04'),
 ('B-03','G', 2.75,21.0, 35.825,36.575, "1'6\"",'Over GW-11, across the porch and the study corner opening, C-05 to C-06'),
 ('B-04','G', 2.75,21.0, 46.125,46.875, "1'6\"",'Over GW-12 (bedroom 1 | living), C-07 to C-08'),
 ('B-05','G', 2.75,21.0, 58.565,59.315, "1'6\"",'Over GW-13 (living | kitchen), C-09 to C-10'),
  ('B-06','G', 2.75,21.0, 66.25,67.0, "1'6\"",'Over GW-14 and across the open area, C-11 to C-12'),
  ('B-07','G', 9.5,21.0, 73.125,73.875, "1'6\"",'Under FW-02, C-14 to C-15'),
 ('B-08','G', 9.5,21.0, 80.065,80.815, "1'3\"",'Over GW-15, C-16 to C-17'),
 ('B-09','G', 9.5,21.0, 94.375,95.125, "1'3\"",'Over GW-08, C-18 to C-19'),
  ('B-10','G', 2.75,3.5, 19.75,67.125, "1'3\"",'East edge beam over GW-01 and the porch side, from B-01 (beam on beam) to C-11'),
  ('B-11','G', 9.5,10.25, 73.125,95.125, "1'3\"",'East edge beam over GW-07, C-14 to C-18'),
  ('B-18','G', 6.0,6.75, 66.375,73.875, "1'3\"",'Over GW-18 (bore court | toilet 2), C-20 to C-21'),
  ('B-19','G', 2.75,6.75, 66.375,67.125, "1'3\"",'Over GW-17 (kitchen | bore court), C-11 to C-20'),
  ('B-20','G', 2.75,10.25, 73.125,73.875, "1'3\"",'Over GW-06, C-21 to C-14; cantilevers 3\'3" east, and the terrace corner cantilevers 4\' south of it'),
 ('B-12','G', 20.25,21.0, 19.75,95.125, "1'3\"",'West edge beam over GW-05, C-02 to C-19'),
 ('B-13','F', 9.5,21.0, 73.125,73.875, "1'3\"",'Over FW-02, C-14 to C-15'),
 ('B-14','F', 9.5,21.0, 79.875,80.625, "1'3\"",'Over FW-05, C-16 to C-17'),
 ('B-15','F', 9.5,21.0, 96.625,97.375, "1'3\"",'Over FW-04, carried by the B-16 and B-17 cantilevers'),
 ('B-16','F', 9.5,10.25, 73.125,97.375, "1'3\"",'Over FW-01, C-14 to C-18, then cantilevers 2\'3" to carry FW-04'),
 ('B-17','F', 20.25,21.0, 73.125,97.375, "1'3\"",'Over FW-03, C-15 to C-19, then cantilevers 2\'3" to carry FW-04'),
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
