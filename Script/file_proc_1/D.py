
r, g, b = map(int, input().split())
#255 165 184
r /= 255.
g /= 255.
b /= 255.

cmax = max(r, g, b)
cmin = min(r, g, b)
diff = cmax - cmin

def huef(r, g, b, cmax, cmin, diff):
    if cmax == cmin and cmax == 0:
        return 0
    if diff == 0:
        return 0
    if cmax == r:
        return (60 * (g - b) / diff + 360) % 360
    if cmax == g:
        return (60 * (r - b) / diff + 120) % 360
    if cmax == b:
        return (60 * (r - g) / diff + 240) % 360

h = huef(r,g,b,cmax,cmin,diff)

def satf(r,g,b,cmax,cmin,diff):
    if cmax == 0:
        return 0.0
    return (diff / cmax) * 100

s = satf(r,g,b,cmax,cmin,diff)

v = cmax * 100

print(int(round(h, 0)), round(s, 1),  round(v, 1))
