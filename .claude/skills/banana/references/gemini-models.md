# Gemini Image Generation Models

> Last updated: 2026-03-19

## Available Models

### gemini-3.1-flash-image-preview -- Nano Banana 2 (DEFAULT)
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-3.1-flash-image-preview` |
| **Status** | Preview -- Active, recommended default |
| **Aspect Ratios** | All 14 ratios including extreme: 1:4, 4:1, 1:8, 8:1 |
| **Max Resolution** | Up to 4096×4096 (4K tier) |
| **Input Tokens** | 131,072 |
| **Features** | Google Search grounding, thinking levels, image-only output |
| **Rate Limits (Free)** | ~5-15 RPM / ~20-500 RPD |
| **Best For** | All standard production generation and editing |

### gemini-2.5-flash-image -- Nano Banana (Original)
| Property | Value |
|----------|-------|
| **Model ID** | `gemini-2.5-flash-image` |
| **Status** | GA -- Active |
| **Aspect Ratios** | 10 ratios (no extreme ratios) |
| **Max Resolution** | Up to 1024×1024 (1K tier) |
| **Cost** | ~$0.039/image at 1K |
| **Best For** | Free-tier users, budget-conscious workflows |

## ⛔ DEPRECATED -- gemini-3-pro-image-preview

**Shut down by Google on March 9, 2026.** Do not use. Replace with `gemini-3.1-flash-image-preview`.

## Domain-to-Model Routing

| Domain Mode | Recommended Model |
|---|---|
| Cinema, Landscape, Abstract | Nano Banana 2 |
| Product, Portrait | Nano Banana 2 |
| UI, Infographic | Nano Banana 2 |
| Logo | Nano Banana 2 |
| Free tier / budget | Nano Banana (original) |

## Aspect Ratios

| Ratio | NB2 (3.1 Flash) | NB (2.5 Flash) |
|-------|:----------------:|:--------------:|
| 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2, 4:5, 5:4, 21:9 | ✅ | ✅ |
| 1:4, 4:1, 1:8, 8:1 | ✅ | ❌ |

## Resolution Tiers

| `imageSize` Value | Pixel Range | Availability |
|-------------------|-------------|--------------|
| `512` | Up to 512×512 | Nano Banana 2 only |
| `1K` | Up to 1024×1024 | All models |
| `2K` | Up to 2048×2048 | Nano Banana 2 only |
| `4K` | Up to 4096×4096 | Nano Banana 2 only |

**CRITICAL:** `imageSize` MUST be UPPERCASE. `"2k"` silently fails.

## Required API Parameters

```json
{
  "contents": [{"parts": [{"text": "your prompt here"}]}],
  "generationConfig": {
    "responseModalities": ["TEXT", "IMAGE"],
    "imageConfig": {
      "aspectRatio": "16:9",
      "imageSize": "2K"
    }
  }
}
```

## Pricing

| Model | Resolution | Cost/Image |
|-------|-----------|------------|
| NB2 (3.1 Flash) | 1K | ~$0.067 |
| NB2 (3.1 Flash) | 2K | ~$0.134 |
| NB2 (3.1 Flash) | 4K | ~$0.268 |
| NB (2.5 Flash) | 1K | ~$0.039 |
| Batch API | Any | 50% discount |

## Key Limitations
- No video generation (image only)
- No transparent backgrounds (use green screen workaround)
- Text rendering: keep under 25 characters
- ONE image per API call -- no batch parameter
- No negative prompt parameter
- `imageSize` MUST be uppercase
