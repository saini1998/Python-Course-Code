sentence = "This is a common interview question"
d = dict()
for x in sentence.lower():
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
max = 0
for key, values in d.items():
    print(key, values)
    if max < values:
        max = values
        max_key = key
print(f"max {max_key} {max}")

d_sorted = sorted(
    d.items(),
    key=lambda kv: kv[1],
    reverse=True
)
print(d_sorted[0])
