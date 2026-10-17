#!/bin/bash
# Copies the latest page of every branch into views/ so all versions can be opened at any time.
cd "$(dirname "$0")"
mkdir -p views
links=""
for br in $(git for-each-ref --format='%(refname:short)' refs/heads/); do
  if git show "$br:home-plan-$br.html" > "views/$br.html" 2>/dev/null; then
    when=$(git log -1 --format='%cd' --date=format:'%d %b %Y %H:%M' "$br")
    msg=$(git log -1 --format='%s' "$br")
    links="$links<li><a href=\"$br.html\"><b>$br</b></a> <span>· $when · $msg</span></li>"
  else
    rm -f "views/$br.html"
  fi
done
cat > views/index.html <<HTML
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Plan Versions</title>
<style>:root{--bg:#f4f2ee;--ink:#1f2328;--muted:#5d646d;--accent:#2f6f4f}
@media (prefers-color-scheme:dark){:root{--bg:#16181b;--ink:#e8e6e1;--muted:#a3a8ae;--accent:#5fb08a}}
body{background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:760px;margin:40px auto;padding:0 16px}
a{color:var(--accent)} span{color:var(--muted);font-size:13px} li{margin:8px 0}</style></head>
<body><h1>Home plan versions</h1><ul>$links</ul></body></html>
HTML
echo "views updated"
