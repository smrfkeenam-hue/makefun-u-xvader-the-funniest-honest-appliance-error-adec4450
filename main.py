import os

# The funniest honest appliance error: a washing machine, flat and
# resigned, reporting the one fault it cannot fix by itself.
# The joke is the truth of it: seven redistributions, one sock.
ENTRY = "Error E4: load unbalanced. I have redistributed your laundry seven times. It is one sock. Please remove the sock."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
