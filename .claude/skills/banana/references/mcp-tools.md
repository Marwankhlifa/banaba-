# MCP Tools Reference -- @ycse/nanobanana-mcp

> Package: `@ycse/nanobanana-mcp`

## Tools

### gemini_generate_image
Generate an image from a text prompt.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `prompt` | string | Yes | Text description of the image to generate |

Returns: Image data + file path (saved to `~/Documents/nanobanana_generated/`)

### gemini_edit_image
Edit an existing image with text instructions.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `imagePath` | string | Yes | Path to the image file to edit |
| `prompt` | string | Yes | Edit instructions |

### gemini_chat
Multi-turn visual conversation maintaining session context.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | string | Yes | Chat message (can reference previous images) |

### set_aspect_ratio
Configure the aspect ratio for subsequent generations.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `ratio` | string | Yes | e.g., "16:9", "1:1", "9:16" |

### set_model
Switch the active Gemini model.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `model` | string | Yes | Model identifier |

Available: `gemini-3.1-flash-image-preview` (default), `gemini-2.5-flash-image`

### get_image_history
Retrieve list of images generated in the current session. No parameters.

### clear_conversation
Reset session context and conversation history. No parameters.

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_AI_API_KEY` | Yes | API key from https://aistudio.google.com/apikey |
| `NANOBANANA_MODEL` | No | Override default model |

## ImageConfig Parameter Reference

| Parameter | Valid values | Notes |
|---|---|---|
| `aspect_ratio` | "1:1", "16:9", "9:16", etc. | See gemini-models.md for full list |
| `image_size` | "512", "1K", "2K", "4K" | MUST be uppercase |
| `person_generation` | "ALLOW_ALL", "ALLOW_ADULT", "ALLOW_NONE" | ALLOW_ALL restricted in EU/UK |

## ❌ Parameters That Do NOT Exist

- `numberOfImages` / `n` / `sampleCount` -- Gemini generates ONE image per call
- `negativePrompt` -- use semantic reframing instead
- `output_mime_type` -- Vertex AI only
- `candidate_count` -- only 1 supported
- `seed` -- not supported

## Error Response Taxonomy

| Error | Cause | Response |
|---|---|---|
| HTTP 429 | Rate limit | Exponential backoff |
| HTTP 400 FAILED_PRECONDITION | Billing not enabled | Enable billing in Google AI Studio |
| `finishReason: "IMAGE_SAFETY"` | Content policy block | Rephrase prompt, retry once |
| Empty `parts` in response | Wrong `responseModalities` | Must include "IMAGE" |
