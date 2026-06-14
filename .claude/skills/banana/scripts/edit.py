#!/usr/bin/env python3
"""Fallback image editing script using Gemini REST API (stdlib only, no pip deps)."""
import argparse
import base64
import json
import mimetypes
import os
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

DEFAULT_MODEL = "gemini-3.1-flash-image-preview"
OUTPUT_DIR = Path.home() / "Documents" / "nanobanana_generated"
SUPPORTED = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".gif": "image/gif"}


def get_api_key(args_key=None):
    return args_key or os.environ.get("GOOGLE_AI_API_KEY") or os.environ.get("GOOGLE_API_KEY")


def edit(image_path, prompt, model, api_key):
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    ext = path.suffix.lower()
    mime = SUPPORTED.get(ext, "image/png")
    b64_image = base64.b64encode(path.read_bytes()).decode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [
            {"text": prompt},
            {"inlineData": {"mimeType": mime, "data": b64_image}},
        ]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def save_image(b64_data):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = OUTPUT_DIR / f"edited_{ts}.png"
    path.write_bytes(base64.b64decode(b64_data))
    return str(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-key")
    args = parser.parse_args()

    api_key = get_api_key(args.api_key)
    if not api_key:
        print(json.dumps({"error": "No API key. Set GOOGLE_AI_API_KEY or pass --api-key"}))
        sys.exit(1)

    for attempt in range(3):
        try:
            result = edit(args.image, args.prompt, args.model, api_key)
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                time.sleep(2 ** (attempt + 1))
            elif e.code == 400:
                body = json.loads(e.read())
                if "FAILED_PRECONDITION" in str(body):
                    print(json.dumps({"error": "Billing not enabled. Visit https://aistudio.google.com to enable."}))
                    sys.exit(1)
                raise
            else:
                raise

    text_response = None
    image_path = None
    for candidate in result.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if "text" in part:
                text_response = part["text"]
            elif "inlineData" in part:
                image_path = save_image(part["inlineData"]["data"])

    finish = result.get("candidates", [{}])[0].get("finishReason", "UNKNOWN")
    output = {"imagePath": image_path, "text": text_response, "model": args.model, "sourceImage": args.image, "finishReason": finish}
    print(json.dumps(output))


if __name__ == "__main__":
    main()
