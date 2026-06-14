# Brand/Style Presets Reference

> Load this on-demand when the user asks about presets or brand consistency.

## Preset Schema

Each preset is stored as `~/.banana/presets/NAME.json`:

```json
{
  "name": "tech-saas",
  "description": "Clean tech SaaS brand",
  "colors": ["#2563EB", "#1E40AF", "#F8FAFC"],
  "style": "clean minimal tech illustration, flat vectors, soft shadows",
  "typography": "bold geometric sans-serif",
  "lighting": "bright diffused studio, no harsh shadows",
  "mood": "professional, trustworthy, modern",
  "default_ratio": "16:9",
  "default_resolution": "2K"
}
```

## Example Presets

### tech-saas
- **Colors:** #2563EB, #1E40AF, #F8FAFC
- **Style:** Clean minimal tech illustration, flat vectors, soft shadows
- **Mood:** Professional, trustworthy, modern

### luxury-brand
- **Colors:** #1A1A1A, #C9A96E, #FAFAF5
- **Style:** Elegant high-end photography, rich textures, deep contrast
- **Mood:** Exclusive, sophisticated, aspirational

### editorial-magazine
- **Colors:** #000000, #FFFFFF, #FF3B30
- **Style:** Bold editorial photography, strong geometric composition
- **Mood:** Bold, provocative, contemporary

## Managing Presets

```bash
presets.py list
presets.py show tech-saas
presets.py create NAME --colors "#hex,#hex" --style "..." --mood "..."
presets.py delete NAME --confirm
```

User instructions always override preset values.
