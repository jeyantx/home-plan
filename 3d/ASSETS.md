# Local assets used by the 3D pages

Everything the 3D pages need is stored here, so they work offline.

## Libraries (`vendor/`)
| Folder | Version | Source | Licence |
|---|---|---|---|
| `vendor/three` | three.js 0.186.1 (build + examples/jsm) | https://www.npmjs.com/package/three | MIT |
| `vendor/three-mesh-bvh` | 0.9.16 (src) | https://www.npmjs.com/package/three-mesh-bvh | MIT |
| `vendor/three-gpu-pathtracer` | 0.0.27 (src) | https://www.npmjs.com/package/three-gpu-pathtracer | MIT |

## Textures (`assets/textures/`), 1k JPG: diffuse, normal (GL), roughness
All CC0 (public domain) from Poly Haven, https://polyhaven.com

| Folder | Used for | Real size of one tile |
|---|---|---|
| `laminate_floor_02` | Living floor, wood-look planks (option 1) | 1.70 m |
| `white_oak_veneer` | Oak shelves, console, coffee table, doors | 0.50 m |
| `oak_veneer_01` | TV centre wall; sofa frame (stained darker) | 1.83 m |
| `rough_linen` | Sofa and cushion weave (normal + roughness only) | 0.27 m |
| `crepe_georgette` | Sheer curtain weave (normal + roughness only) | 0.26 m |
| `hessian_230` | Jute rug | 0.27 m |
| `ceiling_interior` | Paint and plaster surface texture | 2.00 m |

## Sky (`assets/hdri/`)
| File | Used for | Source | Licence |
|---|---|---|---|
| `kloofendal_48d_partly_cloudy_puresky_1k.hdr` | Sky seen through windows; daylight in Photo mode | https://polyhaven.com/a/kloofendal_48d_partly_cloudy_puresky | CC0 |

## Models made in code (no downloads)
- `models/bamboo-plant.js`: bamboo plant in a black pot, procedural, canvas textures.
- `models/vehicles.js`: VW Virtus, Royal Enfield Hunter 350 and Ather 450X to real sizes (procedural), with wheel, steering, side-stand and lean groups for animation.
- `models/tn-plants.js`: Tamil Nadu garden plants (malli, sembaruthi, nandiyavattai, vetchi, kanakambaram, nithya kalyani, rose, karuveppilai, tulsi), procedural.
- `models/garden-plants.js`: garden plan plants GD-01 (areca palm), GD-06 (dwarf banana) and GD-08 (drumstick tree), procedural.
- `models/tn-plants.js` also draws the garden-plan vegetables and herbs (GD-07, GD-09), the climbing jasmine GD-05 and the lemon GD-11.
- `models/neem-tree.js`: the existing neem tree at the gate, rebuilt from the site photos (south lean, fork at about 3 m, south limb cut to a stub). Procedural, canvas textures.

## Site photos (owner's, for reference only)
- `assets/site-photos/site-01.jpg` to `site-16.jpg`: the plot, the neem tree and the neighbour houses, 2026-10-18.

## Downloaded models (`assets/vehicles/`)
| File | What | Source | Licence |
|---|---|---|---|
| `compact-car.glb` | Car in the parking (scaled to VW Virtus size, 4561 x 1752 mm body); materials restyled in `models/vehicles.js` (`loadCarGLB`) | Free3D "Compact Car (Generic)", https://free3d.com/3d-model/compact-car-generic-875091.html, converted from `202009122216-2.blend` with Blender 5.2 | Personal use only (Free3D licence); published here at the owner's choice |
| `vfr800.glb` | Two-wheeler TW-1 along BW-01: Honda VFR800 at its real length (2120 mm); converted from `vfr800.blend` (mirror applied, smoothing off, backdrop removed); its plain materials restyled in the 3D page (`vfrMats`) | "Honda VFR800" by danielfc10, Blend Swap, http://www.blendswap.com/blends/view/45121 | CC BY 3.0: credit danielfc10 |
| `motorcycle.glb` | (not used now) Baotian Sanya motorcycle | Provided by the owner | Not recorded |
| `scooter.glb` | Two-wheeler TW-2 along BW-01 (sized to an Ather 450X, 1837 mm), textures reduced to 1024 px; converted from the owner's `Scooter Textured.blend` | Provided by the owner | Not recorded: check before sharing |

## Appliance models (`assets/appliances/`)
| File | What | Source | Licence |
|---|---|---|---|
| `cooktop.glb` | Free-standing 3-burner glass-top gas stove FU-52, scaled to 70 x 41 x 13 cm; converted from `Cook top Faber N141117.3DS` (turned Y-up, simplified to about 30,000 triangles); materials restyled in the 3D pages (`cookMat`) | archibase.net, provided by the owner | Free download from archibase.net (licence as on the site) |
| `washing-machine.glb` | Front-load washing machine FU-29, scaled to 85 cm high; converted from `Washing machine Zanussi N280220.obj` with Blender; materials restyled (`wmMat`) | archibase.net, provided by the owner | Free download from archibase.net (licence as on the site) |
| `microwave.glb` | Microwave oven FU-67, 46 x 28 x 36 cm; from `Microwave.3DS` (turned Y-up, each axis fitted); its door parts were scattered, so the body, door, glass, handle, panel and knobs are rebuilt round the original control details (`v1/tools/mw2glb.mjs`, run with three.js in Node); materials restyled in the 3D pages (`mwMat`) | archibase.net, provided by the owner | Free download from archibase.net (licence as on the site) |
| `fridge.glb` | Fridge FU-18, double door, 605 x 606 x 1700 mm; converted from `Refrigerator 1 N171009.3DS` (turned Y-up, millimetres to metres); materials restyled in the 3D page (`fridgeMat`) | archibase.net, provided by the owner | Free download from archibase.net (licence as on the site) |

## Garden plant models (`assets/plants/`)
All CC0 (public domain) from Poly Haven, https://polyhaven.com, downloaded as 1k glTF and converted with Blender 5.2 (simplified, textures reduced to 512 px, base on the ground, metres).

| File | What | Source | Licence |
|---|---|---|---|
| `syngonium-pot.glb` | GD-03 syngonium in a terracotta pot, porch (about 9,000 + 3,300 triangles) | "Potted Plant 02" by Rico Cilliers, https://polyhaven.com/a/potted_plant_02 | CC0 |
| `anthurium.glb` | GD-02 anthurium (one plant of the set), in a code-made black pot, porch (8,000 triangles) | "Anthurium Botany 01" by Rob Tuytel and Rico Cilliers, https://polyhaven.com/a/anthurium_botany_01 | CC0 |
| `fern.glb` | GD-04 ferns in the six wall pots, side passage (one fern of the set, 2,400 triangles) | "Fern 02" by Rob Tuytel and Rico Cilliers, https://polyhaven.com/a/fern_02 | CC0 |
| `aloe-pot.glb` | GD-10 aloe-like succulent in a white pot, scaled up to an aloe vera pot (6,400 triangles) | "Potted Plant 04" by James Ray Cock, https://polyhaven.com/a/potted_plant_04 | CC0 |

## Site icon

| File | What | Author | Licence |
|---|---|---|---|
| `favicon.png` | House icon used as the site icon (browser tab) | [Icons8](https://icons8.com) | Free with a link to Icons8 |
