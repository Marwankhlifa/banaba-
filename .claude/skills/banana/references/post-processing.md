# Post-Processing Pipeline Reference

> Load this on-demand when the user needs image manipulation after generation.

## Prerequisites

```bash
which magick    # ImageMagick 7 (preferred)
which convert   # ImageMagick 6 (fallback)
which ffmpeg    # For video/animation
```

Install: `sudo apt install imagemagick` or `brew install imagemagick`

## Common Operations

### Resize for Platforms

```bash
# Instagram post (1080x1080)
magick input.png -resize 1080x1080^ -gravity center -extent 1080x1080 instagram.png

# YouTube thumbnail (1280x720)
magick input.png -resize 1280x720^ -gravity center -extent 1280x720 youtube-thumb.png

# Twitter/X header (1500x500)
magick input.png -resize 1500x500^ -gravity center -extent 1500x500 twitter-header.png
```

### Background Removal (Transparency)

```bash
# Remove solid white background
magick input.png -fuzz 10% -transparent white output.png

# Clean edges after transparency
magick input.png -fuzz 10% -transparent white -channel A -blur 0x1 -level 50%,100% output.png

# Auto-crop transparent padding
magick input.png -trim +repage output.png
```

### Format Conversion

```bash
# PNG to WebP
magick input.png -quality 85 output.webp

# PNG to JPEG
magick input.png -background white -flatten -quality 90 output.jpg
```

### Color Adjustments

```bash
magick input.png -contrast-stretch 2%x1% output.png    # Increase contrast
magick input.png -colorspace Gray output.png            # Grayscale
magick input.png -sepia-tone 80% output.png             # Sepia
```

### Compositing

```bash
# Side-by-side comparison
magick input1.png input2.png +append comparison.png

# Add padding/border
magick input.png -bordercolor white -border 40 output.png
```

## Green Screen Transparency Pipeline

Gemini cannot generate transparent backgrounds. Workaround:

### 1. Append to any prompt
```
on a solid bright green (#00FF00) chroma key background
with a thin white outline separating the subject from the background
```

### 2. Remove green screen
```bash
magick input.png -fuzz 20% -transparent "#00FF00" output.png
```

### 3. Clean edges
```bash
magick output.png -channel A -blur 0x1 -level 50%,100% -trim +repage final.png
```

### 4. FFmpeg alternative (better for batch)
```bash
ffmpeg -i input.png -vf "colorkey=0x00FF00:0.3:0.1,despill=type=green" -pix_fmt rgba output.png
```

## Note on 4K Output

With `imageSize: "4K"`, traditional upscaling post-processing is usually unnecessary. Generate at native 4K instead of upscaling from 1K.
