# Banana Claude – Creative Director for AI Image Generation

**Banana** is an AI image generation skill powered by Google Gemini Nano models, functioning as a Creative Director for visual asset production.

## Core Functionality

The tool orchestrates image generation through a structured pipeline:

1. **Intent Analysis** – Clarify use case, style preference, constraints, and mood before generating
2. **Domain Selection** – Choose expertise lens (Cinema, Product, Portrait, Editorial, UI/Web, Logo, Landscape, Abstract, Infographic)
3. **Prompt Engineering** – Construct prompts using a 5-Component Formula: Subject → Action → Location/Context → Composition → Style
4. **Model & Settings** – Select appropriate Gemini model and aspect ratio for the task
5. **Generation & Error Handling** – Execute with safety fallbacks and retry logic
6. **Post-Processing** – Apply transformations like background removal or format conversion

## Key Commands

| Command | Purpose |
|---------|---------|
| `/banana generate <idea>` | Create image with full prompt engineering |
| `/banana edit <path> <instructions>` | Modify existing images intelligently |
| `/banana chat` | Multi-turn creative sessions maintaining consistency |
| `/banana batch <idea> [N]` | Generate N variations with different components |
| `/banana inspire [category]` | Browse prompt database for ideas |
| `/banana preset [list\|create\|show\|delete]` | Manage brand/style presets |

## Critical Rules

- **Never pass raw user text directly** – always enhance and optimize prompts
- Avoid banned keywords like "8K" or "masterpiece" – use `imageSize` parameter instead
- Name real cameras and brands to trigger visual associations
- Include micro-details (textures, expressions, lighting specifics)
- Use prestigious context anchors ("Vanity Fair editorial," "National Geographic")
- For safety blocks, propose 2-3 rephrased alternatives without auto-retrying

## Default Configuration

- **Model:** `gemini-3.1-flash-image-preview`
- **Resolution:** 2K (balanced quality/speed)
- **Aspect Ratio:** 1:1 (adjustable per use case)

The system maintains cost tracking, preset management, and comprehensive error handling for rate limits, safety blocks, and API failures.

## References

Load these on-demand as needed:
- `references/prompt-engineering.md` – 5-component formula, domain modes, templates
- `references/gemini-models.md` – Model specs, routing, aspect ratios, pricing
- `references/mcp-tools.md` – MCP tool parameters and error taxonomy
- `references/post-processing.md` – ImageMagick/FFmpeg pipelines
- `references/cost-tracking.md` – Pricing and usage tracking
- `references/presets.md` – Brand preset schema

## Fallback Scripts

When MCP is unavailable, use Python fallback scripts:
- `scripts/generate.py --prompt "..." [--aspect-ratio 16:9] [--resolution 2K]`
- `scripts/edit.py --image path/to/image.png --prompt "..."`

Both use only Python stdlib (no pip dependencies). Requires `GOOGLE_AI_API_KEY` env var.
