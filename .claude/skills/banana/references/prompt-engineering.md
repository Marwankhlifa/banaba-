# Prompt Engineering Reference -- Banana Claude

> Load this on-demand when constructing complex prompts or when the user
> asks about prompt techniques. Do NOT load at startup.
>
> Aligned with Google's March 2026 "Ultimate Prompting Guide" for Gemini image generation.

## The 5-Component Prompt Formula

> Based on Google's officially validated prompt structure for Gemini image models.
> Write as natural narrative paragraphs -- NEVER as comma-separated keyword lists.

### Component 1 -- SUBJECT
Who or what is the primary focus. Be specific about physical characteristics,
material, species, age, expression. Never write just "a person" or "a product."

**Good:** "A weathered Japanese ceramicist in his 70s, deep sun-etched
wrinkles mapping decades of kiln work, calloused hands cradling a
freshly thrown tea bowl with an irregular, organic rim"

**Bad:** "old man, ceramic, bowl"

### Component 2 -- ACTION
What the subject is doing, or the primary visual state. Use strong present-
tense verbs. "floats weightlessly," "holds a glowing lantern," "sits perfectly
still." If no action, describe pose or arrangement.

**Good:** "leaning forward with intense concentration, gently smoothing
the rim with a wet thumb, a thin trail of slip running down his wrist"

**Bad:** "making pottery"

### Component 3 -- LOCATION / CONTEXT
Where the scene takes place. Include environmental details, time of day,
atmospheric conditions. "inside the cupola module of the International Space
Station," "on a rain-slicked Tokyo alley at 2am."

**Good:** "inside a traditional wood-fired anagama kiln workshop,
stacked shelves of drying pots visible in the soft background, late
afternoon light filtering through rice paper screens"

**Bad:** "workshop, afternoon"

### Component 4 -- COMPOSITION
Camera perspective, framing, and spatial relationship. "medium shot centered
against the window," "extreme low-angle looking up," "bird's-eye view from
30 meters," "tight close-up on hands."

**Good:** "intimate close-up shot from slightly below eye level,
shallow depth of field isolating the hands and bowl against the
soft bokeh of the workshop behind"

**Bad:** "close up"

### Component 5 -- STYLE (includes lighting)
The visual register, aesthetic, medium, and lighting combined. Reference real
cameras, film stock, photographers, publications, or art movements. Lighting
lives here as a sub-element, not a separate component.

**Good:** "shot on a Fujifilm X-T4 with warm color science and natural
bokeh, warm directional light from a single high window camera-left
creating gentle Rembrandt lighting on the face with deep warm shadows.
Reminiscent of Dorothea Lange's documentary portraiture"

**Bad:** "photorealistic, 8K, masterpiece" (see Banned Keywords below)

## Domain Mode Modifier Libraries

### Cinema Mode
**Camera specs:** RED V-Raptor, ARRI Alexa 65, Sony Venice 2, Blackmagic URSA
**Lenses:** Cooke S7/i, Zeiss Supreme Prime, Atlas Orion anamorphic
**Film stocks:** Kodak Vision3 500T (tungsten), Kodak Vision3 250D (daylight), Fuji Eterna Vivid
**Lighting setups:** three-point, chiaroscuro, Rembrandt, split, butterfly, rim/backlight
**Shot types:** establishing wide, medium close-up, extreme close-up, Dutch angle, overhead crane, Steadicam tracking
**Color grading:** teal and orange, desaturated cold, warm vintage, high-contrast noir

### Product Mode
**Surfaces:** polished marble, brushed concrete, raw linen, acrylic riser, gradient sweep
**Lighting:** softbox diffused, hard key with fill card, rim separation, tent lighting, light painting
**Angles:** 45-degree hero, flat lay, three-quarter, straight-on, worm's-eye
**Style refs:** Apple product photography, Aesop minimal, Bang & Olufsen clean, luxury cosmetics

### Portrait Mode
**Focal lengths:** 85mm (classic), 105mm (compression), 135mm (telephoto), 50mm (environmental)
**Apertures:** f/1.4 (dreamy bokeh), f/2.8 (subject-sharp), f/5.6 (environmental context)
**Pose language:** candid mid-gesture, direct-to-camera confrontational, profile silhouette, over-shoulder glance
**Skin/texture:** freckles visible, pores at macro distance, catch light in eyes, subsurface scattering

### Editorial/Fashion Mode
**Publication refs:** Vogue Italia, Harper's Bazaar, GQ, National Geographic, Kinfolk
**Styling notes:** layered textures, statement accessories, monochromatic palette, contrast patterns
**Locations:** marble staircase, rooftop at golden hour, industrial loft, desert dunes, neon-lit alley
**Poses:** power stance, relaxed editorial lean, movement blur, fabric in wind

### UI/Web Mode
**Styles:** flat vector, isometric 3D, line art, glassmorphism, neumorphism, material design
**Colors:** specify exact hex or descriptive palette (e.g., "cool blues #2563EB to #1E40AF")
**Sizing:** design at 2x for retina, specify exact pixel dimensions needed
**Backgrounds:** transparent (request solid white then post-process), gradient, solid color

### Logo Mode
**Construction:** geometric primitives, golden ratio, grid-based, negative space
**Typography:** bold sans-serif, elegant serif, custom lettermark, monogram
**Colors:** max 2-3 colors, works in monochrome, high contrast
**Output:** request on solid white background, post-process to transparent

### Landscape Mode
**Depth layers:** foreground interest, midground subject, background atmosphere
**Atmospherics:** fog, mist, haze, volumetric light rays, dust particles
**Time of day:** blue hour (pre-dawn), golden hour, magic hour (post-sunset), midnight blue
**Weather:** dramatic storm clouds, clearing after rain, snow-covered, sun-dappled

### Infographic Mode
**Layout:** modular sections, clear visual hierarchy, bento grid, flow top-to-bottom
**Text:** use quotes for exact text, descriptive font style, specify size hierarchy
**Data viz:** bar charts, pie charts, flow diagrams, timelines, comparison tables
**Colors:** high-contrast, accessible palette, consistent brand colors

### Abstract Mode
**Geometry:** fractals, voronoi tessellation, spirals, fibonacci, organic flow, crystalline
**Textures:** marble veining, fluid dynamics, smoke wisps, ink diffusion, watercolor bleed
**Color palettes:** analogous harmony, complementary clash, monochromatic gradient, neon-on-black
**Styles:** generative art, data visualization art, glitch, procedural, macro photography of materials

## Advanced Techniques

### Character Consistency (Multi-turn)
Use `gemini_chat` and maintain descriptive anchors:
- First turn: Generate character with exhaustive physical description
- Following turns: Reference "the same character" + repeat 2-3 key identifiers
- Key identifiers: hair color/style, distinctive clothing, facial feature

**Multi-image reference technique** (3.1 Flash):
- Provide up to 4-5 character reference images in the conversation
- Assign distinct names to each character ("Character A: the red-haired knight")
- Model preserves features across different angles, actions, and environments
- Works best when reference images show the character from multiple angles

### Style Transfer Without Reference Images
Describe the target style exhaustively instead of referencing an image:
```
Render this scene in the style of a 1950s travel poster: flat areas of
color in a limited palette of teal, coral, and cream. Bold geometric
shapes with visible paper texture. Hand-lettered title text with a
mid-century modern typeface feel.
```

### Text Rendering Tips
- Quote exact text: `with the text "OPEN DAILY" in bold condensed sans-serif`
- **25 characters or less** -- this is the practical limit for reliable rendering
- **2-3 distinct phrases max** -- more text fragments degrade quality
- Describe font characteristics, not font names
- Specify placement: "centered at the top third", "along the bottom edge"
- High contrast: light text on dark, or vice versa
- **Text-first hack:** Establish the text concept conversationally first ("I need a sign that says FRESH BREAD"), then generate -- the model anchors on text mentioned early
- Expect creative font interpretations, not exact replication of described styles

### Positive Framing (No Negative Prompts)
Gemini does NOT support negative prompts. Rephrase exclusions:
- Instead of "no blur" → "sharp, in-focus, tack-sharp detail"
- Instead of "no people" → "empty, deserted, uninhabited"
- Instead of "no text" → "clean, uncluttered, text-free"
- Instead of "not dark" → "brightly lit, high-key lighting"

### Search-Grounded Generation
For images based on real-world data (weather, events, statistics),
Gemini can use Google Search grounding to incorporate live information.

**Three-part formula:**
1. `[Source/Search request]` -- What to look up
2. `[Analytical task]` -- What to analyze or extract
3. `[Visual translation]` -- How to render it as an image

## ❌ BANNED PROMPT KEYWORDS -- NEVER USE THESE

NEVER include:
- "4k" / "8k" / "ultra HD" / "high resolution"
- "masterpiece"
- "highly detailed" / "ultra detailed"
- "trending on artstation"
- "hyperrealistic" / "ultra realistic"
- "photorealistic"
- "best quality"
- "award winning"

USE THESE INSTEAD (prestigious context anchors):
- "Pulitzer Prize-winning cover photograph"
- "Vanity Fair editorial portrait"
- "National Geographic cover story"
- "WIRED magazine feature spread"
- "Architectural Digest interior"
- "Magnum Photos documentary"

## ⚠️ NEGATIVE PROMPTS -- No API parameter exists

Correct approach: semantic reframing.

❌ WRONG: "no cars, no people, no clutter in the background"
✅ RIGHT: "an empty, deserted street, completely still, no signs of activity"

For critical constraints, ALL CAPS emphasis improves adherence:
- "MUST contain exactly three figures"
- "NEVER include any visible horizon line"
- "ONLY show the product, nothing else in frame"

## Prompt Length Guide

| Use case | Target length |
|---|---|
| Quick draft / concept | 20–60 words |
| Standard generation | 100–200 words |
| Complex professional | 200–300 words |
| Maximum specification | Up to 2,600 tokens |

## Safety Filter Rephrase Strategies

When a prompt is blocked, the only path forward is rephrasing.

| Category | Rephrase approach |
|----------|-------------------|
| Violence/weapons | Use metaphor or aftermath |
| Medical/gore | Abstract or clinical framing |
| Real public figures | Use archetypes instead |
| Children + risk | Add educational/family context |
| NSFW/suggestive | Use artistic/editorial framing |
