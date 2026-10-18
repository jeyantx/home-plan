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
- `models/tn-plants.js`: Tamil Nadu garden plants (malli, sembaruthi, nandiyavattai, vetchi, kanakambaram, nithya kalyani, rose, karuveppilai, tulsi), procedural.
- `models/neem-tree.js`: the existing neem tree at the gate, rebuilt from the site photos (south lean, fork at about 3 m, south limb cut to a stub). Procedural, canvas textures.

## Site photos (owner's, for reference only)
- `assets/site-photos/site-01.jpg` to `site-16.jpg`: the plot, the neem tree and the neighbour houses, 2026-10-18.
