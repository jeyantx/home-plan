# Home Plan

House plan for a 21' x 106' plot in Tamil Nadu (road on the north).

Open `index.html` for the app: 3D view, 2D plan, and tabs for the overview, parking and outside,
rooms and walls, doors and windows, structure, furniture and the decisions log.
The pages are static; serve the folder with any web server (for example `python3 -m http.server 8765`)
because the 3D view loads its models over HTTP.

The plan data lives in `v1/model.py`. Rebuild after a change:

    cd v1 && python3 build.py && python3 build3d.py

`build.py` writes `plan-2d.html` and `index.html`; `build3d.py` writes `3d/living-room.html`.
Third-party models and libraries are listed with their licences in `3d/ASSETS.md`.
