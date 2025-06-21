import re
import zlib

# Load the full binary
with open("0.zlib", "rb") as f:
    data = f.read()

# Regex pattern for zlib headers (most common)
matches = list(re.finditer(b'\x78[\x01\x9c\xda]', data))
print(f"[+] Found {len(matches)} zlib headers")

for i, match in enumerate(matches):
    start = match.start()
    # Try a reasonably large chunk size
    for size in [2048, 4096, 8192, 16384, 65536]:
        try:
            chunk = data[start:start+size]
            decompressed = zlib.decompress(chunk)
            print(f"\n✅ Chunk {i+1} at offset {start} (size={size}) decompressed:")
            print(decompressed.decode(errors="ignore"))
            with open(f"chunk_{i+1}.out", "wb") as out:
                out.write(decompressed)
            break  # Stop on first successful decompress for this chunk
        except Exception as e:
            continue
