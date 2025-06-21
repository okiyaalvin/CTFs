import os
import zlib

chunk_dir = "."  # or the full path if you're not inside _CA-0.extracted
output_dir = "decompressed_chunks"
os.makedirs(output_dir, exist_ok=True)

for i in range(33):  # 0 to 32 (33 total)
    fname = f"chunk{i}.zlib"
    try:
        with open(fname, "rb") as f:
            data = f.read()
            try:
                decompressed = zlib.decompress(data)
            except zlib.error:
                # Try raw stream (no zlib header)
                decompressed = zlib.decompress(data, wbits=-15)

            outname = os.path.join(output_dir, f"chunk{i}.bin")
            with open(outname, "wb") as out:
                out.write(decompressed)
            print(f"[+] Decompressed {fname} -> {outname}")
    except Exception as e:
        print(f"[!] Failed to decompress {fname}: {e}")
